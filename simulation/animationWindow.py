
from numpy.core.fromnumeric import trace
from sdPy.supportMethods import supportPlotData2
from sdPy.segmentMethods import segPlotData2
from sdPy.loadMethods import loadPlotData2
from sdPy.functionDefinitions import convertTo2D, convertTo3D
from PySide2.QtWidgets import (QComboBox, QDockWidget, QDoubleSpinBox, QGraphicsItem, QGraphicsView, QLabel, QLineEdit, QMainWindow,QGraphicsScene,QAction, QProgressBar, QPushButton, QSpinBox,QToolBar,
                                QDockWidget,QProgressBar)
from simulation.animationMainWindow import Ui_MainWindow
from PySide2.QtGui import QColor, QCursor, QImage, QPainterPath, QPen, QPainter,QPixmap,QIcon, QRegExpValidator
from PySide2.QtCore import QPointF, QRegExp, Qt,QSize
from sampleDatas import resource_path

from time import sleep
from simulation.animationCalculations import calculateFrameMotionData,calculateTimeGraphData,calculateVectorDiagramData
from simulation.mouseGraphics import GraphicsScene
from numpy import nan,isnan,arange,vstack,abs
from sdPy.simulationMethods import fillAnimationFrames, getRescaledData, makeFunData, nanRows,makeFrameData

from sdPy.simulationMethods import (vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp,
                vectorDiagramDataAngles2Dcomp,vectorDiagramDataDisps2Dcomp)
from sdPy.simulationMethods import vectorDiagramDataTrussDisps2Dcomp,vectorDiagramDataTrussForces2Dcomp

