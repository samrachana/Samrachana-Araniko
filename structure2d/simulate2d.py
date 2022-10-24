from UI.simulationEnvironment import Ui_Dialog
from PySide2.QtWidgets import QDialog, QGraphicsItem, QTableWidgetItem,QLabel,QComboBox
from UI.liveLoadDefinition import Ui_Dialog as Dialog
from sdPy.functionDefinitions import convertTo2D, convertTo3D, make2d, structify2d,apply
from numpy import nan, vstack,array
from sdPy.simulationMethods import fillAnimationFrames
from sdPy.loadMethods import loadPlotData2
from sdPy.simulationMethods import (vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp,
                vectorDiagramDataAngles2Dcomp,vectorDiagramDataDisps2Dcomp)
from sdPy.simulationMethods import vectorDiagramDataTrussDisps2Dcomp,vectorDiagramDataTrussForces2Dcomp

# def plotData(self,simulationData):
#     from PySide2 import QtGui,QtCore
#     from numpy import nan
#     data=simulationData
#     rect = QtGui.QPainterPath(QtCore.QPointF(self.rrts(data[0][0]),self.rrts(data[0][1])))
#     for i in range(1,len(data),1):
#         # if data[i][0]!=nan:
#             rect.lineTo(QtCore.QPointF(self.rrts(data[i][0]),self.rrts(data[i][1])))
#         # rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
#     rect=self.scene.addPath(rect) 
#     rect.setFlag(QGraphicsItem.ItemIsSelectable)    

def write_qtable_to_df(table):
    col_count = table.columnCount()
    row_count = table.rowCount()
    headers = [str(table.horizontalHeaderItem(i).text()) for i in range(col_count)]

    # df indexing is slow, so use lists
    df_list = []
    for row in range(row_count):
        df_list2 = []
        for col in range(col_count):
            table_item = table.item(row,col)
            df_list2.append('' if table_item is None else str(table_item.text()))
        df_list.append(df_list2)
    from pandas import DataFrame
    df = DataFrame(df_list, columns=headers)

    return df

def changeKeyFrameTableData(self):
    df=write_qtable_to_df(self.se.keyFrameTable)
    # for i in range(self.se.keyFrameTable.rowCount()):
    #     self.se.keyFrameTable.removeRow(self.se.keyFrameTable.currentRow())
    for i in range(len(df)):
        time=float(df.iloc[i,1])/self.duration*self.se.duration.value()
        frameNo=round(self.fps*time)
        self.se.keyFrameTable.setItem(i,0,QTableWidgetItem(str(i+1)))
        self.se.keyFrameTable.setItem(i,1,QTableWidgetItem(str(time)))
        self.se.keyFrameTable.setItem(i,2,QTableWidgetItem(str(frameNo)))   
