from numpy import append, array
from PySide2 import QtCore, QtGui, QtWidgets
# from structure2d.mouseGraphics import GraphicsScene
from PySide2.QtGui import QBrush, QColor, QImage, QPainter, QPen, QPixmap
from PySide2.QtWidgets import QGraphicsItem, QGraphicsView,QLabel,QLineEdit
from PySide2.QtCore import Qt
from pandas.core.frame import DataFrame
from sdPy.numbaFunctions import sectionProperty
from structure2d.drawSegments import tempDrawSegment
from UI.sectionBuilder import Ui_Dialog as SectionBuilder
from UI.sectionDesigner import Ui_MainWindow as sectionDesigner
import warnings
from sdPy.segmentMethods import arcPlotData2,quadPlotData2
from sdPy.sectionBuilder import breakArc, xCalc,breakQuad
from numpy import arctan2,pi, argmin, vstack
from numpy.linalg import norm
from sampleDatas import resource_path
from structure2d.mouseGraphics import snapper,myround
# from structure2d.st2d import redo, undo
def editPoints(self):
    self.coordinateEdited=None
    x=float(self.editX.text())*self.scale*50
    y=float(self.editY.text())*self.scale*50
    self.x[self.count],self.y[self.count]=x,y
    drawLine(self)
    self.graphicsView.setFocus()


def changeFlag(self, index=None, name=None):
    if name != None:
        index = self.df[self.df["Name"] == name].index[0]
    if self.df.iloc[index, 3].isVisible() == True:
        self.df.iloc[index, 3].hide()
        # self.df.iloc[index, 4].setHidden(True)
        self.df.iloc[index, 5] = False
        if self.df.iloc[index,1] == 'segment':
            self.x[0],self.y[0]=self.df.iloc[index,2]['P1']*self.scale*50
    else:
        self.df.iloc[index, 3].show()
        # self.df.iloc[index, 4].setHidden(False)
        self.df.iloc[index, 5] = True
        if self.df.iloc[index,1] =='segment':
            self.x[0],self.y[0]=self.df.iloc[index,2]['P3']*self.scale*50
def redo(self):
    if not self.historystatus:
        self.historystatus = True
    if self.counter < self.historyposition:
        changeFlag(self,index=self.history[self.counter])
        self.history = append(self.history, self.history[self.counter])
        self.counter += 1
    else:
        self.statusbar.showMessage("No more redo available", 2000)

def undo(self):

    if self.historystatus:
        self.historyposition = len(self.history)
        self.historystatus = False
        self.counter = len(self.history)

    if self.counter > 0:
        changeFlag(self,index=self.history[self.counter-1])
        self.history = append(self.history, self.history[self.counter-1])
        self.counter -= 1
        self.itemss = len(self.df)
    else:
        self.statusbar.showMessage("No more undo available", 2000)


def designSection(self):
    # self.delete=False
    self.count=0
    p3=array([self.x[1],self.y[1]])
    # p3=array([self.x[0],self.y[0]])  

    if not self.escaped:
        self.x[1],self.y[1]=self.data[self.loop][0]*(50*self.scale)

        self.count=1
        self.todraw='line'
        drawLine(self)
        self.data[self.loop].append(self.data[self.loop][0])

    from structure2d.analysis2d import designSection
    
    
        
    main=self.data[0]
    holes=self.data[1:-1]
    holes=[array(x) for x in holes]
    section = {'main' : array(main), 'holes' : array(holes)}
    # data = xCalc(section)
    # print(data)
    data=designSection(self)

    output=''
    self.statusbar.showMessage("Go to in Standard Sections tab to save the section",5000)

    for key,val in data.items():
        output+=str(key)+' = '+str(val.round(self.precison))+'<br>'
    
    image=QImage(700,400,QImage.Format_ARGB32);
    painter=QPainter(image)
    self.graphicsView.render(painter)
    painter.end()
    image.save("test.png","PNG");
    pixmap = QtGui.QPixmap('test.png')
    self.image.setPixmap(pixmap)

    self.sectionResults.setText(f"<p  style='color:blue;font-size:18px;'>{output}</p>")            

    self.sectiondata=[data['area'],data['IXX'],data['IYY'],data['IZZ'],data['k']]    
    output=''
    keys=['  Area','  Ixx ','  Iyy ','  Izz ','  k   ']
    for key,val in zip(keys,self.sectiondata):
        output+='&nbsp;'+'&nbsp;'+str(key)+' = '+str(val.round(self.precison))+'<br>'
    self.output.setText(f"<p  style='color:blue;font-size:30px;'><br><br>{output}</p>")    
    self.count=0
