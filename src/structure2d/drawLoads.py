from structure2d.objectsTable import addDataToTable
from sdPy.loadMethods import loadPlotData2,loadPlotData4,gravityLoad
from PySide2 import QtGui,QtCore,QtWidgets
from PySide2.QtWidgets import QDockWidget, QGraphicsItem, QHBoxLayout, QLabel, QLineEdit, QToolBar, QWidget,QComboBox
from numpy import array,delete,linalg,arctan2 ,pi,append
import warnings
from sdPy.functionDefinitions import make2d,unit
from PySide2.QtCore import Qt
from math import cos, sin, log10
from .objecttree2d import editObjectTree
from PySide2.QtGui import QPen,QColor
from structure2d.objectsTable import addDataToTable
def drawLoad(self,skip=False,name=None):
    pen=self.loadPen
    ps=self.df[(self.df['Graphitem']==self.parent)]['Robject'].iloc[0]
    if not skip:
        if self.delete==True:
            self.scene.removeItem(self.scene.items()[0])
        p1=array([self.x[0],self.y[0]])
        p2=array([self.x[1],self.y[1]])
        if self.todraw=='Point Load' or self.todraw=='Moment':
            normal=p1-p2
            peak=linalg.norm(p2-p1)
        else:    
            p3=array([self.x[2],self.y[2]])
            normal=p2-p3
            peak=linalg.norm(p2-p3)

        degree=self.loadtypes[self.todraw]
        peak=self.rrts(peak if peak <=1 else 10**(self.rts(peak)-1))

        data=loadPlotData2(p1,p2,self.rrts(ps['P1']),self.rrts(ps['P3']),self.rrts(ps['P2']),degree,peak,normal,ps['type'],self.scale,self.loadLogScale)
    else:
        if skip==True:
            Rload=gravityLoad(ps,gNormal=[0,-1])
            data=loadPlotData2(self.rrts(Rload['P1']),self.rrts(Rload['P3']),self.rrts(ps['P1']),self.rrts(ps['P3']),
            self.rrts(ps['P2']), Rload['degree'],self.rrts(Rload['peak']),Rload['normal'],ps['type'],self.scale,self.loadLogScale)
            degree=-10
        else:    
            data=loadPlotData4(ps,skip[0],skip[-1])
            degree=skip[0]
        
    # data=loadPlotData2(Rload['P1'],Rload['P3'],self.rrts(ps['P1']),self.rrts(ps['P3']),
    # self.rrts(ps['P2']), Rload['degree'],Rload['peak'],Rload['normal'],ps['type'],1,1)


    # data=delete(data,0,1)
    rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
    for i in range(1,len(data),1):
        rect.lineTo(QtCore.QPointF(data[i][0],data[i][1]))
        # rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
    rect=self.scene.addPath(rect,pen) 
    # rect.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsFocusable|QGraphicsItem.ItemIsMovable)
    rect.setFlag(QGraphicsItem.ItemIsSelectable)    

    self.delete=False
    self.count=-1
    psName=self.df[(self.df['Graphitem']==self.parent)]['Name'].iloc[0]    
    if degree>= -2:
        with warnings.catch_warnings(record=True) as w:
            Rload=make2d([degree,ps, self.rts(p1), self.rts(p2), self.rts(normal), self.rts(peak), psName])
        if len(w):
            self.statusbar.showMessage(str(w[0].message),2000)
        name = name if name else str(self.loadNumber)+' - '+self.todraw
    elif degree==-3 or degree==-4:
        Rload=make2d([degree]+[ps]+skip[1:]+[psName])
        name = name if name else str(self.loadNumber)+' - '+'MfL' if skip[0]==-4 else str(self.loadNumber)+' - '+'TrL'
    else:
        name= name if name else str(self.loadNumber)+' - '+'Grl'
    # psName=self.df[(self.df['Graphitem']==self.parent)]['Name'].iloc[0]
    # Rload.update({'psName':psName})
    item=QtWidgets.QTreeWidgetItem()
    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
    self.df.loc[len(self.df)]=[name,'load',Rload,self.scene.items()[0],item,True]
    self.ot.load.addChild(item)   
    item.setText(0,name)
    self.ot.load.child(self.loadNumber-1).setData(1,2,str(Rload['degree']))
    combo=QComboBox()
    combo.addItems(reversed(list(self.df[(self.df['Class']=='segment')&(self.df['Flag']==True)]['Name'])))
    combo.currentIndexChanged.connect(lambda:editObjectTree(self))
    combo.setCurrentText(self.df[(self.df['Graphitem']==self.parent)]['Name'].iloc[0])
    item.setData(2,2,self.df[(self.df['Graphitem']==self.parent)]['Name'].iloc[0])
    self.ot.treeWidget.setItemWidget(item,2,combo)
    [self.ot.load.child(self.loadNumber-1).setData(i+1,2,str(list(Rload.values())[i])) for i in range(2,5)]           
    self.ot.load.child(self.loadNumber-1).setData(6,2,str(Rload['peak']))
    # addDataToTable(self,1,name,Rload)


    self.loadNumber += 1
    self.history=append(self.history,len(self.df)-1)
    self.historystatus=True