def liveLoadsDefinition(self,MainWindow):
    self.fps=self.se.fps.value()
    self.duration=self.se.duration.value()
    self.sE.close()
    self.lld=Dialog()
    self.llD=QDialog(parent=MainWindow)
    self.lld.setupUi(self.llD)
    self.keyFramesDataFrame=write_qtable_to_df(self.se.keyFrameTable)
    
    self.listOfKeyFrameIndexes=[]

    keyFrames=self.keyFramesDataFrame['KeyFrame']
    if self.structure:
        self.finalKeyFrameStructures={i:self.structure.copy() for i in keyFrames}
    else:
        self.statusbar.showMessage('Please analyse structure first [ALT+A]',5000)
    keyFrames=[str(i) for i in keyFrames]
    self.lld.keyFrames.addItems(keyFrames)
    self.listOfKeyFrameIndexes.append(str(self.lld.keyFrames.currentIndex()+1))
    loads=self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]
    [self.lld.liveLoadsTable.insertRow(i) for i in range(len(loads))]
    # self.lld.keyFrames.addItems(['ram','sam'])
    import warnings
    def setLoads(loads,r=None):
        names=list(self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]['Name'])
        for i in range(len(loads)):
            # self.lld.liveLoadsTable.insertRow(i)
            loads=list(loads)
            try:
                with warnings.catch_warnings(record=True) as w:
                    load=convertTo2D(loads[i])    
            except:
                load=loads[i]

            self.lld.liveLoadsTable.setItem(i,0,QTableWidgetItem(str(names[i])))
            self.lld.liveLoadsTable.setItem(i,1,QTableWidgetItem(str(load['degree'])))
            self.lld.liveLoadsTable.setItem(i,2,QTableWidgetItem(str(load['P1'])))
            self.lld.liveLoadsTable.setItem(i,3,QTableWidgetItem(str(load['P3'])))
            self.lld.liveLoadsTable.setItem(i,4,QTableWidgetItem(str(load['peak'])))
            self.lld.liveLoadsTable.setItem(i,5,QTableWidgetItem(str(load['normal'])))
    # print(self.finalKeyFrameStructures)

    setLoads(self.finalKeyFrameStructures[self.listOfKeyFrameIndexes[-1]]['loads'],1)
    from numpy import array,fromstring
    def newLoads():
        self.listOfKeyFrameIndexes.append(str(self.lld.keyFrames.currentIndex()+1))
        loads=self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]
        try:
        # if True:
            currentKeyFrameLoads=[]
            for i in range(len(loads)):
                parentSegment=loads['Robject'].iloc[i]['parentSegment']
                degree=float(self.lld.liveLoadsTable.item(i,1).text())
                def formarray(currentText):
                    import re
                    currentText=re.sub('[\[\]]','',currentText)

                    currentText=re.split(',| ',currentText)
                    while '' in currentText:currentText.remove('')
                    currentText=array(currentText,dtype=float) 
                    return currentText
                # P1=fromstring(self.lld.liveLoadsTable.item(i,2).text()[1:-1],sep=' ')
                # P3=fromstring(self.lld.liveLoadsTable.item(i,3).text()[1:-1],sep=' ')
                P1=formarray(self.lld.liveLoadsTable.item(i,2).text())
                P3=formarray(self.lld.liveLoadsTable.item(i,3).text())
                peak=float(self.lld.liveLoadsTable.item(i,4).text())
                # normal=fromstring(self.lld.liveLoadsTable.item(i,5).text()[1:-1],sep=' ')
                normal=formarray(self.lld.liveLoadsTable.item(i,5).text())

                newLoad=make2d([degree,parentSegment,P1,P3,normal,peak])
                currentKeyFrameLoads.append(newLoad)
            
            structure=list(self.df[(self.df["Flag"] == True)&(self.df['Class']!='load')]["Robject"])+currentKeyFrameLoads
            newStructure=structify2d(structure)
            self.finalKeyFrameStructures[self.listOfKeyFrameIndexes[-2]]=newStructure
            setLoads(self.finalKeyFrameStructures[self.listOfKeyFrameIndexes[-1]]['loads'],2)
        except Exception as e:
            print(e)
            # self.lld.keyFrames.setCurrentIndex(int(self.listOfKeyFrameIndexes[-2]))
            setLoads(self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]['Robject'],3)
            self.statusbar.showMessage('Please, Enter valid data',2000)
    self.lld.keyFrames.currentIndexChanged.connect(newLoads)
    self.lld.reset.clicked.connect(lambda:setLoads(self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]['Robject'],4))
    def nextFrame():
        if self.lld.keyFrames.currentIndex()<len(keyFrames)-1:
            self.lld.keyFrames.setCurrentIndex(self.lld.keyFrames.currentIndex()+1)
    self.lld.nextFrame.clicked.connect(nextFrame)
    def previousFrame():
        if self.lld.keyFrames.currentIndex()>0:
            self.lld.keyFrames.setCurrentIndex(self.lld.keyFrames.currentIndex()-1)
    self.lld.previousFrame.clicked.connect(previousFrame)

    def back():
        self.sE.show()
        self.llD.close()
    self.lld.back.clicked.connect(back)
    
    def simulation():
        newLoads()



    # # Vector diagram Options
    #     self.propertiesBar.addSeparator()
    #     self.propertiesBar.addWidget(QLabel('Vector Diagram'))

    #     if not self.trussMode:
    #         self.vectorDiagramOptionsDict={
    #             'Bending Moment':vectorDiagramDataMoments2D,
    #             'Resultant Force':vectorDiagramDataForces2D,
    #             'Shear Force':vectorDiagramDataForces2Dcomp,
    #             'Axial Force':vectorDiagramDataForces2Dcomp,
    #             'Slope':vectorDiagramDataAngles2Dcomp,
    #             'DisplacementX':vectorDiagramDataDisps2Dcomp,
    #             'DisplacementY':vectorDiagramDataDisps2Dcomp
    #             }
    #     else:
    #         self.vectorDiagramOptionsDict={
    #             'Axial Force':vectorDiagramDataTrussForces2Dcomp,
    #             'DisplacementX':vectorDiagramDataTrussDisps2Dcomp,
    #             'DisplacementY':vectorDiagramDataTrussDisps2Dcomp
    #             }

    #     self.vectorDiagramOptions=QComboBox()
    #     self.vectorDiagramOptions.addItems(list(self.vectorDiagramOptionsDict.keys()))   
    #     self.propertiesBar.addWidget(self.vectorDiagramOptions)
    #     self.vectorDiagramOptions.setDisabled(True)

    #     self.propertiesBar.addSeparator()
    #     self.animationModeOptions=QComboBox()
    #     self.animationModeOptions.addItems(['Quick','Accurate'])
    #     self.propertiesBar.addWidget(QLabel('Animation Mode'))
    #     self.propertiesBar.addWidget(self.animationModeOptions)
    #     self.animationModeOptions.setDisabled(True)
        
    #     from structure2d.animationCalculations import calculateVectorDiagramData
    #     self.vectorDiagramOptions.currentIndexChanged.connect(lambda:calculateVectorDiagramData(self))


    # # Animation Bar
    #     self.dockAnimationBar.show()
    #     self.MainWindow.tabifyDockWidget(self.dockAnalysisTable,self.dockAnimationBar)
    #     self.animationModeOptions.setDisabled(False)
        
    #     from sdPy.simulationMethods import interpolateLoads
    #     def animationModeChanged():
    #         self.animationBar.setDisabled(True)
    #         if self.animationModeOptions.currentIndex()==1:
    #             try:
    #                 self.finalKeyFrameStructures= interpolateLoads(self.finalKeyFrameStructures)
    #             except:
    #                 self.finalKeyFrameStructures=interpolateLoads(self.userDefinedKeyframes)
    #         else:
    #             self.finalKeyFrameStructures=self.userDefinedKeyframes
    #         self.keyFrames=list(self.finalKeyFrameStructures.keys())

    #         self.masterData={}
    #         from sdPy.structureMethods import frame2d,truss2d
    #         strMode=truss2d if self.trussMode else frame2d
    #         for i in self.keyFrames:
    #             self.masterData[i]=strMode(self.finalKeyFrameStructures[i],self.shearMode,self.inextensibleMode,self.simplifyMode)            
    #             self.statusbar.showMessage(f'Preparing Evironment : {round(i/self.keyFrames[-1]*100)}%',100)
    #             self.app.processEvents()     

    #         self.loadPlotData={}
    #         for i in self.keyFrames:
    #             x=self.finalKeyFrameStructures[i]['loads'][0]
    #             x=convertTo2D(x)

    #             lData=loadPlotData2(
    #                             x['P1'],x['P3'],
    #                             x['parentSegment']['P1'],x['parentSegment']['P3'],x['parentSegment']['P2'],
    #                             x['degree'],x['peak'],x['normal'],x['parentSegment']['type'],self.scale,1  
    #                 )
    #             lData=vstack((lData,[nan,nan]))    
    #             for x in self.finalKeyFrameStructures[i]['loads'][1:]:
    #                 x=convertTo2D(x)
    #                 valData = loadPlotData2(
    #                             x['P1'],x['P3'],
    #                             x['parentSegment']['P1'],x['parentSegment']['P3'],x['parentSegment']['P2'],
    #                             x['degree'],x['peak'],x['normal'],x['parentSegment']['type'],self.scale,1  
    #                 )
    #                 valData=vstack((valData,[nan,nan]))
    #                 lData=vstack((lData,valData))
    #             self.loadPlotData[i]=lData
    #             self.app.processEvents()     
    #         if self.animationModeOptions.currentIndex()==0:
    #             fillAnimationFrames(self.loadPlotData,'spline')

    #         self.animationBar.setDisabled(False)

    #     animationModeChanged()
    #     self.animationModeOptions.currentIndexChanged.connect(animationModeChanged)

    #     self.dockAnimationBar.show()
    #     self.MainWindow.tabifyDockWidget(self.dockAnalysisTable,self.dockAnimationBar)

        from simulation.animationWindow import AnimationWindow
        AnimationWindow(self)


    self.lld.done.clicked.connect(simulation)
    self.llD.show()


