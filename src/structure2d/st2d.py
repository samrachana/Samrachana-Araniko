from . import *
from time import sleep
# sleep(5)
class Window2d(Ui_MainWindow):
    def __init__(self, MainWindow,app,directOpen=None):
        
        Ui_MainWindow.setupUi(self, MainWindow)
        
        self.app=app
        self.MainWindow = MainWindow


        self.objectProperties()
        self.variables()
        self.connectors()
        toolbars(self)
        self.dockObjectTree=QDockWidget('Object Tree',MainWindow)
        self.oT = QtWidgets.QDialog(parent=MainWindow)
        # self.MainWindow.showMaximized()
        self.createScene()

        # from structure2d.objectsTable import objectsTable
        # objectsTable(self)
        self.ot = ObjectTree()
        self.ot.setupUi(self.oT, MainWindow)
        self.dockObjectTree.setWidget(self.oT)
        objectTree(self, self.MainWindow)
        MainWindow.addDockWidget(QtCore.Qt.BottomDockWidgetArea,self.dockObjectTree)

        editPeakAndNormal(self)
        self.dockPeakNormal.close()
        self.threadpool = QtCore.QThreadPool()

        try:
            MainWindow.signals.finished.connect(lambda:saveFile(self))
        except:
            pass

        defaultTweaks(self)
        if directOpen:
            openFile(self,directOpen)
            head,tail=os.path.split(directOpen)
            self.MainWindow.setWindowTitle('Samrachana - '+tail)
        else:
            self.MainWindow.setWindowTitle('Samrachana - '+ 'Untitiled.str')    

        # from simulation.animationWindow import AnimationWindow
        # AnimationWindow(self)
        self.graphicsView.fitInView(0, 0, self.graphicsView.geometry(
            ).width(), self.graphicsView.geometry().height())
    def objectProperties(self):

        self.bgColor = (245,247,253, 255)
        self.segmentColor = (202, 1, 209, 255)
        self.loadColor = (200, 0, 50, 255)
        
        self.afdColor = (0, 0, 250, 255)
        self.sfdColor = (0, 250, 0, 255)
        self.bmdColor = (250, 0, 0, 255)
        self.translationColor = (0, 200, 0, 255)
        self.rotationColor = (0, 200, 0, 255)
        
        self.rollerColor = (100, 100, 200, 255)
        self.hingeColor = (0, 200, 200, 255)
        self.fixedColor = (120, 0, 120, 255)
        self.internalHingeColor = (100, 200, 100, 255)
        self.customSupportColor = (10, 200, 100, 255)

        self.segmentWidth = 3
        self.loadWidth = 2
        self.currentUnit = 'SI'
        self.force = 1
        self.length = 1
        self.temperature='C'
        self.precison = 3
        self.scale = 1
        self.totalGridLines=0
        self.smallGridLines=0
        self.cursorPath='./ico/cursors/light/'
        self.fileName=None
        self.setunits = False
        self.darkMode=False
        self.previousDiagram=False


    def variables(self):
        self.snapPoints=[]
        self.structure=None
        self.previousSectionIndex=0
        self.previousMaterialIndex=0
        # self.previousDiagram=False
        self.calculatorMode=True
        self.zoomState=0
        self.cut=False
        self.clipboardItems=[]
        self.nodes=[]
        self.supportNumber = 1
        self.loadNumber = 1
        self.segmentNumber = 1
        # self.section = read_csv("./datafiles/sections.csv")
        # self.section.loc[len(self.section)]=[len(self.section),'Custom',1,1,1,1,1,1]
        try:            
            units = read_csv('./datafiles/units.csv')
            self.material = read_csv("./datafiles/material.csv")
            self.material.loc[len(self.material)]=[len(self.material),'Custom',1,1,0,1]
            self.section = read_csv("./datafiles/sections.csv")
            self.section.loc[len(self.section)]=[len(self.section),'Custom',1,1,1,1,1]
        except FileNotFoundError:
            writeFiles()
            units = read_csv('./datafiles/units.csv')
            self.material = read_csv("./datafiles/material.csv")
            self.section = read_csv("./datafiles/sections.csv")
        except:
            from sampleDatas import material,section,units
            self.material= DataFrame(material)
            self.section=DataFrame(section)
            self.units=DataFrame(units)
        
        self.SIscales = ['1:1.0', '1:10.0', '1:100.0', 'Custom']
        self.SIunitsOfForce = dict(units[(units['Quantity'] == 'Force') & (
            units['System'] == 'SI')][['Symbol', 'Conversion']].values.tolist())
        self.SIunitsOfLength = dict(units[(units['Quantity'] == 'Length') & (
            units['System'] == 'SI')][['Symbol', 'Conversion']].values.tolist())

        self.ENGscales = ['1:1.0', '1:6.0', '1:12.0', 'Custom']
        self.ENGunitsOfForce = dict(units[(units['Quantity'] == 'Force') & (
            units['System'] == 'ENG')][['Symbol', 'Conversion']].values.tolist())
        self.ENGunitsOfLength = dict(units[(units['Quantity'] == 'Length') & (
            units['System'] == 'ENG')][['Symbol', 'Conversion']].values.tolist())
        self.supportColors = {"Roller": self.rollerColor, 
                "Hinge": self.hingeColor, 
                "Fixed": self.fixedColor,
                "Internal Hinge":self.internalHingeColor,
                'custom Support':self.customSupportColor}
        customSupports=['000', '010', '100', '110', '001', '011', '101', '111', 'Node']
        tempdict = {x:self.customSupportColor for x in customSupports}
        self.supportColors.update(tempdict)
        self.historystatus = True
        self.historyposition = 1
        self.counter = 1
        self.history = array([], dtype="int8")
        self.df = DataFrame(
            columns=["Name", "Class", "Robject",
                     "Graphitem", "Treeitem", "Flag"],
            index=None,
        )
        self.currentDiagram = None
        self.segmentNumber = 1
        self.supportNumber = 1
        self.loadNumber = 1
        self.todraw = 'select'

        self.delete = False
        self.member = None
        self.loadtypes = {
            'Moment': -2,
            'Point Load': -1,
            'UDL': 0,
            'UVL': 1,
            'Poly Load': 2}
    def zoomOut(self):
        
        if self.zoomState>-10:
            self.graphicsView.scale(1/1.1,1/1.1)
            # self.graphicsView.shear(1/1.1,1/1.1)
            self.zoomState-=1
            if self.zoomState==10:
            #     self.smallgrid(True)
            # else:
                self.smallgrid(False) 
    def zoomIn(self):

        if self.zoomState<30:            
            self.graphicsView.scale(1.1,1.1)
            # self.graphicsView.shear(1.1,1.1)
            self.zoomState+=1
            if self.zoomState==10:
                self.smallgrid(True)
            # else:
            #     self.smallgrid(False)    

    def message(self,message):

        from UI.textWindow import Ui_Form as Message
        self.mB = QtWidgets.QDialog(self.MainWindow)
        self.mb = Message()
        self.mb.setupUi(self.mB)
        with open(resource_path('./resources/'+message+'.html')) as f:
            text=f.read()
        self.mb.textBrowser.setHtml(text)
        self.mB.setWindowTitle(message.capitalize())
        if message=='about':
            self.mB.resize(450,200)
        self.mB.show()

    def clearScreen(self):
        # self.toolBar.close()
        self.dockObjectTree.close()
        self.propertiesBar.close()
        try:
            self.dockAnalysisTable.close()
        except:
            pass    
    def connectors(self):
        self.actionClear_Screen.triggered.connect(self.clearScreen)
        self.actionGenerateReport.triggered.connect(lambda:generateReport(self))
        self.actionMeasure.triggered.connect(self.measure)
        self.actionTweaks.triggered.connect(lambda:tweaks(self))
        self.actionCalculator.triggered.connect(lambda:calculator(self))

        self.actionAbout.triggered.connect(lambda:self.message('about'))
        self.actionLicense.triggered.connect(lambda:self.message('license'))
        self.actionUpdate.triggered.connect(lambda:self.message('update'))
        self.actionManual.triggered.connect(lambda: os.system('start '+resource_path('./resources/tutorials/index.html')))
        
        self.actionGravityLoad.triggered.connect(lambda:gLoad(self))
        self.actionTemprLoad.triggered.connect(lambda:temprLoad(self))
        self.actionMisfitLoad.triggered.connect(lambda :misfitLoad(self))
        
        # from structure2d.objectsTable import editObjectsTable
        # self.actionObjects.triggered.connect(lambda:editObjectsTable(self))
        from structure2d.simulate2d import simulationEnvironment
        self.actionVisualize.triggered.connect(lambda:visualize(self))
        self.actionSimulate.triggered.connect(lambda:simulationEnvironment(self,self.MainWindow))
        self.actionzoomOut.triggered.connect(self.zoomOut)
        self.actionzoomIn.triggered.connect(self.zoomIn)

        self.actionColor_profile.triggered.connect(lambda:preferenceDialog(self,self.MainWindow))
        self.actionGrid.triggered.connect(self.gridLines)
        self.actionAxis.triggered.connect(self.axis)
        def close():
            self.MainWindow.close()
        self.actionClose.triggered.connect(close)

        self.actionDark_Mode.triggered.connect(lambda:darkMode(self,self.app))

        self.actionPrint.triggered.connect(lambda: printFile(self))
        self.actionNew.triggered.connect(lambda: newFile(self))
        self.actionSave_As.triggered.connect(lambda: saveAsFile(self))
        self.actionSave.triggered.connect(lambda: saveFile(self))
        self.actionOpen.triggered.connect(lambda: openFile(self))
        from sectionbuilder import sectionBuilder
        self.actionMOI_calculator.triggered.connect(lambda:sectionBuilder(self,self.MainWindow))
        self.actionUnits.triggered.connect(
            lambda: unitWindow(self, self.MainWindow))
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)

        self.actionAnalyse.triggered.connect(lambda:analysisModes(self))

        self.actionObject_Tree.setShortcut("o")
        self.actionObject_Tree.triggered.connect(
            lambda: toggleObjectTree(self))

        self.actionLine.triggered.connect(lambda: self.segments("line"))
        self.actionArc.triggered.connect(lambda: self.segments("arc"))
        self.actionQuad.triggered.connect(lambda: self.segments("quad"))

        self.actionFixed.triggered.connect(lambda: supports(self,"Fixed"))
        self.actionHinge.triggered.connect(lambda: supports(self,"Hinge"))
        self.actionRoller.triggered.connect(lambda: supports(self,"Roller"))
        self.actionInternalHinge.triggered.connect(
            lambda: supports(self,"Internal Hinge"))
        self.actionCustomSupport.triggered.connect(
            lambda: supports(self,'custom Support'))
        
        self.actionPointLoad.triggered.connect(
            lambda: self.loads("Point Load"))
        self.actionUDL.triggered.connect(lambda: self.loads("UDL"))
        self.actionUVL.triggered.connect(lambda: self.loads("UVL"))
        self.actionPolyLoad.triggered.connect(lambda: self.loads("Poly Load"))
        self.actionMoment.triggered.connect(lambda: self.loads("Moment"))


    def measure(self):
        self.todraw='measure'
        self.count=0
        self.member=None   
        cursor=QPixmap(resource_path(self.cursorPath+"draw"+self.todraw.capitalize()+".png"))
        self.graphicsView.setCursor(QtGui.QCursor(cursor,5,32))     

    def editPoints(self):
        x=self.rrts(float(self.editX.text()))
        y=self.rrts(float(self.editY.text()))
        if self.coordinateSystem.currentText()=='Polar':
            y=self.rts(y)
            r=x*cos(y*pi/180)
            y=x*sin(y*pi/180)
            x=r
        if self.coordinateMode.currentText()=='Relative' and self.count>0:
            x,y=x+self.x[0],y+self.y[0]
        self.x[self.count],self.y[self.count]=x,y
        # self.graphicsView.setFocus()
        if self.coordinateEdited=='x':
            self.editY.setFocus()
            self.editY.selectAll()
        elif self.coordinateEdited=='y':
            self.editX.setFocus()
            self.editX.selectAll()
        self.drawAll()
        
    
        


      

    def diagrams(self, name):
        check = self.df[(self.df["Class"] == "segment")
                        & (self.df["Name"] == name)]
        if check.empty == False:
            try:
                self.nd.statusbar.showMessage(f"Analysing the member : {name}")
            except:
                self.statusbar.showMessage(f"Analysing the member : {name}")
            robj = self.df[self.df["Name"] == name]["Robject"]
            self.robj = robj.iloc[0]
            self.df[self.df["Name"] == name]["Graphitem"].iloc[0].setSelected(True)
            try:
                self.matrix
            except:
                self.statusbar.showMessage('Analyse the structure first',3000)
                return
            worker = WorkerThread2(convertTo3D(
                self.robj), self.structure, self.matrix,self.NoOfPointsInResponseAndAction,self.trussMode,
                self.shearMode,self.inextensibleMode)

            def assign(a):
                self.actionData = a[0]
                self.responseData = a[1]
            worker.signals.result.connect(assign)
            worker.signals.finished.connect(
                lambda: showDiagrams(name, self, self.MainWindow, True)
            )
            self.threadpool.start(worker)
        else:
            self.statusbar.showMessage(
                "Please select a valid segment to view diagrams", 5000
            )


    def segments(self, todraw):

        self.member = 'segment'
        self.pen=QPen(QColor(*self.segmentColor),self.segmentWidth)
        self.todraw = todraw
        self.count = 0
        if self.delete == True:
            self.delete = False
            self.scene.removeItem(self.scene.items()[0])
        cursor=QPixmap(resource_path(self.cursorPath+"draw"+self.todraw.capitalize()+".png"))
        self.graphicsView.setCursor(QtGui.QCursor(cursor,0,32))

    def loads(self, todraw):
        self.member = 'load'
        self.todraw = todraw
        self.count = 0
        self.loadPen=QPen(QColor(*self.loadColor),self.loadWidth)

        if self.delete == True:
            self.delete = False
            self.scene.removeItem(self.scene.items()[0])
        cursor=QPixmap(resource_path(self.cursorPath+"draw"+self.todraw.capitalize()+".png"))
        self.graphicsView.setCursor(QtGui.QCursor(cursor,0,32))
        self.dockPeakNormal.show()
    def createScene(self):

        self.scene = GraphicsScene(self)
        self.pen = QPen(Qt.red)
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setWidth(3)

        self.pen.setStyle(Qt.SolidLine)
        from structure2d.graphicsView import GraphicsView
        self.graphicsView = GraphicsView(self.scene, self.MainWindow,self)
        # self.graphicsView = QGraphicsView(self.scene)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.viewport().installEventFilter(self.MainWindow)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        # self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        
        from PySide2.QtGui import QTransform
        self.graphicsView.setTransform(QTransform(1., 0., 0., -1., 0, 0))
        # self.graphicsView.rotate(270)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.grid()

    def grid(self):
        # scale=50
        self.MainWindow.showMaximized()
        # self.MainWindow.updateGeometry()
        # self.MainWindow.update()
        import numpy as np
        # xrange = 50 * round((self.MainWindow.width()-150)/50)
        # yrange = 50*round((self.MainWindow.height()-300)/50)
        xrange = 50 * round((self.app.primaryScreen().availableGeometry().width()-150)/50)
        yrange = 50*round((self.app.primaryScreen().availableGeometry().height()-300)/50)

        xrange=int(xrange)
        yrange=int(yrange)
        self.xrange=xrange
        self.yrange=yrange
        self.scene.addLine(0, 0, 0, yrange, QPen(Qt.green, 1.5))
        self.scene.addLine(0, 0, xrange, 0, QPen(Qt.green, 1.5))
        for x in range(0, xrange, self.scale*50):
            self.scene.addLine(x, 0, x, yrange, QPen(Qt.black, 0.25))
            self.totalGridLines+=1
            # [self.scene.addLine(x+a*5, 0, x+a*5, yrange, QPen(Qt.black, 0.02)) for a in range(1,10)]
        self.scene.addLine(x+50, 0, x+50, yrange, QPen(Qt.black, 0.25))
   
        for y in range(0, yrange, self.scale*50):
            self.scene.addLine(0, y, xrange, y, QPen(Qt.black, 0.25))
            self.totalGridLines+=1
            # [self.scene.addLine(0,y+a*5,xrange, y+a*5, QPen(Qt.black, 0.02)) for a in range(1,10)]

        self.scene.addLine(0, y+50, xrange, y+50, QPen(Qt.black, 0.25))
        self.totalGridLines+=2
        self.tempGrid()
        self.smallgrid(False)
        # self.graphicsView.fitInView(0, 0, self.graphicsView.geometry(
        # ).width(), self.graphicsView.geometry().height())
        self.scene.setBackgroundBrush(QBrush(QColor(*self.bgColor)))  
        # self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio);

    def tempGrid(self):
        xrange=self.xrange
        yrange=self.yrange
        for x in range(0, xrange, self.scale*50):
            self.totalGridLines+=9
            self.smallGridLines+=9
            [self.scene.addLine(x+a*5, 0, x+a*5, yrange, QPen(Qt.black, 0.02)) for a in range(1,10)]
        for y in range(0, yrange, self.scale*50):
            self.totalGridLines+=9
            self.smallGridLines+=9
            [self.scene.addLine(0,y+a*5,xrange, y+a*5, QPen(Qt.black, 0.02)) for a in range(1,10)]


    def changeFlag(self, index=None, name=None):
        if name != None:
            index = self.df[self.df["Name"] == name].index[0]
        if self.df.iloc[index, 3].isVisible() == True:
            self.df.iloc[index, 3].hide()
            self.df.iloc[index, 4].setHidden(True)
            self.df.iloc[index, 5] = False
            if self.df.iloc[index,1] == 'segment':
                self.x[0],self.y[0]=self.rrts(self.df.iloc[index,2]['P1'])
        else:
            self.df.iloc[index, 3].show()
            self.df.iloc[index, 4].setHidden(False)
            self.df.iloc[index, 5] = True
            if self.df.iloc[index,1] =='segment':
                self.x[0],self.y[0]=self.rrts(self.df.iloc[index,2]['P3'])
    def redo(self):
        if not self.historystatus:
            self.historystatus = True
        if self.counter < self.historyposition:
            self.changeFlag(index=self.history[self.counter])
            self.history = append(self.history, self.history[self.counter])
            self.counter += 1
        else:
            self.statusbar.showMessage("No more redo available", 2000)

    def undo(self):
        if self.historystatus:
            self.historyposition = len(self.history)
            self.historystatus = False
            self.counter = len(self.history)

        if self.counter > 0:
            self.changeFlag(index=self.history[self.counter-1])
            self.history = append(self.history, self.history[self.counter-1])
            self.counter -= 1
            self.itemss = len(self.df)
        else:
            self.statusbar.showMessage("No more undo available", 2000)

    def drawAll(self,properties=None,name=None):
        self.coordinateEdited=None
        # if self.todraw=='select':
        #     if self.count==1:
        #         from PySide2.QtCore import Qt
        #         h=abs(self.y[1]-self.y[0])
        #         w=abs(self.x[1]-self.x[0])          
        #         a=self.scene.items(min(self.x[0],self.x[1]),min(self.y[0],self.y[1]),w,h,
        #             Qt.ItemSelectionMode.ContainsItemBoundingRect,Qt.SortOrder.AscendingOrder)
        #         [x.setSelected(True) for x in a]
        #         self.count=0
        #         return
        #     else:
        #         self.count=1
        #         return
        if self.member=='segment':
            if self.count==1:
                if self.todraw=='line':
                    drawLine(self,pen=self.pen,properties=properties,name=name)
            elif self.count==2 :
                if self.todraw=='arc' or self.todraw=='quad':
                    drawLine(self,pen=self.pen,properties=properties,name=name)
            self.count +=1
        
        elif self.member=='support':
            drawSupport(self,normal=properties,name=name)
        elif self.member=='load':
            a=self.parent
            if a:
                if self.count==1:
                    if self.todraw=='Moment' or self.todraw=='Point Load':
                        drawLoad(self,name=name)
                elif self.count==2 :
                    drawLoad(self,name=name)
                self.count +=1
            else:
                self.statusbar.showMessage("Please select a valid segment",5000)
        elif self.todraw=='measure':
            self.count=1



            # self.count=1 if self.count==0 else 0  



    def axis(self):
        if self.actionAxis.isChecked()==True:
            self.scene.items()[-1].show()
            self.scene.items()[-2].show()
        else:
            self.scene.items()[-2].hide()
            self.scene.items()[-1].hide()

    def smallgrid(self,zoom):
        if zoom:
            for i in range(self.totalGridLines-self.smallGridLines,self.totalGridLines):
               self.scene.items()[-i-3].show()
        else:
            for i in range(self.totalGridLines-self.smallGridLines,self.totalGridLines):
               self.scene.items()[-i-3].hide()
    def gridLines(self):
        if self.actionGrid.isChecked() == True:
            for i in range(self.totalGridLines):
               self.scene.items()[-i-3].show()
        else:
            for i in range(self.totalGridLines):
               self.scene.items()[-i-3].hide()

    def rts(self, a):
        from numpy import round as npround
        try:
            return npround(a/(self.scale*50), self.precison)
        except:
            return npround(a/(self.scale*50), self.precison)

    def rrts(self, a):
        try:
            return a*self.scale*50
        except Exception as e:
            return a*self.scale*50
# %%
