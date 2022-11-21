from PySide2.QtWidgets import QMainWindow,QStyledItemDelegate
from UI.generateWindow import Ui_MainWindow
from sdPy.extensions import generate3d,generate2d
from PySide2 import QtWidgets
from sdPy.extensions import convert
from numpy import array
from structure3d.fileOperations import openFile

def callGenerate(self,app=None):
    beamYm =   self.generate.beamYoungModulus.text()
    beamSm =   self.generate.beamShearModulus.text()
    beamArea = self.generate.beamArea.text()
    beamIyy =  self.generate.beamIyy.text()
    beamIzz =  self.generate.beamIzz.text()
    beamTc =   self.generate.beamTorsionConstant.text()
    beamK =    self.generate.beamShapeFactor.text()
    beamProp=array([beamYm,beamSm,beamArea,beamIyy,beamIzz,beamTc,beamK],dtype='float')

    columnYm =   self.generate.columnYoungModulus.text()
    columnSm =   self.generate.columnShearModulus.text()
    columnArea = self.generate.columnArea.text()
    columnIyy =  self.generate.columnIyy.text()
    columnIzz =  self.generate.columnIzz.text()
    columnTc =   self.generate.columnTorsionConstant.text()
    columnK =    self.generate.columnShapeFactor.text()
    columnProp=array([columnYm,columnSm,columnArea,columnIyy,columnIzz,columnTc,columnK],dtype='float')

    lengthOfBuilding=self.generate.buildingLength.value()
    breadthOfBuilding = self.generate.buildingBreadth.value()
    heightOfBuilding = self.generate.buildingHeight.value()
    buildingDimension=array([lengthOfBuilding,breadthOfBuilding,heightOfBuilding],dtype='int')
    frameDimension=array([lengthOfBuilding,heightOfBuilding],dtype='int')
    
    lengthOfRoom=self.generate.roomLength.value()
    breadthOfRoom = self.generate.roomBreadth.value()
    heightOfRoom = self.generate.roomHeight.value()
    RoomDimension=array([lengthOfRoom,breadthOfRoom,heightOfRoom],dtype='float')
    elementDimension=array([lengthOfRoom,heightOfRoom],dtype='float')
    support=self.generate.addSupport.isChecked()
    add=self.generate.addToBuilding.isChecked()
    origin = array(self.generate.origin.text()[1:-1].split(','),dtype='float')
    name=self.generate.buildingName.text()
    if self.generate.building.isChecked()==True:
        generate3d(buildingDimension = buildingDimension,
                roomDimension = RoomDimension,
                XbeamProp = beamProp,
                YbeamProp = beamProp,
                columnProp = columnProp,
                add = add,
                origin = origin,
                support = support,
                name = name)
        name=name+str(buildingDimension) + '.csv'        
    else:
        generate2d(frameDimension = frameDimension,
                elementDimension = elementDimension,
                beamProp = beamProp,
                columnProp = columnProp,
                add = add,
                origin = origin,
                support = support,
                name = name)
        name=name+str(frameDimension) + '.csv'        
    if app:
        openFile(self,app,name)


def generateBuilding3d(self,MainWindow,app):
    self.sD = QtWidgets.QMainWindow(parent=MainWindow)
    self.generate = Ui_MainWindow()
    self.generate.setupUi(self.sD)

    self.generate.columnSection.addItems(list(self.section['name']))
    self.generate.columnMaterial.addItems(list(self.material['name']))

    self.generate.columnMaterial.setItemDelegate(QStyledItemDelegate())
    self.generate.columnSection.setItemDelegate(QStyledItemDelegate())
    def section():
        section = self.generate.columnSection.currentIndex()
        if self.currentUnit=='SI':
            # convert(self.material.iloc[material,2],[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])
            self.generate.columnArea.setText(str(convert(float(self.section.iloc[section,2]),[0,2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnIyy.setText(str(convert(float(self.section.iloc[section,2]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnIzz.setText(str(convert(float(self.section.iloc[section,3]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnTorsionConstant.setText(str(convert(float(self.section.iloc[section,4]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
        else:
            self.generate.columnArea.setText(str(convert(float(self.section.iloc[section,2]),[0,2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnIyy.setText(str(convert(float(self.section.iloc[section,2]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnIzz.setText(str(convert(float(self.section.iloc[section,3]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnTorsionConstant.setText(str(convert(float(self.section.iloc[section,4]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
        self.generate.columnShapeFactor.setText(str(self.section.iloc[section,5]))
        self.current_section=section
    def material():
        material=self.generate.columnMaterial.currentIndex()
        if self.currentUnit=="SI":
            self.generate.columnYoungModulus.setText(str(convert(float(self.material.iloc[material,2]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnShearModulus.setText(str(convert(float(self.material.iloc[material,3]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
        else:
            self.generate.columnYoungModulus.setText(str(convert(float(self.material.iloc[material,2]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.columnShearModulus.setText(str(convert(float(self.material.iloc[material,3]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
        self.current_material = material
    self.generate.columnMaterial.currentIndexChanged.connect(material)
    self.generate.columnSection.currentIndexChanged.connect(section)
    self.generate.columnMaterial.setCurrentIndex(self.current_material)
    self.generate.columnSection.setCurrentIndex(self.current_section)




    self.generate.beamSection.addItems(list(self.section['name']))
    self.generate.beamMaterial.addItems(list(self.material['name']))

    self.generate.beamMaterial.setItemDelegate(QStyledItemDelegate())
    self.generate.beamSection.setItemDelegate(QStyledItemDelegate())
    def beamsection():
        section = self.generate.beamSection.currentIndex()
        if self.currentUnit=='SI':
            # convert(self.material.iloc[material,2],[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])
            self.generate.beamArea.setText(str(convert(float(self.section.iloc[section,2]),[0,2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamIyy.setText(str(convert(float(self.section.iloc[section,2]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamIzz.setText(str(convert(float(self.section.iloc[section,3]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamTorsionConstant.setText(str(convert(float(self.section.iloc[section,4]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
        else:
            self.generate.beamArea.setText(str(convert(float(self.section.iloc[section,2]),[0,2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamIyy.setText(str(convert(float(self.section.iloc[section,2]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamIzz.setText(str(convert(float(self.section.iloc[section,3]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamTorsionConstant.setText(str(convert(float(self.section.iloc[section,4]),[0,4],['SI',1,1],[self.currentUnit,self.force,self.length])))
        self.generate.beamShapeFactor.setText(str(self.section.iloc[section,5]))
        self.current_section=section
    def beammaterial():
        material=self.generate.beamMaterial.currentIndex()
        if self.currentUnit=="SI":
            self.generate.beamYoungModulus.setText(str(convert(float(self.material.iloc[material,2]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamShearModulus.setText(str(convert(float(self.material.iloc[material,3]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
        else:
            self.generate.beamYoungModulus.setText(str(convert(float(self.material.iloc[material,2]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
            self.generate.beamShearModulus.setText(str(convert(float(self.material.iloc[material,3]),[1,-2],['SI',1,1],[self.currentUnit,self.force,self.length])))
        self.current_material = material
    self.generate.beamMaterial.currentIndexChanged.connect(beammaterial)
    self.generate.beamSection.currentIndexChanged.connect(beamsection)
    self.generate.beamMaterial.setCurrentIndex(self.current_material)
    self.generate.beamSection.setCurrentIndex(self.current_section)




    self.generate.generate.clicked.connect(lambda: callGenerate(self))
    self.generate.generateAndOpen.clicked.connect(lambda: callGenerate(self,app))






    self.sD.show()
