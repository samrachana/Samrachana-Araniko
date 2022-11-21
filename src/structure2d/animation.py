from PySide2 import QtCore, QtGui, QtWidgets
from sampleDatas import resource_path
from PySide2.QtWidgets import QDockWidget, QSizePolicy,QProgressBar
from PySide2.QtCore import Qt
from time import sleep
from structure2d.animationCalculations import calculateFrameMotionData,calculateTimeGraphData,calculateVectorDiagramData
from numpy import nan,isnan,arange
from sdPy.simulationMethods import nanRows

def plotPath(self,dataMatrix,pen):
    index = [-1] + list(nanRows(dataMatrix))
    for i in arange(len(index)-1):
        data=(dataMatrix[index[i]+1:index[i+1]])
    
        rect = QtGui.QPainterPath(QtCore.QPointF(self.rrts(data[0][0]),self.rrts(data[0][1])))
        for i in range(1,len(data),1):
            rect.lineTo(QtCore.QPointF(self.rrts(data[i][0]),self.rrts(data[i][1])))

        # rect.setFillRule(QtCore.Qt.WindingFill)
        rect=self.scene.addPath(rect,pen)
        self.toClear.append(self.scene.items()[0]) 


def animateStructure(self):
    self.toClear=[]
    if not (self.animationVectorDiagram.isChecked()
        or self.animationSimulateMotion.isChecked()
        or self.animationTimeGraph.isChecked()):
        self.statusbar.showMessage('Please select the type of animation first')
        self.animationPlay.setChecked(False)
        return
    totalKeyFrames=self.fps*self.duration
    self.progressBar.setMaximum(totalKeyFrames)
    self.progressBar.setFormat('Frame No: %v')
    loads=self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]
    for load in range(len(loads)):
        loads.iloc[load]['Graphitem'].hide()
    while (self.keyFrameNo != totalKeyFrames):
        if self.pause:self.pause=False;break

        if self.deletePlot:
            [self.scene.removeItem(i) for i in self.toClear]
            self.toClear=[]
        data=self.animationPlotData[self.keyFrameNo][:,1:-1]
        plotPath(self,data,self.animationPen)
        # rect = QtGui.QPainterPath(QtCore.QPointF(self.rrts(data[0][0]),self.rrts(data[0][1])))
        # for i in range(1,len(data),1):
        #     rect.lineTo(QtCore.QPointF(self.rrts(data[i][0]),self.rrts(data[i][1])))
        # rect=self.scene.addPath(rect,self.animationPen) 
        # self.toClear.append(rect)

        data=self.loadPlotData[self.keyFrameNo]
        plotPath(self,data, self.loadPen)
        # rect = QtGui.QPainterPath(QtCore.QPointF(self.rrts(data[0][0]),self.rrts(data[0][1])))
        # for i in range(1,len(data),1):
        #     rect.lineTo(QtCore.QPointF(self.rrts(data[i][0]),self.rrts(data[i][1])))
        # rect=self.scene.addPath(rect,self.loadPen)         
        
        self.deletePlot=True
        self.keyFrameNo+=1
        self.progressBar.setValue(self.keyFrameNo)
        sleep(self.duration/totalKeyFrames)
        self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio);

        self.app.processEvents()

    if self.keyFrameNo == totalKeyFrames:
        [self.scene.removeItem(i) for i in self.toClear]
 
        self.deletePlot=False      
        self.animationPlay.setChecked(False)

        for load in range(len(loads)):
            loads.iloc[load]['Graphitem'].show()
        self.keyFrameNo=0
        self.progressBar.setValue(self.keyFrameNo)
        

def animationToolbar(self,app):
    self.keyFrameData=[]
    self.animationPlotData=None
    self.pause=False
    self.keyFrameNo=0
    self.deletePlot=False
    self.dockAnimationBar=QDockWidget('Animation Bar',self.MainWindow)
    self.animationBar = QtWidgets.QToolBar('Animation Bar',self.MainWindow)
    
    # self.MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.animationBar)
    self.dockAnimationBar.setWidget(self.animationBar)
    self.MainWindow.addDockWidget(Qt.BottomDockWidgetArea,self.dockAnimationBar)

    self.animationBar.setAutoFillBackground(True)
    self.animationBar.setIconSize(QtCore.QSize(40, 30))
    self.animationBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    self.animationBar.setEnabled(True)

    self.animationVectorDiagram = QtWidgets.QAction()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolVectorDiagram.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.animationVectorDiagram.setIcon(icon)   
    self.animationVectorDiagram.setCheckable(True) 
    self.animationBar.addAction(self.animationVectorDiagram)
   
    self.animationSimulateMotion = QtWidgets.QAction()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolSimulateMotion.png")), QtGui.QIcon.Normal,QtGui.QIcon.On)
    self.animationSimulateMotion.setIcon(icon)    
    self.animationSimulateMotion.setCheckable(True)
    self.animationBar.addAction(self.animationSimulateMotion)
    
    self.animationBar.addSeparator()
 
    self.animationPlay = QtWidgets.QAction()
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(resource_path("./ico/Tools/toolPlay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon1.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolpause.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
    self.animationPlay.setIcon(icon1)
    self.animationPlay.setCheckable(True)
    self.animationBar.addAction(self.animationPlay)

    # self.animationPause = QtWidgets.QAction()
    # icon2 = QtGui.QIcon()
    # icon2.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolpause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    # self.animationPause.setIcon(icon2)
    # self.animationBar.addAction(self.animationPause)


    self.animationPrevious = QtWidgets.QAction()
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolprev.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.animationPrevious.setIcon(icon3)
    self.animationBar.addAction(self.animationPrevious)


    self.progressBar=QProgressBar()
    self.animationBar.addWidget(self.progressBar)

    self.animationNext = QtWidgets.QAction()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolnext.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.animationNext.setIcon(icon)    
    self.animationBar.addAction(self.animationNext)

    self.animationBar.addSeparator()


    self.animationTimeGraph = QtWidgets.QAction()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(resource_path("./ico/tools/toolTimeGraph.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.animationTimeGraph.setIcon(icon)    
    self.animationTimeGraph.setCheckable(True)
    self.animationBar.addAction(self.animationTimeGraph)

    self.animationSimulateMotion.triggered.connect(lambda:calculateFrameMotionData(self))
    self.animationVectorDiagram.triggered.connect(lambda:calculateVectorDiagramData(self))
    self.animationTimeGraph.triggered.connect(lambda:calculateTimeGraphData(self))
    def nextFrame():
        self.keyFrameNo+=10
        if self.keyFrameNo>(self.fps*self.duration):self.keyFrameNo=self.fps*self.duration
    self.animationNext.triggered.connect(nextFrame)
    def previousFrame():
        if self.keyFrameNo==(self.fps*self.duration):
           self.keyFrameNo-=10
           play()
        else:
            self.keyFrameNo-=10
        if self.keyFrameNo<0:self.keyFrameNo=0
    self.animationPrevious.triggered.connect(previousFrame)
    def pause():

        self.pause=True
    # self.animationPause.triggered.connect(pause)
    def play():
        if self.animationPlay.isChecked():
            animateStructure(self)
        else:    
            self.pause=True
    self.animationPlay.triggered.connect(play)
    # self.animationBar.addWidget(self.spacerWidget)    

    # self.animationBar.show()