def editPeakAndNormal(self):
    self.dockPeakNormal=QDockWidget('Peak and Normal',self.MainWindow)
    self.dockPeakNormal.setAllowedAreas(Qt.RightDockWidgetArea)
    # self.MainWindow.addDockWidget(Qt.TopDockWidgetArea,self.dockPeakNormal)

    pw = self.MainWindow.width()
    px = self.MainWindow.geometry().x()
    py = self.MainWindow.geometry().y()            
    self.dockPeakNormal.setGeometry(px+pw-250, py, 270, 50)

    widget=QWidget(self.MainWindow)
    bar=QHBoxLayout()
    # if self.actionDark_Mode.isChecked()==True:
    #     widget.setStyleSheet("QWidget,QLabel,QLineEdit{background-color:rgb(40,40,40)}")
    # else:
    #     widget.setStyleSheet("QWidget{background-color:rgb(250,250,250)}")

    def edit():
        peak=float(self.editPeak.text())
        angle=float(self.editNormal.text())*pi/180
        peak=self.rrts(peak if peak <=1 else log10(peak)+1)
        if self.count==1:
            self.x[1],self.y[1]=peak*cos(angle)+self.x[0],peak*sin(angle)+self.y[0]
            drawLoad(self)
        elif self.count==2:
            self.x[2],self.y[2]=peak*cos(angle)+self.x[1],peak*sin(angle)+self.y[1]
            drawLoad(self)
        self.graphicsView.setFocus()    
    # bar.addStretch()
    bar.addWidget(QLabel('Peak'))
    self.editPeak=QLineEdit()
    self.editPeak.setMaximumWidth(75)
    self.editPeak.setValidator(self.floatValidator)
    self.editPeak.returnPressed.connect(edit)
    bar.addWidget(self.editPeak)
    
    bar.addWidget(QLabel('Normal'))
    self.editNormal=QLineEdit()
    self.editNormal.setValidator(self.floatValidator)
    bar.addWidget(self.editNormal)
    self.editNormal.setMaximumWidth(50)
    self.editNormal.returnPressed.connect(edit)
    widget.setLayout(bar)
    self.dockPeakNormal.setWidget(widget)
    self.dockPeakNormal.setTitleBarWidget(QWidget())    
    # self.dockPeakNormal.resize(bar.sizeHint())

