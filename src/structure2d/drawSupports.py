from operator import add

from numpy.linalg.linalg import norm
from structure2d.objectsTable import addDataToTable
from sdPy.supportMethods import supportPlotData2

from PySide2 import QtGui,QtCore,QtWidgets
from PySide2.QtWidgets import QGraphicsItem
from numpy import array,delete,append
from sdPy.functionDefinitions import make2d
from sdPy.extensions import snap2seg2
from PySide2.QtGui import QPixmap,QColor,QPen
from sampleDatas import resource_path
from structure2d.objectsTable import addDataToTable
def drawSupport(self,pen=None,normal=array([0,1]),name=None):
    if type(normal)==type(None):
        normal=array([0,1])

    if not pen:
        pen=self.supportPen
    location=array([self.x[0],self.y[0]])
    try:
        a=self.scene.selectedItems()[0]
        parent=self.df[self.df['Graphitem']==a]['Robject'].iloc[0]
        location=self.rrts(snap2seg2(parent,self.rts(location)))
    except:
        pass    
    if self.todraw=='custom Support':
        self.todraw=self.customSupportParameters
    data=supportPlotData2(self.todraw,location,normal=normal,scale=self.scale)        
    # data=delete(data,0,1)
    rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
    for i in range(1,len(data)):
        rect.lineTo(QtCore.QPointF(QtCore.QPointF(data[i][0],data[i][1])))
        # rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
    supportName =name if name else str(self.supportNumber)+ ' - '+ self.todraw 
    settlement=[0,0,0]
    Rsupport = make2d([self.todraw, self.rts(location),settlement,normal])
    rect=self.scene.addPath(rect,pen) 
    rect.setFlag(QGraphicsItem.ItemIsSelectable)
    self.delete=False


    item=QtWidgets.QTreeWidgetItem()
    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
    self.df.loc[len(self.df)]=[supportName,'support',Rsupport,self.scene.items()[0],item,True]
    self.ot.support.addChild(item)   
    item.setText(0,supportName)
    [self.ot.support.child(self.supportNumber-1).setData(i+1,2,str(list(Rsupport.values())[i])) for i in range(4)]           
    # addDataToTable(self,2,supportName,Rsupport)
    self.supportNumber+=1
    self.history=append(self.history,len(self.df)-1)
    self.historystatus=True     
    self.snapPoints.append([Rsupport['location']])



def supports(self, todraw):
    self.todraw = todraw
    color=self.supportColors[self.todraw]
    self.supportPen=QPen(QColor(*color),1.5)
    if self.todraw=='custom Support':
        self.customSupportParameters='000'
        
        form=QtWidgets.QDialog(parent=self.MainWindow)
        form.setWindowTitle('Custom Support')
        vlayout=QtWidgets.QVBoxLayout(form)
        vlayout.addWidget(QtWidgets.QLabel('Check boxes to restrain forces/moments'))
        # supportParameters=QtWidgets.QLineEdit()
        # supportParameters.setValidator(input_validator)
        fx=QtWidgets.QCheckBox('Fx')
        fy=QtWidgets.QCheckBox('Fy')
        M=QtWidgets.QCheckBox('M')
        ok=QtWidgets.QPushButton('OK')
        vlayout.addWidget(fx)
        vlayout.addWidget(fy)
        vlayout.addWidget(M)
        vlayout.addWidget(ok)

        def setCustomDetails():            
            self.customSupportParameters=[fx.isChecked(),fy.isChecked(),M.isChecked()]
            self.customSupportParameters=['1' if x==True else '0' for x in self.customSupportParameters]
            self.customSupportParameters=''.join(self.customSupportParameters)
            form.close()
        ok.clicked.connect(setCustomDetails)
        # supportParameters.returnPressed.connect(setCustomDetails)
        # vlayout.addWidget(supportParameters)
        form.setLayout(vlayout)
        
        form.show()   

    self.member = 'support'
    self.count = 0
    if self.delete == True:
        self.delete = False
        self.scene.removeItem(self.scene.items()[0])
    cursor=QPixmap(resource_path(self.cursorPath+"draw"+self.todraw+".png"))
    self.graphicsView.setCursor(QtGui.QCursor(cursor,0,32))