def toolbars(self):
    reg_ex = QtCore.QRegExp("[0-9]*\.?[0-9]*")
    self.floatValidator = QtGui.QRegExpValidator(reg_ex)    
    self.propertiesBar = QtWidgets.QToolBar('Properties Bar',self.MainWindow)
    self.MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.propertiesBar)
    self.editX=QtWidgets.QLineEdit()
    self.editX.setFixedWidth(100)
    self.editX.setValidator(self.floatValidator)
    self.editY=QtWidgets.QLineEdit()
    self.editY.setFixedWidth(100)
    self.editY.setValidator(self.floatValidator)
    self.propertiesBar.addWidget(QLabel(' X '))
    self.propertiesBar.addWidget(self.editX)
    self.propertiesBar.addWidget(QLabel(' Y '))
    self.propertiesBar.addWidget(self.editY)
    self.propertiesBar.addSeparator()    
    def assign(a):self.coordinateEdited=a
    self.coordinateEdited=None
    self.editX.textEdited.connect(lambda:assign('x'))
    self.editY.textEdited.connect(lambda:assign('y'))
    self.editX.returnPressed.connect(lambda:editPoints(self))
    self.editY.returnPressed.connect(lambda:editPoints(self))

    self.propertiesBar.addWidget(QLabel(' Scale '))
    self.editScale=QtWidgets.QLineEdit()
    
    self.editScale.setValidator(self.floatValidator)
    self.editScale.setFixedWidth(100)
    self.editScale.setText(str(self.scale))
    self.propertiesBar.addWidget(self.editScale)
    def scale():
        scale=float(self.editScale.text())
        if scale>0:
            self.scale=scale
        else:
            self.scale=1
            self.editScale.setText(str(1))    
        self.graphicsView.setFocus()

    self.editScale.editingFinished.connect(scale)    
    
    self.propertiesBar.addWidget(QLabel(' Precision '))
    self.editPrecison=QtWidgets.QLineEdit()
    reg_ex = QtCore.QRegExp("[0-9]")
    validator = QtGui.QRegExpValidator(reg_ex)
    self.editPrecison.setValidator(validator)
    self.editPrecison.setFixedWidth(100)
    self.editPrecison.setText(str(self.precison))
    self.propertiesBar.addWidget(self.editPrecison)
    def precison():
        self.precison=int(self.editPrecison.text())
        self.graphicsView.setFocus()
    self.editPrecison.editingFinished.connect(precison)    

    self.propertiesBar.addSeparator()

