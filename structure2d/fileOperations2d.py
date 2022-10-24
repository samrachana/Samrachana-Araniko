import configparser
import os
from PySide2 import QtCore, QtGui, QtWidgets
from numpy.testing._private.utils import assert_equal
from pandas import DataFrame,read_excel,read_csv,to_pickle,read_pickle
from numpy import array,testing
from configparser import ConfigParser
# from rbindings import R
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QBrush,QColor,QPen
from sdPy.segmentMethods import segPlotData2
from sdPy.loadMethods import loadPlotData2, loadPlotData4
from sdPy.supportMethods import supportPlotData2
from PySide2.QtWidgets import QGraphicsItem,QMessageBox
import json
from structure2d.objecttree2d import editObjectTree

attributesForConfigFile={
    'UNITS':['currentUnit', 'force', 'length', 'precison', 'scale'], 
    'COLORS':['bgColor', 'segmentColor', 'loadColor', 'afdColor', 'sfdColor', 'bmdColor', 'translationColor', 'rotationColor', 'rollerColor', 'hingeColor', 'fixedColor', 
    'internalHingeColor'], 
    'WIDTHS':['segmentWidth', 'loadWidth'],
    'TWEAKS':['NoOfPointsInResponseAndAction', 'NoOfPointsInVector', 'NoOfPointsInMotion', 'NoOfPointsInCurvedSegments', 'loadLogScale', 'interpolationMode'],
    'OTHERS':['setunits', 'darkMode'], 
 }


def saveConfigFile(self):
    # configObject=ConfigParser()
    configObject={}
    for section,values in attributesForConfigFile.items():
        configObject[section]={x:getattr(self,x) for x in values}
    with open(self.fileName.split('.')[0]+'.ini','w') as f:
        json.dump(configObject,f,indent=4)
        # configObject.write(f)
def loadConfigFile(self):
    with open(self.fileName.split('.')[0]+'.ini') as f:
        configObject=json.loads(f.read())
    # configObject.read(self.fileName.split('.')[0]+'.ini')
    for section,values in attributesForConfigFile.items():
        [setattr(self,x,configObject[section][x]) for x in values]

    self.editPrecison.setText(str(self.precison))
    self.editScale.setText(str(self.scale))
    self.scene.setBackgroundBrush(QBrush(QColor(*self.bgColor)))

    units=f'''Length : {self.length}m\nForce   : {self.force}N''' if self.currentUnit=='SI' else f'''Length : {self.length}ft\nForce   : {self.force}pdl'''
    self.currentUnitLabel.setText('Units : '+self.currentUnit)
    from.dark2d import darkMode
    if configObject['OTHERS']['darkMode']:
    # if data['darkMode']:
        self.actionDark_Mode.setChecked(True)
        darkMode(self,self.app)
    else:    
        self.actionDark_Mode.setChecked(False)
        darkMode(self,self.app)

def printFile(self):
    from PySide2.QtWidgets import QFileDialog
    fileName, _ = QFileDialog.getSaveFileName(caption="Print Graph as png Image")
    from PySide2.QtGui import QImage, QPainter
    width,height=self.graphicsView.size().width(),self.graphicsView.size().height()

    image=QImage(width,height,QImage.Format_ARGB32);
    painter=QPainter(image)
    painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing | QPainter.HighQualityAntialiasing | QPainter.NonCosmeticDefaultPen)
    
    self.graphicsView.render(painter)
    painter.end()
    image.save("test.png","PNG")

    # a=self.scene.renderToArray((1080,1920))
    # from PIL import Image
    # im = Image.fromarray(a,mode='RGBA')
    if fileName:
        image.save(fileName+'.png',"PNG")
    else:
        image.save('./sampleFiles/graph.png',"PNG")    
def newFile(self):
    items=self.df[self.df['Flag']==True]
    [self.scene.removeItem(x) for x in self.nodes]
    self.nodes=[]
    if len(items)>0:
        ret = QMessageBox.question(self.MainWindow, "The structure has been modified.\n"," Do you want to save your changes?",
                            QMessageBox.Save | QMessageBox.Discard
                            | QMessageBox.Cancel)
        if ret==QMessageBox.Save:
            saveFile(self)
            if self.fileName==None: return        
        elif ret==QMessageBox.Cancel:
            return
    self.statusbar.showMessage('Opening new file',3000)
    # for item in range(len(self.scene.items())-self.totalGridLines-2):
    #     self.scene.removeItem(self.scene.items()[0])
    graphitems=self.df['Graphitem']
    for i in graphitems:
        self.scene.removeItem(i)
    self.ot.segment.takeChildren()
    self.ot.load.takeChildren()
    self.ot.support.takeChildren()
    self.variables()
    self.MainWindow.setWindowTitle('Samrachana - '+'Untitled.str')
    # import os
    # os.execl(sys.executable, sys.executable, *sys.argv)
 