def tempDrawLoad(self,x,y,event=None):
    p1=array([self.x[0],self.y[0]])
    p3=array([x,y])


    if self.todraw=='Point Load' or self.todraw=='Moment':
        p2=p3
        normal=p1-p2
        peak=linalg.norm(p1-p2)
        angle=-arctan2(normal[1],normal[0])*180/pi

    else:    
        p2=array([self.x[1],self.y[1]])
        peak=linalg.norm(p3-p2)
        normal=p2-p3
        angle=-arctan2(normal[1],normal[0])*180/pi
    angle=round(180-angle,self.precison)

    ps=self.df[(self.df['Graphitem']==self.parent)]['Robject'].iloc[0]
    degree=self.loadtypes[self.todraw]
    # data=loadplotdata2(p1,p2,ps['P1'],ps['P3'],ps['P2'],degree,peak,normal,ps['type'],1,self.loadLogScale) 
    # print(p1,p2,self.rrts(ps['P1']),self.rrts(ps['P3']),self.rrts(ps['P2']),peak,normal)
    vpeak=peak if peak <=1 else 10**(self.rts(peak)-1)
    data=loadPlotData2(p1,p2,self.rrts(ps['P1']),self.rrts(ps['P3']),self.rrts(ps['P2']),degree,self.rrts(vpeak),normal,ps['type'],self.scale,self.loadLogScale)
    # try:
    # data=delete(data,0,1)
    # angle=round(arctan2(normal[1],normal[0])*180/pi,3)
    # self.statusbar.showMessage('Peak = '+str(self.rts(peak))+'     '+'Normal = '+str(angle),2000)
    # vpeak=peak if peak <=1 else 10**(self.rts(peak)-1)
    self.editPeak.setText(str(round(vpeak,self.precison)))
    self.editNormal.setText(str(angle))
    # self.editPeak.setFocus()
    rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
    for i in range(1,len(data),1):
        rect.lineTo(QtCore.QPointF(data[i][0],data[i][1]))
        # rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
    self.scene.addPath(rect) 
    self.delete=True

    # except Exception as e:
    #     self.statusbar.showMessage(str(e),2000)

def temprLoad(self):
    self.member='load'
    if not self.scene.selectedItems():
        self.statusbar.showMessage('Select segment to add temperature load',2000)
        return
    self.temprDialog=QtWidgets.QDialog(self.MainWindow)
    grid=QtWidgets.QGridLayout(self.temprDialog)

    grid.addWidget(QtWidgets.QLabel('Lower Temperature (\u03b8<sub>1</sub>)'),0,0,1,1)
    grid.addWidget(QtWidgets.QLabel('Higher Temperature (\u03b8<sub>2</sub>)'),1,0,2,1)
    grid.addWidget(QtWidgets.QLabel('Depth'),3,0,4,1)

    theta1=QtWidgets.QLineEdit()
    theta2=QtWidgets.QLineEdit()
    depth=QtWidgets.QLineEdit()
    grid.addWidget(theta1,0,1,1,2)
    grid.addWidget(theta2,1,1,2,2)
    grid.addWidget(depth,3,1,4,2)
    
    def setValues():
        t1=float(theta1.text())
        t2=float(theta2.text())
        d=float(depth.text())
        self.loadPen=QPen(QColor(*self.loadColor),self.loadWidth)
        for item in self.scene.selectedItems():
            self.parent=item
            drawLoad(self,[-3,t1,t2,d])
        self.temprDialog.close()
    done=QtWidgets.QPushButton('Done')
    grid.addWidget(done,6,1,7,2)
    done.clicked.connect(setValues)
    self.temprDialog.setLayout(grid)
    self.temprDialog.setWindowTitle('Temperature')
    self.temprDialog.show()


def misfitLoad(self):
    self.member='load'
    if not self.scene.selectedItems():
        self.statusbar.showMessage('Select segment to add misfit load',2000)
        return
    self.misfitDialog=QtWidgets.QDialog(self.MainWindow)
    grid=QtWidgets.QGridLayout(self.misfitDialog)
    self.misfitDialog.setLayout(grid)
    misfit=QtWidgets.QLineEdit()
    grid.addWidget(misfit)
    def setValue():
        misfitValue=float(misfit.text())
        self.loadPen=QPen(QColor(*self.loadColor),self.loadWidth)
        for item in self.scene.selectedItems():
            self.parent=item
            drawLoad(self,[-4,misfitValue])
        self.misfitDialog.close()
    misfit.returnPressed.connect(setValue)
    self.misfitDialog.setWindowTitle('Misfit')
    self.misfitDialog.show()

def gLoad(self):
    self.member='load'
    if not self.scene.selectedItems():
        self.statusbar.showMessage('Select segments to add gravity load',2000)
        return
    self.loadPen=QPen(QColor(*self.loadColor),self.loadWidth)

    for item in self.scene.selectedItems():
        # ps=self.df[(self.df['Graphitem']==item)]['Robject'].iloc[0]
        self.parent=item
        drawLoad(self,True)