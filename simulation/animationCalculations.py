from typing import final
from sdPy.simulationMethods import fillAnimationFrames, getRescaledData, makeFunData
from sdPy.loadMethods import loadPlotData2
from sdPy.functionDefinitions import convertTo2D,convertTo3D
from sdPy.simulationMethods import vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp
from PySide2 import QtWidgets,QtGui,QtCore
from threads import MultiThread
from numpy import vstack,nan
from numpy.linalg import norm
import math
scaler=lambda x: math.floor(math.log10(x)) if x>1 else (math.floor(math.log10(x)) if x>0 else 0) 
def slicer(a,n=None,noOfSlice=None):
    if noOfSlice:
        n=int(len(a)/noOfSlice)
    for i in range(0, len(a),n):
        yield a[i:i+n]

def calculateMaxFrame(self):
    maxFrame=maxLoad=0
    for i,frame in self.ui.finalKeyFrameStructures.items():
        loads=frame['loads']
        maxToad=[x['peak']*max(norm(x['P1']-x['parentSegment']['P1']),norm(x['P1']-x['parentSegment']['P3'])) for x in loads]    
        maxToad=max(*maxToad) if len(maxToad)>1 else maxToad[0]  
        if maxToad > maxLoad : maxFrame=i;maxLoad=maxToad
        self.ui.app.processEvents()
    return maxFrame

def setScales(self):
    self.adjuster=False
    self.singleStep=10**scaler(self.zoomFactor)
    self.animationScaleBox.setSingleStep(self.singleStep)
    decimals= -scaler(self.zoomFactor) if scaler(self.zoomFactor)<0 else 0
    self.animationScaleBox.setMinimum(10**(-max(5,decimals+1)))
    self.animationScaleBox.setDecimals(max(5,decimals+1))
    self.animationScaleBox.setValue(self.zoomFactor)
    self.adjuster=True

def MultiProcessor(self,function,indexedParameters,parameters,keyFrames):
    finalData={}
    threadCount=max(1,QtCore.QThreadPool.globalInstance().maxThreadCount())
    keys=list(slicer(keyFrames,noOfSlice=4-1))

    def result(matrix):
        finalData.update(matrix)
        # print(list(matrix.keys())[-1])
        self.statusbar.showMessage(f'Loading: {len(finalData)}%')
        print(len(finalData))
        if len(keyFrames)==len(finalData):
            start(self,finalData)
            return finalData
    # print(keys)
    # self.thread0 = QtCore.QThreadPool()
    # worker0=MultiThread(function,indexedParameters,parameters,keys[0])
    # worker0.signals.result.connect(result)
    # self.thread0.start(worker0)

    # self.ui.thread1 = QtCore.QThreadPool()
    # worker1=MultiThread1(function,indexedParameters,parameters,keys[1])
    # worker1.signals.result.connect(result)
    # self.thread0.start(worker1)

    # self.thread2 = QtCore.QThreadPool()
    # worker2=MultiThread2(function,indexedParameters,parameters,keys[2])
    # worker2.signals.result.connect(result)
    # self.thread2.start(worker2)
    # threadPool = QtCore.QThreadPool.globalInstance()
    # for i in range(len(keys)):
    #     # setattr(self,'thread'+str(i),QtCore.QThreadPool())
    #     # setattr(self,'worker'+str(i), MultiThread(function, indexedParameters,parameters,keys[i]))
    #     # getattr(self,'worker'+str(i)).signals.result.connect(result)
    #     # getattr(self,'thread'+str(i)).start(getattr(self,'worker'+str(i)))        
    #     runnable=  MultiThread(function, indexedParameters,parameters,keys[i])
    #     runnable.signals.result.connect(result)
    #     threadPool.start(runnable)
  

