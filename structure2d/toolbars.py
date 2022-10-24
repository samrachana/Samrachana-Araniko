from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QLabel, QWidget
from PySide2.QtCore import Qt


class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, arg__1=None, parent=None,ui=None):
        super().__init__(arg__1, parent)
        self.ui=ui
    def keyReleaseEvent(self, event):
        if  event.key()==QtCore.Qt.Key_Escape:
            self.ui.graphicsView.setFocus()
def defaultToolbar(self):
    pass



def toolbars(self):
    reg_ex = QtCore.QRegExp("-?[0-9]*\.?[0-9]*")
    self.floatValidator = QtGui.QRegExpValidator(reg_ex)

    self.MainWindow.addToolBarBreak(Qt.TopToolBarArea)
    self.propertiesBar = QtWidgets.QToolBar('Properties Bar',self.MainWindow)
    self.MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.propertiesBar)
    
    self.propertiesBar.addWidget(QLabel('Material '))
    self.materialChoices=QtWidgets.QComboBox()
    self.materialChoices.addItems(self.material['name'][1:])
    def changeMaterial():
        try:
            material=self.materialChoices.currentText()
            if material=='Custom':
                customUnit,ok=QtWidgets.QInputDialog().getText(QWidget(),'Enter Custom Material','Material Name,  Youngs Modulus,  Shear Molulus, Alpha, Density  ')
                if customUnit and ok:
                    print(customUnit)
                    name,ym,sm,alpha,density=customUnit.split(',')
                    if name in ['custom','Custom','']:
                        name = 'Unnamed'
                    self.material.loc[len(self.material)]=[len(self.material),name,float(ym),float(sm),float(alpha),float(density)]
                    self.materialChoices.addItem(name)
                    self.materialChoices.setCurrentText(name)
                else:
                    raise Exception    
            self.previousMaterialIndex=self.materialChoices.currentIndex()
            material=self.materialChoices.currentIndex()+1
            ym=self.material.iloc[material,2]
            sm=self.material.iloc[material,3]
            alpha=self.material.iloc[material,4]
            density=self.material.iloc[material,5]
            self.statusbar.showMessage(f'Youngs Modulus = {ym} , Shear Modulus = {sm},alpha = {alpha}, Density = {density}',5000)                
            self.previousMaterialIndex=self.materialChoices.currentIndex()

        except:
            self.materialChoices.setCurrentIndex(self.previousMaterialIndex)
            self.statusbar.showMessage('Please, Enter valid material',3000)
    self.materialChoices.activated.connect(changeMaterial)
    self.propertiesBar.addWidget(self.materialChoices)

    self.propertiesBar.addSeparator()
    self.propertiesBar.addWidget(QLabel('Section '))
    self.sectionChoices=QtWidgets.QComboBox()
    
    self.sectionChoices.addItems(self.section['name'][1:])
    def changeSection():
        try:
            section=self.sectionChoices.currentText()
            if section=='Custom':
                customUnit,ok=QtWidgets.QInputDialog().getText(QWidget(),'Enter Custom section','Section Name, Area, MOI,  ShapeFactor')
                if customUnit and ok:
                    name,A,I,Sf=customUnit.split(',')
                    if name in ['custom','Custom','']:
                        name = 'Unnamed'                    
                    self.section.loc[len(self.section)]=[len(self.section),name,float(A),float(I),1,1,float(Sf)]
                    self.sectionChoices.addItem(name)
                    self.sectionChoices.setCurrentText(name)
                else:
                    raise Exception
            section=self.sectionChoices.currentIndex()+1
            A=self.section.iloc[section,2]
            I=self.section.iloc[section,2]    
            Sf=self.section.iloc[section,5]    
            self.statusbar.showMessage(f'A = {A} , I = {I} , SF={Sf}',5000)
            self.previousSectionIndex=self.sectionChoices.currentIndex()

        except:
            self.sectionChoices.setCurrentIndex(self.previousSectionIndex)
            self.statusbar.showMessage('Please, Enter valid section',3000)            
    
    self.sectionChoices.activated.connect(changeSection)
    self.propertiesBar.addWidget(self.sectionChoices)

    self.propertiesBar.addSeparator()
    self.editX=LineEdit(ui=self)
    self.editX.setFixedWidth(100)
    self.editX.setValidator(self.floatValidator)
    self.editY=LineEdit(ui=self)
    self.editY.setFixedWidth(100)
    self.editY.setValidator(self.floatValidator)
    # hlayout=QtWidgets.QWidget()
    # label=QLabel('X')
    # label.setBuddy(self.editX)
    # hlayout.addWidget(label)
    # hlayout.addWidget(self.editX)
    # self.propertiesBar.addWidget(label)
    self.coordinateSystem = QtWidgets.QComboBox()
    self.coordinateSystem.addItems(['Cartesian','Polar'])

    self.coordinateMode = QtWidgets.QComboBox()
    self.coordinateMode.addItems(['Absolute','Relative'])

    self.propertiesBar.addWidget(QLabel('Coordinate System'))
    
    self.propertiesBar.addWidget(self.coordinateMode)
    self.propertiesBar.addWidget(self.coordinateSystem)    
    def changeMode(self):
        if self.coordinateSystem.currentText()=='Polar':
            self.labelX.setText(' r ')
            self.labelY.setText(' \u0398 ')
        else:
            self.labelX.setText(' X ')
            self.labelY.setText(' Y ')                
    self.coordinateSystem.currentIndexChanged.connect(lambda:changeMode(self))
    # self.coordinateSystem.currentIndexChanged.connect(lambda:changeMode(self))

    self.labelX=QLabel(' X ')
    self.labelY=QLabel(' Y ')
    self.propertiesBar.addWidget(self.labelX)
    self.propertiesBar.addWidget(self.editX)
    self.propertiesBar.addWidget(self.labelY)
    self.propertiesBar.addWidget(self.editY)
    self.propertiesBar.addSeparator()
    def assign(a):self.coordinateEdited=a
    self.coordinateEdited=None
    self.editX.textEdited.connect(lambda:assign('x'))
    self.editY.textEdited.connect(lambda:assign('y'))
    self.editX.returnPressed.connect(self.editPoints)
    self.editY.returnPressed.connect(self.editPoints)

    self.propertiesBar.addWidget(QLabel(' Scale '))
    self.editScale=QtWidgets.QLineEdit()
    
    self.editScale.setValidator(self.floatValidator)
    self.editScale.setFixedWidth(100)
    self.editScale.setText(str(self.scale))
    self.propertiesBar.addWidget(self.editScale)
    def scale():
        scale=float(self.editScale.text())
        if scale > 0:
            self.scale=scale
        else:
            self.scale=1
            self.editScale.setText(str(1))
        
        self.graphicsView.setFocus()

    self.editScale.editingFinished.connect(scale)    
    
    self.propertiesBar.addWidget(QLabel(' Precision '))
    self.editPrecison=QtWidgets.QLineEdit()
    reg_ex = QtCore.QRegExp("[0-9]{0,2}")
    validator = QtGui.QRegExpValidator(reg_ex)
    self.editPrecison.setValidator(validator)
    self.editPrecison.setFixedWidth(100)
    self.editPrecison.setText(str(self.precison))
    self.propertiesBar.addWidget(self.editPrecison)
    def precison():
        precison=int(self.editPrecison.text()) 
        self.precison=precison if precison<15 else 15
        self.editPrecison.setText(str(self.precison))
        self.graphicsView.setFocus()
    self.editPrecison.editingFinished.connect(precison)    



    self.actionPropertiesBar.toggled['bool'].connect(self.propertiesBar.setVisible)
    self.propertiesBar.visibilityChanged['bool'].connect(self.actionPropertiesBar.setChecked)
    self.propertiesBar.addSeparator()
    self.currentUnitLabel=QLabel('Units : '+self.currentUnit)
    self.propertiesBar.addWidget(self.currentUnitLabel)
    units=f'''Length : {self.length}m\nForce   : {self.force}N''' if self.currentUnit=='SI' else f'''Length : {self.length}ft\nForce   : {self.force}pdl'''
    self.allCurrentUnits =QLabel(units)
    self.propertiesBar.addWidget(self.allCurrentUnits)
    self.propertiesBar.addSeparator()
    self.propertiesBar.show()