from PySide2.QtGui import QPen, QTransform,QCursor
from PySide2.QtWidgets import QGraphicsTextItem,QGraphicsScene,QMenu
from PySide2.QtCore import QPointF, Qt,QPoint

from structure2d.drawSegments import tempDrawSegment
from structure2d.drawLoads import tempDrawLoad
from structure2d.analysis2d import analysisModes
from structure2d.simulate2d import simulationEnvironment
from numpy import array,pi,arctan2,append,argmin,vstack
from PySide2.QtCore import Qt
from sdPy.functionDefinitions import unit
from numpy.linalg import norm
from math import sqrt,pi,atan2
from sdPy.segmentMethods import arcLength, quadLength

myround=lambda number,base: base*round(number/base)
def snapper(self,event):
    x=event.scenePos().x()
    y=event.scenePos().y()
    angle=arctan2(x-self.ui.x[self.ui.count-1],y-self.ui.y[self.ui.count-1])*180/pi
    angle=abs(round(angle))
    if event.modifiers()&Qt.ShiftModifier:
        x=myround(x,50)
        y=myround(y,50)                
    if event.modifiers()&Qt.ControlModifier:
        if angle>45 and angle<135:
            y=self.ui.y[self.ui.count-1]
        else:    
            x=self.ui.x[self.ui.count-1]

    return x,y

def delete(self,item=None):
    if item:
        index = self.df[self.df["Graphitem"] == item].index[0]
        self.changeFlag(index=index)
        self.history = append(self.history, index)
        self.historystatus = True
        return
    if len(self.scene.selectedItems()):

        for a in self.scene.selectedItems():
            if a in self.nodes:
                self.scene.removeItem(a)
                self.nodes.remove(a)
                continue

            index = self.df[self.df["Graphitem"] == a].index[0]
            self.changeFlag(index=index)
            self.history = append(self.history, index)
            self.historystatus = True

def altSnapper(self,x,y,a):
    ps = self.ui.df[self.ui.df["Graphitem"] == a].iloc[0]['Robject']
    xv = unit(ps['P3']-ps['P1'])
    normal = array([-xv[1],xv[0]])
    p1=array([self.ui.x[self.ui.count-1],self.ui.y[self.ui.count-1]])
    peak=norm(array([x,y])-p1)
    x,y=p1+peak*normal 
    return x,y   
