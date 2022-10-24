from math import log10
from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QSizePolicy, QTreeWidget ,QGridLayout,QTreeWidgetItem,QPushButton,QGraphicsItem,QDockWidget
from PySide2.QtGui import QIcon, QPen,QPixmap,QColor
from PySide2.QtCore import Qt
from PySide2 import QtGui,QtWidgets,QtCore
from numpy import array,append
from sdPy.functionDefinitions import make2d, structify2d
from threads import WorkerThread
from sdPy.structureMethods import frame2d
import re
from sdPy.segmentMethods import segPlotData2
from sdPy.loadMethods import loadPlotData2, loadPlotData4
from sdPy.supportMethods import supportPlotData2
editableitems=['P1','P2','P3','peak','normal','location','degree','type','parentSegment']


def arrayMaker(columnName,currentText,parentName):
    if columnName in ['P1','P2','P3','normal','location','settlement']:                
        currentText=re.sub('[\[\]]','',currentText)
        currentText=re.split(',| ',currentText)
        while '' in currentText:currentText.remove('')
        if len(currentText)==2:
            currentText=array(currentText,dtype=float) 
        else:                    
            if columnName=='normal':
                currentText=array([0]+[currentText[0]],dtype=float)
            else:
                currentText=array([currentText[0]]+[0],dtype=float)         
    elif columnName=='type':
        if parentName == 'support':
            currentText=currentText.title()
        elif parentName == 'segment':
            currentText = currentText.lower()  
    else:
        try:
            currentText=float(currentText)
        except ValueError:
            currentText=float(currentText[1])
        except:
            raise Exception
            return False
    return currentText
def editObjects(self,item):
    from structure2d.mouseGraphics import delete

    editDialog=QDialog(self.MainWindow)
    item=self.df[(self.df['Graphitem']==item)].iloc[0]
    editDialog.setWindowTitle(f"Edit {item['Class']}")
    gridLayout=QGridLayout()
    editDialog.setLayout(gridLayout)
    totalItems=len(item['Robject'])
    skipItems=['class','parent','psName','parentSegment']
    for i in range(len(item['Robject'])):
        key,value=list(item['Robject'].keys())[i],list(item['Robject'].values())[i]
        if key in skipItems: continue
        setattr(self,'label'+key,QLabel(key.capitalize()))
        gridLayout.addWidget(getattr(self,'label'+key),i,0,1,1)
        setattr(self,'edit'+key,QLineEdit(str(value)))
        gridLayout.addWidget(getattr(self,'edit'+key),i,1,1,1)        


    editDialog.setMinimumHeight(totalItems*30)
    
    done=QPushButton('Done')
    gridLayout.addWidget(done,i+1,1,1,1)
    def accept():
        Robject=item['Robject'].copy()
        for i in range(len(item['Robject'])):
            key,value=list(item['Robject'].keys())[i],list(item['Robject'].values())[i]
            if key in skipItems:
                pass
            else:
                try:
                    value= arrayMaker(key,getattr(self,'edit'+key).text(),item['Class'])
                    Robject[key]=value
                except:
                    self.statusbar.showMessage(f'Enter valid {key}',3000)
                    return    
        self.member=item['Class']
        name=item['Name']
        if self.member=='segment':
            self.todraw=Robject['type']
            self.count=1 if self.todraw=='line' else 2
            self.x[0],self.y[0]=self.rrts(Robject['P1'])
            self.x[1],self.y[1]=self.rrts(Robject['P3'])
            self.x[2],self.y[2]=self.rrts(Robject['P2'])
            data=list(Robject.values())[4:11]
            self.drawAll(properties=data,name=name)
        elif self.member=='support':
            self.todraw=Robject['type']
            self.x[0],self.y[0]=self.rrts(Robject['location'])
            self.drawAll(properties=Robject['normal'],name=name)
        elif self.member=='load':
            
            self.todraw=list(self.loadtypes.keys())[list(self.loadtypes.values()).index(Robject['degree'])]
            self.x[0],self.y[0]=self.rrts(Robject['P1'])
            peak=Robject['peak']
            peak=peak if peak <=1 else log10(peak)+1

            if self.todraw=='Point Load' or self.todraw=='Moment':
                self.count=1
                self.x[1],self.y[1]=self.rrts(Robject['P1']-peak*Robject['normal'])

            else:
                self.count=2
                self.x[1],self.y[1]=self.rrts(Robject['P3'])            
                self.x[2],self.y[2]=self.rrts(Robject['P3']-peak*Robject['normal'])
            self.parent=self.df[self.df['Name']==Robject['psName']]['Graphitem'].iloc[0]            
            self.drawAll(name=name)
        delete(self,item['Graphitem'])
        self.todraw=None
        self.count=0
        editDialog.close()
    done.clicked.connect(accept)
    editDialog.show()