def calculateVectorDiagramData(self):
    if self.animationVectorDiagram.isChecked(): 
        pass 
    else: 
        return

    self.animationBarInitialState()
    self.animationVectorDiagram.setChecked(True)    
    self.statusbar.showMessage('Calculating...')

    try:
        segments=[]
        if len(self.scene.selectedItems()):
            for i in self.scene.selectedItems():
                segment=self.df[(self.df['Graphitem']==i)&(self.df['Class']=='segment')]['Robject']
                if not segment.empty :
                    segments.append(segment.iloc[0])
                self.ui.app.processEvents()
        else:
            segments=list(self.df[self.df['Class']=='segment']['Robject'])
            [x.setSelected(True) for x in self.df[self.df['Class']=='segment']['Graphitem']]
            self.statusbar.showMessage('No segments are selected. So, all the segments are selected by default',5000)        
        self.selectedSegments=segments
        # if len(segments)==0:raise Exception
        function=self.vectorDiagramOptionsDict[self.vectorDiagramOptions.currentText()]
        currenttext=self.vectorDiagramOptions.currentText()
        if currenttext=='Shear Force' or currenttext=='DisplacementY':
            component='y'
        elif currenttext=='Axial Force' or currenttext=='DisplacementX':
            component='x'    
        else:
            component=None
        vectorDiagramData={}
        masterData=self.masterData

        self.maxFrame=maxFrame=calculateMaxFrame(self)
        self.ui.app.processEvents()
        calc= lambda x: function(convertTo3D(x),masterData[maxFrame],component,self.ui.shearMode,self.ui.inextensibleMode,False,self.ui.NoOfPointsInVector,1)
        self.ui.app.processEvents()
        rescaler=[calc(x) if component else calc(x) for x in segments]  
        self.ui.app.processEvents()
        self.zoomFactor,_=getRescaledData([convertTo3D(x) for x in segments],rescaler)
        
        setScales(self)

        self.ZoomFactorResponse,self.ZoomFactorAction=self.zoomFactor,self.zoomFactor

        if self.vectorDiagramOptions.currentIndex()>3:            
            parameters=[component,self.ui.shearMode,self.ui.inextensibleMode,False,self.ui.NoOfPointsInVector,self.ZoomFactorResponse]  
        else:
            parameters=[component,self.ui.shearMode,self.ui.inextensibleMode,False,self.ui.NoOfPointsInVector,self.ZoomFactorAction]  

        for i in self.keyFrames:
            fdata= function(convertTo3D(segments[0]),masterData[i],*parameters) 
            fdata=vstack((fdata,[nan,nan,nan,nan]))
            for segment in segments[1:]:
                data= function(convertTo3D(segment),masterData[i],*parameters) 
                data=vstack((data,[nan,nan,nan,nan]))
                fdata=vstack((fdata,data))
                self.ui.app.processEvents()
                
            vectorDiagramData[i]=fdata
            self.statusbar.showMessage(f'Loading: {round(i/self.keyFrames[1]*100)}%')
            self.ui.app.processEvents() 
        self.animationPen=QtGui.QPen(QtGui.QColor(*self.diagramColors[self.vectorDiagramOptions.currentText()]),3)
        if self.animationModeOptions.currentIndex()==0:
            fillAnimationFrames(vectorDiagramData,'spline')
        self.keyFrameData.append({
            'function':self.vectorDiagramOptions.currentText(),
            'segments':segments,
            'data':vectorDiagramData
            })
        self.animationPlotData=vectorDiagramData
        self.animationPlay.setDisabled(False)

        self.statusbar.showMessage('Press play button to start animation',2000)
        self.keyFrameNo=self.ui.fps*self.ui.duration
        self.keyFrameNo=0

    except Exception as e:
        import traceback
        traceback.print_exc()
        # self.statusbar.showMessage("Select segments for vector diagrams",2000)    
        self.animationVectorDiagram.setChecked(False)