def drawLine(self):
    if self.delete==True:
        self.scene.removeItem(self.scene.items()[0])
    if not self.todraw:
        return
    pen=QPen(Qt.red,3)
    try: 
        p1=array([self.x[0],self.y[0]])  
        p3=array([self.x[1],self.y[1]])  
        if self.todraw=='line':
            line=self.scene.addLine(self.x[0],self.y[0],self.x[1],self.y[1],pen)
            line.setFlag(QGraphicsItem.ItemIsSelectable)
            self.data[self.loop].append((p1/(50*self.scale)).round(self.precison))
            p2=(p1+p3)/2
            
        else:
            p2=array([self.x[2],self.y[2]]) 
            if self.todraw=='arc':
                data=arcPlotData2(p1,p3,p2,self.scale)
            elif self.todraw=='quad':
                data=quadPlotData2(p1,p3,p2,self.scale)

            [self.data[self.loop].append((x/50).round(self.precison)) for x in data]
            rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
            for i in range(2,len(data),2):
                rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
            rect=self.scene.addPath(rect,pen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable)


        Rsegment={  'P1':(p1/50).round(self.precison),
                    'P2':(p2/50).round(self.precison),
                    'P3':(p3/50).round(self.precison),
                    'type':self.todraw}
        self.df.loc[len(self.df)]=[self.segmentNumber,'segment',Rsegment,self.scene.items()[0],' ',True]
        self.segmentNumber += 1
        self.snapPoints.append([p1,p2,p3])
        self.history=append(self.history,len(self.df)-1)
        self.historystatus=True

    except Exception as e:
        self.statusbar.showMessage(str(e),2000)
    self.x[0],self.y[0]=self.x[1],self.y[1]
    self.count=0
    self.delete=False




class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__ (self, ui,parent=None):
        self.ui=ui
        self.ui.count=0
        self.ui.x=[0,0,0]
        self.ui.y=[0,0,0]
        self.ui.delete=False
        self.ui.todraw=None
        self.ui.segmentNumber=0
        self.ui.loop=0
        self.ui.data=[]
        self.ui.data.append([])
        super(GraphicsScene, self).__init__ (parent)


    def mouseMoveEvent(self,event):
        if self.ui.delete==True:
            self.ui.scene.removeItem(self.ui.scene.items()[0])
        x,y=snapper(self,event)
        if event.modifiers()&Qt.AltModifier:            
            cMatrix=vstack(self.ui.snapPoints)*self.ui.scale
            check = norm(array([x,y])-cMatrix,axis=1)            
            x,y=cMatrix[argmin(check)]
        if self.ui.todraw:
            if self.ui.count==1:
                self.ui.scene.addLine(self.ui.x[0],self.ui.y[0],x,y)            
                self.ui.delete=True
            elif self.ui.count==2:
                tempDrawSegment(self.ui,x,y)
        x,y=round(x/(50*self.ui.scale),self.ui.precison),round(y/(50*self.ui.scale),self.ui.precison)
        if not self.ui.coordinateEdited:
            self.ui.editX.setText(str(x))
            self.ui.editY.setText(str(y))
        elif self.ui.coordinateEdited=='y':
            self.ui.editX.setText(str(x))
        elif self.ui.coordinateEdited=='x':
            self.ui.editY.setText(str(y))  


    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton and self.ui.todraw:
            x,y=snapper(self,event)
            if event.modifiers()&Qt.AltModifier:            
                cMatrix=vstack(self.ui.snapPoints)*self.ui.scale
                check = norm(array([x,y])-cMatrix,axis=1)            
                x,y=cMatrix[argmin(check)]
            x=round(x/(50),self.ui.precison)*50
            y=round(y/(50),self.ui.precison)*50
            self.ui.x[self.ui.count],self.ui.y[self.ui.count]=x,y
            if self.ui.count==1:
                if self.ui.todraw=='line':
                    drawLine(self.ui)
            elif self.ui.count==2 :
                if self.ui.todraw=='arc' or self.ui.todraw=='quad':
                    drawLine(self.ui)
            self.ui.count +=1
            self.ui.escaped=False
                
    def keyPressEvent(self,event):
        key = event.key()
        def delete():
            if len(self.ui.scene.selectedItems()):
                for a in self.ui.scene.selectedItems():
                    index = self.ui.df[self.ui.df["Graphitem"] == a].index[0]
                    changeFlag(self.ui,index=index)
                    self.ui.history = append(self.ui.history, index)
                    self.ui.historystatus = True
        if key == QtCore.Qt.Key_Escape:
            if self.ui.delete==True:
                self.ui.scene.removeItem(self.ui.scene.items()[0])
                self.ui.delete=False
            self.ui.graphicsView.setCursor(QtGui.QCursor())
            p3=array([self.ui.x[1],self.ui.y[1]])  
            # self.ui.x[1],self.ui.y[1]=self.ui.data[self.ui.loop][0]*(50*self.ui.scale)
            # self.ui.count=1
            # self.ui.todraw='line'
            # drawLine(self.ui)
            self.ui.data[self.ui.loop].append(self.ui.data[self.ui.loop][0].round(self.ui.precison))
            self.ui.data.append([])
            self.ui.loop+=1
            # self.ui.x[0],self.ui.y[0]=p3
            self.ui.count=0
            self.ui.todraw=None
            self.ui.escaped=True


   
        elif key==QtCore.Qt.Key_D:
            designSection(self.ui)
        elif key==QtCore.Qt.Key_Delete:
            delete()
        elif key ==QtCore.Qt.Key_R and  event.modifiers()&QtCore.Qt.ControlModifier:
            [a.setSelected(True) for a in self.ui.scene.items()]
            [self.ui.scene.removeItem(x) for x in self.ui.scene.selectedItems()]
            self.ui.data=[[]]
            self.ui.loop=0
            self.count=0
            self.ui.segmentNumber=0
        elif key ==QtCore.Qt.Key_Z and  event.modifiers()&QtCore.Qt.ControlModifier:
           undo(self.ui) 
        elif key ==QtCore.Qt.Key_Y and  event.modifiers()&QtCore.Qt.ControlModifier:
           redo(self.ui) 
        elif key == QtCore.Qt.Key_Y:
            self.ui.editY.setFocus()
        elif key == QtCore.Qt.Key_X:
            self.ui.editX.setFocus() 
        elif key ==Qt.Key_A and  event.modifiers()&Qt.ControlModifier:
            [a.setSelected(True) for a in self.ui.scene.items()]            

    def wheelEvent(self, event):
        if event.delta()>0:
            self.ui.graphicsView.scale(1/1.1,1/1.1)            
        else:    
            self.ui.graphicsView.scale(1.1,1.1)
