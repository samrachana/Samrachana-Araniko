from PySide2 import QtWidgets
from UI.unitWindow import Ui_Dialog



def inputForce(self):
    self.units.SIforceMagnitude.clearFocus()
    self.units.SIforceMagnitude.setReadOnly(True)

    if self.edit:
        customUnit,ok=QtWidgets.QInputDialog().getText(self.uW,'Unit of Force','Custom unit name')
        if customUnit and ok:
            self.edit=False
            self.SIunitsOfForce[customUnit]=float(self.units.SIforceMagnitude.text())
            self.units.SIunitOfForce.addItem(customUnit)
            self.units.SIunitOfForce.setCurrentText(customUnit)
            self.force=float(self.units.SIforceMagnitude.text())

def changeForce(self):
    if self.units.SIunitOfForce.currentText()=='Custom':
        self.units.SIforceMagnitude.setReadOnly(False)
        self.units.SIforceMagnitude.setFocus()
        self.edit=True
        self.units.SIforceMagnitude.returnPressed.connect(lambda:inputForce(self))
    else:
        text=self.units.SIunitOfForce.currentText()
        self.edit=False
        self.units.SIforceMagnitude.setText(str(self.SIunitsOfForce[text]))

def inputLength(self):
    self.units.SIlengthMagnitude.clearFocus()
    self.units.SIlengthMagnitude.setReadOnly(True)

    if self.edit:
        customUnit,ok=QtWidgets.QInputDialog().getText(self.uW,'Unit of Length','Custom unit name')
        if customUnit and ok:
            self.edit=False
            self.SIunitsOfLength[customUnit]=float(self.units.SIlengthMagnitude.text())
            self.units.SIunitOfLength.addItem(customUnit)
            self.units.SIunitOfLength.setCurrentText(customUnit)
            self.length=float(self.units.SIlengthMagnitude.text())

def changeLength(self):
    if self.units.SIunitOfLength.currentText()=='Custom':
        self.units.SIlengthMagnitude.setReadOnly(False)
        self.units.SIlengthMagnitude.setFocus()
        self.edit=True
        self.units.SIlengthMagnitude.returnPressed.connect(lambda:inputLength(self))
    else:
        self.edit=False
        text=self.units.SIunitOfLength.currentText()
        self.units.SIlengthMagnitude.setText(str(self.SIunitsOfLength[text]))

def changeScale(self):
    if self.units.SIunitOfScale.currentText()=='Custom':
        customUnit,ok=QtWidgets.QInputDialog().getText(self.uW,'Unit of Scale','Custom Scale')
        if customUnit and ok:
            self.units.SIunitOfScale.addItem(customUnit)
            self.SIscales.append(customUnit)
            self.units.SIunitOfScale.setCurrentText(customUnit)
            try:
                self.scale=float(self.units.SIunitOfScale.currentText().split(":")[1])
            except:
                self.scale=float(self.units.SIunitOfScale.currentText())

    else:
        self.scale=float(self.units.SIunitOfScale.currentText().split(":")[1])
def inputForceENG(self):
    self.units.ENGforceMagnitude.clearFocus()
    self.units.ENGforceMagnitude.setReadOnly(True)

    if self.edit:
        customUnit,ok=QtWidgets.QInputDialog().getText(self.uW,'Unit of Force','Custom unit name')
        if customUnit and ok:
            self.edit=False
            self.ENGunitsOfForce[customUnit]=float(self.units.ENGforceMagnitude.text())
            self.units.ENGunitOfForce.addItem(customUnit)
            self.units.ENGunitOfForce.setCurrentText(customUnit)
            self.force=float(self.units.ENGforceMagnitude.text())

def changeForceENG(self):
    if self.units.ENGunitOfForce.currentText()=='Custom':
        self.units.ENGforceMagnitude.setReadOnly(False)
        self.units.ENGforceMagnitude.setFocus()
        self.edit=True
        self.units.ENGforceMagnitude.returnPressed.connect(lambda:inputForceENG(self))
    else:
        text=self.units.ENGunitOfForce.currentText()
        self.edit=False
        self.units.ENGforceMagnitude.setText(str(self.ENGunitsOfForce[text]))

