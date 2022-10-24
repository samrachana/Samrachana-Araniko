from PySide2 import QtWidgets
from PySide2.QtGui import QColor, QBrush
def setColorsandWidth(self):
    self.bgColor = self.pd.bgColor.color(mode='byte')
    self.segmentColor = self.pd.segmentColor.color(mode='byte')
    self.loadColor = self.pd.loadColor.color(mode='byte')
    self.afdColor = self.pd.afdColor.color(mode='byte')
    self.sfdColor = self.pd.sfdColor.color(mode='byte')
    self.bmdColor = self.pd.bmdColor.color(mode='byte')
    self.translationColor = self.pd.translationColor.color(mode='byte')
    self.rotationColor = self.pd.rotationColor.color(mode='byte')
    self.rollerColor = self.pd.rollerColor.color(mode='byte')
    self.hingeColor = self.pd.hingeColor.color(mode='byte')
    self.fixedColor = self.pd.fixedColor.color(mode='byte')
    self.internalHingeColor = self.pd.internalHingeColor.color(mode='byte')
    self.segmentWidth=self.pd.segementWidth.value()
    self.loadWidth = self.pd.loadWidth.value()
    self.scene.setBackgroundBrush(QBrush(QColor(*self.bgColor)))
    self.supportColors = {"Roller": self.rollerColor, 
    "Hinge": self.hingeColor, 
    "Fixed": self.fixedColor,
    "Internal Hinge":self.internalHingeColor,
    'custom Support':self.customSupportColor}


def preferenceDialog(self,MainWindow):
    from UI.preferenceDialog import Ui_Dialog as PreferenceUi_Dialog
    self.pD = QtWidgets.QDialog(parent=MainWindow)
    self.pd = PreferenceUi_Dialog()
    self.pd.setupUi(self.pD)   

    self.pd.bgColor.setColor(color=self.bgColor)
    self.pd.segmentColor.setColor(color=self.segmentColor)
    self.pd.loadColor.setColor(color=self.loadColor)
    self.pd.afdColor.setColor(color=self.afdColor)
    self.pd.sfdColor.setColor(color=self.sfdColor)
    self.pd.bmdColor.setColor(color=self.bmdColor)
    self.pd.translationColor.setColor(color=self.translationColor)
    self.pd.rotationColor.setColor(color=self.rotationColor)
    self.pd.rollerColor.setColor(color=self.rollerColor)
    self.pd.hingeColor.setColor(color=self.hingeColor)
    self.pd.fixedColor.setColor(color=self.fixedColor)
    self.pd.internalHingeColor.setColor(color=self.internalHingeColor)
    self.pD.show()

    self.pd.buttonBox.accepted.connect(lambda:setColorsandWidth(self))

    