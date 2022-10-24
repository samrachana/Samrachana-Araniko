from structure3d import *


class App(Ui_MainWindow):
    def __init__(self,MainWindow,app):
        super().setupUi(MainWindow)
        # R.__init__(R)
        self.app=app
        self.objectProperties()
        self.variables()
        self.oT = QtWidgets.QDialog(parent=MainWindow)
        self.ot = ObjectTree()
        self.ot.setupUi(self.oT,MainWindow)
        self.connectors()
        self.threadpool = QtCore.QThreadPool()

    def objectProperties(self):
        self.supportNumber = 1
        self.loadNumber = 1
        self.segmentNumber = 1

        self.bgColor = (0, 0, 0, 255)
        self.segmentColor = (202, 1, 209, 255)
        self.loadColor = (200, 0, 0, 255)
        self.afdColor = (0, 0, 250, 255)
        self.sfdColor = (0, 250, 0, 255)
        self.bmdColor = (250, 0, 0, 255)
        self.translationColor = (0, 200, 0, 255)
        self.rotationColor = (0, 200, 0, 255)
        self.rollerColor = (200, 200, 0, 255)
        self.hingeColor = (0, 200, 200, 255)
        self.fixedColor = (120, 0, 120, 255)
        self.internalHingeColor = (100, 200, 100, 255)
        self.segmentWidth = 3
        self.loadWidth = 2

    def variables(self):
        self.setunits=False
        try:
            units=read_csv('./datafiles/units.csv')
            self.material = read_csv("./datafiles/material.csv")
            self.section = read_csv("./datafiles/sections.csv") 
        except:
            writeFiles()
            units=read_csv('./datafiles/units.csv')
            self.material = read_csv("./datafiles/material.csv")
            self.section = read_csv("./datafiles/sections.csv")        
        self.currentUnit='SI'
        self.force=1
        self.length=1
        self.precison=8
        self.scale=1
        self.SIscales=['1:1.0','1:10.0','1:100.0','Custom']
        self.SIunitsOfForce=dict(units[(units['Quantity']=='Force')&(units['System']=='SI')][['Symbol','Conversion']].values.tolist())
        self.SIunitsOfLength=dict(units[(units['Quantity']=='Length')&(units['System']=='SI')][['Symbol','Conversion']].values.tolist())

        self.ENGscales=['1:1.0','1:6.0','1:12.0','Custom']
        self.ENGunitsOfForce=dict(units[(units['Quantity']=='Force')&(units['System']=='ENG')][['Symbol','Conversion']].values.tolist())
        self.ENGunitsOfLength=dict(units[(units['Quantity']=='Length')&(units['System']=='ENG')][['Symbol','Conversion']].values.tolist())

        self.current_material = 0
        self.current_section = 0
        self.historystatus = True
        self.historyposition = 1
        self.counter = 1
        self.history = array([], dtype="int8")
        self.df = DataFrame(
            columns=["Name", "Class", "Robject", "Graphitem", "Treeitem", "Flag"],
            index=None,
        )
        self.currentDiagram = False
        self.cameraDistance = 30
        self.itemss = 0
        self.supportColors = {"Roller": self.rollerColor, "Hinge": self.hingeColor, "Fixed": self.fixedColor,"Internal Hinge":self.internalHingeColor}
        self.fileName=None
    def connectors(self):
        self.graphWidget = GraphWidget()
        self.gridLayout.addWidget(self.graphWidget, 0, 0, 4, 1)
        self.actionDark_Mode.setChecked(True)
        self.graphWidget.setMouseTracking(True)

        self.actionUnits.triggered.connect(lambda:unitWindow(self,MainWindow))
        # self.actionSI_Units.triggered.connect(lambda: unitWindow(self,MainWindow))
        # self.actionEngineering_Units.triggered.connect(lambda:unitWindowENG(self,MainWindow))
        self.actionPrint.triggered.connect(lambda: printFile(self))
        self.actionNew.triggered.connect(lambda: newFile(self))
        self.actionSave_As.triggered.connect(lambda: saveAsFile(self))
        self.actionSave.triggered.connect(lambda: saveFile(self))
        self.actionOpen.triggered.connect(lambda: openFile(self, app))
        
        self.actionScript.triggered.connect(lambda:generateBuilding3d(self,MainWindow,app))
        self.actionMOI_calculator.setText("Section Calculator")
        self.actionMOI_calculator.triggered.connect(
            lambda: sectionBuilder(self, MainWindow)
        )
        self.actionObject_Tree.setShortcut("o")
        # self.graphWidget.pan(10,10,10,relative=False)
        # self.graphWidget.setCameraPosition(pos=(100,100,100))
        self.graphWidget.setCameraPosition(distance=self.cameraDistance, azimuth=50)

        self.actionAnalyse.triggered.connect(self.analyse)

        self.actionLine.triggered.connect(lambda: segmentDialog(self,"line",MainWindow))
        self.actionArc.triggered.connect(lambda: segmentDialog(self,"arc",MainWindow))
        self.actionQuad.triggered.connect(lambda: segmentDialog(self,"quad",MainWindow))

        self.actionPointLoad.triggered.connect(lambda: loadDialog(self,"Point Load",MainWindow))
        self.actionUDL.triggered.connect(lambda: loadDialog(self,"UDL",MainWindow))
        self.actionUVL.triggered.connect(lambda: loadDialog(self,"UVL",MainWindow))
        self.actionPolyLoad.triggered.connect(lambda: loadDialog(self,"Poly Load",MainWindow))
        self.actionmoment.triggered.connect(lambda: loadDialog(self,"Moment",MainWindow))

        self.actionRoller.triggered.connect(lambda: supportDialog(self,"Roller",MainWindow))
        self.actionHinge.triggered.connect(lambda: supportDialog(self,"Hinge",MainWindow))
        self.actionFixed.triggered.connect(lambda: supportDialog(self,"Fixed",MainWindow))
        self.actionInternalHinge.triggered.connect(lambda: supportDialog(self,"Internal Hinge",MainWindow))
        
        self.actionzoomIn.triggered.connect(self.zoomIn)
        self.actionzoomOut.triggered.connect(self.zoomOut)
        self.actionConsole.triggered.connect(self.console)
        
        self.actionColor_profile.triggered.connect(self.preferenceDialog)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionClear_Screen.triggered.connect(self.clearScreen)
        
        self.actionGrid.triggered.connect(self.grid)
        self.actionAxis.triggered.connect(self.axis)
        self.actionClose.triggered.connect(self.app.quit)
        self.actionPlan.triggered.connect(lambda: self.graphWidget.setCameraPosition(pos=(0,0,25)))
        self.actionFront.triggered.connect(self.frontview)
        self.actionBack.triggered.connect(lambda: self.graphWidget.setCameraPosition(pos=(-25,0,0)))
        self.actionRight.triggered.connect(lambda: self.graphWidget.setCameraPosition(pos=(0,25,0)))
        self.actionLeft.triggered.connect(lambda: self.graphWidget.setCameraPosition(pos=(0,-25,0)))
        self.actionObject_Tree.triggered.connect(lambda:objectTree(self,MainWindow))
        self.actionDark_Mode.triggered.connect(self.darkMode)
        
        self.actionAbout.triggered.connect(self.message)
        self.actionLicense.triggered.connect(self.message)
        self.actionManual.triggered.connect(self.message)
        self.actionUpdate.triggered.connect(self.message)


        Plot(self.graphWidget)
    def frontview(self):
        self.graphWidget.pan(0, 13, 8)
        self.graphWidget.setCameraPosition(pos=(25, 0, 0))

    def diagrams(self, name):
        check = self.df[(self.df["Class"] == "segment") & (self.df["Name"] == name)]
        if check.empty == False:
            try:
                self.nd.statusbar.showMessage(f"Analysing the member : {name}")
            except:
                self.statusbar.showMessage(f"Analysing the member : {name}")
            robj = self.df[self.df["Name"] == name]["Robject"]
            self.robj = robj.iloc[0]
            worker = WorkerThread2(self.robj, self.structure, self.matrix)
            def assign(a):
                self.actionData=a[0]
                self.responseData=a[1]
            worker.signals.result.connect(assign)
            worker.signals.finished.connect(
                lambda: showDiagrams(name, self, MainWindow)
            )
            self.threadpool.start(worker)
        else:
            self.statusbar.showMessage(
                "Please select a valid segment to view diagrams", 5000
            )



    def analyse(self):
        self.statusbar.showMessage("Analysing the structure")
        self.structure = structify(self.df.loc[self.df["Flag"] == True]["Robject"])
        worker = WorkerThread(frame3d, self.structure)
        worker.signals.result.connect(self.analysis)

        self.threadpool.start(worker)

    def analysis(self,matrix):
        self.statusbar.showMessage("Analysis Complete", 1500)

        self.nD = QtWidgets.QMainWindow(parent=MainWindow)
        self.nd = NodalDisplacements()
        self.nd.setupUi(self.nD)
        # self.structure=list(self.df.loc[self.df['Flag']==True]['Robject'])
        
        self.matrix = matrix
        responses = array(self.matrix['response'])
        actions = array(self.matrix['action'])
        r, c = responses.shape

        for i in range(r):
            self.nd.displacementTable.insertRow(i)
            for j in range(c):
                self.nd.displacementTable.setItem(
                    i, j, QtGui.QTableWidgetItem(str(round(responses[i][j],self.precison)))
                )
        r, c = actions.shape
        names = list(
            self.df[(self.df["Flag"] == True) & (self.df["Class"] == "segment")]["Name"]
        )
        for i in range(r):
            self.nd.forcesTable.insertRow(i)
            if i % 2 == 0:
                self.nd.forcesTable.setItem(
                    i, 0, QtGui.QTableWidgetItem(names[int(i / 2)])
                )
            for j in range(c):
                self.nd.forcesTable.setItem(
                    i, j + 1, QtGui.QTableWidgetItem(str(round(actions[i][j],self.precison)))
                )
        self.nD.show()

        def test():
            selectedItem = self.nd.forcesTable.selectedItems()
            if len(selectedItem) != 0:
                self.diagrams(selectedItem[0].text())

        # self.nd.forcesTable.itemSelectionChanged.connect(test)
        self.nd.forcesTable.itemClicked.connect(test)

    def message(self):
        self.mB = QtWidgets.QDialog()
        self.mb = Message()
        self.mb.setupUi(self.mB)
        self.mB.show()




    def darkMode(self):
        if self.actionDark_Mode.isChecked()==True:
            self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
            self.graphWidget.setBackgroundColor((0,0,0,255))
        else:
            self.app.setStyleSheet('')  
            self.graphWidget.setBackgroundColor(255,255,255,255)  
    def zoomIn(self):
        self.cameraDistance-=2
        self.graphWidget.setCameraPosition(distance=self.cameraDistance)
    def zoomOut(self):
        self.cameraDistance+=2
        self.graphWidget.setCameraPosition(distance=self.cameraDistance)
            
    def axis(self):
        if self.actionAxis.isChecked()==True:
            self.graphWidget.items[0].show()
        else:
            self.graphWidget.items[0].hide()
    def grid(self):
        if self.actionGrid.isChecked() == True:
            self.graphWidget.items[1].show()
            self.graphWidget.items[2].show()
            self.graphWidget.items[3].show()
        else:
            self.graphWidget.items[1].hide()
            self.graphWidget.items[2].hide()
            self.graphWidget.items[3].hide()
    def clearScreen(self):
        for index in range(len(self.df)):
            if  self.df.iloc[index,3].visible()==True:
                self.df.iloc[index,3].hide()
                self.df.iloc[index,4].setHidden(True)
                self.df.iloc[index,5]=False

    def changeFlag(self, index=None, name=None):
        if name != None:
            index = self.df[self.df["Name"] == name].index[0]
        if self.df.iloc[index, 3].visible() == True:
            self.df.iloc[index, 3].hide()
            self.df.iloc[index, 4].setHidden(True)
            self.df.iloc[index, 5] = False
        else:
            self.df.iloc[index, 3].show()
            self.df.iloc[index, 4].setHidden(False)
            self.df.iloc[index, 5] = True

    def redo(self):
        if not self.historystatus:
            self.historystatus=True
        if self.counter<self.historyposition:
            self.changeFlag(index=self.history[self.counter])
            self.history=append(self.history,self.history[self.counter])
            self.counter+=1         
        else:
            self.statusbar.showMessage("No more redo available",2000) 
    def undo(self):

        if self.historystatus:
            self.historyposition=len(self.history)
            self.historystatus=False
            self.counter=len(self.history)     
        
        if self.counter>0:
            self.changeFlag(index=self.history[self.counter-1])
            self.history=append(self.history,self.history[self.counter-1])
            self.counter-=1
            self.itemss=len(self.df)
        else:
            self.statusbar.showMessage("No more undo available",2000)
        
    def preferenceDialog(self):
        from UI.preferenceDialog import Ui_Dialog as PreferenceUi_Dialog
        self.pD = QtWidgets.QDialog()
        self.pd = PreferenceUi_Dialog()
        self.pd.setupUi(self.pD)   

        self.pd.bgColor.setColor(color=self.bgColor)
        self.pd.segmentColor.setColor(color=self.segmentColor)
        self.pd.loadColor.setColor(color=self.loadColor)
        self.pd.afdColor.setColor(color=self.afdColor)
        self.pd.sfdColor.setColor(color=self.sfdColor)
        self.pd.bmdColor.setColor(color=self.bmdColor)
        self.pd.translationColor.setColor(color=self.translationColor)
        self.pd.rotationColor.setColor(color=self.rotationColor)
        self.pd.rollerColor.setColor(color=self.rollerColor)
        self.pd.hingeColor.setColor(color=self.hingeColor)
        self.pd.fixedColor.setColor(color=self.fixedColor)
        self.pd.internalHingeColor.setColor(color=self.internalHingeColor)
        self.pD.show()

        self.pd.buttonBox.accepted.connect(self.setColorsandWidth)
    def setColorsandWidth(self):
        self.bgColor = self.pd.bgColor.color(mode='byte')
        self.segmentColor = self.pd.segmentColor.color(mode='byte')
        self.loadColor = self.pd.loadColor.color(mode='byte')
        self.afdColor = self.pd.afdColor.color(mode='byte')
        self.sfdColor = self.pd.sfdColor.color(mode='byte')
        self.bmdColor = self.pd.bmdColor.color(mode='byte')
        self.translationColor = self.pd.translationColor.color(mode='byte')
        self.rotationColor = self.pd.rotationColor.color(mode='byte')
        self.rollerColor = self.pd.rollerColor.color(mode='byte')
        self.hingeColor = self.pd.hingeColor.color(mode='byte')
        self.fixedColor = self.pd.fixedColor.color(mode='byte')
        self.internalHingeColor = self.pd.internalHingeColor.color(mode='byte')
        self.segmentWidth=self.pd.segementWidth.value()
        self.loadWidth = self.pd.loadWidth.value()
        self.graphWidget.setBackgroundColor(pg.mkColor(self.bgColor))
        
    def console(self):
        from PySide2 import QtGui
        from pyqtgraph.console import ConsoleWidget
        
        text = """ This is interactive console to run python codes"""
        # names={'R':R}
        self.c = ConsoleWidget(text=text)
        self.c.setStyleSheet('''QWidget{
            background-color:rgb(220, 220, 227);
            font-size: 20px;
            font-weight:150;
            color: rgb(2,200,10);
            };''')
        self.c.setWindowTitle('StructDote Script')
        self.c.show()