class TreeWidget(QTreeWidget):
    def __init__(self,parent=None,arg=None):
        super().__init__(parent=parent)
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Control:
            self.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        if event.key()==Qt.Key_Escape :
            pass
        else:
            QTreeWidget.keyPressEvent(self,event)

    def keyReleaseEvent(self, event):
        if event.key()== Qt.Key_Control:
            # self.selectedEditableItems=self.selectedItems()
            self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        QTreeWidget.keyReleaseEvent(self,event)

    

class ObjectTree(TreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
    def setupUi(self,Form,MainWindow):
        Form.resize(320, 566)
        Form.setWindowTitle('Object Tree')
        self.gridLayout = QGridLayout(Form)
        self.treeWidget = TreeWidget(Form)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)

        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setIndentation(15)
        self.treeWidget.setAnimated(True)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 2, 2)
        
        # self.treeWidget.setEditTriggers(self.treeWidget.AllEditTriggers)
        
        self.pushbutton=QPushButton('Expand')
        def changesize():
            ph = MainWindow.height()
            px = MainWindow.geometry().x()
            py = MainWindow.geometry().y()
            if self.pushbutton.text()=='Expand':                
                Form.setGeometry(px, py + 100, 1200, ph - 130)
                self.pushbutton.setText('Collapse')
            else:   
                Form.setGeometry(px, py + 100, 320, ph - 130)
                self.pushbutton.setText('Expand')                
        # self.pushbutton.clicked.connect(changesize)     
        # self.gridLayout.addWidget(self.pushbutton,0,0,1,2)
        header=QTreeWidgetItem()
        header.setText(0,'Structure')
        self.treeWidget.setHeaderItem(header)
        self.segment = QTreeWidgetItem(self.treeWidget)
        self.segment.setText(0,'Segment')
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("./UI/icons/line.png"), QIcon.Normal, QIcon.Off)
        self.segment.setIcon(0, icon1)
        
        self.treeWidget.addTopLevelItem(self.segment)
        segmentProperties=['Segments','P1','P3','P2','youngsModulus','shearModulus','area','I','shapeFactor','alpha','density','type']
        self.treeWidget.setColumnCount(12)
        
        [self.treeWidget.topLevelItem(0).setText(i,segmentProperties[i]) for i in range(12)]

       
        
        loadProperties =['Loads','degree','parentSegment','P1','P3','normal','peak']
        self.load = QTreeWidgetItem(self.treeWidget)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./UI/icons/polyload.png"), QIcon.Normal, QIcon.Off)
        self.load.setIcon(0, icon2)
        self.treeWidget.addTopLevelItem(self.load)
        [self.treeWidget.topLevelItem(1).setText(i,loadProperties[i]) for i in range(7)]
       
        supportProperties = ['Supports','type','location','settlement','normal']
        self.support = QTreeWidgetItem(self.treeWidget)
        icon = QIcon()
        icon.addPixmap(QPixmap("./UI/icons/hinge.png"), QIcon.Normal, QIcon.Off)
        self.support.setIcon(0, icon)
        self.treeWidget.addTopLevelItem(self.support)
        [self.treeWidget.topLevelItem(2).setText(i,supportProperties[i]) for i in range(5)]
       


        self.treeWidget.expandAll()