def saveFile(self):
    self.statusbar.showMessage('Saving File',3000)
    # aa=self.df[(self.df['Class']=='load')&(self.df['Flag']==True)]['Robject']
    dd=self.df[(self.df['Flag']==True)][['Name','Class','Robject','Flag']]        
    if self.fileName==None:
        saveAsFile(self)
    elif self.fileName.endswith('.csv'):
        dd.to_csv(self.fileName)
    elif self.fileName.endswith('.detail'):
        # types=[i[0] for i  in self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]['Robject']]
        p1=[i[1] for i  in self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]['Robject']]
        p2=[i[2] for i  in self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]['Robject']]
        prop=[i[4:] for i  in self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]['Robject']]

        data={'Name':dd['Name'],'Class':dd['Class'],'Initial Point':p1,'Final Point':p2,'Properties(E,G,A,I,k)':prop,}
        dd=DataFrame(data)
        dd.to_csv(self.fileName+'segments.csv')
    else:    
        dd.to_pickle(self.fileName)            
    if self.fileName==None:return

    saveConfigFile(self)
    self.statusbar.showMessage('File saved as %s'%(self.fileName),1000)
    head,tail=os.path.split(self.fileName)
    self.MainWindow.setWindowTitle('Samrachana - '+tail)
def saveAsFile(self):
    from PySide2.QtWidgets import QFileDialog
    fileName, _ = QFileDialog.getSaveFileName(caption="Save File")
    if fileName=='': self.statusbar.showMessage('File not saved, Enter proper file name to save file',2000); return
    if not fileName.endswith(('.str','.csv')):
        self.fileName=fileName+'.str'
    else:
        self.fileName= fileName 
    saveFile(self)   