def calculateTimeGraphData(self):
    if self.animationTimeGraph.isChecked(): 
        pass 
    else: 
        return
    self.animationBarInitialState()
    self.animationTimeGraph.setChecked(True)
    self.animationPlay.setDisabled(True)
    
    from sdPy.simulationMethods import timeGraphData
    i=self.scene.selectedItems()[0]
    s=self.df[(self.df['Graphitem']==i)&(self.df['Class']=='segment')]['Robject']
    if not s.empty :
        segment=s.iloc[0]
    else:
        return
    # for i in self.keyFrameData:
    #     if self.vectorDiagramOptions.currentText() ==i['function']:
    #         segmentID=i['segments']
    segmentName=self.df[(self.df['Graphitem']==i)&(self.df['Class']=='segment')]['Name'].iloc[0]
    segmentID=self.keyFrameData[-1]['segments'].index(segment)
    
    timegraphdata=timeGraphData(segmentID,segment,self.keyFrameData[-1]['data'],self.ZoomFactorAction)
    import pyqtgraph as pg
    from numpy import array
    
    dialog=QtWidgets.QDialog(parent=self.MainWindow)
    dialog.setWindowTitle('Time Graph')
    dialog.resize(600,500)
    win = pg.GraphicsWindow(parent=dialog)
    win.setBackground(self.ui.bgColor)

    gridLayout=QtWidgets.QGridLayout()
    dialog.setLayout(gridLayout)
    gridLayout.addWidget(win,0,0,1,1)   
    p1 = win.addPlot(row=1, col=0)
    from PySide2.QtCore import Qt
    slider=QtWidgets.QSlider(Qt.Horizontal)
    keys=list(timegraphdata.keys())
    interval=keys[1]-keys[0]
    slider.setRange(keys[0],len(keys)*10)
    slider.setTickInterval(interval)
    takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))    
    gridLayout.addWidget(slider,1,0,2,1)

    function=self.vectorDiagramOptions.currentText()
    # segmentName=self.df[(self.df['Robject']==segment)].iloc[0]['Name']
    
    self.dockTimeGraph =QtWidgets.QDockWidget('Time Graph',self.MainWindow)
    self.dockTimeGraph.setWidget(dialog)
    try:
        self.dockGraphicsView
    except:
        self.dockGraphicsView=QtWidgets.QDockWidget('Main Graph',self.MainWindow)
        self.dockGraphicsView.setWidget(self.centralwidget)
        self.dockGraphicsView.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)            
        self.MainWindow.addDockWidget(QtCore.Qt.TopDockWidgetArea,self.dockGraphicsView)


    self.MainWindow.addDockWidget(QtCore.Qt.TopDockWidgetArea,self.dockTimeGraph)
    self.MainWindow.tabifyDockWidget(self.dockGraphicsView,self.dockTimeGraph)

    self.MainWindow.setTabPosition(QtCore.Qt.TopDockWidgetArea, 
                                    QtWidgets.QTabWidget.North)

    def showTimeGraphs():
        if p1.items:
            p1.clear()
            # [p1.items[i].hide() for i in p1.items]
        index=takeClosest(slider.value()/(len(keys)*10)*keys[-1],keys)
        # index=takeClosest(slider.value(),keys)

        shear = timegraphdata[index]
        pen = pg.mkPen(color=self.ui.bmdColor,width = 2)
        shearForceY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name=self.vectorDiagramOptions.currentText())                
        p1.addItem(shearForceY)
        p1.setLabel(axis='bottom', text="<span style='font-size: 12pt'>%s in %s @ x=%0.3f </span>" % (function,segmentName,index))
        vb1=p1.vb
        vLine1 = pg.InfiniteLine(angle=90, movable=False)
        hLine1 = pg.InfiniteLine(angle=0, movable=False)
        p1.addItem(vLine1, ignoreBounds=True)
        p1.addItem(hLine1, ignoreBounds=True)
        def mouseMovedactionGraphs(evt):
            pos = evt[0]
            if p1.sceneBoundingRect().contains(pos):
                mousePoint = vb1.mapSceneToView(pos)
                # index = int(mousePoint.x())   index = int(mousePoint.x())
                
                # if index > 0 and index < array(R.r.range(robj))[0]:
                p1.setLabel(axis='top', text="<span style='font-size: 12pt'>x=%0.3f <span style='color: red'>y=%0.3f</span>" % (mousePoint.x(), mousePoint.y()))
                vLine1.setPos(mousePoint.x())
                hLine1.setPos(mousePoint.y())
        dialog.proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=10, slot=mouseMovedactionGraphs)
    showTimeGraphs()
    slider.valueChanged.connect(showTimeGraphs)
    # win.show()
    dialog.show()
    # self.animationPlay.setDisabled(False)
    # self.animationBar.setDisabled(True)
    


