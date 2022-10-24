from PySide2 import QtWidgets,QtGui,QtCore
import pyqtgraph as pg
from UI.newdiagramsWindow import Ui_MainWindow as Diagrams
from numpy import array
# from rbindings import R


def showDiagrams(name,mainApp,MainWindow,str2d=False):  
    try:
        mainApp.nd.statusbar.showMessage(f'Analysis the member : {name} complete',2000)
    except :
        mainApp.statusbar.showMessage(f'Analysis the member : {name} complete',2000)
    dW=QtWidgets.QMainWindow(parent=MainWindow)
    diagramWindow=Diagrams()
    diagramWindow.setupUi(dW)
    dW.setWindowTitle(f'{name} : Diagrams')
    # if mainApp.currentDiagram:     
    #     diagramWindow.comboBox.setCurrentText(mainApp.currentDiagram)
    # mainApp.currentDiagram=name    
    lists=list(mainApp.df[(mainApp.df['Flag']==True)&(mainApp.df['Class']=='segment')]['Name'])

    diagramWindow.comboBox.addItems(list(reversed(lists)))
    diagramWindow.comboBox.setCurrentText(name)
    diagramWindow.comboBox.setItemDelegate(QtWidgets.QStyledItemDelegate())
    diagramWindow.comboBox.currentIndexChanged.connect(lambda:mainApp.diagrams(diagramWindow.comboBox.currentText()))
    diagramWindow.comboBox.setCurrentText(name)
    actions=['shearForce','axialForce','bendingMoment']
    responses=['displacementX','displacementY','Slope']
    win = pg.GraphicsWindow(parent=dW)
    win.setBackground(mainApp.bgColor)
    diagramWindow.gridLayout.addWidget(win, 1, 0, 1, 2)
    p1 = win.addPlot(row=1, col=0)
    def changestate(index,action):
        if action.isChecked()==False:
            p1.items[index+1].hide()
        else:
            p1.items[index+1].show()    
    def changestateResponse(index,action):
        if action.isChecked()==False:
            p2.items[index+1].hide()
        else:
            p2.items[index+1].show()                                    

    def actionsMenu():
        diagramWindow.toolmenu1 = QtWidgets.QMenu()

        action1 = diagramWindow.toolmenu1.addAction(actions[0])
        action1.setCheckable(True)
        action1.setChecked(True)
        action1.triggered.connect(lambda: changestate(1,action1)) 

        action2 = diagramWindow.toolmenu1.addAction(actions[1])
        action2.setCheckable(True)
        action2.setChecked(True)
        action2.triggered.connect(lambda: changestate(2,action2))

        action3 = diagramWindow.toolmenu1.addAction(actions[2])
        action3.setCheckable(True)
        action3.setChecked(True)
        action3.triggered.connect(lambda: changestate(3,action3))

       

        diagramWindow.actionDiagramsMenu.setMenu(diagramWindow.toolmenu1)
        diagramWindow.actionDiagramsMenu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    actionsMenu()

    def responsesMenu():
        diagramWindow.toolmenu = QtWidgets.QMenu()

        response1 = diagramWindow.toolmenu.addAction(responses[0])
        response1.setCheckable(True)
        response1.setChecked(True)
        response1.triggered.connect(lambda: changestateResponse(1,response1)) 

        response2 = diagramWindow.toolmenu.addAction(responses[1])
        response2.setCheckable(True)
        response2.setChecked(True)
        response2.triggered.connect(lambda: changestateResponse(2,response2))

        response3 = diagramWindow.toolmenu.addAction(responses[2])
        response3.setCheckable(True)
        response3.setChecked(True)
        response3.triggered.connect(lambda: changestateResponse(3,response3))

        diagramWindow.responseDiagramsMenu.setMenu(diagramWindow.toolmenu)
        diagramWindow.responseDiagramsMenu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    responsesMenu()

    def actionGraph():    

        vLine1 = pg.InfiniteLine(angle=90, movable=False)
        hLine1 = pg.InfiniteLine(angle=0, movable=False)
        p1.addItem(vLine1, ignoreBounds=True)
        p1.addItem(hLine1, ignoreBounds=True)
        p1.addLegend(offset=(0,0))       
        # allData=R.sc.actionData(robj,structure,matrix)
        allData=mainApp.actionData
        def shearForceY():                    
            shear = allData[:,[0,2]]
            pen = pg.mkPen(color=mainApp.sfdColor,width = 1.5)
            shearForceY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='ShearForce')                
            p1.addItem(shearForceY)
            # actionslegend.addItem(shearForceY,'shearForceY')


        def axialForce():                    
            shear = allData[:,[0,1]]
            pen = pg.mkPen(color=mainApp.afdColor,width = 1.5)
            axialForce = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='axialForce')                
            p1.addItem(axialForce)
            # actionslegend.addItem(axialForce,'axialForce')


        def bendingMomentZ():                    
            shear = allData[:,[0,6]]
            pen = pg.mkPen(color=mainApp.bmdColor,width = 1.5)
            bendingMomentZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='bendingMoment')                
            p1.addItem(bendingMomentZ)
            # actionslegend.addItem(bendingMomentZ,'bendingMomentZ')
        shearForceY()
        axialForce()
        bendingMomentZ()


        vb1=p1.vb
        def mouseMovedactionGraphs(evt):
            pos = evt[0]
            if p1.sceneBoundingRect().contains(pos):
                mousePoint = vb1.mapSceneToView(pos)
                # index = int(mousePoint.x())   index = int(mousePoint.x())
                
                # if index > 0 and index < array(R.r.range(robj))[0]:
                p1.setLabel(axis='top', text="<span style='font-size: 12pt'>x=%0.3f <span style='color: red'>y=%0.3f</span>" % (mousePoint.x(), mousePoint.y()))
                vLine1.setPos(mousePoint.x())
                hLine1.setPos(mousePoint.y())
        diagramWindow.proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=10, slot=mouseMovedactionGraphs)
    actionGraph()


    win = pg.GraphicsWindow(parent=dW)
    win.setBackground(mainApp.bgColor)

    diagramWindow.gridLayout_3.addWidget(win, 3, 0, 1, 2)
    p2 = win.addPlot(row=1, col=0)    
    def responseGraph():
        # p2.a=False
        vLine = pg.InfiniteLine(angle=90, movable=False)
        hLine = pg.InfiniteLine(angle=0, movable=False)
        p2.addItem(vLine, ignoreBounds=True)
        p2.addItem(hLine, ignoreBounds=True)

        p2.addLegend(offset=(0,0))
        allData=mainApp.responseData
        def displacementX():                    
            shear = allData[:,[0,2]]
            pen = pg.mkPen(color=mainApp.sfdColor,width = 1.5)
            displacementY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='displacementY')                
            p2.addItem(displacementY)

        def displacementY():                    
            shear = allData[:,[0,1]]
            pen = pg.mkPen(color=(100,100,100),width = 1.5)
            displacementZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='displacementX')                
            p2.addItem(displacementZ)

        def bendAngleZ():                    
            shear = allData[:,[0,6]]
            pen = pg.mkPen(color=mainApp.bmdColor,width = 1.5)
            bendAngleZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='Slope')                
            p2.addItem(bendAngleZ)
        displacementY()
        displacementX()
        bendAngleZ()


        vb=p2.vb
        def mouseMovedresponseGraph(evt):
            pos = evt[0]
            if p2.sceneBoundingRect().contains(pos):
                mousePoint = vb.mapSceneToView(pos)
                p2.setLabel(axis='top',text="<span style='font-size: 12pt'>x=%.10f <span style='color: red'>y=%.10f</span>" % (mousePoint.x(), mousePoint.y()))
                vLine.setPos(mousePoint.x())
                hLine.setPos(mousePoint.y())  


        diagramWindow.proxy1 = pg.SignalProxy(p2.scene().sigMouseMoved, rateLimit=10, slot=mouseMovedresponseGraph)
    responseGraph()    
    # dW.show()
    # mainApp.dW=dW    
    if not mainApp.previousDiagram:
        mainApp.dockDiagrams=QtWidgets.QDockWidget(name,MainWindow)
        mainApp.dockDiagrams.setWidget(dW)
        
        mainApp.dockGraphicsView=QtWidgets.QDockWidget('Main Graph',MainWindow)
        mainApp.dockGraphicsView.setWidget(mainApp.centralwidget)
        mainApp.dockGraphicsView.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        MainWindow.addDockWidget(QtCore.Qt.TopDockWidgetArea,mainApp.dockGraphicsView)
        MainWindow.addDockWidget(QtCore.Qt.TopDockWidgetArea,mainApp.dockDiagrams)

        MainWindow.tabifyDockWidget(mainApp.dockGraphicsView,mainApp.dockDiagrams)

        MainWindow.setTabPosition(QtCore.Qt.TopDockWidgetArea, 
                                    QtWidgets.QTabWidget.North)

    else:
        mainApp.dockDiagrams=QtWidgets.QDockWidget(name,MainWindow)
        mainApp.dockDiagrams.setWidget(dW)
        MainWindow.tabifyDockWidget(mainApp.previousDiagram,mainApp.dockDiagrams)

    mainApp.previousDiagram=mainApp.dockDiagrams