def grid(self):
    self.scale=1
    import numpy as np
    xrange = 50 * round((self.MainWindow.width()-100)/50)
    yrange = 50*round((self.MainWindow.height()-150)/50)
    xrange=int(xrange)
    yrange=int(yrange)
    self.scene.addLine(0, 0, 0, yrange, QPen(Qt.green, 3))
    self.scene.addLine(0, 0, xrange, 0, QPen(Qt.green, 3))
    for x in range(0, xrange, self.scale*50):
        self.scene.addLine(x, 0, x, yrange, QPen(Qt.black, 0.25))
    self.scene.addLine(x+50, 0, x+50, yrange, QPen(Qt.black, 0.25))

    for y in range(0, yrange, self.scale*50):
        self.scene.addLine(0, y, xrange, y, QPen(Qt.black, 0.25))
    self.scene.addLine(0, y+50, xrange, y+50, QPen(Qt.black, 0.25))

    # self.graphicsView.fitInView(0, 0, self.graphicsView.geometry(
    # ).width(), self.graphicsView.geometry().height())

def createScene(self):
    self.scene = GraphicsScene(self)
    self.graphicsView.setScene(self.scene)
    self.graphicsView.setMouseTracking(True)
    self.graphicsView.setRenderHint(QPainter.Antialiasing)
    from PySide2.QtGui import QTransform
    self.graphicsView.setTransform(QTransform(1., 0., 0., -1., 0, 0))
    self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)
    grid(self)

def segments(self, todraw,parent):
    self.todraw = todraw
    # if self.segmentNumber==0:
    #     self.count=0 
    # else:
    #     self.count = 1
    
    if self.delete == True:
        self.delete = False
        self.scene.removeItem(self.scene.items()[0])
    cursor=QPixmap(resource_path(parent.cursorPath+"draw"+self.todraw.capitalize()+".png"))
    self.graphicsView.setCursor(QtGui.QCursor(cursor,0,32))
        
