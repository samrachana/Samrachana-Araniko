from sdPy.simulationMethods import fillAnimationFrames
from sdPy.loadMethods import loadPlotData2
from sdPy.functionDefinitions import convertTo2D,convertTo3D
import numpy as np
from sdPy.simulationMethods import vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp
from PySide2 import QtWidgets,QtGui,QtCore

from numpy import vstack,nan

def calculateVectorDiagramData(self):
    if self.animationVectorDiagram.isChecked(): 
        pass 
    else: 
        return
    diagramColors={
        'Bending Moment':self.bmdColor,
        'Resultant Force':self.sfdColor,
        'Shear Force':self.sfdColor,
        'Axial Force':self.afdColor,
        'Slope':self.rotationColor,
        'DisplacementX':self.translationColor,
        'DisplacementY':self.translationColor}
    self.animationSimulateMotion.setChecked(False)
    self.animationTimeGraph.setChecked(False)
    self.animationPlay.setChecked(False)
    self.vectorDiagramOptions.setDisabled(False)
    self.animationPlay.setDisabled(True)
    self.statusbar.showMessage('Calculating...')

    count=0
    try:
        segments=[]
        for i in self.scene.selectedItems():
            segment=self.df[(self.df['Graphitem']==i)&(self.df['Class']=='segment')]['Robject']
            if not segment.empty :segments.append(segment.iloc[0])
            self.app.processEvents()
        
        if len(segments)==0:raise Exception
        count+=1
        function=self.vectorDiagramOptionsDict[self.vectorDiagramOptions.currentText()]
        currenttext=self.vectorDiagramOptions.currentText()
        if currenttext=='Shear Force' or currenttext=='DisplacementY':
            component='y'
        else:
            component='x'    
        vectorDiagramData={}
        masterData=self.masterData
        if self.vectorDiagramOptions.currentIndex()>3:            
            parameters=[component,self.shearMode,self.inextensibleMode,False,'vecPlot',self.NoOfPointsInVector,self.ZoomFactorResponse]  
        else:
            parameters=[component,self.shearMode,self.inextensibleMode,False,'vecPlot',self.NoOfPointsInVector,self.ZoomFactorAction]  

        for i in self.keyFrames:
            fdata= function(convertTo3D(segments[0]),masterData[i],*parameters) 
            fdata=vstack((fdata,[nan,nan]))
            for segment in segments[1:]:
                data= function(convertTo3D(segment),masterData[i],*parameters) 
                data=vstack((data,[nan,nan]))
                fdata=vstack((fdata,data))
                self.app.processEvents()
            vectorDiagramData[i]=fdata
            self.statusbar.showMessage(f'Loading: {round(i/self.keyFrames[-1]*100)}%')
            self.app.processEvents()
        # vectorDiagramData={i:function(convertTo3D(segment),self.masterData[i]['simplified'],self.masterData[i]['actionRaw'],'vecPlot',20) for i in self.keyFrames}
        
        self.animationPen=QtGui.QPen(QtGui.QColor(*diagramColors[self.vectorDiagramOptions.currentText()]),1.5)
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
        self.keyFrameNo=0

    except Exception as e:
        import traceback
        traceback.print_exc()
        self.statusbar.showMessage("Select segments for vector diagrams",2000)    
        self.animationVectorDiagram.setChecked(False)

    # function=self.vectorDiagramOptionsDict[self.vectorDiagramOptions.currentText()]
    # if self.vectorDiagramOptions.currentText() in ['Bending Moment','Resultant Force']:
    #     vectorDiagramData={i:function(convertTo3D(segment),self.masterData[i]['simplified'],self.masterData[i]['actionRaw'],'vecPlot',200) for i in self.keyFrames}
    # elif self.vectorDiagramOptions.currentText()=='Shear Force':
    #     vectorDiagramData={i:function(convertTo3D(segment),self.masterData[i]['simplified'],self.masterData[i]['actionRaw'],'y','vecPlot') for i in self.keyFrames}
    # else:
    #     vectorDiagramData={i:function(convertTo3D(segment),self.masterData[i]['simplified'],self.masterData[i]['actionRaw'],'x','vecPlot') for i in self.keyFrames}

    # fillAnimationFrames(vectorDiagramData,'spline')
    # self.animationPlotData=vectorDiagramData
    # self.keyFrameNo=0

def calculateTimeGraphData(self):
    if self.animationTimeGraph.isChecked(): 
        pass 
    else: 
        return
    self.animationVectorDiagram.setChecked(False)
    self.animationSimulateMotion.setChecked(False)
    self.animationPlay.setChecked(False)
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
    
    timegraphdata=timeGraphData(segmentID,segment,self.keyFrameData[-1]['data'])
    import pyqtgraph as pg
    from numpy import array
    
    dialog=QtWidgets.QDialog(parent=self.MainWindow)
    dialog.setWindowTitle('Time Graph')
    dialog.resize(600,500)
    win = pg.GraphicsWindow(parent=dialog)
    win.setBackground(self.bgColor)

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
        pen = pg.mkPen(color=self.sfdColor,width = 1)
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
    self.animationVectorDiagram.setChecked(False)
    self.animationTimeGraph.setChecked(False)
    self.animationPlay.setChecked(False)
    self.animationPlay.setDisabled(True)

    from sdPy.simulationMethods import simulateFrameMotion2D,simulateTrussMotion2

    simulationFrameMotionData={}
    finalKeyFrameStructures=self.finalKeyFrameStructures
    masterData=self.masterData
    shear=self.shearMode
    inextensible=self.inextensibleMode
    keyFrames=self.keyFrames
    function=simulateTrussMotion2 if self.trussMode else simulateFrameMotion2D

    for i in keyFrames:
        simulationFrameMotionData[i]=function(finalKeyFrameStructures[i],masterData[i],shear,inextensible,self.NoOfPointsInMotion,self.ZoomFactorMotion)
        self.statusbar.showMessage(f'Loading: {round(i/keyFrames[-1]*100)}%')
        self.app.processEvents()

    # from sdPy.simulationMethods import vectorDiagramData2D
    # from sdPy.segmentMethods import responseData
    # from numpy import repeat,NAN,vstack
    # individualData = lambda seg : vstack((vectorDiagramData2D(seg,responseData(seg,self.masterData[i],self.shearMode,self.inextensibleMode,20,True,10)[:,:4],'l')['vecPlot'][1:-1],repeat(NAN,2)))
    # for i in self.keyFrames:
    #     toReturn=[]
    #     for segment in self.finalKeyFrameStructures[i]['segments']:
    #         toReturn = individualData(segment)
    #         self.app.processEvents()
    #     simulationFrameMotionData[i] = vstack(toReturn)
    #     self.statusbar.showMessage(f'Loading: {round(i/self.keyFrames[-1]*100)}%')
    #     self.app.processEvents()

    if self.animationModeOptions.currentIndex()==0:
        fillAnimationFrames(simulationFrameMotionData,'spline')
    
    self.animationPlotData=simulationFrameMotionData
    self.animationPen=QtGui.QPen(QtGui.QColor(*self.segmentColor),1.5)
    self.animationPlay.setDisabled(False)

    self.statusbar.showMessage('Press play button to start animation',2000)

    self.keyFrameNo=0






# import concurrent.futures
# def jpt(i):
#     ..................
# executor = concurrent.futures.ThreadPoolExecutor(10)
# futures = [executor.submit(jpt, item) for item in self.keyFrames]
# concurrent.futures.wait(futures)