def calculateFrameMotionData(self):
    if self.animationSimulateMotion.isChecked(): 
        pass 
    else: 
        return
    self.animationBarInitialState()
    self.animationSimulateMotion.setChecked(True)
    from sdPy.simulationMethods import simulateFrameMotion2D,simulateTrussMotion2

    simulationFrameMotionData={}
    finalKeyFrameStructures=self.ui.finalKeyFrameStructures
    masterData=self.masterData
    shear=self.ui.shearMode
    inextensible=self.ui.inextensibleMode
    keyFrames=self.keyFrames
    function=simulateTrussMotion2 if self.ui.trussMode else simulateFrameMotion2D

    self.maxFrame=maxFrame=calculateMaxFrame(self)
    segments=list(self.ui.df[(self.ui.df['Flag']==True)&(self.ui.df['Class']=='segment')]['Robject'])
    self.selectedSegments=segments
    calc= function(self.ui.finalKeyFrameStructures[maxFrame],masterData[maxFrame],shear,inextensible,self.ui.NoOfPointsInMotion,1)
    # rescaler=[calc(x)[component] if component else calc(x) for x in segments]  
    self.ui.app.processEvents()
    self.zoomFactor,_=getRescaledData([convertTo3D(x) for x in segments],makeFunData(calc))

    setScales(self)

    self.ZoomFactorMotion=self.zoomFactor

    # indexedParameters=[finalKeyFrameStructures,masterData]
    # parameters=[shear,inextensible,self.ui.NoOfPointsInMotion,self.ZoomFactorMotion]


    # simulationFrameMotionData=MultiProcessor(self,function,indexedParameters,parameters,keyFrames)
    for i in keyFrames:
        simulationFrameMotionData[i]=function(finalKeyFrameStructures[i],masterData[i],shear,inextensible,self.ui.NoOfPointsInMotion,self.ZoomFactorMotion)
        self.statusbar.showMessage(f'Loading: {round(i/keyFrames[-1]*100)}%')
        self.ui.app.processEvents()
    start(self,simulationFrameMotionData)
def start(self,simulationFrameMotionData):        
    if self.animationModeOptions.currentIndex()==0:
        fillAnimationFrames(simulationFrameMotionData,'spline')
    
    self.animationPlotData=simulationFrameMotionData
    self.animationPen=QtGui.QPen(QtGui.QColor(*self.ui.segmentColor),3)
    self.animationPlay.setDisabled(False)

    self.statusbar.showMessage('Press play button to start animation',2000)
    
    self.keyFrameNo=self.ui.fps*self.ui.duration
    self.keyFrameNo=0

    # worker2 = MultiThread(function, indexdedParameters,parameters,keys2)
    # worker2.signals.result.connect(result2)
    # self.thread2.start(worker2)    
    
    # for i in keyFrames[0:len(keyFrames/2)]:
    #     simulationFrameMotionData[i]=function(finalKeyFrameStructures[i],masterData[i],shear,inextensible,self.ui.NoOfPointsInMotion,self.ZoomFactorMotion)
    #     self.statusbar.showMessage(f'Loading: {round(i/keyFrames[-1]*100)}%')
    #     self.ui.app.processEvents()


    # for i in keyFrames:
    #     simulationFrameMotionData[i]=function(finalKeyFrameStructures[i],masterData[i],shear,inextensible,self.ui.NoOfPointsInMotion,self.ZoomFactorMotion)
    #     self.statusbar.showMessage(f'Loading: {round(i/keyFrames[-1]*100)}%')
    #     self.ui.app.processEvents()


    # if self.animationModeOptions.currentIndex()==0:
    #     fillAnimationFrames(simulationFrameMotionData,'spline')
    
    # self.animationPlotData=simulationFrameMotionData
    # self.animationPen=QtGui.QPen(QtGui.QColor(*self.ui.segmentColor),3)
    # self.animationPlay.setDisabled(False)

    # self.statusbar.showMessage('Press play button to start animation',2000)
    
    # self.keyFrameNo=self.ui.fps*self.ui.duration
    # self.keyFrameNo=0


    # def process(key):
    #     matrix=[]
    #     for i in key:
            
    #         matrix={i:self.function(*[x[i] for x in self.indexedParameters],
    #         *self.parameters) for i in self.keys }            
    #         self.statusbar.showMessage(f'Loading: {round(i/keyFrames[-1]*100)}%')
    #         self.ui.app.processEvents()
    #     finalData.update(matrix)
    #     if len(keyFrames)==len(finalData):
    #         start(self,finalData)
    #         return finalData
    # print(__name__)
    # if __name__ =='simulation.animationCalculations':
    #     for i in range(len(keys)):
    #         setattr(self,'p'+str(i),multiprocessing.Process(target=process,args=(keys[i],)))
    #         getattr(self,'p'+str(i)).start()
    #         getattr(self,'p'+str(i)).join()

 



   