def selectionChanged(self):
    sEI=self.ot.treeWidget.selectedEditableItems
    sitems=self.ot.treeWidget.selectedItems()
    if self.ot.treeWidget.selectionMode()==QtWidgets.QAbstractItemView.MultiSelection and len(sitems)>0:
        sEI.append([self.ot.treeWidget.currentItem(),self.ot.treeWidget.currentColumn()])
    else:        
        self.ot.treeWidget.selectedEditableItems=[[self.ot.treeWidget.currentItem(),self.ot.treeWidget.currentColumn()]]
def editObjectTree(self):
    tree=self.ot.treeWidget
    if not tree.currentItem():
        return
    originalColumn=tree.currentColumn()    
    originalText = tree.currentItem().text(originalColumn)
    if not tree.selectedEditableItems:
        return
    for currentItemlist in tree.selectedEditableItems:
        try:
            currentItem=currentItemlist[0]
            column=currentItemlist[1]
            previousData=None
            row=currentItem.parent().indexOfChild(currentItem)            
            
            parent=currentItem.parent()
            parentName=parent.text(0)[:-1].lower()    

            data=self.df[(self.df['Class']==parentName)].iloc[row,2]
            name=self.df[(self.df['Class']==parentName)].iloc[row,0]
            index= self.df[self.df['Name']==name].index[0]
            columnName=parent.text(column)
            currentText = originalText

            if columnName not in ['Segments','Loads','Supports']:
                previousData=data[columnName]
                if columnName in ['P1','P2','P3','normal','location','settlement']:                
                    currentText=re.sub('[\[\]]','',currentText)
                    currentText=re.split(',| ',currentText)
                    while '' in currentText:currentText.remove('')
                    if len(currentText)==2:
                        currentText=array(currentText,dtype=float) 
                    else:                    
                        if columnName=='normal':
                            currentText=array([0]+[currentText[0]],dtype=float)
                        else:
                            currentText=array([currentText[0]]+[0],dtype=float)     

                elif columnName=='type':
                    if parentName == 'Supports':
                        currentText=currentText.title()
                    elif parentName == 'Segments':
                        currentText = currentText.lower()    
                elif columnName=='parentSegment':
                    pass
                else:
                    try:
                        currentText=float(currentText)
                    except ValueError:
                        currentText=float(currentText[1])
                    except:
                        raise Exception
                        continue
            else:
                previousData=name
                if currentText not in list(self.df['Name']):
                    self.df.iat[index,0]=currentText
                else:
                    raise NameError
            item=currentItem
            if columnName=='parentSegment':
                combo=tree.itemWidget(currentItem,column)         
                currentText=combo.currentText()
                data[columnName]=self.df[self.df['Name']==currentText].iloc[0]['Robject']
                data=make2d(list(data.values()))
                item.setData(column+1,2,str(data['P1']))
                item.setData(column+2,2,str(data['P3']))
                item.setData(column+3,2,str(data['normal']))
                item.setData(column+4,2,str(data['peak']))
                data.update({'psName':currentText})
            elif columnName in ['Segments','Loads','Supports']:
                pass
            else:
                data[columnName]=currentText
                data=make2d(list(data.values()))
                item.setData(column,2,str(data[columnName]))
        
            self.df.iat[index,2]=data    
            if columnName in editableitems:
                if parentName=='segment':
                    Rsegment = data
                    
                    data=segPlotData2(Rsegment['type'],self.rrts(Rsegment['P1']),
                    self.rrts(Rsegment['P3']),scale=1,P2=self.rrts(Rsegment['P2']),no=self.NoOfPointsInCurvedSegments)
                    pen=self.pen

                elif parentName=='support':
                    Rsupport=data
                    data=supportPlotData2(Rsupport['type'] , self.rrts(Rsupport['location']),1,Rsupport['normal'])
                    color=self.supportColors[Rsupport['type']]
                    self.supportPen=QPen(QColor(*color),1.5)
                    pen=self.supportPen

                else:
                    Rload=data
                    ps=data['parentSegment']
                    pen=self.loadPen
                    # psName=self.df[(self.df['Graphitem']==self.parent)]['Name'].iloc[0]
                    # Rload.update({'psName':psName})                    

                    if Rload['degree']> -3:
                        data=loadPlotData2(self.rrts(Rload['P1']),self.rrts(Rload['P3']),self.rrts(ps['P1']),self.rrts(ps['P3']),
                        self.rrts(ps['P2']), Rload['degree'],self.rrts(Rload['peak']),Rload['normal'],ps['type'],self.scale,self.loadLogScale)
                    else:
                        data=loadPlotData4(ps,Rload['degree'],self.rrts(Rload['peak']))



                rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
                for i in range(1,len(data),1):
                    rect.lineTo(QtCore.QPointF(data[i][0],data[i][1]))
                rect=self.scene.addPath(rect,pen) 
                rect.setFlag(QGraphicsItem.ItemIsSelectable)
                from structure2d.mouseGraphics import delete

                # self.df.iloc[index,3].hide()
                delete(self,item=self.df.iloc[index,3])
                self.df.iat[index,3]=self.scene.items()[0]
        # except NameError:
        #     self.statusbar.showMessage('Enter a unique name',5000)
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()

            if type(previousData)!=type(None):
                currentItem.setData(column,2,str(previousData))
            self.statusbar.showMessage('Enter a valid data',2000)
        self.app.processEvents()

    tree.selectedEditableItems=[]
