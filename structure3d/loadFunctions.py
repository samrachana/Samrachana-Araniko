from UI.loadDialog import Ui_Dialog as LoadUi_Dialog
from sdPy.loadMethods import loadPlotData
from PySide2 import QtWidgets
from sdPy.functionDefinitions import make
from structure3d.plot import Plot
from PySide2.QtCore import Qt
from numpy import append,array
from numpy.linalg import norm
import warnings
def loadobjectMaker(self):
    try:
        name = self.ld.name.text()
        if name == "":
            segmentName = "Load-" + str(self.loadNumber)+' ('+self.loadtype+') '
        else:
            segmentName = name
        self.segment = []
        name = segmentName
        p1 = (self.ld.p1x.text(), self.ld.p1y.text(), self.ld.p1z.text())
        p3 = (self.ld.p3x.text(), self.ld.p3y.text(), self.ld.p3z.text())
        normal = [self.ld.n1.text(), self.ld.n2.text(), self.ld.n3.text()]        
        parentSegment = self.ld.parentSegment.currentText()
        ps=self.df[(self.df['Name']==parentSegment)]['Robject'].iloc[0]
        degree = self.ld.degree.text()
        peak = self.ld.peak.text()
        if p1==('','',''):
            p1=self.ld.initialSlider.value()/1000
            p3=self.ld.finalSlider.value()/1000
        with warnings.catch_warnings(record=True) as w:
            Rload=make([degree,ps, p1, p3, normal, peak])
            Rloaddata=loadPlotData(Rload['P1'],Rload['P3'],ps['P1'],ps['P3'],
            ps['P2'], Rload['degree'],Rload['peak'],Rload['normal'],ps['type'],self.scale)

            if len(w):
                self.statusbar.showMessage(str(w[0].message),2000)
        Plot.plott(Plot, array(Rloaddata), self.graphWidget, self.loadColor,self.loadWidth)

        item=QtWidgets.QTreeWidgetItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.df.loc[len(self.df)]=[name,'load',Rload,self.graphWidget.items[len(self.graphWidget.items)-1],item,True]
        self.ot.load.addChild(item)   
        item.setText(0,name)
        [self.ot.load.child(self.loadNumber-1).setData(i+1,2,str(list(Rload.values())[i])) for i in range(6)]           
        
        self.loadNumber += 1
        self.history=append(self.history,len(self.df)-1)
        self.historystatus=True
    except Exception as e:
        self.statusbar.showMessage(str(e),2000)   


def loadDialog(self,types,MainWindow):
    # try:
    self.loadtype=types
    self.lD = QtWidgets.QDialog(parent=MainWindow)
    self.ld = LoadUi_Dialog()
    self.ld.setupUi(self.lD)

    ls=self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]
    ls=ls['Robject'].iloc[len(ls)-1]
    p1=ls['P1'];p3=ls['P3']
    # a=array(R.r.magnitude(self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]['Robject'].iloc[0]))
    # print(a)
    ranges=int(norm(p1-p3)*1000)
    self.ld.initialSlider.setMaximum(ranges)
    self.ld.initialBox.setMaximum(ranges/1000)
    self.ld.finalSlider.setMaximum(ranges)
    self.ld.finalBox.setMaximum(ranges/1000)
    self.ld.initialSlider.valueChanged.connect(lambda: self.ld.initialBox.setValue(self.ld.initialSlider.value()/1000))
    self.ld.initialBox.valueChanged.connect(lambda: self.ld.initialSlider.setValue(int(self.ld.initialBox.value()*1000)))
    self.ld.finalSlider.valueChanged.connect(lambda: self.ld.finalBox.setValue(self.ld.finalSlider.value()/1000))
    self.ld.finalBox.valueChanged.connect(lambda: self.ld.finalSlider.setValue(int(self.ld.finalBox.value()*1000)))
    lists=list(self.df[(self.df['Flag']==True)&(self.df['Class']=='segment')]['Name'])
    self.ld.parentSegment.addItems(list(reversed(lists))) #############
    def setter():
        parentSegment = self.ld.parentSegment.currentText()
        ps=self.df[(self.df['Name']==parentSegment)]['Robject'].iloc[0]
        p1=ps['P1'];p3=ps['P3']
        # a=array(rangee(p1,p3)
        
        ranges=int(norm(p1-p3)*1000)
        self.ld.initialSlider.setMaximum(ranges)
        self.ld.initialBox.setMaximum(ranges/1000)
        self.ld.finalSlider.setMaximum(ranges)
        self.ld.finalBox.setMaximum(ranges/1000)
        self.ld.finalSlider.setValue(ranges)
        self.ld.finalBox.setValue(ranges/1000)
    self.ld.parentSegment.currentIndexChanged.connect(setter)

    self.loadtypes={'Moment':-2,'Point Load':-1,'UDL':0,'UVL':1,'Poly Load':2}
    self.ld.degree.setValue(self.loadtypes[self.loadtype])
    self.lD.setWindowTitle(self.loadtype+' Detials')
    px = MainWindow.geometry().x()
    py = MainWindow.geometry().y()
    dw = self.lD.width()
    dh = self.lD.height()   
    self.lD.setGeometry( px, py+120, dw, dh )    

    self.ld.parentSegment.setItemDelegate(QtWidgets.QStyledItemDelegate())

    self.lD.show()
    self.ld.p1x.setFocus()
    self.ld.buttonBox.accepted.connect(lambda:loadobjectMaker(self))
    # except IndexError:
    #     self.statusbar.showMessage("Enter a segment first", 3000)
