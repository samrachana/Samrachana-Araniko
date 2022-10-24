from PySide2 import QtWidgets,QtCore
from PySide2.QtWidgets import QTableWidgetItem
from numpy.core.fromnumeric import argmax
from sdPy.functionDefinitions import rowPos, structify2d
from threads import WorkerThread
from sdPy.structureMethods import frame2d, truss2d
from numpy import array, delete
from UI.newnodalDisplacements2d import Ui_MainWindow as NodalDisplacements

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

def analysis(self, matrix):
    if matrix==None:
        self.statusbar.showMessage('Problem encountered while analysing structure, try again,after entering valid supports',6000)
        return

    self.statusbar.showMessage("Analysis Complete", 1500)

    self.nD = QtWidgets.QMainWindow(parent=self.MainWindow)
    self.nd = NodalDisplacements()
    self.nd.setupUi(self.nD)

    self.matrix = matrix

    
    if not self.trussMode:
        responses = array(self.matrix['response'])
        actions = array(self.matrix['action'])
        reactions=array(self.matrix['reactions'])
        nodes = self.matrix['response'][:,:2]

    else:
        nodes = self.matrix['response'][:,1:3]
        actions = array(self.matrix['action'])
        self.nd.displacementTable.removeColumn(5)
        self.nd.forcesTable.removeColumn(5)
        self.nd.forcesTable.removeColumn(4)
        self.nd.forcesTable.removeColumn(3)
        self.nd.reactionTable.removeColumn(3)

        responses = delete(array(self.matrix['response']),0,1)
        actions = delete(array(self.matrix['action']),0,1)
        reactions=delete(array(self.matrix['reactions']),[0,3],1)
        # reactions=delete(reactions,3,1)
    r, c = responses.shape
    # self.nd.displacementTable.insertColumn(0)
    # header2 = QTableWidgetItem()
    # header2.setText("Nodes");
    # self.nd.displacementTable.setHorizontalHeaderItem(0,header2);
    delegate = AlignDelegate(self.nd.displacementTable)
    self.nd.displacementTable.setItemDelegate(delegate)    
    delegate = AlignDelegate(self.nd.reactionTable)
    self.nd.reactionTable.setItemDelegate(delegate)  
    delegate = AlignDelegate(self.nd.forcesTable)
    self.nd.forcesTable.setItemDelegate(delegate)  
    
    for i in range(r):
        self.nd.displacementTable.insertRow(i)
        self.nd.displacementTable.setItem(
            i, 0, QtWidgets.QTableWidgetItem(f'Node-{str(i+1)}')     )   
        for j in range(c):
            self.nd.displacementTable.setItem(
                i, j+1, QtWidgets.QTableWidgetItem(
                    str(round(responses[i][j], max(6,self.precison))))
            )

    names = list(
        self.df[(self.df["Flag"] == True) & (
            self.df["Class"] == "segment")]["Name"]
    )
    pts=actions[:,:2]
    actions=actions[:,2:]
    r, c = actions.shape

    # nodelist=self.matrix['memLoc'].flatten()+1


    for i in range(r):
        self.nd.forcesTable.insertRow(i)
        if i % 2 == 0:
            self.nd.forcesTable.setItem(
                i, 0, QtWidgets.QTableWidgetItem(names[int(i / 2)])
            )
        
        self.nd.forcesTable.setItem(
            i, 1, QtWidgets.QTableWidgetItem('Node-'+str(rowPos(pts[i],nodes)+1)
        ))            
        for j in range(c):
            self.nd.forcesTable.setItem(
                i, j + 2, QtWidgets.QTableWidgetItem(
                    str(round(actions[i][j], self.precison)))
            )
    
    # self.nd.reactionTable.insertColumn(0)
    # header2 = QTableWidgetItem()
    # header2.setText("Nodes");
    # self.nd.reactionTable.setHorizontalHeaderItem(0,header2);
    reactions=reactions[:,2:]
    r,c = reactions.shape

    for i in range(r):
        self.nd.reactionTable.insertRow(i)
        self.nd.reactionTable.setItem(
            i, 0, QtWidgets.QTableWidgetItem(f'Node-{str(i+1)}')     )  
        for j in range(c):
            self.nd.reactionTable.setItem(
                i, j+1, QtWidgets.QTableWidgetItem(
                    str(round(reactions[i][j], self.precison)))
            )

    

    def test():
        selectedItem = self.nd.forcesTable.selectedItems()
        if len(selectedItem) != 0:
            self.diagrams(selectedItem[0].text())

    # self.nd.forcesTable.itemSelectionChanged.connect(test)
    


    self.dockAnalysisTable=QtWidgets.QDockWidget('Structure Analysis Results',self.MainWindow)
    self.dockAnalysisTable.setWidget(self.nD)
    self.MainWindow.addDockWidget(QtCore.Qt.BottomDockWidgetArea,self.dockAnalysisTable)
    self.dockObjectTree.close()
    self.actionObject_Tree.setChecked(False)
    self.MainWindow.tabifyDockWidget(self.dockObjectTree,self.dockAnalysisTable)
    # self.dockAnalysisTable.setFocus()

    
    for a in self.nodes:
        self.scene.removeItem(a)
        self.nodes.remove(a)

    from PySide2.QtWidgets import QGraphicsTextItem
    from PySide2.QtGui import QTransform
    # self.nodes=[]
    r,c =responses.shape
    for i in range(r):
        text = QGraphicsTextItem()
        text.setPos(self.rrts(responses[i][0])+10,self.rrts(responses[i][1])-10)
        text.setHtml(f"<p style='color:blue;font-size:18px'>{str(i+1)}</p>")   
        text.setTransform(QTransform(1., 0., 0., -1., 0, 0))
        text.setFlag(QGraphicsTextItem.ItemIsSelectable)     
        self.scene.addItem(text)
        self.nodes.append(self.scene.items()[0]) 
    
    self.nd.displacementTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    self.nd.reactionTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    self.nd.forcesTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    self.nd.forcesTable.itemClicked.connect(test)
    self.nD.show()