def simulationEnvironment(self,MainWindow):
    # import sys
    # sys.setrecursionlimit(200)
    self.se=Ui_Dialog()
    self.sE=QDialog(parent=MainWindow)
    self.se.setupUi(self.sE)
    def setFps():
        self.fps=self.se.fps.value()
        changeKeyFrameTableData(self)
    def setDuration():
        changeKeyFrameTableData(self)
        self.duration=self.se.duration.value()
    setFps()
    setDuration()
    self.se.fps.valueChanged.connect(setFps)
    self.se.duration.valueChanged.connect(setDuration)
    self.se.fps.setValue(10)
    from PySide2.QtCore import Qt 
    def addRow():
        row=self.se.keyFrameTable.rowCount()
        totalFrames=self.fps*self.duration
        self.se.keyFrameTable.insertRow(row)
        if row==0:
            self.keyFramesEdited=False
            self.se.keyFrameTable.setItem(0,0,QTableWidgetItem(str(1)))
            self.se.keyFrameTable.setItem(0,1,QTableWidgetItem(str(0)))
            self.se.keyFrameTable.setItem(0,2,QTableWidgetItem(str(0)))
        if not self.keyFramesEdited:
            for i in range(1,row+1):
                duration=round(self.duration/(row)*i,3)
                frameNo=round(totalFrames/(row)*i)
                self.se.keyFrameTable.setItem(i,0,QTableWidgetItem(str(i+1)))
                self.se.keyFrameTable.setItem(i,1,QTableWidgetItem(str(duration)))
                self.se.keyFrameTable.setItem(i,2,QTableWidgetItem(str(frameNo)))            
        else:
            self.se.keyFrameTable.setItem(row,0,QTableWidgetItem(str(row+1)))
    addRow()
    addRow()
    self.se.addRow.clicked.connect(addRow)
    def subtractRow():
        self.se.keyFrameTable.removeRow(self.se.keyFrameTable.currentRow())
    self.se.subtractRow.clicked.connect(subtractRow)    
    
    def itemChanged():
        
        currentItem=self.se.keyFrameTable.currentItem()
        if currentItem:
            row=currentItem.row()
            col=currentItem.column()
            totalFrames=self.fps*self.duration
            
            frameNo=self.se.keyFrameTable.item(row,2)
            frameNo=int(frameNo.text()) if frameNo else 0
            time=self.se.keyFrameTable.item(row,1)
            time=float(time.text()) if time else 0
            if frameNo!=round(self.fps*time):
                self.keyFramesEdited=True
                if col==1:          
                    self.se.keyFrameTable.setItem(row,2,
                    QTableWidgetItem(str(round(totalFrames*time/self.duration))))
                elif col==2:
                    self.se.keyFrameTable.setItem(row,1,
                    QTableWidgetItem(str(round(self.duration*frameNo/totalFrames,3))))

    self.se.keyFrameTable.itemChanged.connect(itemChanged)
    self.se.next.clicked.connect(lambda:liveLoadsDefinition(self,MainWindow))
    self.sE.show()