class GraphicsScene(QGraphicsScene):
    def __init__ (self, ui,parent=None):
        self.ui=ui
        self.ui.count=0
        self.ui.selectCount=0
        self.ui.x=[0,0,0]
        self.ui.y=[0,0,0]
        super(GraphicsScene, self).__init__ (parent)
        self._pan=False
        self.ui.deleteText=False
        # self.setAcceptDrops(True)

    def mouseMoveEvent(self,event):

        if self.ui.delete==True:
            self.ui.scene.removeItem(self.ui.scene.items()[0])
            self.ui.delete=False
        if self.ui.todraw=='select' and self.ui.selectCount==1:      
            x,y=event.scenePos().x(),event.scenePos().y()
            self.ui.scene.addRect(self.ui.x[0],self.ui.y[0],x-self.ui.x[0],y-self.ui.y[0],QPen(Qt.DashLine))
            self.ui.delete=True
            return
        if self._pan:        
            self.ui.graphicsView.horizontalScrollBar().setValue(self.ui.graphicsView.horizontalScrollBar().value() - (event.scenePos().x() - self._panStartX))
            self.ui.graphicsView.verticalScrollBar().setValue(self.ui.graphicsView.verticalScrollBar().value() + (event.scenePos().y() - self._panStartY))
            self._panStartX = event.scenePos().x()
            self._panStartY = event.scenePos().y()
            event.accept()
            return            


        x,y=snapper(self,event)
        if event.modifiers()&Qt.AltModifier:
            if not (self.ui.member=='load' and self.ui.count>=1):
                cMatrix=self.ui.rrts(vstack(self.ui.snapPoints))
                check = norm(array([x,y])-cMatrix,axis=1)            
                x,y=cMatrix[argmin(check)]

     #measure
        if self.ui.deleteText:
            self.ui.scene.removeItem(self.ui.deleteText)
            self.ui.scene.removeItem(self.ui.scene.items()[0]) 
            self.ui.deleteText=False            

        if self.ui.todraw=='measure' and self.ui.count==1:
            x1,y1=self.ui.rts(array([x,y]))
            angle=atan2(y1-self.ui.rts(self.ui.y[0]),x1-self.ui.rts(self.ui.x[0]))
            angle=round(angle*180/pi,self.ui.precison)
            x1,y1=x1-self.ui.rts(self.ui.x[0]),y1-self.ui.rts(self.ui.y[0])
            
            length=(x1*x1+y1*y1)**0.5
            length=round(length,self.ui.precison)
            # self.ui.statusbar.showMessage(f'Length={length}')
            
            text = QGraphicsTextItem()
            text.setPos(self.ui.x[0],self.ui.y[0])
            text.setHtml(f"<p style='color:blue;font-size:15px'>&#8736;={str(angle)}&#176;</p>")   
            text.setTransform(QTransform(1., 0., 0., -1., 0, 0))    
            self.ui.scene.addItem(text)
            self.ui.deleteText=self.ui.scene.items()[0]

            text = QGraphicsTextItem()
            text.setPos(x+1,y-1)
            text.setHtml(f"<p style='color:blue;font-size:15px'>{str(length)}</p>")   
            text.setTransform(QTransform(1., 0., 0., -1., 0, 0))    
            self.ui.scene.addItem(text)
            self.ui.deleteText=self.ui.scene.items()[0]

            self.ui.scene.addLine(self.ui.x[0],self.ui.y[0],x,y,QPen(Qt.DashLine))
            self.ui.delete=True
        
        if self.ui.member=='segment':
            if self.ui.count==1:
                self.ui.scene.addLine(self.ui.x[0],self.ui.y[0],x,y)
                self.ui.delete=True
            elif self.ui.count==2:
                # x=event.scenePos().x()
                # y=event.scenePos().y() 
                tempDrawSegment(self.ui,x,y)
    
        elif self.ui.member=='load':
            a=self.ui.scene.selectedItems()
            if len(a):
                self.ui.parent=a[0]                


                if self.ui.count==1:
                    if self.ui.todraw=='Point Load' or self.ui.todraw=='Moment':
                        if event.modifiers()&Qt.AltModifier and self.ui.count>=1:
                            x,y=altSnapper(self,x,y,a[0])
                        tempDrawLoad(self.ui,x,y)
                    else:
                        cMatrix=self.ui.rrts(vstack(self.ui.snapPoints))
                        check = norm(array([x,y])-cMatrix,axis=1)            
                        x,y=cMatrix[argmin(check)]
                        self.ui.scene.addLine(self.ui.x[0],self.ui.y[0],x,y)
                        self.ui.delete=True
                elif self.ui.count==2:
                    if event.modifiers()&Qt.AltModifier and self.ui.count>=1:
                        x,y=altSnapper(self,x,y,a[0])
                    tempDrawLoad(self.ui,x,y)

        x,y=self.ui.rts(array([x,y]))
        if self.ui.coordinateSystem.currentText()=='Polar':
            r=round(sqrt((x**2+y**2)),self.ui.precison)
            y=round(atan2(y,x)*180/pi, self.ui.precison)
            x=r
        if self.ui.coordinateMode.currentText()=='Relative' and self.ui.count>0:
            
            x,y=x-self.ui.rts(self.ui.x[0]),y-self.ui.rts(self.ui.y[0])
            x,y=round(x,self.ui.precison),round(y,self.ui.precison)    
        if not self.ui.coordinateEdited:
            self.ui.editX.setText(str(x))
            self.ui.editY.setText(str(y))
        elif self.ui.coordinateEdited=='y':
            self.ui.editX.setText(str(x))
        elif self.ui.coordinateEdited=='x':
            self.ui.editY.setText(str(y))         
        self.ui.app.processEvents()
        # QGraphicsScene.mouseMoveEvent(self,event)

    def mousePressEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.ui.todraw:
            if self.ui.todraw=='select':
                self.ui.selectCount=1
                self.ui.x[0],self.ui.y[0]=event.scenePos().x(),event.scenePos().y()               
                return
            x,y=snapper(self,event)
            if event.modifiers()&Qt.AltModifier:
                if not (self.ui.member=='load' and self.ui.count>=1):
                    cMatrix=self.ui.rrts(vstack(self.ui.snapPoints))
                    check = norm(array([x,y])-cMatrix,axis=1)            
                    x,y=cMatrix[argmin(check)]
                elif self.ui.member=='load':
                    if self.ui.count==1:
                        if self.ui.todraw=='Point Load' or self.ui.todraw=='Moment':
                            x,y=altSnapper(self,x,y,self.ui.parent)
                        else:
                            cMatrix=self.ui.rrts(vstack(self.ui.snapPoints))
                            check = norm(array([x,y])-cMatrix,axis=1)            
                            x,y=cMatrix[argmin(check)]                    
                    elif self.ui.count>1:
                        x,y=altSnapper(self,x,y,self.ui.parent)
                  
            x=round(x/50,self.ui.precison)*50
            y=round(y/50,self.ui.precison)*50 
            self.ui.x[self.ui.count],self.ui.y[self.ui.count]=x,y            
            self.ui.drawAll()   
            
            if self.ui.count==1 and self.ui.todraw=='measure':
                x=round(x/50,self.ui.precison)*50
                y=round(y/50,self.ui.precison)*50 
                self.ui.x[0],self.ui.y[0]=x,y                

        elif event.buttons() & Qt.MiddleButton:
            self.ui.zoomState=0
            self.ui.graphicsView.fitInView(0, 0, self.ui.graphicsView.geometry(
                ).width(), self.ui.graphicsView.geometry().height())
            # self.ui.graphicsView.fitInView(self.ui.scene.sceneRect())
        elif event.buttons() & Qt.RightButton:
            self._panStartX = event.scenePos().x()
            self._panStartY = event.scenePos().y()
            self.ui.graphicsView.setCursor(Qt.ClosedHandCursor)
            self._pan = True
            event.accept()
            return                          
        # else:
        #     QGraphicsScene.mousePressEvent(self,event)

    def mouseReleaseEvent(self,event):
        if (event.button() & Qt.LeftButton) and self.ui.todraw=='select' and self.ui.selectCount==1:
            self.ui.x[1],self.ui.y[1]=event.scenePos().x(),event.scenePos().y()
            h=abs(self.ui.y[1]-self.ui.y[0])
            w=abs(self.ui.x[1]-self.ui.x[0])          
            a=self.ui.scene.items(min(self.ui.x[0],self.ui.x[1]),min(self.ui.y[0],self.ui.y[1]),w,h,
                Qt.ItemSelectionMode.ContainsItemBoundingRect,Qt.SortOrder.AscendingOrder)
            [x.setSelected(True) for x in a]
            self.ui.selectCount=0
            event.accept()
            return

        if (event.button()& Qt.RightButton):        
            self._pan = False
            self.ui.graphicsView.setCursor(Qt.ArrowCursor)
            event.accept()
            return     
            
        else:
            QGraphicsScene.mouseReleaseEvent(self,event)
        # event.ignore()

    def mouseDoubleClickEvent(self,event):
        if self.ui.todraw=='measure':
            self.ui.count=0
            selectedItems=self.ui.scene.selectedItems()
            if len(selectedItems):
                ps=self.ui.df[(self.ui.df['Graphitem']==selectedItems[0])]['Robject']   
                if not ps.empty:
                    segment=ps.iloc[0]
                    if segment['type']=='arc':
                        length=arcLength(segment['P1'],segment['P3'],segment['P2'])
                        self.ui.statusbar.showMessage(f'Length={round(length,self.ui.precison)}',3000)
                    elif segment['type']=='quad':
                        length=quadLength(segment['P1'],segment['P3'],segment['P2'])    
                        self.ui.statusbar.showMessage(f'Length={round(length,self.ui.precison)}',3000)
                    elif segment['type']=='line':
                        length= norm(segment['P1']-segment['P3'])   
                        self.ui.statusbar.showMessage(f'Length={round(length,self.ui.precison)}',3000)        
        QGraphicsScene.mouseDoubleClickEvent(self,event)

    def fitToScreen(self):
        self.ui.zoomState=0
        self.ui.graphicsView.fitInView(0, 0, self.ui.graphicsView.geometry(
            ).width(), self.ui.graphicsView.geometry().height())

    def contextMenuEvent(self, event):
        from structure2d.objecttree2d import editObjects
        item = self.itemAt(event.scenePos().x(),event.scenePos().y(),QTransform(1., 0., 0., -1., 0, 0))
        if item:
            item.setSelected(True)            
            menu = QMenu()
            menu.addAction('Edit',lambda:editObjects(self.ui,item))
            if self.ui.df[(self.ui.df['Graphitem']==item)]['Class'].iloc[0]=='segment':
                name=self.ui.df[(self.ui.df['Graphitem']==item)]['Name'].iloc[0]
                menu.addAction('Show Diagrams',lambda:self.ui.diagrams(name))
            menu.exec_(event.screenPos())
            

        else:
            menu = QMenu()

            menu.addAction('Analyse',lambda:analysisModes(self.ui))
            menu.addAction('Simulate',lambda:simulationEnvironment(self.ui,self.ui.MainWindow))
            menu.addAction('Fit to Screen',self.fitToScreen)
            menu.addAction('FullScreen',self.ui.clearScreen)
            menu.exec_(event.screenPos())

        event.accept()

    # def wheelEvent(self,event):

    #     from PySide2.QtWidgets import QGraphicsView
    #     # oldPos = self.ui.graphicsView.mapToScene(event.pos())
    #     # self.ui.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
    #     if event.delta()>0:
    #         self.ui.zoomOut()
            
    #     else:    
    #         self.ui.zoomIn()
    #     # newPos = self.ui.graphicsView.mapToScene(event.pos())
    #     # delta=newPos-oldPos
    #     # self.ui.graphicsView.translate(delta.x(),delta.y())

    def keyPressEvent(self,event):

        key = event.key()
        if key == Qt.Key_Escape:
            if self.ui.delete==True:
                self.ui.scene.removeItem(self.ui.scene.items()[0])
                
                # getattr(self.ui,'action'+self.ui.todraw.title()).setChecked(False)
                self.ui.delete=False
            if self.ui.deleteText:
                self.ui.scene.removeItem(self.ui.deleteText)
                self.ui.scene.removeItem(self.ui.scene.items()[0])

                self.ui.deleteText=False
            if self.ui.todraw != 'select': 
                attribute= self.ui.todraw.title().replace(' ','') if self.ui.todraw not in ['UDL','UVL'] else self.ui.todraw
                attribute = 'CustomSupport' if self.ui.todraw[0] in['0','1'] else attribute
                getattr(self.ui,'action'+attribute).setChecked(False)

            self.ui.todraw='select'
            self.ui.member=None
            self.ui.count=0
            self.ui.coordinateEdited=None
            self.ui.cut=False
            self.ui.graphicsView.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.scene.clearSelection()
            self.ui.dockPeakNormal.close()
            self.ui.clipboardItems=[]
        

        elif key== Qt.Key_Delete:            
            delete(self.ui)

        elif key == Qt.Key_Y:
            self.ui.editY.setFocus()

        elif key in [Qt.Key_1,Qt.Key_2,Qt.Key_3,Qt.Key_4,Qt.Key_5]:
            segments=self.ui.df[(self.ui.df['Class']=='segment')&(self.ui.df['Flag']==True)]
            try:
                ci=segments.iloc[int(chr(key))-1]['Graphitem']
                if ci.isSelected():
                    ci.setSelected(False)
                else:
                    ci.setSelected(True)    
            except:
                pass

        elif key == Qt.Key_E:
            from structure2d.objecttree2d import objectTree
            try:
                a=self.ui.scene.selectedItems()[0]
                ps=self.ui.df[(self.ui.df['Graphitem']==a)]['Treeitem'].iloc[0]
                objectTree(self.ui,self.ui.MainWindow)
                ps.setSelected(True)
                # self.contextMenuEvent(event)
            except Exception as e:
                import traceback
                print(traceback.format_exc())
                self.ui.statusbar.showMessage("Select any object to edit",2000)

        elif key ==Qt.Key_A and  event.modifiers()&Qt.ControlModifier:
            [a.setSelected(True) for a in self.ui.scene.items()]


        elif event.modifiers() & Qt.ControlModifier and key == Qt.Key_C:
            self.ui.clipboardItems=self.ui.scene.selectedItems()
            if len(self.ui.clipboardItems)>0:
                self.ui.statusbar.showMessage(str(len(self.ui.clipboardItems)) + ' item/s copied to clipboard',2000)
            else:
                self.ui.statusbar.showMessage('Select items to copy',2000)
        elif event.modifiers()&Qt.ControlModifier and key == Qt.Key_X:
            self.ui.cut=True
            try:
                self.ui.clipboardItems=self.ui.scene.selectedItems()
                self.ui.statusbar.showMessage(str(len(self.ui.clipboardItems)) + ' item/s added to clipboard',2000)
            except:
                self.ui.statusbar.showMessage('Select items to copy',2000)

        elif key == Qt.Key_X:
            self.ui.editX.setFocus()
        elif event.modifiers()&Qt.ControlModifier and key == Qt.Key_V:
            if len(self.ui.clipboardItems)==0:
                self.ui.statusbar.showMessage('No items to paste',5000)
                return                
            x=float(self.ui.editX.text())
            y=float(self.ui.editY.text())
            from numpy import array
            finalPoint=array([self.ui.rrts(x),self.ui.rrts(y)])

            smembers=self.ui.df[(self.ui.df['Class']!='load')]
            length=100000
            for item in self.ui.clipboardItems:
                firstMember=smembers[(smembers['Graphitem']==item)].iloc[0]

                
                if  firstMember['Class']=='segment':
                    p1=self.ui.rrts(firstMember['Robject']['P1'])
                    p2=self.ui.rrts(firstMember['Robject']['P3'])
                    initialPoint=p1 if norm(p1)<norm(p2) else p2
                else:
                    initialPoint=self.ui.rrts(firstMember['Robject']['location'])
                
                if norm(initialPoint)<length:
                    length=norm(initialPoint)
                    nearestPoint= initialPoint
                    
            translationVector=finalPoint-nearestPoint

            for item in self.ui.clipboardItems:
                member=smembers[(smembers['Graphitem']==item)].iloc[0]
                self.ui.member=member['Class']
                self.ui.todraw=member['Robject']['type']
                if self.ui.member=='segment':
                    self.ui.count=1
                    self.ui.x[0],self.ui.y[0]=self.ui.rrts(member['Robject']['P1'])+translationVector
                    self.ui.x[1],self.ui.y[1]=self.ui.rrts(member['Robject']['P3'])+translationVector
                    self.ui.x[2],self.ui.y[2]=self.ui.rrts(member['Robject']['P2'])+translationVector

                    if self.ui.todraw !='line':
                        self.ui.count=2
                    data=list(member['Robject'].values())[4:11]
                    self.ui.drawAll(properties=data)
                elif self.ui.member == 'support':
                    # print(translationVector,self.ui.rrts(member['Robject']['location']))
                    self.ui.x[0],self.ui.y[0]=self.ui.rrts(member['Robject']['location'])+translationVector
                    self.ui.drawAll()

            self.ui.todraw=None
            self.ui.count=0
            if self.ui.cut==True:
                delete(self.ui)
                self.ui.cut==False


        elif key==Qt.Key_C:
            from .calculator import calculator
            if self.ui.calculatorMode:
                self.ui.actionCalculator.setChecked(True)
            calculator(self.ui)


        elif key==Qt.Key_Space:

            # self.ui.member='segment'
            # self.ui.todraw='line'
            # from numpy import nan,array,isnan
            # from PySide2.QtGui import QPen,QColor

            # self.ui.x=[100,1000]
            # self.ui.y=[200,200]
            # self.ui.count=1
            # self.ui.drawAll()           
  
        
            # self.ui.loadPen=QPen(QColor(*self.ui.loadColor),self.ui.loadWidth)
            # self.ui.parent=self.ui.scene.items()[0]
            # self.ui.scene.items()[0].setSelected(True)
            # self.ui.member='load'
            # self.ui.todraw='Point Load'
            # self.ui.x=[1000,1000]
            # self.ui.y=[200,300]
            # self.ui.count=1
            # self.ui.drawAll()
            # self.ui.x=[500,500]
            # self.ui.y=[200,300]
            # self.ui.count=1
            # self.ui.drawAll()

            # self.ui.supportPen=QPen(QColor(*self.ui.fixedColor),1.5)
            # self.ui.member='support'
            # self.ui.todraw='Fixed'
            # self.ui.x=[100,1000,0]
            # self.ui.y=[200,200,0]
            # self.ui.count=1
            # self.ui.drawAll()            

            # self.ui.todraw='segment'
            from structure2d.analysis2d import analysisModes,analyse
            from structure2d.fileOperations2d import openFile
            openFile(self.ui,directOpen='./default.str')
            analysisModes(self.ui)
            self.ui.aM.close()
            analyse(self.ui)
        else:
            QGraphicsScene.keyPressEvent(self,event)
            

