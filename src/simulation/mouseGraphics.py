from PySide2.QtGui import QTransform
from PySide2.QtWidgets import QGraphicsTextItem

from PySide2 import QtWidgets,QtCore,QtGui
from numpy import array,pi,arctan2
from PySide2.QtCore import Qt
from sdPy.functionDefinitions import unit
from numpy.linalg import norm
from math import sqrt,pi,atan2
from sdPy.segmentMethods import arcLength, quadLength

myround=lambda number,base: base*round(number/base)
class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__ (self, ui,parent=None):
        self.ui=ui
        self.ui.count=0
        self.ui.x=[0,0,0]
        self.ui.y=[0,0,0]
        self.ui.todraw=None
        super(GraphicsScene, self).__init__ (parent)
        self._pan=False
        self.ui.delete=False
        self.ui.deleteText=False
        # self.setAcceptDrops(True)

    def mouseMoveEvent(self,event):
        if self._pan:        
            self.ui.graphicsView.horizontalScrollBar().setValue(self.ui.graphicsView.horizontalScrollBar().value() - (event.scenePos().x() - self._panStartX))
            self.ui.graphicsView.verticalScrollBar().setValue(self.ui.graphicsView.verticalScrollBar().value() + (event.scenePos().y() - self._panStartY))
            self._panStartX = event.scenePos().x()
            self._panStartY = event.scenePos().y()
            event.accept()
            return            
    
        x=event.scenePos().x()
        y=event.scenePos().y()

        if event.modifiers()&QtCore.Qt.ControlModifier:
            angle=arctan2(event.scenePos().x()-self.ui.x[self.ui.count-1],event.scenePos().y()-self.ui.y[self.ui.count-1])*180/pi
            angle=abs(round(angle))
            if event.modifiers()&QtCore.Qt.ShiftModifier:
                if angle>45 and angle<135:
                    x,y=myround(event.scenePos().x(),50),self.ui.y[self.ui.count-1]
                else:    
                    x,y=self.ui.x[self.ui.count-1],myround(event.scenePos().y(),50)                
                if self.ui.count==0:
                    x,y=myround(event.scenePos().x(),50),myround(event.scenePos().y(),50)
            else:
                if angle>45 and angle<135:
                    x,y=event.scenePos().x(),self.ui.y[self.ui.count-1]
                else:    
                    x,y=self.ui.x[self.ui.count-1],event.scenePos().y()

        else:
            x=event.scenePos().x()
            y=event.scenePos().y()

        if self.ui.delete==True:
            self.ui.scene.removeItem(self.ui.scene.items()[0])
            self.ui.delete=False
     #measure
        if self.ui.deleteText:
            self.ui.scene.removeItem(self.ui.deleteText)
            self.ui.scene.removeItem(self.ui.scene.items()[0])
            self.ui.deleteText=False

        if self.ui.todraw=='measure' and self.ui.count==1:

            x1,y1=self.ui.ui.rts(array([x,y]))
            angle=atan2(y1-self.ui.ui.rts(self.ui.y[0]),x1-self.ui.ui.rts(self.ui.x[0]))
            angle=round(angle*180/pi,self.ui.ui.precison)
            x1,y1=x1-self.ui.ui.rts(self.ui.x[0]),y1-self.ui.ui.rts(self.ui.y[0])
            
            length=(x1*x1+y1*y1)**0.5
            length=round(length,self.ui.ui.precison)
            # self.ui.statusbar.showMessage(f'Length={length}')
            
            text = QGraphicsTextItem()
            text.setPos(self.ui.x[0],self.ui.y[0])
            text.setHtml(f"<h3 style='color:blue'>&#8736;={str(angle)}&#176;</h3>")   
            text.setTransform(QTransform(1., 0., 0., -1., 0, 0))    
            self.ui.scene.addItem(text)
            self.ui.deleteText=self.ui.scene.items()[0]

            text = QGraphicsTextItem()
            text.setPos(x+1,y-1)
            text.setHtml(f"<h3 style='color:blue'>{str(length)}</h3>")   
            text.setTransform(QTransform(1., 0., 0., -1., 0, 0))    
            self.ui.scene.addItem(text)
            self.ui.deleteText=self.ui.scene.items()[0]

            self.ui.scene.addLine(self.ui.x[0],self.ui.y[0],x,y,QtGui.QPen(Qt.DashLine))
            self.ui.delete=True
        
        # x,y=self.ui.ui.rts(array([x,y]))
        # if self.ui.coordinateSystem.currentText()=='Polar':
        #     r=round(sqrt((x**2+y**2)),self.ui.ui.precison)
        #     y=round(atan2(y,x)*180/pi, self.ui.ui.precison)
        #     x=r
        # if self.ui.coordinateMode.currentText()=='Relative' and self.ui.count>0:
            
        #     x,y=x-self.ui.ui.rts(self.ui.x[0]),y-self.ui.ui.rts(self.ui.y[0])
        #     x,y=round(x,self.ui.ui.precison),round(y,self.ui.ui.precison)    
        # if not self.ui.coordinateEdited:
        #     self.ui.editX.setText(str(x))
        #     self.ui.editY.setText(str(y))
        # elif self.ui.coordinateEdited=='y':
        #     self.ui.editX.setText(str(x))
        # elif self.ui.coordinateEdited=='x':
        #     self.ui.editY.setText(str(y))         
        QtWidgets.QGraphicsScene.mouseMoveEvent(self,event)

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton and self.ui.todraw:
            if  event.modifiers()&QtCore.Qt.ControlModifier:
                angle=arctan2(event.scenePos().x()-self.ui.x[self.ui.count-1],event.scenePos().y()-self.ui.y[self.ui.count-1])*180/pi
                angle=abs(round(angle))
                if event.modifiers()&QtCore.Qt.ShiftModifier:
                    if angle>45 and angle<135:
                        x,y=myround(event.scenePos().x(),50),self.ui.y[self.ui.count-1]
                    else:    
                        x,y=self.ui.x[self.ui.count-1],myround(event.scenePos().y(),50)                
                    if self.ui.count==0:
                        x,y=myround(event.scenePos().x(),50),myround(event.scenePos().y(),50)
                else:
                    if angle>45 and angle<135:
                        x,y=event.scenePos().x(),self.ui.y[self.ui.count-1]
                    else:    
                        x,y=self.ui.x[self.ui.count-1],event.scenePos().y()
          
            else:
                x=event.scenePos().x()
                y=event.scenePos().y() 

            x=round(x/50,self.ui.ui.precison)*50
            y=round(y/50,self.ui.ui.precison)*50 
            self.ui.x[self.ui.count],self.ui.y[self.ui.count]=x,y
            self.ui.count=1
            
            if self.ui.count==1 and self.ui.todraw=='measure':
                x=round(x/50,self.ui.ui.precison)*50
                y=round(y/50,self.ui.ui.precison)*50 
                self.ui.x[0],self.ui.y[0]=x,y                
            #     selectedItems=self.ui.scene.selectedItems()
            #     ps=self.ui.df[(self.ui.df['Graphitem']==selectedItems[0])]['Robject']
            #     if not ps.empty:
            #         segment=ps.iloc[0]
            #         if segment['class']=='arc':
            #             length=arcLength(segment['P1'],segment['P3'],segment['P2'])
            #             self.ui.statusbar.showMessage(f'Length={length}')
            #         elif segment['class']=='quad':
            #             length=quadLength(segment['P1'],segment['P3'],segment['P2'])    
            #             self.ui.statusbar.showMessage(f'Length={length}',2000)

        elif event.buttons() & QtCore.Qt.RightButton:
            self._panStartX = event.scenePos().x()
            self._panStartY = event.scenePos().y()
            self.ui.graphicsView.setCursor(Qt.ClosedHandCursor)
            self._pan = True
            event.accept()
            return                          
        # else:
        #     QtWidgets.QGraphicsScene.mousePressEvent(self,event)

    def mouseReleaseEvent(self,event):
        
        if (event.button()& Qt.RightButton):        
            self._pan = False
            self.ui.graphicsView.setCursor(Qt.ArrowCursor)
            event.accept()
            return     
        else:
            QtWidgets.QGraphicsScene.mouseReleaseEvent(self,event)
        # event.ignore()

    def mouseDoubleClickEvent(self,event):
        QtWidgets.QGraphicsScene.mouseDoubleClickEvent(self,event)
        if self.ui.todraw=='measure':
            self.ui.count=0
            selectedItems=self.ui.scene.selectedItems()
            if len(selectedItems):
                ps=self.ui.df[(self.ui.df['Graphitem']==selectedItems[0])]['Robject']   
                if not ps.empty:
                    segment=ps.iloc[0]
                    if segment['type']=='arc':
                        length=arcLength(segment['P1'],segment['P3'],segment['P2'])
                        self.ui.statusbar.showMessage(f'Length={round(length,self.ui.ui.precison)}',3000)
                    elif segment['type']=='quad':
                        length=quadLength(segment['P1'],segment['P3'],segment['P2'])    
                        self.ui.statusbar.showMessage(f'Length={round(length,self.ui.ui.precison)}',3000)
                    elif segment['type']=='line':
                        length= norm(segment['P1']-segment['P3'])   
                        self.ui.statusbar.showMessage(f'Length={round(length,self.ui.ui.precison)}',3000)        
                            
    def wheelEvent(self,event):

        if event.delta()>0:
            self.ui.zoomOut()
        else:    
            self.ui.zoomIn()

    def keyPressEvent(self,event):
        from numpy import append

        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            if self.ui.delete==True:
                self.ui.scene.removeItem(self.ui.scene.items()[0])
                self.ui.delete=False
            if self.ui.deleteText:
                self.ui.scene.removeItem(self.ui.deleteText)
                self.ui.scene.removeItem(self.ui.scene.items()[0])

                self.ui.deleteText=False
            self.ui.todraw=None
            self.ui.count=0

            self.ui.graphicsView.setCursor(QtGui.QCursor(Qt.ArrowCursor))
            self.ui.scene.clearSelection()

        