from pandas import DataFrame
class AnimationWindow(Ui_MainWindow):
    def __init__(self,ui):
        self.MainWindow=QMainWindow(parent=ui.MainWindow)
        Ui_MainWindow.setupUi(self, self.MainWindow)   
        self.ui=ui
        self.variables()
        self.createScene()
        self.animationToolbar()
        self.dockAnimationBar.show()
        self.animationPropertiesBar()
        self.postSimulationWindow()
        self.plotStructure()
        self.MainWindow.show()

    def variables(self):
        self.loadPen=QPen(QColor(*self.ui.loadColor),self.ui.loadWidth)
        self.maxFrame=None
        self.diagramColors={
            'Bending Moment':self.ui.bmdColor,
            'Resultant Force':self.ui.sfdColor,
            'Shear Force':self.ui.sfdColor,
            'Axial Force':self.ui.afdColor,
            'Slope':self.ui.rotationColor,
            'DisplacementX':self.ui.translationColor,
            'DisplacementY':self.ui.translationColor}
        self.zoomState=0
        self.toClear=[]
        self.zoomFactor=0
        self.selectedSegments=[]
        self.animationPlotData=[]
        self.captureFrame=False
        self.df = DataFrame(columns=["Name","Class", "Robject","Graphitem"],index=None)
    def animationBarInitialState(self):
        self.keyFrameNo=0
        self.animationVectorDiagram.setChecked(False)
        self.animationSimulateMotion.setChecked(False)
        self.animationTimeGraph.setChecked(False)
        if self.animationPlay.isChecked():
            self.animationPlay.setChecked(False)
            self.pause=True
        
        self.vectorDiagramOptions.setDisabled(False)
        self.animationPlay.setDisabled(True)
        self.progressBar.setValue(0)

    def zoomOut(self):
        if self.zoomState>-10:
            self.graphicsView.scale(1/1.1,1/1.1)
            self.zoomState-=1

    def zoomIn(self):
        if self.zoomState<30:            
            self.graphicsView.scale(1.1,1.1)
            self.zoomState+=1

    def createScene(self):
        self.scene = GraphicsScene(self)

        self.graphicsView = QGraphicsView(self.scene, self.MainWindow)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.viewport().installEventFilter(self.MainWindow)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        # self.aw.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        
        from PySide2.QtGui import QTransform
        self.graphicsView.setTransform(QTransform(1., 0., 0., -1., 0, 0))
        # self.graphicsView.rotate(270)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        # self.aw.grid()
        xrange = 50 * round((self.MainWindow.width()-35)/50)
        yrange = 50*round((self.MainWindow.height()-150)/50)
        self.scene.addLine(0, 0, 0, yrange, QPen(Qt.green, 0.05))
        self.scene.addLine(0, 0, xrange, 0, QPen(Qt.green, 0.05))    # self.aW.show()
        self.graphicsView.setBackgroundBrush(QColor(*self.ui.bgColor));

    def animationPropertiesBar(self):
     # Vector diagram Options
        self.MainWindow.addToolBarBreak(Qt.TopToolBarArea)
        self.propertiesBar = QToolBar('Properties Bar',self.MainWindow)
        self.MainWindow.addToolBar(Qt.TopToolBarArea, self.propertiesBar)
        
        self.propertiesBar.addWidget(QLabel('Vector Diagram'))
        # self.ui.trussMode=False
        if not self.ui.trussMode:
            self.vectorDiagramOptionsDict={
                'Bending Moment':vectorDiagramDataMoments2D,
                'Resultant Force':vectorDiagramDataForces2D,
                'Shear Force':vectorDiagramDataForces2Dcomp,
                'Axial Force':vectorDiagramDataForces2Dcomp,
                'Slope':vectorDiagramDataAngles2Dcomp,
                'DisplacementX':vectorDiagramDataDisps2Dcomp,
                'DisplacementY':vectorDiagramDataDisps2Dcomp
                }
        else:
            self.vectorDiagramOptionsDict={
                'Axial Force':vectorDiagramDataTrussForces2Dcomp,
                'DisplacementX':vectorDiagramDataTrussDisps2Dcomp,
                'DisplacementY':vectorDiagramDataTrussDisps2Dcomp
                }

        self.vectorDiagramOptions=QComboBox()
        self.vectorDiagramOptions.addItems(list(self.vectorDiagramOptionsDict.keys()))   
        self.propertiesBar.addWidget(self.vectorDiagramOptions)
        self.vectorDiagramOptions.setDisabled(True)

        self.propertiesBar.addSeparator()
        self.animationModeOptions=QComboBox()
        self.animationModeOptions.addItems(['Quick','Accurate'])
        self.propertiesBar.addWidget(QLabel('Animation Mode'))
        self.propertiesBar.addWidget(self.animationModeOptions)
        self.animationModeOptions.setDisabled(False)
        
        self.vectorDiagramOptions.currentIndexChanged.connect(lambda:calculateVectorDiagramData(self))
        # self.animationModeOptions.currentIndexChanged.connect(animationModeChanged)
        self.propertiesBar.addSeparator()
        self.measureButton = QPushButton('Measure')
        self.propertiesBar.addWidget(self.measureButton)
        self.measureButton.clicked.connect(self.measure)

        self.propertiesBar.addSeparator()
        self.exportVideoButton = QPushButton('Export Video')
        self.propertiesBar.addWidget(self.exportVideoButton)
        self.exportVideoButton.clicked.connect(self.exportVideo)

        self.propertiesBar.addSeparator()
        self.propertiesBar.addWidget(QLabel('Zoom Factor'))
        self.animationScaleBox = QDoubleSpinBox()
        self.animationScaleBox.setRange(10e-10,10e10)
        self.propertiesBar.addWidget(self.animationScaleBox)
        self.animationScaleBox.valueChanged.connect(self.animationScale)
        self.adjuster=True
        self.animationScaleBox.textChanged.connect(self.adjustScale)

        self.propertiesBar.addSeparator()
        self.visualizeButton = QPushButton('Visualize')
        self.propertiesBar.addWidget(self.visualizeButton)
        from structure2d.visualizer import visualize
        self.visualizeButton.clicked.connect(lambda:visualize(self))

    def adjustScale(self):

        if self.adjuster:
            from simulation.animationCalculations import scaler
            value=self.animationScaleBox.value()
            self.animationScaleBox.setSingleStep(10**scaler(value))
            self.animationScale()
            
       
    def exportVideo(self):
        if self.animationPlotData:
            from PySide2.QtWidgets import QFileDialog
            fileName, _ = QFileDialog.getSaveFileName(caption="Save File")
            if fileName=='': self.statusbar.showMessage('File not saved, Enter proper file name to save file',2000); return
            if not fileName.endswith(('.mp4')):
                self.fileName=fileName+'.mp4'
            else:
                self.fileName= fileName 

            self.captureFrame=True
            self.keyFrameNo=0
            self.exportVideoButton.setDisabled(True)
            self.animateStructure()



        else:
            self.statusbar.showMessage('Select a type of animation first',5000)
    def animationScale(self):
        if self.selectedSegments and self.zoomFactor and self.animationPlotData:
            segments=[convertTo3D(x) for x in self.selectedSegments]
            scale=self.animationScaleBox.value()/self.zoomFactor
            magnitude = self.animationPlotData[self.maxFrame][:,-1]
            # if max(abs(magnitude))*scale<10:
            try:
                data={x:makeFrameData(getRescaledData(segments,makeFunData(self.animationPlotData[x]),scale)[1]) for x in self.animationPlotData.keys()}
                self.animationPlotData=data
                self.zoomFactor=scale*self.zoomFactor
            except:
                import traceback
                traceback.print_exc()
    def measure(self):
        self.todraw='measure'
        self.count=0
        self.pause=True
        self.animationPlay.setChecked(False)

        cursor=QPixmap(resource_path(self.ui.cursorPath+"draw"+'Measure'+".png"))
        self.graphicsView.setCursor(QCursor(cursor,5,32))     


    def animationToolbar(self):

        self.keyFrameData=[]
        self.animationPlotData=None
        self.pause=False
        self.keyFrameNo=0
        # self.deletePlot=False
        self.dockAnimationBar=QDockWidget('Animation Bar',self.MainWindow)
        self.animationBar = QToolBar('Animation Bar',self.MainWindow)
        
        # self.MainWindow.addToolBar(Qt.BottomToolBarArea, self.animationBar)
        self.dockAnimationBar.setWidget(self.animationBar)
        self.MainWindow.addDockWidget(Qt.BottomDockWidgetArea,self.dockAnimationBar)

        self.animationBar.setAutoFillBackground(True)
        self.animationBar.setIconSize(QSize(40, 30))
        self.animationBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.animationBar.setEnabled(True)

        self.animationVectorDiagram = QAction()
        icon = QIcon()
        icon.addPixmap(QPixmap(resource_path("./ico/tools/toolVectorDiagram.png")), QIcon.Normal, QIcon.Off)
        self.animationVectorDiagram.setIcon(icon)   
        self.animationVectorDiagram.setCheckable(True) 
        self.animationBar.addAction(self.animationVectorDiagram)
    
        self.animationSimulateMotion = QAction()
        icon = QIcon()
        icon.addPixmap(QPixmap(resource_path("./ico/tools/toolSimulateMotion.png")), QIcon.Normal,QIcon.On)
        self.animationSimulateMotion.setIcon(icon)    
        self.animationSimulateMotion.setCheckable(True)
        self.animationBar.addAction(self.animationSimulateMotion)
        
        self.animationBar.addSeparator()
    
        self.animationPlay = QAction()
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(resource_path("./ico/Tools/toolPlay.png")), QIcon.Normal, QIcon.Off)
        icon1.addPixmap(QPixmap(resource_path("./ico/tools/toolpause.png")), QIcon.Normal, QIcon.On)
        self.animationPlay.setIcon(icon1)
        self.animationPlay.setCheckable(True)
        self.animationBar.addAction(self.animationPlay)
        self.animationPlay.setShortcut('Space')
        self.animationPrevious = QAction()
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(resource_path("./ico/tools/toolprev.png")), QIcon.Normal, QIcon.Off)
        
        self.animationPrevious.setIcon(icon3)
        self.animationBar.addAction(self.animationPrevious)
        self.animationPrevious.setShortcut('Left')

        self.progressBar=QProgressBar()
        self.animationBar.addWidget(self.progressBar)
        
        self.frameNo=QLineEdit()
        self.animationBar.addWidget(self.frameNo)
        reg_ex = QRegExp("[0-9]+")
        validator = QRegExpValidator(reg_ex)
        self.frameNo.setValidator(validator)
        self.frameNo.setMaximumWidth(50)
        def editFrame():
            value=int(self.frameNo.text())
            if value>=0 and value <= (self.ui.duration*self.ui.fps):
                self.keyFrameNo = value
                if not self.animationPlay.isChecked():
                    self.pause=True
                    self.animateStructure()
            else:
                self.statusbar.showMessage(f'Please enter value less than or equal to {self.ui.fps * self.ui.duration}',5000)    
        self.frameNo.editingFinished.connect(editFrame)
        
        self.animationNext = QAction()
        icon = QIcon()
        icon.addPixmap(QPixmap(resource_path("./ico/tools/toolnext.png")), QIcon.Normal, QIcon.Off)
        self.animationNext.setIcon(icon)    
        self.animationNext.setShortcut('Right')
        self.animationBar.addAction(self.animationNext)

        self.animationBar.addSeparator()


        self.animationTimeGraph = QAction()
        icon = QIcon()
        icon.addPixmap(QPixmap(resource_path("./ico/tools/toolTimeGraph.png")), QIcon.Normal, QIcon.Off)
        self.animationTimeGraph.setIcon(icon)    
        self.animationTimeGraph.setCheckable(True)
        self.animationBar.addAction(self.animationTimeGraph)

        self.animationSimulateMotion.triggered.connect(lambda:calculateFrameMotionData(self))
        self.animationVectorDiagram.triggered.connect(lambda:calculateVectorDiagramData(self))
        self.animationTimeGraph.triggered.connect(lambda:calculateTimeGraphData(self))
        def nextFrame():
            self.keyFrameNo+=10
            if self.keyFrameNo>(self.ui.fps*self.ui.duration):self.keyFrameNo=self.ui.fps*self.ui.duration
            self.progressBar.setValue(round(self.keyFrameNo/self.ui.fps*1000,3))
            if not self.animationPlay.isChecked():
                self.pause=True
                self.animateStructure()        
        self.animationNext.triggered.connect(nextFrame)
        def previousFrame():
            if self.keyFrameNo==(self.ui.fps*self.ui.duration):
                self.keyFrameNo-=10
                play()
            else:
                self.keyFrameNo-=10
            if self.keyFrameNo<0:self.keyFrameNo=0
            self.progressBar.setValue(round(self.keyFrameNo/self.ui.fps*1000,3))
            if not self.animationPlay.isChecked():
                self.pause=True
                self.animateStructure() 
        self.animationPrevious.triggered.connect(previousFrame)

        def play():
            if self.animationPlay.isChecked():
                self.animateStructure()
            else:    
                self.pause=True
        self.animationPlay.triggered.connect(play)
        # self.animationBar.addWidget(self.spacerWidget)    

        # self.animationBar.show()   
        # 
        #   

    def plotPath(self,dataMatrix,pen):
        index = [-1] + list(nanRows(dataMatrix))
        for i in arange(len(index)-1):
            data=(dataMatrix[index[i]+1:index[i+1]])
        
            rect = QPainterPath(QPointF(self.ui.rrts(data[0][0]),self.ui.rrts(data[0][1])))
            for i in range(1,len(data),1):
                rect.lineTo(QPointF(self.ui.rrts(data[i][0]),self.ui.rrts(data[i][1])))

            rect=self.scene.addPath(rect,pen)
            self.toClear.append(self.scene.items()[0]) 


    def animateStructure(self):

        if not (self.animationVectorDiagram.isChecked()
            or self.animationSimulateMotion.isChecked()
            or self.animationTimeGraph.isChecked()):
            self.statusbar.showMessage('Please select the type of animation first')
            self.animationPlay.setChecked(False)
            return
        totalKeyFrames=self.ui.fps*self.ui.duration
        self.progressBar.setMaximum(self.ui.duration*1000)
        self.progressBar.setFormat('%v ms')
        loads=self.df[(self.df['Class']=='load')]
        for load in range(len(loads)):
            loads.iloc[load]['Graphitem'].hide()
      #disable measure tool  
        if self.delete==True:
            self.scene.removeItem(self.scene.items()[0])
            self.delete=False
        if self.deleteText:
            self.scene.removeItem(self.deleteText)
            self.scene.removeItem(self.scene.items()[0])
            self.deleteText=False
        self.todraw=None
        self.count=0

        self.graphicsView.setCursor(QCursor(Qt.ArrowCursor))

        width,height=self.graphicsView.size().width(),self.graphicsView.size().height()

        while (self.keyFrameNo != totalKeyFrames+1):


            # if self.deletePlot:
            [self.scene.removeItem(i) for i in self.toClear]
            self.toClear=[]
            data=self.animationPlotData[self.keyFrameNo][:,1:-1]
            self.plotPath(data,self.animationPen)


            data=self.loadPlotData[self.keyFrameNo]
            self.plotPath(data, self.loadPen)

            # self.deletePlot=True
            self.frameNo.setText(str(self.keyFrameNo))
            self.progressBar.setValue(round(self.keyFrameNo/self.ui.fps*1000,3))
            # self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio);

            if self.captureFrame:
                image=QImage(width,height,QImage.Format_ARGB32)
                painter=QPainter(image)
                painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing | QPainter.HighQualityAntialiasing | QPainter.NonCosmeticDefaultPen)
                self.graphicsView.render(painter)
                
                painter.end()
                image.save(".\\simulation\\video\\frames\\"+str(self.keyFrameNo)+".png","PNG");                
                self.statusbar.showMessage(f'Exporting video :-   {round(self.keyFrameNo/totalKeyFrames*100)}%')
            else:
                sleep(self.ui.duration/totalKeyFrames)
            if self.pause:
                self.pause=False
                break

            self.frameNo.setText(str(self.keyFrameNo))
            self.progressBar.setValue(round(self.keyFrameNo/self.ui.fps*1000,3))
            self.ui.app.processEvents()
            self.keyFrameNo+=1
        if self.keyFrameNo == totalKeyFrames+1:
            if self.captureFrame:
                import os
                os.system(f'''.\\simulation\\video\\ffmpeg\\bin\\ffmpeg.exe -r {self.ui.fps}   -i .\\simulation\\video\\frames\\%d.png -vcodec mpeg4 -vb 20M -y {self.fileName}''')             
                self.captureFrame=False
                self.exportVideoButton.setDisabled(False)
                self.statusbar.showMessage('Video saved',5000)
            # [self.scene.removeItem(i) for i in self.toClear]
            # self.toClear=[]
            # self.deletePlot=False      
            self.animationPlay.setChecked(False)

            for load in range(len(loads)):
                loads.iloc[load]['Graphitem'].show()
            self.keyFrameNo=0
            self.progressBar.setValue(round(self.keyFrameNo/self.ui.fps*1000,3))


    def postSimulationWindow(self):
        self.userDefinedKeyframes={int(k):v for k,v in zip(list(self.ui.keyFramesDataFrame['Frame No']),self.ui.finalKeyFrameStructures.values())}
        from sdPy.simulationMethods import interpolateLoads
        def animationModeChanged():
            self.animationBar.setDisabled(True)
            self.keyFrameNo=self.ui.fps*self.ui.duration
            self.keyframeNo=0
            self.progressBar.setValue(0)
            if self.animationModeOptions.currentIndex()==1:
                try:
                    self.ui.finalKeyFrameStructures= interpolateLoads(self.ui.finalKeyFrameStructures)
                except:
                    self.ui.finalKeyFrameStructures=interpolateLoads(self.userDefinedKeyframes)
            else:
                self.ui.finalKeyFrameStructures=self.userDefinedKeyframes
            self.keyFrames=list(self.ui.finalKeyFrameStructures.keys())

            self.masterData={}
            from sdPy.structureMethods import frame2d,truss2d
            strMode=truss2d if self.ui.trussMode else frame2d
            for i in self.keyFrames:
                self.masterData[i]=strMode(self.ui.finalKeyFrameStructures[i],self.ui.shearMode,self.ui.inextensibleMode,self.ui.simplifyMode)            
                self.statusbar.showMessage(f'Preparing Evironment : {round(i/self.keyFrames[-1]*100)}%',100)
                self.ui.app.processEvents()     

            self.loadPlotData={}
            for i in self.keyFrames:
                x=self.ui.finalKeyFrameStructures[i]['loads'][0]
                x=convertTo2D(x)

                lData=loadPlotData2(
                                self.ui.rrts(x['P1']),self.ui.rrts(x['P3']),
                                self.ui.rrts(x['parentSegment']['P1']),self.ui.rrts(x['parentSegment']['P3']),self.ui.rrts(x['parentSegment']['P2']),
                                x['degree'],self.ui.rrts(x['peak']),x['normal'],x['parentSegment']['type'],self.ui.scale,self.ui.loadLogScale 
                    )/(self.ui.scale*50)
                lData=vstack((lData,[nan,nan]))    
                for x in self.ui.finalKeyFrameStructures[i]['loads'][1:]:
                    x=convertTo2D(x)
                    valData = loadPlotData2(
                                self.ui.rrts(x['P1']),self.ui.rrts(x['P3']),
                                self.ui.rrts(x['parentSegment']['P1']),self.ui.rrts(x['parentSegment']['P3']),self.ui.rrts(x['parentSegment']['P2']),
                                x['degree'],self.ui.rrts(x['peak']),x['normal'],x['parentSegment']['type'],self.ui.scale,self.ui.loadLogScale 
                    )/(self.ui.scale*50)
                    valData=vstack((valData,[nan,nan]))
                    lData=vstack((lData,valData))
                self.loadPlotData[i]=lData
                self.ui.app.processEvents()     
            if self.animationModeOptions.currentIndex()==0:
                fillAnimationFrames(self.loadPlotData,'spline')

            self.animationBar.setDisabled(False)

        animationModeChanged()
        self.animationModeOptions.currentIndexChanged.connect(animationModeChanged)

    def plotStructure(self):
        tempdf=self.ui.df
     #plot segments
        self.pen=QPen(QColor(*self.ui.segmentColor),self.ui.segmentWidth-1)    
        aa=tempdf[(tempdf['Class']=='segment')&(tempdf['Flag']==True)]    
        for element in range(len(aa)):
            Rsegment=aa.iloc[element,2]
            name=aa.iloc[element,0]
            if Rsegment['type']=='line':
                rect=self.scene.addLine(self.ui.rrts(Rsegment['P1'])[0],self.ui.rrts(Rsegment['P1'])[1],self.ui.rrts(Rsegment['P3'])[0],self.ui.rrts(Rsegment['P3'])[1],self.pen)
            else:
                data=segPlotData2(Rsegment['type'],self.ui.rrts(Rsegment['P1']),self.ui.rrts(Rsegment['P3']),self.ui.scale,self.ui.rrts(Rsegment['P2']),no=self.ui.NoOfPointsInCurvedSegments)

                rect = QPainterPath(QPointF(data[0][0],data[0][1]))
                for i in range(2,len(data),2):
                    rect.quadTo(QPointF(data[i-1][0],data[i-1][1]),QPointF(data[i][0],data[i][1]))
                rect=self.scene.addPath(rect,self.pen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable)
            self.df.loc[len(self.df)]=[name,'segment',Rsegment,self.scene.items()[0]]

     #plot loads
        loadPen=QPen(QColor(*self.ui.loadColor),self.ui.loadWidth-1)
        aa=tempdf[(tempdf['Class']=='load')&(tempdf['Flag']==True)]
        for element in range(len(aa)):
            Rload=aa.iloc[element,2]
            name=aa.iloc[element,0]
            ps=Rload['parentSegment']
            data=loadPlotData2(self.ui.rrts(Rload['P1']),self.ui.rrts(Rload['P3']),self.ui.rrts(ps['P1']),self.ui.rrts(ps['P3']),
            self.ui.rrts(ps['P2']), Rload['degree'],self.ui.rrts(Rload['peak']),Rload['normal'],ps['type'],self.ui.scale,self.ui.loadLogScale)

            rect = QPainterPath(QPointF(data[0][0],data[0][1]))
            for i in range(1,len(data),1):
                rect.lineTo(QPointF(data[i][0],data[i][1]))
                # rect.quadTo(QPointF(data[i-1][0],data[i-1][1]),QPointF(data[i][0],data[i][1]))
            rect=self.scene.addPath(rect,loadPen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable) 
            self.df.loc[len(self.df)]=[name,'load',Rload,self.scene.items()[0]]

     #plot supports
        aa=tempdf[(tempdf['Class']=='support')&(tempdf['Flag']==True)]       
        for element in range(len(aa)):
            Rsupport = aa.iloc[element,2]
            data=supportPlotData2(Rsupport['type'] , self.ui.rrts(Rsupport['location']),normal=Rsupport['normal'],scale=0.02)
            rect = QPainterPath(QPointF(data[0][0],data[0][1]))
            
            color=self.ui.supportColors[Rsupport['type']]
            self.supportPen=QPen(QColor(*color),1.5)
            
            types=aa.iloc[element,2]['type']
            for i in range(1,len(data)):
                rect.lineTo(QPointF(QPointF(data[i][0],data[i][1])))            
            rect=self.scene.addPath(rect,self.supportPen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable)
   