def openFile(self,directOpen=None):
    if directOpen==None:
        from PySide2.QtWidgets import QFileDialog
        fileName, _ = QFileDialog.getOpenFileName(caption='Open Structure File',filter=("Structure Files(Samrachana) (*.str);;csv (*.csv);;excel files(*.xlsx *.xls);;All files (*.*)"))
    else:
        fileName=directOpen
    from pandas import read_pickle    
    
    if fileName.endswith('.str')==True:
        tempdf = read_pickle(fileName)
    elif fileName.endswith('.csv')==True:
        tempdf=read_csv(fileName)
        tempdf=tempdf.drop(columns=['Unnamed: 0'])
        import ast
        # tempdf['Robject']=tempdf.apply(ast.literal_eval)
        for i in range(len(tempdf)):
            x=tempdf.iloc[i,2]                
            tempdf.iat[i,2]=eval(x)
        
    else:
        fileName=False    
    if fileName:
        self.fileName=fileName
        newFile(self)
        try:
            loadConfigFile(self)
        except:
            import traceback
            traceback.print_exc()
            pass
        self.statusbar.showMessage('Opening File',3000)
        self.pen=QPen(QColor(*self.segmentColor),self.segmentWidth)    
        aa=tempdf[(tempdf['Class']=='segment')&(tempdf['Flag']==True)]    
        self.segmentNumber=len(aa)+1
        for element in range(len(aa)):
            Rsegment=aa.iloc[element,2]
            if Rsegment['type']=='line':
                rect=self.scene.addLine(self.rrts(Rsegment['P1'])[0],self.rrts(Rsegment['P1'])[1],self.rrts(Rsegment['P3'])[0],self.rrts(Rsegment['P3'])[1],self.pen)
            else:
                data=segPlotData2(Rsegment['type'],self.rrts(Rsegment['P1']),self.rrts(Rsegment['P3']),1,self.rrts(Rsegment['P2']),no=self.NoOfPointsInCurvedSegments)

                rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
                for i in range(2,len(data),2):
                    rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
                rect=self.scene.addPath(rect,self.pen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable)
            
            name=aa.iloc[element,0]
            item=QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.df.loc[len(self.df)]=[name,'segment',Rsegment,self.scene.items()[0],item,True]
            self.ot.segment.addChild(item)   
            item.setText(0,name)
            [self.ot.segment.child(element).setData(i+1,2,str(list(Rsegment.values())[i+1])) for i in range(10)]           
            self.ot.segment.child(element).setData(11,2,Rsegment['type'])
            self.app.processEvents()
        self.loadPen=QPen(QColor(*self.loadColor),self.loadWidth)

        aa=tempdf[(tempdf['Class']=='load')&(tempdf['Flag']==True)]
        self.loadNumber=0
        for element in range(len(aa)):
            self.loadNumber+=1
            Rload=aa.iloc[element,2]
            ps=Rload['parentSegment']
            if Rload['degree']> -3:
                data=loadPlotData2(self.rrts(Rload['P1']),self.rrts(Rload['P3']),self.rrts(ps['P1']),self.rrts(ps['P3']),
                self.rrts(ps['P2']), Rload['degree'],self.rrts(Rload['peak']),Rload['normal'],ps['type'],self.scale,self.loadLogScale)
            else:
                data=loadPlotData4(ps,Rload['degree'],self.rrts(Rload['peak']))
            rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
            for i in range(1,len(data),1):
                rect.lineTo(QtCore.QPointF(data[i][0],data[i][1]))
                # rect.quadTo(QtCore.QPointF(data[i-1][0],data[i-1][1]),QtCore.QPointF(data[i][0],data[i][1]))
            rect=self.scene.addPath(rect,self.loadPen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable) 

            name=aa.iloc[element,0]
            item=QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.df.loc[len(self.df)]=[name,'load',Rload,self.scene.items()[0],item,True]
            self.ot.load.addChild(item)   
            item.setText(0,name)
            # [self.ot.load.child(element).setData(i+1,2,str(list(Rload.values())[i])) for i in range(6)]           
            self.ot.load.child(self.loadNumber-1).setData(1,2,Rload['degree'])
            combo=QtWidgets.QComboBox()
            combo.addItems(reversed(list(self.df[(self.df['Class']=='segment')&(self.df['Flag']==True)]['Name'])))
            combo.setCurrentText(Rload['psName'])
            combo.currentIndexChanged.connect(lambda:editObjectTree(self))
            item.setData(2,2,self.df[(self.df['Name']==name)]['Name'].iloc[0])
            self.ot.treeWidget.setItemWidget(item,2,combo)
            [self.ot.load.child(self.loadNumber-1).setData(i+1,2,str(list(Rload.values())[i])) for i in range(2,6)]           
            # self.ot.load.child(self.loadNumber-1).setData(6,2,Rload['peak'])           
            self.app.processEvents()
        self.loadNumber+=1

        aa=tempdf[(tempdf['Class']=='support')&(tempdf['Flag']==True)]
        self.supportNumber=len(aa)+1
        
        for element in range(len(aa)):
            Rsupport = aa.iloc[element,2]
            data=supportPlotData2(Rsupport['type'] , self.rrts(Rsupport['location']),normal=Rsupport['normal'],scale=0.02)
            rect = QtGui.QPainterPath(QtCore.QPointF(data[0][0],data[0][1]))
            
            color=self.supportColors[Rsupport['type']]
            self.supportPen=QPen(QColor(*color),1.5)
            
            types=aa.iloc[element,2]['type']
            for i in range(1,len(data)):
                rect.lineTo(QtCore.QPointF(QtCore.QPointF(data[i][0],data[i][1])))            
            rect=self.scene.addPath(rect,self.supportPen) 
            rect.setFlag(QGraphicsItem.ItemIsSelectable)
          
            supportName=aa.iloc[element,0]
            item=QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.df.loc[len(self.df)]=[supportName,'support',Rsupport,self.scene.items()[0],item,True]
            self.ot.support.addChild(item)   
            item.setText(0,supportName)
            [self.ot.support.child(element).setData(i+1,2,str(list(Rsupport.values())[i])) for i in range(4)]           
            self.app.processEvents()
        # self.segmentNumber=len(self.df[(self.df['Class']=='segment')])
        # self.loadNumber=len(self.df[(self.df['Class']=='load')])
        # self.supportNumber=len(self.df[(self.df['Class']=='support')])
        self.historystatus=True
    else:
        self.statusbar.showMessage('Unable to open file. Select a valid .str file',2000)


    head,tail=os.path.split(self.fileName)
    self.MainWindow.setWindowTitle('Samrachana - '+tail)