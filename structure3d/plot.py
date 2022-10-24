import pyqtgraph.opengl as gl
from pyqtgraph import QtGui,QtCore
from numpy import array
from OpenGL.GL import *
import numpy as np

class CustomTextItem(gl.GLGraphicsItem.GLGraphicsItem):
    def __init__(self, X, Y, Z,GLViewWidget, text):
        gl.GLGraphicsItem.GLGraphicsItem.__init__(self)
        self.text = text
        self.X = X
        self.Y = Y
        self.Z = Z
        self.GLViewWidget = GLViewWidget

    def setText(self, text):
        self.text = text
        self.update()

    def setX(self, X):
        self.X = X
        self.update()

    def setY(self, Y):
        self.Y = Y
        self.update()

    def setZ(self, Z):
        self.Z = Z
        self.update()

    def paint(self):
        self.GLViewWidget.qglColor(QtCore.Qt.red)
        self.GLViewWidget.renderText(self.X, self.Y, self.Z, self.text)
class Axis(gl.GLAxisItem):
    def __init__(self, size=None, antialias=True, glOptions='translucent'):
        gl.GLAxisItem.__init__(self,size,antialias,glOptions)
    def paint(self):
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        #glEnable( GL_BLEND )
        #glEnable( GL_ALPHA_TEST )
        self.setupGLState()
        
        if self.antialias:
            glEnable(GL_LINE_SMOOTH)
            glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
            
        glLineWidth(2.5)
        glBegin( GL_LINES )
        
        x,y,z = self.size()
        
        glColor4f(0, 0.45, 0, 1)  # z is green
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, z)

        glColor4f(0.6, 0, 0, .6)  # y is red
        glVertex3f(0, 0, 0)
        glVertex3f(0, y, 0)

        glColor4f(0, 0, 0.6, .6)  # x is blue
        glVertex3f(0, 0, 0)
        glVertex3f(x, 0, 0)
        glEnd()

class Grid(gl.GLGridItem):

    def __init__(self, size=None, color=(255, 255, 255, 76.5), antialias=True, glOptions='translucent'):
        gl.GLGridItem.__init__(self,size,color,antialias,glOptions)
    def paint(self):
        self.setupGLState()
        
        if self.antialias:
            glEnable(GL_LINE_SMOOTH)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
            
        glBegin( GL_LINES )
        
        x,y,z = self.size()
        xs,ys,zs = self.spacing()
        xvals = np.arange(-x/2., x/2. + xs*0.001, xs) 
        yvals = np.arange(-y/2., y/2. + ys*0.001, ys) 
        glColor4f(0.2, 0.2, 0, .3)
        for x in xvals:
            glVertex3f(x, yvals[0], 0)
            glVertex3f(x,  yvals[-1], 0)
        for y in yvals:
            glVertex3f(xvals[0], y, 0)
            glVertex3f(xvals[-1], y, 0)
        
        glEnd()


class Plot():
    def __init__(self,GraphWidget):
        self.axis(GraphWidget)
        self.grid(GraphWidget)
    
    def axis(self,GraphWidget):
         axes=Axis(size=QtGui.QVector3D(105,105,105),antialias=True,glOptions='opaque')
         GraphWidget.addItem(axes)

    def grid(self,GraphWidget):      
            
        xgrid = Grid(glOptions='translucent',size=QtGui.QVector3D(100,100,1),antialias=True)
        ygrid = Grid(glOptions='translucent',size=QtGui.QVector3D(100,100,1),antialias=True)
        zgrid = Grid(glOptions='translucent',size=QtGui.QVector3D(100,100,1),antialias=True)
       
        ## rotate x and y grids to face the correct direction
        xgrid.rotate(90, 0, 1, 0)
        ygrid.rotate(90, 1, 0, 0)
        zgrid.translate(50,50,0)        
        ygrid.translate(50,0,50)
        xgrid.translate(0,50,50)
      
        GraphWidget.addItem(xgrid)
        GraphWidget.addItem(ygrid)
        GraphWidget.addItem(zgrid)
    #     scale=1
    #     for i in range(0,100,scale):
    #         origin=CustomTextItem(-0.1,-0.1,i,GraphWidget,str(i)) 
    #         GraphWidget.addItem(origin)
    #     for i in range(1,100,scale):
    #         origin=CustomTextItem(-0.1,i,-0.1,GraphWidget,str(i))    
    #         GraphWidget.addItem(origin)
    #     for i in range(1,100,scale):
    #         origin=CustomTextItem(i,-0.1,-0.1,GraphWidget,str(i))
    #         GraphWidget.addItem(origin)
    def plotsupport(self,pts,GraphWidget,color):
        pts=pts
        pp = gl.GLLinePlotItem(pos=pts,width=3.5,color=color,antialias=True)
        GraphWidget.addItem(pp)

    def plott(self,lists,GraphWidget,color,width):     
        color=array(color)/255
        pp = gl.GLLinePlotItem(pos=lists,width=width,color=tuple(color),antialias=True)
        GraphWidget.addItem(pp)
        
 