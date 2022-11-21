from sdPy.functionDefinitions import make2d
from UI.objectsTable import Ui_MainWindow as objectsTableUI
from PySide2.QtWidgets import QGraphicsItem, QMainWindow,QHeaderView, QTableWidgetItem,QComboBox
from numpy import array
import re
from sdPy.segmentMethods import segPlotData2
from sdPy.loadMethods import loadPlotData2, loadPlotData4
from sdPy.supportMethods import supportPlotData2
from PySide2.QtGui import QPainterPath, QPen,QColor
from PySide2.QtCore import Qt,QPointF
segmentColumns={
    0:'Name',
    1:'P1',
    2:'P3',
    3:'P2',
    4:'youngsModulus',
    5:'shearModulus',
    6:'area',
    7:'I',
    8:'shapeFactor',
    9:'density',
    10:'alpha',
    11:'type'}
loadColumns={
    0:'Name',
    1:'degree',
    2:'peak',
    3:'parentSegment',
    4:'P1',
    5:'P3',
    6:'normal',
    }
supportColumns={
    0:'Name',
    1:'type',
    2:'location',
    3:'normal',
    4:'settlement'
    }
columnTypes={0:segmentColumns,1:loadColumns,2:supportColumns}
tableClass={0:'segment',1:'load',2:'support'}
editableitems=['P1','P2','P3','peak','normal','location','degree','type','parentSegment']

def editObjectsTable(self):
    pass

def addDataToTable(self,tableIndex,name,values):
    table=self.objectTables[tableIndex]
    rows = table.rowCount()
    columns = table.columnCount()
    table.insertRow(rows)
    table.setItem(rows,0,QTableWidgetItem(name))
    columnHeaders=columnTypes[tableIndex]
    for i in range(1,columns):
        table.setItem(rows,i,QTableWidgetItem(str(values[columnHeaders[i]])))
    if tableIndex==1:
        combo=QComboBox()
        combo.addItems(reversed(list(self.df[(self.df['Class']=='segment')&(self.df['Flag']==True)]['Name'])))
        combo.currentIndexChanged.connect(lambda:editObjectsTable(self))
        combo.setCurrentText(self.df[(self.df['Graphitem']==self.parent)]['Name'].iloc[0])
        table.setCellWidget(rows,3,combo)        


def editMembers(self,tab): 
    try:
        currentItem=self.objectTables[tab].currentItem()
        self.graphicsView.setFocus()
        if currentItem:
            row=currentItem.row()
            column=currentItem.column()
            currentText=currentItem.text()
            columnName=columnTypes[tab][column]
            data=self.df[(self.df['Class']==tableClass[tab]) & (self.df['Flag']==True)].iloc[row,2]
            index= self.df[(self.df['Class']==tableClass[tab]) & (self.df['Flag']==True)].index[0]

            if columnName not in['Name','parentSegment']:
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
                    currentText=currentText.capitalize()
                else:
                    currentText=float(currentText)
            else:
                if currentText not in list(self.df['Name']):
                    self.df.iat[index,0]=currentText
                else:
                    raise NameError                       
            if columnName=='parentSegment':
                combo=self.ee.loadsTable.cellWidget(row,column)                
                currentText=combo.currentText()
                data[columnName]=self.df[self.df['Name']==currentText].iloc[0]['Robject']
                data=make2d(list(data.values()))
                self.ee.loadsTable.setItem(row,4,QTableWidgetItem(data['P1']))
                self.ee.loadsTable.setItem(row,5,QTableWidgetItem(data['P3']))
                self.ee.loadsTable.setItem(row,6,QTableWidgetItem(data['normal']))
                self.ee.loadsTable.setItem(row,2,QTableWidgetItem(data['peak']))
            else:
                # prevData=data[columnName]
                data[columnName]=currentText
                data=make2d(list(data.values()))
                self.df.iat[index,2]=data

                print(row,column)
                if str(self.prevData)==str(data[columnName]):
                    return
                self.prevData=data[columnName]
                
                self.objectTables[tab].setItem(
                    row,column,QTableWidgetItem(str(currentText))
                    )
            if columnName in editableitems:
                if tab==0:
                    Rsegment = data                
                    data=segPlotData2(Rsegment['type'],self.rrts(Rsegment['P1']),
                    self.rrts(Rsegment['P3']),scale=1,P2=self.rrts(Rsegment['P2']),no=self.NoOfPointsInCurvedSegments)
                    pen=self.pen

                elif tab==2:
                    Rsupport=data
                    data=supportPlotData2(Rsupport['type'] , self.rrts(Rsupport['location']),1/(self.scale*50),Rsupport['normal'])
                    color=self.supportColors[Rsupport['type']]
                    self.supportPen=QPen(QColor(*color),1.5)
                    pen=self.supportPen

                else:
                    Rload=data
                    ps=data['parentSegment']
                    pen=self.loadPen

                    if Rload['degree']> -3:
                        data=loadPlotData2(self.rrts(Rload['P1']),self.rrts(Rload['P3']),self.rrts(ps['P1']),self.rrts(ps['P3']),
                        self.rrts(ps['P2']), Rload['degree'],self.rrts(Rload['peak']),Rload['normal'],ps['type'],self.scale,self.loadLogScale)
                    else:
                        data=loadPlotData4(ps,Rload['degree'],self.rrts(Rload['peak']))



                rect = QPainterPath(QPointF(data[0][0],data[0][1]))
                for i in range(1,len(data),1):
                    rect.lineTo(QPointF(data[i][0],data[i][1]))
                rect=self.scene.addPath(rect,pen) 
                rect.setFlag(QGraphicsItem.ItemIsSelectable)

                self.df.iloc[index,3].hide()
                self.df.iat[index,3]=self.scene.items()[0]            

    except NameError:
        self.statusbar.showMessage('Enter a unique name',5000)
    except:
        import traceback
        traceback.print_exc()
        self.statusbar.showMessage('Enter a valid data',5000)
def editLoads(self):
    pass

def editSupports(self):
    pass



def objectsTable(self):
    self.eE=QMainWindow(parent=self.MainWindow)
    self.ee=objectsTableUI()
    self.ee.setupUi(self.eE)
    self.prevData=None
    self.objectTables={
        0:self.ee.segmentsTable,
        1:self.ee.loadsTable,
        2:self.ee.supportsTable
    }
    [self.objectTables[i].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) for i in [0,1,2]]
    self.ee.segmentsTable.itemChanged.connect(lambda:editMembers(self,0))
    self.ee.loadsTable.itemChanged.connect(lambda:editMembers(self,1))
    self.ee.supportsTable.itemChanged.connect(lambda:editMembers(self,2))
    self.eE.show()