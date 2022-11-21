from UI.supportDialog import SupportUi_Dialog
from sdPy.supportMethods import supportPlotData
from PySide2 import QtWidgets
from sdPy.functionDefinitions import make
from structure3d.plot import Plot
from PySide2.QtCore import Qt
from numpy import append
from numpy import array
def supportobjectMaker(self):
    try:            
        location = [self.spd.px.text(), self.spd.py.text(), self.spd.pz.text()]
        normal = [self.spd.nx.text(), self.spd.ny.text(), self.spd.nz.text()]
        settlement = [
            self.spd.dx.text(),
            self.spd.dy.text(),
            self.spd.dz.text(),
            self.spd.rx.text(),
            self.spd.ry.text(),
            self.spd.rz.text()
        ]
        types = self.spd.comboBox.currentText()
        supportName = "Support-" + str(self.supportNumber)+ ' ('+types+')'
        Rsupport = make([types, location,settlement,normal])
        Rsupportdata=supportPlotData(Rsupport['type'] , Rsupport['location'],self.scale,Rsupport['normal'])
        color = self.supportColors[types]
        Plot.plotsupport(Plot,array(Rsupportdata), self.graphWidget, color)
    
        item=QtWidgets.QTreeWidgetItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.df.loc[len(self.df)]=[supportName,'support',Rsupport,self.graphWidget.items[len(self.graphWidget.items)-1],item,True]
        self.ot.support.addChild(item)   
        item.setText(0,supportName)
        [self.ot.support.child(self.supportNumber-1).setData(i+1,2,str(list(Rsupport.values())[i])) for i in range(4)]           

        self.supportNumber+=1
        self.history=append(self.history,len(self.df)-1)
        self.historystatus=True     
    except Exception as e:
        self.statusbar.showMessage(str(e),2000)

def supportDialog(self, types,MainWindow):
    self.supporttype = types
    self.spD = QtWidgets.QDialog(parent=MainWindow)
    self.spd = SupportUi_Dialog()
    self.spd.setupUi(self.spD)
    self.spD.setWindowTitle(self.supporttype+' Support Detials')
    self.spd.comboBox.setCurrentText(self.supporttype)
    px = MainWindow.geometry().x()
    py = MainWindow.geometry().y()
    dw = self.spD.width()
    dh = self.spD.height()   
    self.spD.setGeometry( px, py+140, dw, dh )   
    delegate = QtWidgets.QStyledItemDelegate()
    self.spd.comboBox.setItemDelegate(delegate)             
    self.spD.show()
    self.spd.px.setFocus()
    self.spd.buttonBox.accepted.connect(lambda:supportobjectMaker(self))
