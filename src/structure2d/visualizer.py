from numpy.linalg.linalg import norm
from sdPy.simulationMethods import fillAnimationFrames, getRescaledData, makeFunData
from sdPy.loadMethods import loadPlotData2
from sdPy.functionDefinitions import convertTo2D,convertTo3D
from sdPy.simulationMethods import vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp
from numpy import vstack, nan

from sdPy.simulationMethods import (vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp,
                vectorDiagramDataAngles2Dcomp,vectorDiagramDataDisps2Dcomp)
from sdPy.simulationMethods import vectorDiagramDataTrussDisps2Dcomp,vectorDiagramDataTrussForces2Dcomp
from PySide2 import QtWidgets,QtCore
from PySide2.QtGui import QPen,QColor,QFont
from PySide2.QtCore import QPointF
from sdPy.segmentMethods import segPlotData2
from numpy import array,nanargmin
import pyqtgraph as pg
def generateDiagramData(self,function,parameters):
    segments=list(self.df[self.df['Class']=='segment']['Robject'])
    for segment in segments:
        data= function(convertTo3D(segment),self.matrix,*parameters) 
        data=vstack((data,[nan,nan,nan,nan]))
        self.ui.app.processEvents()
    return data

def segmentsData(self):
    tempdf=self.ui.df
    #plot segments
    self.pen=QPen(QColor(*self.ui.segmentColor),self.ui.segmentWidth-1)    
    aa=tempdf[(tempdf['Class']=='segment')&(tempdf['Flag']==True)]    
    alldata=[]
    for element in range(len(aa)):
        Rsegment=aa.iloc[element,2]
        name=aa.iloc[element,0]
        data=segPlotData2(Rsegment['type'],Rsegment['P1'],Rsegment['P3'],self.ui.scale,Rsegment['P2'],no=self.ui.NoOfPointsInCurvedSegments)
        alldata.append(data)
    return alldata   

def visualize(self):
    data=self.animationPlotData[self.keyFrameNo][:,1:-1]
    data=makeFunData(data)
    function=self.vectorDiagramOptions.currentText()

    dialog=QtWidgets.QDialog(parent=self.MainWindow)
    name=function+' @ '+ str(self.keyFrameNo)
    dialog.setWindowTitle(name)
    dialog.resize(600,500)
    win = pg.GraphicsWindow(parent=dialog)
    win.setBackground(self.ui.bgColor)

    gridLayout=QtWidgets.QGridLayout()
    dialog.setLayout(gridLayout)
    gridLayout.addWidget(win,0,0,1,1)   
    p1 = win.addPlot(row=1, col=0)

    pen = pg.mkPen(color=self.ui.segmentColor,width = 1.5)
    segdata=segmentsData(self)
    for i in segdata:
        graph = pg.PlotDataItem(array(i),pen=pen,antialias=True,name=name)                
        p1.addItem(graph)        

    pen = pg.mkPen(color=self.diagramColors[function],width = 2)
    for i in data:
        graph = pg.PlotDataItem(array(i),pen=pen,antialias=True,name=name)                
        p1.addItem(graph)

    vb1=p1.vb
    vLine1 = pg.InfiniteLine(angle=90, movable=False)
    hLine1 = pg.InfiniteLine(angle=0, movable=False)
    textColor=self.diagramColors[function]
    fillBrush = pg.mkBrush(color=self.ui.bgColor)
    borderPen = pg.mkPen(color=self.diagramColors[function],width = 0.5)

    cText= pg.TextItem('0,0',textColor,anchor=(0.5,1),fill=fillBrush,border=borderPen)
    p1.addItem(vLine1, ignoreBounds=True)
    p1.addItem(hLine1, ignoreBounds=True)
    p1.addItem(cText)
   


    def mouseMovedactionGraphs(evt):
        pos = evt[0]
        if p1.sceneBoundingRect().contains(pos):
            mousePoint = vb1.mapSceneToView(pos)
            # index = int(mousePoint.x())   index = int(mousePoint.x())
            
            # if index > 0 and index < array(R.r.range(robj))[0]:
            x,y=mousePoint.x(), mousePoint.y()
            pos = array([x,y])
            cMatrix=self.animationPlotData[self.keyFrameNo]
            check = norm(pos-cMatrix[:,1:-1],axis=1)            
            p,x,y,mag=cMatrix[nanargmin(check)]
            # x,y=p,mag
            # p1.setLabel(axis='top', text="<span style='font-size: 12pt'>x=%0.3f <span style='color: red'>y=%0.3f</span>" % (x,y))
            tText=str(round(mag/self.zoomFactor,self.ui.precison))+'@'+str(round(p,self.ui.precison))
            cText.setText(tText,textColor)
            cText.setPos(x,y)
            vLine1.setPos(mousePoint.x())
            hLine1.setPos(mousePoint.y())
    dialog.proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=10, slot=mouseMovedactionGraphs)



    # segmentName=self.df[(self.df['Robject']==segment)].iloc[0]['Name']
    
    self.dockVisualize =QtWidgets.QDockWidget(name,self.MainWindow)
    self.dockVisualize.setWidget(dialog)
    try:
        self.dockGraphicsView
    except:
        self.dockGraphicsView=QtWidgets.QDockWidget('Main Graph',self.MainWindow)
        self.dockGraphicsView.setWidget(self.centralwidget)
        self.dockGraphicsView.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)            
        self.MainWindow.addDockWidget(QtCore.Qt.TopDockWidgetArea,self.dockGraphicsView)

    self.MainWindow.addDockWidget(QtCore.Qt.TopDockWidgetArea,self.dockVisualize)
    self.MainWindow.tabifyDockWidget(self.dockGraphicsView,self.dockVisualize)

    self.MainWindow.setTabPosition(QtCore.Qt.TopDockWidgetArea, 
                                    QtWidgets.QTabWidget.North)    