def sectionBuilder(self,MainWindow):
    self.sB=QtWidgets.QMainWindow(parent=MainWindow)
    self.sb=sectionDesigner()
    self.sb.setupUi(self.sB)
    # self.sb.precison=self.precison
    self.sb.MainWindow=self.sB
    self.sb.coordinateEdited=None
    self.sb.scale=1
    self.sb.precison=3
    self.sb.history = array([], dtype="int8")
    self.sb.historystatus=False
    self.sb.sectionDesignerAccuracy = self.sectionDesignerAccuracy
    self.sb.counter=1
    self.sb.snapPoints=[]
    self.sb.df = DataFrame(
            columns=["Name", "Class", "Robject",
                     "Graphitem", "Treeitem", "Flag"],
            index=None,
        )
    toolbars(self.sb)
    # from structure2d.st2d import Window2d
    # self.sb.app=self.app
    # self.sb.grid=Window2d.grid
    # Window2d.createScene(self.sb)   

    
    # self.sb.smallGrid=Window2d.smallgrid(self.sb)
    # self.sb.tempGrid=Window2d.tempGrid(self.sb)
    createScene(self.sb)
    self.sb.actionLine.triggered.connect(lambda: segments(self.sb,"line",self))
    self.sb.actionarc.triggered.connect(lambda: segments(self.sb,"arc",self))
    self.sb.actionquad.triggered.connect(lambda: segments(self.sb,"quad",self))   
    self.sb.actionDesign.triggered.connect(lambda:designSection(self.sb))
    self.sb.shapes.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.sb.output.setFontPointSize(15)
    pixmap = QtGui.QPixmap(resource_path('./ico/sectionShapes/Rectangle.png'))
    self.sb.image.setPixmap(pixmap)
    self.sb.output.setTextColor(QColor(206,13,243))

    self.sb.sectionResults=QtWidgets.QLabel()
    self.sb.sectionResults.setStyleSheet('''QLabel{ 
                    background-color:rgb(232, 255, 247);
                    border: 2px solid gray;
                    border-radius: 6px;} ''')
    self.sb.sectionResults.setMinimumWidth(0)
    self.sb.gridLayout_4.addWidget(self.sb.sectionResults,0,1,2,2)

    def shapes():
        shape = self.sb.shapes.currentText()
        name=resource_path('./ico/sectionShapes/'+shape+'.png')
        pixmap = QtGui.QPixmap(name)
        self.sb.image.setPixmap(pixmap)
    self.sb.shapes.currentIndexChanged.connect(shapes)
    def calculation():            
        try:
            types= self.sb.shapes.currentText()
            length = self.sb.length.text()
            breadth = self.sb.breadth.text()
            flanges = self.sb.flanges.text()
            width = self.sb.width.text()
            d=[]
            for i in [length,breadth,flanges,width]:
                if i=='':
                    d.append(0)
                else:
                    d.append(float(i))

            data = sectionProperty(types=types,length=d[0],breadth=d[1],flanges=d[2],width=d[3])
            self.sb.output.setText('\n\n \tA\t=\t%.5f\n \tIxx\t=\t%.5f\n \tIyy\t=\t%.5f\n \tJ\t=\t%.5f\n \tk\t=\t%.5f '%((data[0],data[1],data[2],data[3],data[4])))
            self.sb.sectiondata=data
        except:
            import traceback
            traceback.print_exc()
            self.sb.statusbar.showMessage('Invalid data',3000)    
    self.sb.calculate.clicked.connect(calculation)
    def save():
        self.name = self.sb.sectionName.text()
        if self.name=='':self.name='Custom-Section'
        # print(self.section.loc[2])
        # print(append([1,self.name],self.sb.sectiondata))
        self.section.loc[len(self.section)]=append([len(self.section),self.name],self.sb.sectiondata)
        self.statusbar.showMessage('Custom Section Saved',2000)
        self.section.to_csv('./datafiles/sections.csv',index=None)

        self.sectionChoices.addItem(self.name)
        self.sectionChoices.setCurrentText(self.name)

    self.sb.saveSection.clicked.connect(save)
    self.sB.show()