def analyse(self):
    try:
        self.shearMode=self.am.shearMode.isChecked()
        self.inextensibleMode=self.am.inextensibleMode.isChecked()
        self.simplifyMode=self.am.simplifyMode.isChecked()
        analysisParameters={
            'shear':self.shearMode,
            'inextensible':self.inextensibleMode,
            'simplify':self.simplifyMode,
            'structureAnalysisAccuracy':self.structuralAnalysisAccuracy
        }
        self.aM.close
        self.statusbar.showMessage("Analysing the structure")
        self.structure = structify2d(
            self.df.loc[self.df["Flag"] == True]["Robject"])
        if self.am.frameMode.isChecked()==True:
            self.trussMode=False
            worker = WorkerThread(frame2d, self.structure,analysisParameters)
        else:
            self.trussMode=True
            worker = WorkerThread(truss2d, self.structure,analysisParameters)
        def result(matrix):
            analysis(self,matrix)
        worker.signals.result.connect(result)
        self.threadpool.start(worker)
    except Exception as e:
        import traceback
        traceback.print_exc()
        self.statusbar.showMessage(str(e), 2000)

def analysisModes(self):
    # designSection(self)

    self.aM=QtWidgets.QDialog(self.MainWindow)
    from UI.analysisModes import Ui_Dialog
    self.am=Ui_Dialog()
    self.am.setupUi(self.aM)
    self.am.buttonBox.accepted.connect(lambda:analyse(self))
    self.am.simplifyMode.setChecked(True)
    self.aM.show()





from sdPy.sectionBuilder import breakArc, breakQuad
from numpy import vstack,append,array
def designSection(self):
    from sdPy.sectionBuilder import xCalc
    from numpy import array
    segs = self.df[(self.df['Class']=='segment')&(self.df['Flag']==True)]
    segs.index=range(0,len(segs))

    allLoops=[]
    while (len(segs)!=0):
        # main =array([segs.iloc[0,2]['P1']])
        main=array([])
        initial=segs.iloc[0,2]['P3']

        for _ in range(1,len(segs)):
            for i in range(1,len(segs)):
                xseg=segs.iloc[i,2]

                if (xseg['P1']==initial).all():
                    if xseg['type']=='line':
                        main=append([main],[xseg['P1']])
                    elif xseg['type']=='arc':
                        main=append([main],[breakArc(xseg['P1'],xseg['P3'],xseg['P2'],self.sectionDesignerAccuracy)])
                    elif xseg['type']=='quad':    
                        main=append([main],[breakQuad(xseg['P1'],xseg['P3'],xseg['P2'],self.sectionDesignerAccuracy)])

                    print(len(segs),xseg['P1']==initial,(xseg['P1']==initial).all(),xseg['P1'],xseg['P2'])
                    initial =xseg['P3']
                    segs=segs.drop([i])
                    segs.index=range(0,len(segs))
                    break
                elif (xseg['P3']==initial).all():
                    if xseg['type']=='line':
                        main=append([main],[xseg['P3']])
                    elif xseg['type']=='arc':
                        main=append([main],[breakArc(xseg['P3'],xseg['P1'],xseg['P2'],self.sectionDesignerAccuracy)[::-1]])
                    elif xseg['type']=='quad':    
                        main=append([main],[breakQuad(xseg['P3'],xseg['P1'],xseg['P2'],self.sectionDesignerAccuracy)[::-1]])
                    # main.append(xseg['P3'])
                    print(xseg['P3']==initial,xseg['P3'],initial)
                    initial =xseg['P1']
                    segs=segs.drop([i])
                    segs.index=range(0,len(segs))
                    break

        if segs.iloc[0,2]['type']=='line':
            main=append([main],[segs.iloc[0,2]['P1']])
            main=append([main],[segs.iloc[0,2]['P3']])

        elif segs.iloc[0,2]['type']=='arc':
            xseg=segs.iloc[0,2]
            main=append([main],[breakArc(xseg['P1'],xseg['P3'],xseg['P2'],self.sectionDesignerAccuracy)])
        elif segs.iloc[0,2]['type']=='quad':    
            xseg=segs.iloc[0,2]
            main=append([main],[breakQuad(xseg['P1'],xseg['P3'],xseg['P2'],self.sectionDesignerAccuracy)])
        # main.append(segs.iloc[0,2]['P1'])
        segs=segs.drop([0])
        segs.index=range(0,len(segs))
        main=main.reshape((int(main.size/2),2))
        allLoops.append(main)
    

    from sdPy.sectionBuilder import I0,lines
    from numpy import argmax,array
    area=array([I0(lines(array(x))) for x in allLoops])
    main=allLoops[argmax(area)]
    holes=allLoops[:argmax(area)]+allLoops[1+argmax(area):]
        
    section = {'main' : array(main), 'holes' : array(holes)}
    # print(section)
    data = xCalc(section)  
    return data     
    