def inputLengthENG(self):
    self.units.ENGlengthMagnitude.clearFocus()
    self.units.ENGlengthMagnitude.setReadOnly(True)

    if self.edit:
        customUnit,ok=QtWidgets.QInputDialog().getText(self.uW,'Unit of Length','Custom unit name')
        if customUnit and ok:
            self.edit=False
            self.ENGunitsOfLength[customUnit]=float(self.units.ENGlengthMagnitude.text())
            self.units.ENGunitOfLength.addItem(customUnit)
            self.units.ENGunitOfLength.setCurrentText(customUnit)
            self.length=float(self.units.ENGlengthMagnitude.text())

def changeLengthENG(self):
    if self.units.ENGunitOfLength.currentText()=='Custom':
        self.units.ENGlengthMagnitude.setReadOnly(False)
        self.units.ENGlengthMagnitude.setFocus()
        self.edit=True
        self.units.ENGlengthMagnitude.returnPressed.connect(lambda:inputLengthENG(self))
    else:
        self.edit=False
        text=self.units.ENGunitOfLength.currentText()
        self.units.ENGlengthMagnitude.setText(str(self.ENGunitsOfLength[text]))

def changeScaleENG(self):
    if self.units.ENGunitOfScale.currentText()=='Custom':
        customUnit,ok=QtWidgets.QInputDialog().getText(self.uW,'Unit of Scale','Custom Scale')
        if customUnit and ok:
            self.units.ENGunitOfScale.addItem(customUnit)
            self.ENGscales.append(customUnit)
            self.units.ENGunitOfScale.setCurrentText(customUnit)
            self.scale=float(self.units.ENGunitOfScale.currentText().split(":")[1])
    else:
        self.scale=float(self.units.ENGunitOfScale.currentText().split(":")[1])
        
def changePrecison(self):
    self.precison=self.units.SIprecison.value()
def changePrecisonENG(self):
    self.precison=self.units.ENGprecison.value()
def unitWindow(self,MainWindow):
    self.uW=QtWidgets.QDialog(parent=MainWindow)
    self.units=Ui_Dialog()
    self.units.setupUi(self.uW)
    self.units.save.setAutoDefault(False)
    self.units.cancel.setAutoDefault(False)
    # self.units.SIunitOfScale.addItems(self.SIscales)
    self.units.SIunitOfForce.addItems(self.SIunitsOfForce.keys())
    self.units.SIunitOfLength.addItems(self.SIunitsOfLength.keys())

    self.units.SIunitOfForce.currentIndexChanged.connect(lambda:changeForce(self))
    self.units.SIunitOfLength.currentIndexChanged.connect(lambda:changeLength(self))
    # self.units.SIunitOfScale.currentIndexChanged.connect(lambda:changeScale(self))
    # self.units.SIprecison.valueChanged.connect(lambda:changePrecison(self))         

    # self.units.ENGunitOfScale.addItems(self.ENGscales)
    self.units.ENGunitOfForce.addItems(self.ENGunitsOfForce.keys())
    self.units.ENGunitOfLength.addItems(self.ENGunitsOfLength.keys())    

    self.units.ENGunitOfForce.currentIndexChanged.connect(lambda:changeForceENG(self))
    self.units.ENGunitOfLength.currentIndexChanged.connect(lambda:changeLengthENG(self))
    # self.units.ENGunitOfScale.currentIndexChanged.connect(lambda:changeScaleENG(self))
    # self.units.ENGprecison.valueChanged.connect(lambda:changePrecison(self))
    
    def save():
        self.setunits=True

        if self.units.SIunits.isChecked()==True:
            self.currentUnit='SI'
            # self.precison=self.units.SIprecison.value()
            # self.scale=float(self.units.SIunitOfScale.currentText().split(":")[1])
            self.length=float(self.units.SIlengthMagnitude.text())
            self.force=float(self.units.SIforceMagnitude.text())
            self.length=round(self.length,self.precison)
            self.force=round(self.force,self.precison)            
        else:
            self.currentUnit="ENG"
            # self.precison=self.units.ENGprecison.value()
            # self.scale=float(self.units.ENGunitOfScale.currentText().split(":")[1])
            self.length=float(self.units.ENGlengthMagnitude.text())
            self.force=float(self.units.ENGforceMagnitude.text())
        self.length=round(self.length,self.precison)
        self.force=round(self.force,self.precison) 
        units=f'''Length : {self.length}m\nForce   : {self.force}N''' if self.currentUnit=='SI' else f'''Length : {self.length}ft\nForce   : {self.force}pdl'''
        self.currentUnitLabel.setText('Units : '+self.currentUnit)
        self.allCurrentUnits.setText(units)
        self.uW.close()

    # self.units.buttonGroup.buttonToggled.connect(toggle)
    self.units.save.clicked.connect(save)
    # self.units.SIunits.setChecked(True)    

    if self.currentUnit=='SI':
        self.units.SIunits.setChecked(True)
        if self.setunits:   
            self.units.SIunitOfForce.setCurrentText(str(list(self.SIunitsOfForce.keys())[list(self.SIunitsOfForce.values()).index(self.force)]))
            self.units.SIunitOfLength.setCurrentText(str(list(self.SIunitsOfLength.keys())[list(self.SIunitsOfLength.values()).index(self.length)]))
            # self.units.SIunitOfScale.setCurrentText('1:'+str(self.scale))
            # self.units.SIprecison.setValue(self.precison)
    else:
        self.units.ENGunits.setChecked(True)    
        if self.setunits:   
            self.units.ENGunitOfForce.setCurrentText(str(list(self.ENGunitsOfForce.keys())[list(self.ENGunitsOfForce.values()).index(self.force)]))
            self.units.ENGunitOfLength.setCurrentText(str(list(self.ENGunitsOfLength.keys())[list(self.ENGunitsOfLength.values()).index(self.length)]))
            # self.units.ENGunitOfScale.setCurrentText('1:'+str(self.scale))
            # self.units.ENGprecison.setValue(self.precison)

    self.units.SIunitOfLength.setItemDelegate(QtWidgets.QStyledItemDelegate())    
    # self.units.SIunitOfScale.setItemDelegate(QtWidgets.QStyledItemDelegate())    
    self.units.SIunitOfForce.setItemDelegate(QtWidgets.QStyledItemDelegate())        

    self.units.ENGunitOfLength.setItemDelegate(QtWidgets.QStyledItemDelegate())    
    # self.units.ENGunitOfScale.setItemDelegate(QtWidgets.QStyledItemDelegate())    
    self.units.ENGunitOfForce.setItemDelegate(QtWidgets.QStyledItemDelegate())        
    def changeTemperature():
        if self.units.celsius.isChecked():
            self.temperature='C'
        else:
            self.temperature='F'    
    self.units.temperature.buttonClicked.connect(changeTemperature)
    self.uW.setWindowTitle('Units')

    self.uW.show()









