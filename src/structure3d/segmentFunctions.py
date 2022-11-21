from UI.segmentDialog import Ui_Dialog as SegmentUi_Dialog
from sdPy.segmentMethods import segPlotData, actionData
from PySide2 import QtWidgets
from sdPy.functionDefinitions import make
from structure3d.plot import Plot
from PySide2.QtCore import Qt
from numpy import append
from sdPy.extensions import convert


def segmentobjectMaker(self):
    try:
        name = self.sd.name.text()
        if name == "":
            segmentName = "Segment-" + str(self.segmentNumber)+' ('+self.segtype+') '
        else:
            segmentName = name
        name = segmentName
        p1 = [self.sd.p1x.text(), self.sd.p1y.text(), self.sd.p1z.text()]
        p2 = [self.sd.p2x.text(), self.sd.p2y.text(), self.sd.p2z.text()]
        p3 = [self.sd.p3x.text(), self.sd.p3y.text(), self.sd.p3z.text()]
        ym = self.sd.youngsModulus.text()
        sm = self.sd.shearModulus.text()
        area = self.sd.area.text()
        ixx = self.sd.ixx.text()
        av = self.sd.axisVector.text()
        iyy = self.sd.iyy.text()
        tc = self.sd.torsionConstant.text()
        k = self.sd.shapeFactor.text()
        
        import warnings
        with warnings.catch_warnings(record=True) as w:
            Rsegment=make([self.segtype, p1, p2, p3, ym, sm, area, ixx, iyy,tc,k,av,1,1])
            sdata=segPlotData(Rsegment['type'],Rsegment['P1'],Rsegment['P3'],Rsegment['axisVector'],self.scale ,Rsegment['P2'])
            if len(w):
                self.statusbar.showMessage(str(w[0].message),2000)
        Plot.plott(Plot,sdata, self.graphWidget, self.segmentColor,self.segmentWidth)      
        
        item=QtWidgets.QTreeWidgetItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.df.loc[len(self.df)]=[name,'segment',Rsegment,self.graphWidget.items[-1],item,True]
        self.ot.segment.addChild(item)   
        item.setText(0,name)
        [self.ot.segment.child(self.segmentNumber-1).setData(i+1,2,str(list(Rsegment.values())[i+1])) for i in range(11)]           
        self.ot.segment.child(self.segmentNumber-1).setData(12,2,Rsegment['type'])

        # self.df.loc[len(self.df)]=[name,'segment',Rsegment,self.graphWidget.items[-1],item,True]
        # item=QtWidgets.QTreeWidgetItem()
        # item.setText(0,name)
        # self.ot.segment.addChild(item)
        # item=QtWidgets.QTreeWidgetItem()
        # text='P1='+str(p1)+' ,P3='+str(p2)+' ,P2='+str(p3)
        # item.setText(0,text)
        # self.ot.segment.child(self.segmentNumber-1).addChild(item) 
        self.segmentNumber += 1
        self.history=append(self.history,len(self.df)-1)
        self.historystatus=True
    except Exception as e:
        print(e)
        self.statusbar.showMessage(str(e),3000)   

def segmentDialog(self,types,MainWindow):
    self.segtype=types
    self.sD = QtWidgets.QDialog(parent=MainWindow)
    self.sd = SegmentUi_Dialog()
    self.sd.setupUi(self.sD)
    self.sD.setWindowTitle(self.segtype.capitalize()+' Segment Detials')
    px = MainWindow.geometry().x()
    py = MainWindow.geometry().y()
    dw = self.sD.width()
    dh = self.sD.height()   
    self.sD.setGeometry( px, py+100, dw, dh )
    self.sD.show()
    self.sd.p1x.setFocus()


    self.sd.segmentSection.addItems(list(self.section['name']))
    self.sd.segmentMaterial.setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.sd.segmentSection.setItemDelegate(QtWidgets.QStyledItemDelegate())
    def section():
        section = self.sd.segmentSection.currentIndex()
        if self.currentUnit=='SI':
            # convert(self.material.iloc[material,2],[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])
            self.sd.area.setText(str(convert(float(self.section.iloc[section,2]),[0,2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.ixx.setText(str(convert(float(self.section.iloc[section,2]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.iyy.setText(str(convert(float(self.section.iloc[section,3]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.torsionConstant.setText(str(convert(float(self.section.iloc[section,4]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
        else:
            self.sd.area.setText(str(convert(float(self.section.iloc[section,2]),[0,2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.ixx.setText(str(convert(float(self.section.iloc[section,2]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.iyy.setText(str(convert(float(self.section.iloc[section,3]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.torsionConstant.setText(str(convert(float(self.section.iloc[section,4]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
        self.sd.shapeFactor.setText(str(self.section.iloc[section,5]))
        self.current_section=section
    def material():
        material=self.sd.segmentMaterial.currentIndex()
        if self.currentUnit=="SI":
            self.sd.youngsModulus.setText(str(convert(float(self.material.iloc[material,2]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.shearModulus.setText(str(convert(float(self.material.iloc[material,3]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
        else:
            self.sd.youngsModulus.setText(str(convert(float(self.material.iloc[material,2]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.sd.shearModulus.setText(str(convert(float(self.material.iloc[material,3]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
        self.current_material = material
    self.sd.segmentMaterial.currentIndexChanged.connect(material)
    self.sd.segmentSection.currentIndexChanged.connect(section)

    self.sd.segmentMaterial.setCurrentIndex(self.current_material)
    self.sd.segmentSection.setCurrentIndex(self.current_section)
    
    self.sd.buttonBox.accepted.connect(lambda:segmentobjectMaker(self))
