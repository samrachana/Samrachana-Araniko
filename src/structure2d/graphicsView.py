from PySide2 import QtWidgets
from PySide2.QtWidgets import QGraphicsView
from PySide2.QtCore import Qt
from PySide2.QtGui import QTransform
from structure2d.fileOperations2d import openFile
from structure2d.analysis2d import analysisModes
from structure2d.simulate2d import simulationEnvironment
        
class GraphicsView(QGraphicsView):
    def __init__(self,scene,parent=None,ui=None):

        super().__init__(scene,parent)
        self._pan=False
        self.ui=ui
        self.setAcceptDrops(True)
        
 

    def dragLeaveEvent(self, event):
        for url in event.mimeData().urls():
            self.path = url.toLocalFile()
        openFile(self.ui,self.path)
        event.accept()
        


    # def contextMenuEvent(self, event):
    #     menu = QtWidgets.QMenu()

    #     menu.addAction('Analyse',lambda:analysisModes(self.ui))
    #     menu.addAction('Simulate',lambda:simulationEnvironment(self.ui,self.ui.MainWindow))
    #     menu.addAction('Fit to Screen',self.fitToScreen)
    #     menu.addAction('FullScreen',self.ui.clearScreen)
    #     menu.exec_(event.globalPos())

    #     item = self.itemAt(event.globalPos())
    #     self.mapToScene(event.globalPos())
    #     print(event.globalPos(),event.pos())
    #     print(item)
    #     event.accept()

    def wheelEvent(self, event):
        # Zoom Factor


        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.delta() > 0:
            self.ui.zoomOut()
        else:
            self.ui.zoomIn()
        # self.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())

    # def dragPressEvent(self,event):
    #     if (event.buttons() & Qt.RightButton):
        
    #         self._pan = True
    #         self._panStartX = event.x()
    #         self._panStartY = event.y()
    #         self.setCursor(Qt.ClosedHandCursor)
    #         event.accept()
    #         return
        
    #     event.ignore()

    # # def mouseReleaseEvent(self,event):
    # #     if (event.button()& Qt.RightButton):
        
    # #         self._pan = False
    # #         self.setCursor(Qt.ArrowCursor)
    # #         event.accept()
    # #         return
    # #     QGraphicsView.mouseReleaseEvent(self,event)
    # #     event.ignore()


    # def dragMoveEvent(self,event):
    #     if (self._pan):        
    #         self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (event.x() - self._panStartX))
    #         self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (event.y() - self._panStartY))
    #         self._panStartX = event.x()
    #         self._panStartY = event.y()
    #         event.accept()
    #         return
        
    #     event.ignore()

        # fullScreen=QtWidgets.QAction('Full Screen')
        # fullScreen.setCheckable(True)
        # def fullScs():
        #     if fullScreen.isChecked():
        #         self.ui.clearScreen()
        #         self.fullScreenChecked=True
        #     else:
        #         self.ui.dockObjectTree.close()
        #         self.ui.propertiesBar.close()
        #         try:
        #             self.ui.dockAnalysisTable.close()
        #         except:
        #             pass                   
        # fullScreen.triggered.connect(fullScs)