# def unitWindow(self,MainWindow):
#     self.uW=QtWidgets.QDialog(parent=MainWindow)
#     self.uW.setWindowTitle('Units')
#     gridLayout = QtWidgets.QGridLayout(self.uW)

#     self.unitOfForce=QtWidgets.QComboBox()
#     self.unitOfForce.addItems(self.SIunitsOfForce.keys())
#     self.unitOfForce.setItemDelegate(QtWidgets.QStyledItemDelegate())
    
#     self.unitOfForce.currentIndexChanged.connect(lambda:changeForce(self))
    

#     self.unitOfLength=QtWidgets.QComboBox()
#     self.unitOfLength.addItems(self.SIunitsOfLength.keys())
#     self.unitOfLength.setItemDelegate(QtWidgets.QStyledItemDelegate())

    
#     self.unitOfScale=QtWidgets.QLineEdit()
#     self.unitOfPrecison=QtWidgets.QSpinBox()
 
#     label1=QtWidgets.QLabel()
#     label1.setText('Force')
#     label2=QtWidgets.QLabel()
#     label2.setText('Length')
#     label3=QtWidgets.QLabel()
#     label3.setText('Scale')
#     label4=QtWidgets.QLabel()
#     label4.setText('Precison')
 
#     gridLayout.addWidget(label1,0,0,1,1)
#     gridLayout.addWidget(self.unitOfForce,0,1,1,2)

#     gridLayout.addWidget(label2,1,0,2,1)
#     gridLayout.addWidget(self.unitOfLength,1,1,2,2)

#     gridLayout.addWidget(label3,2,0,3,1)
#     gridLayout.addWidget(self.unitOfScale,2,1,3,2)

#     gridLayout.addWidget(label4,3,0,4,1) 
#     gridLayout.addWidget(self.unitOfPrecison,3,1,4,2)
    
#     self.uW.resize(150,200)    
#     self.uW.show()