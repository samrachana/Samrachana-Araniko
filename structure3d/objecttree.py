from PySide2.QtWidgets import QTreeWidget,QDialog ,QGridLayout,QTreeWidgetItem,QPushButton
from PySide2.QtGui import QIcon,QPixmap
from PySide2.QtCore import Qt
from UI.objectTable import Ui_MainWindow as objectsTable
from PySide2 import QtGui,QtWidgets
from numpy import array,append
from sdPy.functionDefinitions import structify
from threads import WorkerThread
from sdPy.structureMethods import frame3d

from sdPy.segmentMethods import segPlotData
from sdPy.loadMethods import loadPlotData
from sdPy.supportMethods import supportPlotData
from structure3d.plot import Plot

def objectTree(self,MainWindow):

    self.ot.treeWidget.expandAll()
    ph = MainWindow.height()
    px = MainWindow.geometry().x()
    py = MainWindow.geometry().y()
    dw = self.oT.width()
    # dh = self.oT.height()

    self.oT.setGeometry(px, py + 100, dw, ph - 130)
    def edit():
        try:
            row=self.ot.treeWidget.currentItem().parent().indexOfChild(self.ot.treeWidget.currentItem())            
            column=self.ot.treeWidget.currentColumn()
            parent=self.ot.treeWidget.currentItem().parent()
            parentName=parent.text(0)[:-1].lower()        
            data=self.df[(self.df['Class']==parentName)& (self.df['Flag']==True)].iloc[row,2]
            name=self.df[(self.df['Class']==parentName)& (self.df['Flag']==True)].iloc[row,0]
            # print(row,len(data),self.df[self.df['Robject']==data])
            index= self.df[self.df['Name']==name].index[0]
            currentText = self.ot.treeWidget.currentItem().text(column)
            columnName=parent.text(column)
            
            # visibleItems=self.df[self.df['Flag']==True]

            try:
                currentText=eval(currentText)
            except SyntaxError:
                currentText=array(currentText[1:-1].split(),dtype=float)    
            except:
                pass
            if columnName not in ['Segments','Loads','Supports']:
                data[columnName]=currentText
                self.df.iat[index,3]=data
            else:
                self.df.iat[index,1]=currentText
            editableitems=['P1','P2','P3','peak','normal','location','degree','type']

            if columnName in editableitems:

                if parentName=='segment':
                    Rsegment = data
                    sdata=segPlotData(Rsegment['type'],Rsegment['P1'],Rsegment['P3'],Rsegment['axisVector'],self.scale,Rsegment['P2'])
                    Plot.plott(Plot, array(sdata), self.graphWidget, self.segmentColor,self.segmentWidth)      
                    self.df.iloc[index,3].hide()
                    self.df.iat[index,3]=self.graphWidget.items[-1]
                elif parentName=='support':
                    Rsupport=data
                    Rsupportdata=supportPlotData(Rsupport['type'] , Rsupport['location'],self.scale,Rsupport['normal'])
                    color = self.supportColors[data['type']]
                    Plot.plotsupport(Plot,array(Rsupportdata), self.graphWidget, color)
                    self.df.iloc[index,3].hide()
                    self.df.iat[index,3]=self.graphWidget.items[-1]
                else:
                    Rload=data
                    ps=data['parentSegment']
                    Rloaddata=loadPlotData(Rload['P1'],Rload['P3'],ps['P1'],ps['P3'],
                    ps['P2'], Rload['degree'],Rload['peak'],Rload['normal'],ps['type'],self.scale)
                    Plot.plott(Plot, array(Rloaddata), self.graphWidget, self.loadColor,self.loadWidth)
                    self.df.iloc[index,3].hide()
                    self.df.iat[index,3]=self.graphWidget.items[-1]
        except Exception :
            self.statusbar.showMessage('Enter a valid data',2000)
    
    def menuContextuelAlbum(self):
        def delete():
            a = self.ot.treeWidget.selectedItems()
            if len(a) != 0:
                self.changeFlag(name=a[0].text(0))
                index = self.df[self.df["Name"] == a[0].text(0)].index[0]
                self.history = append(self.history, index)
                self.historystatus = True
            # self.ot.treeWidget.takeTopLevelItem(self.ot.treeWidget.indexOfTopLevelItem(a[0]))

        self.ot.menu = QtWidgets.QMenu(self.ot.treeWidget)
        # self.ot.actionedit = self.ot.menu.addAction("Edit")
        self.ot.actionDiagrams = self.ot.menu.addAction("Diagrams")
        self.ot.actiondelete = self.ot.menu.addAction("Delete")
        self.ot.actiondelete.triggered.connect(delete)

        def analysestr():
            a = self.ot.treeWidget.selectedItems()
            if len(a) != 0:
                if self.analyseStatus < len(self.df):
                    self.structure = structify(self.df.loc[self.df["Flag"] == True]["Robject"])
                    worker = WorkerThread(frame3d, self.structure)
                    def assign(s):self.matrix=s
                    worker.signals.result.connect(assign)
                    worker.signals.finished.connect(lambda : self.diagrams(a[0].text(0)))
                    self.threadpool.start(worker)

                else:
                    self.diagrams(a[0].text(0))
                self.analyseStatus = len(self.df)

        self.ot.actionDiagrams.triggered.connect(analysestr)
        self.ot.menu.exec_(QtGui.QCursor.pos())
    
    
    self.ot.treeWidget.itemChanged.connect(edit)
    self.ot.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.ot.treeWidget.customContextMenuRequested.connect(lambda:menuContextuelAlbum(self))
    self.oT.show()










class ObjectTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
    def setupUi(self,Form,MainWindow):
        Form.resize(320, 566)
        Form.setWindowTitle('Object Tree')
        self.gridLayout = QGridLayout(Form)
        self.treeWidget = QTreeWidget(Form)
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
        self.pushbutton.clicked.connect(changesize)     
        self.gridLayout.addWidget(self.pushbutton,0,0,1,2)
        header=QTreeWidgetItem()
        header.setText(0,'Structure')
        self.treeWidget.setHeaderItem(header)
        self.segment = QTreeWidgetItem(self.treeWidget)
        self.segment.setText(0,'Segment')
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("./UI/icons/line.png"), QIcon.Normal, QIcon.Off)
        self.segment.setIcon(0, icon1)
        
        self.treeWidget.addTopLevelItem(self.segment)
        segmentProperties=['Segments','P1','P3','P2','youngsModulus','shearModulus','area','Iyy','Izz','J','shapeFactor','axisVector','type']
        self.treeWidget.setColumnCount(13)
        
        [self.treeWidget.topLevelItem(0).setText(i,segmentProperties[i]) for i in range(13)]

       
        
        loadProperties =['Loads','degree','parentSegment','P1','P3','normal','peak']
        self.load = QTreeWidgetItem(self.treeWidget)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./UI/icons/polyload.png"), QIcon.Normal, QIcon.Off)
        self.load.setIcon(0, icon2)
        self.treeWidget.addTopLevelItem(self.load)
        [self.treeWidget.topLevelItem(1).setText(i,loadProperties[i]) for i in range(7)]
       
        supportProperties = ['Supports','type','location','settlements','normal']
        self.support = QTreeWidgetItem(self.treeWidget)
        icon = QIcon()
        icon.addPixmap(QPixmap("./UI/icons/hinge.png"), QIcon.Normal, QIcon.Off)
        self.support.setIcon(0, icon)
        self.treeWidget.addTopLevelItem(self.support)
        [self.treeWidget.topLevelItem(2).setText(i,supportProperties[i]) for i in range(5)]
       


        self.treeWidget.expandAll()


if __name__ == '__main__':
    from PySide2.QtWidgets import QDialog,QApplication
    import sys
    app=QApplication(sys.argv)
    aa=QDialog()
    dia= ObjectTree()
    dia.setupUi(aa)
    aa.show()
    app.exec_()

import ast
def listConverter(tempdf):
        for i in range(len(tempdf)):
            x=tempdf.iloc[i,3]       
            tempdf.iat[i,3]=ast.literal_eval(x)
        
        return tempdf







def objects(tempdf):

    objectTable= objectsTable()
    objectTable.setupUi(aa)

    segments=tempdf[(tempdf['Class']=='segment')&(tempdf['Flag']==True)]['Robject']
    r,c=len(segments),12

    for i in range(r):
        objectTable.segmentsTable.insertRow(i)
        for j in range(2,c):
            if j==5:
                materialbox=QtWidgets.QComboBox()
                materialbox.addItems(['ram','hari'])
                objectTable.segmentsTable.setCellWidget(i,j,materialbox)
            elif j==6:
                materialbox=QtWidgets.QComboBox()
                objectTable.segmentsTable.setCellWidget(i,j,materialbox)
            else:    
                data=str(segments.iloc[i][j])
                objectTable.segmentsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
        objectTable.segmentsTable.itemPressed.connect(lambda:print(objectTable.segmentsTable.selectedItems())  )  

# import pandas as pd 
# df=pd.read_csv('/home/xx/Desktop/StructDote/sampleFiles/BurjKhalifa-3x3x1.csv')
# df=listConverter(df) 
# objects(df)
# aa.show()
# app.exec_()    