import os
from PySide2 import QtCore, QtGui, QtWidgets
from pandas import DataFrame,read_excel,read_csv,to_pickle,read_pickle
from numpy import array
from structure3d.plot import Plot
# from rbindings import R
import sys

from PySide2.QtCore import Qt

from sdPy.segmentMethods import segPlotData
from sdPy.loadMethods import loadPlotData
from sdPy.supportMethods import supportPlotData

def printFile(self):
    from PySide2.QtWidgets import QFileDialog
    fileName, _ = QFileDialog.getSaveFileName(caption="Print Graph as GIF Image")
    a=self.graphWidget.renderToArray((1080,1920))
    from PIL import Image
    im = Image.fromarray(a,mode='RGBA')
    if fileName:
        im.save('./sampleFiles/'+fileName+'.gif')
    else:
        im.save('./graph.gif')    
def newFile(self):
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)
 
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

        data={'Name':dd['Name'],'Class':dd['Class'],'Initial Point':p1,'Final Point':p2,'Properties(E,G,A,Ixx,Iyy,J,k)':prop,}
        dd=DataFrame(data)
        dd.to_csv(self.fileName+'segments.csv')
    else:    
        dd.to_pickle(self.fileName)            
    self.statusbar.showMessage('File saved as %s'%(self.fileName),1000)
    head,tail=os.path.split(self.fileName)
    self.MainWindow.setWindowTitle('Samrachana - '+tail)
def saveAsFile(self):
    from PySide2.QtWidgets import QFileDialog
    fileName, _ = QFileDialog.getSaveFileName(caption="Save File")
    if not fileName.endswith(('.str','.csv')):
        self.fileName=fileName+'.str'
    else:
        self.fileName= fileName 
    saveFile(self)   




def openFile(self,app,directOpen=None):
    if directOpen==None:
        from PySide2.QtWidgets import QFileDialog
        fileName, _ = QFileDialog.getOpenFileName(caption='Open Structure File')
    else:
        fileName='./sampleFiles/'+directOpen
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
        self.statusbar.showMessage('Opening File',3000)
    
        aa=tempdf[(tempdf['Class']=='segment')&(tempdf['Flag']==True)]    
        self.segmentNumber=len(aa)+1
        for element in range(len(aa)):
            Rsegment=aa.iloc[element,2]
            sdata=segPlotData(Rsegment['type'],Rsegment['P1'],Rsegment['P3'],Rsegment['axisVector'],self.scale,Rsegment['P2'])

            Plot.plott(Plot,sdata, self.graphWidget, self.segmentColor,self.segmentWidth) 
            name=aa.iloc[element,0]
            item=QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.df.loc[len(self.df)]=[name,'segment',Rsegment,self.graphWidget.items[-1],item,True]
            self.ot.segment.addChild(item)   
            item.setText(0,name)
            [self.ot.segment.child(element).setData(i+1,2,str(list(Rsegment.values())[i+1])) for i in range(11)]           
            self.ot.segment.child(element).setData(12,2,Rsegment['type'])

            app.processEvents()

        aa=tempdf[(tempdf['Class']=='load')&(tempdf['Flag']==True)]
        self.loadNumber=len(aa)+1
        for element in range(len(aa)):
            Rload=aa.iloc[element,2]
            ps=Rload['parentSegment']
            Rloaddata=loadPlotData(Rload['P1'],Rload['P3'],ps['P1'],ps['P3'],
         ps['P2'], Rload['degree'],Rload['peak'],Rload['normal'],ps['type'],self.scale)
            Plot.plott(Plot, array(Rloaddata), self.graphWidget, self.loadColor,self.loadWidth)
      
            name=aa.iloc[element,0]
            item=QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.df.loc[len(self.df)]=[name,'load',Rload,self.graphWidget.items[len(self.graphWidget.items)-1],item,True]
            self.ot.load.addChild(item)   
            item.setText(0,name)
            [self.ot.load.child(element).setData(i+1,2,str(list(Rload.values())[i])) for i in range(6)]           
           
            app.processEvents()
            

        aa=tempdf[(tempdf['Class']=='support')&(tempdf['Flag']==True)]
        self.supportNumber=len(aa)+1
        colors = {"Roller": self.rollerColor, "Hinge": self.hingeColor, "Fixed": self.fixedColor,"Internal Hinge":self.internalHingeColor}
        for element in range(len(aa)):
            Rsupport = aa.iloc[element,2]
            Rsupportdata=supportPlotData(Rsupport['type'] , Rsupport['location'],self.scale,Rsupport['normal'])
        
            types=aa.iloc[element,2]['type']
            color = colors[types]
            Plot.plotsupport(Plot,Rsupportdata, self.graphWidget, color)
            
            supportName=aa.iloc[element,0]
            item=QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.df.loc[len(self.df)]=[supportName,'support',Rsupport,self.graphWidget.items[len(self.graphWidget.items)-1],item,True]
            self.ot.support.addChild(item)   
            item.setText(0,supportName)
            [self.ot.support.child(element).setData(i+1,2,str(list(Rsupport.values())[i])) for i in range(4)]           
        
            app.processEvents()
        # self.segmentNumber=len(self.df[(self.df['Class']=='segment')])
        # self.loadNumber=len(self.df[(self.df['Class']=='load')])
        # self.supportNumber=len(self.df[(self.df['Class']=='support')])
        self.historystatus=True
    else:
        self.statusbar.showMessage('Unable to open file. Select a valid .str file',2000)