def toggleObjectTree(self):
    if self.actionObject_Tree.isChecked():
        self.dockObjectTree.show()
        self.actionObject_Tree.setChecked(True)
    else:
        self.dockObjectTree.close()    
        self.actionObject_Tree.setChecked(False)

def objectTree(self,MainWindow):
    # if self.actionObject_Tree.isChecked():
    #     self.dockObjectTree.show()
    # else:
    #     self.dockObjectTree.close()
    self.ot.treeWidget.expandAll()
    # self.actionObject_Tree.toggled['True'].connect(self.dockObjectTree.show)
    # self.actionObject_Tree.toggled['False'].connect(self.dockObjectTree.close)
    self.ot.treeWidget.selectedEditableItems=[]
    self.dockObjectTree.visibilityChanged['bool'].connect(self.actionObject_Tree.setChecked)
    def menuContextuelAlbum(self):
        def delete():
            a = self.ot.treeWidget.selectedItems()
            if len(a) != 0:
                self.changeFlag(name=a[0].text(0))
                index = self.df[self.df["Name"] == a[0].text(0)].index[0]
                self.history = append(self.history, index)
                self.historystatus = True

        self.ot.menu = QtWidgets.QMenu(self.ot.treeWidget)
        # self.ot.actionDiagrams = self.ot.menu.addAction("Diagrams")
        self.ot.actiondelete = self.ot.menu.addAction("Delete")
        self.ot.actiondelete.triggered.connect(delete)

        def analysestr():
            a = self.ot.treeWidget.selectedItems()
            if len(a) != 0:
                if self.analyseStatus < len(self.df):
                    self.structure = structify2d(self.df.loc[self.df["Flag"] == True]["Robject"])
                    worker = WorkerThread(frame2d, self.structure)
                    def assign(s):self.matrix=s
                    worker.signals.result.connect(assign)
                    worker.signals.finished.connect(lambda : self.diagrams(a[0].text(0)))
                    self.threadpool.start(worker)

                else:
                    self.diagrams(a[0].text(0))
                self.analyseStatus = len(self.df)

        # self.ot.actionDiagrams.triggered.connect(analysestr)
        self.ot.menu.exec_(QtGui.QCursor.pos())
    
    
    self.ot.treeWidget.itemChanged.connect(lambda:editObjectTree(self))
    self.ot.treeWidget.itemClicked.connect(lambda:selectionChanged(self))
    self.ot.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.ot.treeWidget.customContextMenuRequested.connect(lambda:menuContextuelAlbum(self))
    self.oT.show()



