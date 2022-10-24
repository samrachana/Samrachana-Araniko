from OpenGL.GL import *
from PySide2 import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import numpy as np
class GraphWidget(gl.GLViewWidget):
    def __init__(self):
        gl.GLViewWidget.__init__(self)
    def mousePressEvent(self, ev):
        self.mousePos = ev.pos()
        print('pos ',ev.pos())
        print('projection mat ',self.projectionMatrix())
        print('model view ',self.viewMatrix())
        print(self.projectionMatrix()*self.viewMatrix())
        print(self.projectionMatrix())
    def mouseMoveEvent(self, ev):
        
        try:       
            diff = ev.pos() -self.mousePos
        except:
            pass    
        self.mousePos = ev.pos()
        if ev.buttons() == QtCore.Qt.LeftButton:
            
            self.orbit(-diff.x(), diff.y())
            #print self.opts['azimuth'], self.opts['elevation']
        elif ev.buttons() == QtCore.Qt.MidButton:
            if (ev.modifiers() & QtCore.Qt.ControlModifier):
                self.pan(diff.x(), 0, diff.y(), relative=True)
            else:
                self.pan(diff.x(), diff.y(), 0, relative=True)
        elif ev.buttons() == QtCore.Qt.RightButton:
            self.orbit(-diff.x(),0)        
    def mouseReleaseEvent(self, ev):
        pass
            # Example item selection code:
            # region = (ev.pos().x()-5, ev.pos().y()-5, 50, 50)
            # print(self.itemsAt(region))
            
            # # debugging code: draw the picking region
            # glViewport(*self.getViewport())
            # glClear( GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT )
            # region = (region[0], self.height()-(region[1]+region[3]), region[2], region[3])
            # self.paintGL(region=region)
            # self.swapBuffers()
    def setCameraPosition(self, pos=None, distance=None, elevation=None, azimuth=None):
        import numpy as np
        if distance is not None:
            self.opts['distance'] = distance
        if elevation is not None:
            self.opts['elevation'] = elevation
        if azimuth is not None:
            self.opts['azimuth'] = azimuth
        if pos is not None:
            dis=np.linalg.norm(pos)
            elv=np.arcsin(pos[2]/dis)
            self.opts['elevation'] = elv*180/np.pi
            self.opts['azimuth'] = -np.arccos(pos[0]/(dis*np.cos(elv)))*180/np.pi
            self.opts['distance'] = dis
        self.update()   
    def pan(self, dx, dy, dz, relative=False):


        if not relative:
            self.opts['center'] = QtGui.QVector3D(dx, dy, dz)
        else:
            cPos = self.cameraPosition()
            cVec = self.opts['center'] - cPos
            dist = cVec.length()  ## distance from camera to center
            xDist = dist * 2. * np.tan(0.5 * self.opts['fov'] * np.pi / 180.)  ## approx. width of view at distance of center point
            xScale = xDist / self.width()
            zVec = QtGui.QVector3D(0,0,1)
            xVec = QtGui.QVector3D.crossProduct(zVec, cVec).normalized()
            yVec = QtGui.QVector3D.crossProduct(xVec, zVec).normalized()
            self.opts['center'] = self.opts['center'] + xVec * xScale * dx + yVec * xScale * dy + zVec * xScale * dz
        self.update()