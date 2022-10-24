from PySide2 import QtWidgets,QtGui
import pyqtgraph as pg
from UI.newdiagramsWindow import Ui_MainWindow as Diagrams
from numpy import array
# from rbindings import R


def showDiagrams(name,mainApp,MainWindow):  
    try:
        mainApp.nd.statusbar.showMessage(f'Analysis the member : {name} complete',2000)
    except :
        mainApp.statusbar.showMessage(f'Analysis the member : {name} complete',2000)
    
    # if mainApp.currentDiagram:     
    #     mainApp.prevDiagram.comboBox.setCurrentText(mainApp.currentDiagram)
    dW=QtWidgets.QMainWindow(parent=MainWindow)
    diagramWindow=Diagrams()
    diagramWindow.setupUi(dW)
    dW.setWindowTitle(f'{name} : Diagrams')
    mainApp.prevDiagram=diagramWindow    

    # mainApp.currentDiagram=name    
    lists=list(mainApp.df[(mainApp.df['Flag']==True)&(mainApp.df['Class']=='segment')]['Name'])

    diagramWindow.comboBox.addItems(list(reversed(lists)))
    diagramWindow.comboBox.setCurrentText(name)
    diagramWindow.comboBox.setItemDelegate(QtWidgets.QStyledItemDelegate())
    diagramWindow.comboBox.currentIndexChanged.connect(lambda:mainApp.diagrams(diagramWindow.comboBox.currentText()))
    diagramWindow.comboBox.setCurrentText(name)
    actions=['shearForceY','shearForceZ','axialForce','twistMoment','bendingMomentY','bendingMomentZ']
    responses=['displacementY','displacementZ','axialDisplacement','twistAngle','bendAngleY','bendAngleZ']
    win = pg.GraphicsWindow(parent=dW)
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
        diagramWindow.toolmenu = QtWidgets.QMenu()

        action1 = diagramWindow.toolmenu.addAction(actions[0])
        action1.setCheckable(True)
        action1.setChecked(True)
        action1.triggered.connect(lambda: changestate(1,action1)) 

        action2 = diagramWindow.toolmenu.addAction(actions[1])
        action2.setCheckable(True)
        action2.setChecked(True)
        action2.triggered.connect(lambda: changestate(2,action2))

        action3 = diagramWindow.toolmenu.addAction(actions[2])
        action3.setCheckable(True)
        action3.setChecked(True)
        action3.triggered.connect(lambda: changestate(3,action3))

        action4 = diagramWindow.toolmenu.addAction(actions[3])
        action4.setCheckable(True)
        action4.setChecked(True)
        action4.triggered.connect(lambda: changestate(4,action4))

        action5 = diagramWindow.toolmenu.addAction(actions[4])
        action5.setCheckable(True)
        action5.setChecked(True)
        action5.triggered.connect(lambda: changestate(5,action5))

        action6 = diagramWindow.toolmenu.addAction(actions[5])
        action6.setCheckable(True)
        action6.setChecked(True)
        action6.triggered.connect(lambda: changestate(6,action6))

        diagramWindow.actionDiagramsMenu.setMenu(diagramWindow.toolmenu)
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

        response4 = diagramWindow.toolmenu.addAction(responses[3])
        response4.setCheckable(True)
        response4.setChecked(True)
        response4.triggered.connect(lambda: changestateResponse(4,response4))

        response5 = diagramWindow.toolmenu.addAction(responses[4])
        response5.setCheckable(True)
        response5.setChecked(True)
        response5.triggered.connect(lambda: changestateResponse(5,response5))

        response6 = diagramWindow.toolmenu.addAction(responses[5])
        response6.setCheckable(True)
        response6.setChecked(True)
        response6.triggered.connect(lambda: changestateResponse(6,response6))

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
            shearForceY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='ShearForceY')                
            p1.addItem(shearForceY)
            # actionslegend.addItem(shearForceY,'shearForceY')

        def shearForceZ():                    
            shear = allData[:,[0,3]]
            pen = pg.mkPen(color=(100,100,100),width = 1.5)
            shearForceZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='shearForceZ')                
            p1.addItem(shearForceZ)
            # actionslegend.addItem(shearForceZ,'shearForceZ')
        def axialForce():                    
            shear = allData[:,[0,1]]
            pen = pg.mkPen(color=mainApp.afdColor,width = 1.5)
            axialForce = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='axialForce')                
            p1.addItem(axialForce)
            # actionslegend.addItem(axialForce,'axialForce')
        def twistMoment():                    
            shear = allData[:,[0,4]]
            pen = pg.mkPen(color=(0, 200, 100),width = 1.5)
            twistMoment = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='twistMoment')                
            p1.addItem(twistMoment)
            # actionslegend.addItem(twistMoment,'twistMoment')
        def bendingMomentY():                    
            shear = allData[:,[0,5]]
            pen = pg.mkPen(color=(250, 200, 100),width = 1.5)
            bendingMomentY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='bendingMomentY')                
            p1.addItem(bendingMomentY)
            # actionslegend.addItem(bendingMomentY,'bendingMomentY')
        def bendingMomentZ():                    
            shear = allData[:,[0,6]]
            pen = pg.mkPen(color=mainApp.bmdColor,width = 1.5)
            bendingMomentZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='bendingMomentZ')                
            p1.addItem(bendingMomentZ)
            # actionslegend.addItem(bendingMomentZ,'bendingMomentZ')
        shearForceY()
        shearForceZ()
        axialForce()

        twistMoment()
        bendingMomentY()
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
        def displacementY():                    
            shear = allData[:,[0,2]]
            pen = pg.mkPen(color=mainApp.sfdColor,width = 1.5)
            displacementY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='displacementY')                
            p2.addItem(displacementY)
        def displacementZ():                    
            shear = allData[:,[0,3]]
            pen = pg.mkPen(color=(100,100,100),width = 1.5)
            displacementZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='displacementZ')                
            p2.addItem(displacementZ)
        def axialDisplacement():                    
            shear = allData[:,[0,1]]
            pen = pg.mkPen(color=mainApp.afdColor,width = 1.5)
            axialDisplacement = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='axialDisplacement')                
            p2.addItem(axialDisplacement)
        def twistAngle():                    
            shear = allData[:,[0,4]]
            pen = pg.mkPen(color=(0, 200, 100),width = 1.5)
            twistAngle = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='twistAngle')                
            p2.addItem(twistAngle)
        def bendAngleY():                    
            shear = allData[:,[0,5]]
            pen = pg.mkPen(color=(250, 200, 100),width = 1.5)
            bendAngleY = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='bendAngleY')                
            p2.addItem(bendAngleY)
        def bendAngleZ():                    
            shear = allData[:,[0,6]]
            pen = pg.mkPen(color=mainApp.bmdColor,width = 1.5)
            bendAngleZ = pg.PlotDataItem(array(shear),pen=pen,antialias=True,name='bendAngleZ')                
            p2.addItem(bendAngleZ)
        displacementY()
        displacementZ()
        axialDisplacement()

        twistAngle()
        bendAngleY()
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
    dW.show()
        
