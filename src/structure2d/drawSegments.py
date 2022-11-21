from PySide2 import QtGui,QtCore,QtWidgets
from PySide2.QtWidgets import QGraphicsItem
from numpy import array,delete,append,round
from sdPy.extensions import convert, transform
# from segmentFunctions import segmentDialog
from sdPy.segmentMethods import segPlotData2
import warnings
from sdPy.functionDefinitions import make2d
from numpy.core.umath import arctan2


# QPainterPath RoundItem::shape() const
# {
#     QPainterPath path;
#     path.addEllipse(boundingRect());
#     return path;
# }
# class QPath(QtGui.QPainterPath):
#     def __init__(self,parent=None):
#         QtGui.QPainterPath.__init__(self,parent)
#     def boundingRect(self):
#         print('Hello')
def tempDrawSegment(self,x,y):
    # x=event.scenePos().x()
    # y=event.scenePos().y()
    try:
        with warnings.catch_warnings(record=True) as w:
            data=segPlotData2(self.todraw,array([self.x[0],self.y[0]]),array([self.x[1],self.y[1]]),P2=array([x,y]),no=20,scale=1)     
        # data=delete(data,0,1)
        rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
        for i in range(2,len(data),2):
            rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
        rect=self.scene.addPath(rect) 
        if not len(w):
            self.delete=True
    except Exception as e:
        self.delete=False
        self.statusbar.showMessage(str(e),2000)        



def drawLine(self,pen=None,properties=None,name=None):
    if self.delete==True:
        self.scene.removeItem(self.scene.items()[0])

    # if True:
    try:
        p1=array([self.x[0],self.y[0]])  
        p3=array([self.x[1],self.y[1]])  
        if properties == None:
            material=self.materialChoices.currentIndex()+1
            section=self.sectionChoices.currentIndex()+1

            ym=convert(float(self.material.iloc[material,2]),[1,-2,0],['SI',1,1,'C'],[self.currentUnit,self.force,self.length,'C'])
            sm=convert(float(self.material.iloc[material,3]),[1,-2,0],['SI',1,1,'C'],[self.currentUnit,self.force,self.length,'C'])
            alpha=convert(float(self.material.iloc[material,4]),[1,-2,0],['SI',1,1,'C'],[self.currentUnit,self.force,self.length,'C'])
            density=convert(float(self.material.iloc[material,5]),[1,-2,0],['SI',1,1,'C'],[self.currentUnit,self.force,self.length,'C'])


            area=convert(float(self.section.iloc[section,2]),[0,2,0],['SI',1,1,'C'],[self.currentUnit,self.force,self.length,'C'])
            ixx=convert(float(self.section.iloc[section,3]),[0,4,0],['SI',1,1,'C'],[self.currentUnit,self.force,self.length,'C'])
            sf=self.section.iloc[section,6]
            properties=[ym,sm,area,ixx,sf,alpha,density]
            # properties=[round(i,max(3,self.precison)) for i in properties]
            # print(properties)
        if self.todraw=='line':
            line=self.scene.addLine(self.x[0],self.y[0],self.x[1],self.y[1],pen)
            line.setFlag(QGraphicsItem.ItemIsSelectable)
            line.setFlag(QGraphicsItem.ItemIsMovable)

            Rsegment=make2d([self.todraw, self.rts(p1), self.rts(p3), self.rts((p1+p3)/2), *properties])
        elif self.todraw=='arc' or self.todraw=='quad':
            p2=array([self.x[2],self.y[2]])  
            with warnings.catch_warnings(record=True) as w:
                data=segPlotData2(self.todraw,array([self.x[0],self.y[0]]),array([self.x[1],self.y[1]]),P2=array([self.x[2],self.y[2]]),no=self.NoOfPointsInCurvedSegments,scale=1)        
                Rsegment=make2d([self.todraw, self.rts(p1), self.rts(p3), self.rts(p2),*properties])
            if len(w):
                self.statusbar.showMessage(str(w[0].message),2000)
            # data=delete(data,0,1)
            rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
            # rect = QPath(QtCore.QPointF(data[0][0],data[0][1]))  
            for i in range(2,len(data),2):
                rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
            rect=self.scene.addPath(rect,pen) 
            # rect.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemClipsToShape)
            rect.setFlag(QGraphicsItem.ItemIsSelectable)

        item=QtWidgets.QTreeWidgetItem()
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        name= name if name else str(self.segmentNumber)+' - ' +self.todraw.capitalize()
        self.df.loc[len(self.df)]=[name,'segment',Rsegment,self.scene.items()[0],item,True]
        self.ot.segment.addChild(item)   
        item.setText(0,name)
        [self.ot.segment.child(self.segmentNumber-1).setData(i+1,2,str(list(Rsegment.values())[i+1])) for i in range(3)]           
        [self.ot.segment.child(self.segmentNumber-1).setData(i+1,2,str(list(Rsegment.values())[i+1])) for i in range(3,10)]
        self.ot.segment.child(self.segmentNumber-1).setData(11,2,Rsegment['type'])
        # from structure2d.objectsTable import addDataToTable
        # addDataToTable(self,0,name,Rsegment)
        self.segmentNumber += 1
        self.history=append(self.history,len(self.df)-1)
        self.historystatus=True
        self.snapPoints.append([Rsegment['P1'],Rsegment['P2'],Rsegment['P3']])


    except Exception as e:
        import traceback
        traceback.print_exc()
        self.statusbar.showMessage(str(e),2000)
    self.x[0],self.y[0]=self.x[1],self.y[1]
    self.count=0
    self.delete=False