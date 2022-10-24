from PySide2.QtWidgets import QDialog
from UI.tweaks import Ui_Dialog 
from math import log10

def defaultTweaks(self):    
    self.NoOfPointsInResponseAndAction=20
    self.NoOfPointsInVector=20
    self.NoOfPointsInMotion=20
    self.NoOfPointsInCurvedSegments=100
    self.loadLogScale = True
    self.sectionDesignerAccuracy = 0.9995
    self.structuralAnalysisAccuracy = 0.9995
    # self.ZoomFactorAction=10**0
    # self.ZoomFactorResponse=10**0
    # self.ZoomFactorMotion=10**0
    self.interpolationMode='spline'
def tweaks(self):
    self.tweakDialog=QDialog(self.MainWindow)
    self.tweaks=Ui_Dialog()
    self.tweaks.setupUi(self.tweakDialog)

    self.tweaks.NoOfPointsInResponseAndAction.setValue(self.NoOfPointsInResponseAndAction)
    self.tweaks.NoOfPointsInVector.setValue(self.NoOfPointsInVector )
    self.tweaks.NoOfPointsInMotion.setValue(self.NoOfPointsInMotion )
    self.tweaks.NoOfPointsInCurvedSegments.setValue(self.NoOfPointsInCurvedSegments )
    self.tweaks.sectionDesignerAccuracy.setValue(self.sectionDesignerAccuracy*100)
    self.tweaks.structureAnalysisAccuracy.setValue(self.structuralAnalysisAccuracy*100)
    # self.tweaks.logScale.setChecked(self.loadLogScale)
    # self.tweaks.ZoomFactorAction.setValue(int(log10(self.ZoomFactorAction)))
    # self.tweaks.ZoomFactorResponse.setValue(int(log10(self.ZoomFactorResponse)))
    # self.tweaks.ZoomFactorMotion.setValue(int(log10(self.ZoomFactorMotion)))


    def setValues():
        self.NoOfPointsInResponseAndAction=self.tweaks.NoOfPointsInResponseAndAction.value()
        self.NoOfPointsInVector = self.tweaks.NoOfPointsInVector.value()
        self.NoOfPointsInMotion = self.tweaks.NoOfPointsInMotion.value()
        self.NoOfPointsInCurvedSegments = self.tweaks.NoOfPointsInCurvedSegments.value()
        self.loadLogScale = self.tweaks.logScale.isChecked()
        self.sectionDesignerAccuracy = self.tweaks.sectionDesignerAccuracy.value()/100
        self.structureAnalysisAccuracy = self.tweaks.structuralAnalysisAccuracy.value()/100
        # self.ZoomFactorAction =   10**self.tweaks.ZoomFactorAction.value()
        # self.ZoomFactorResponse = 10**self.tweaks.ZoomFactorResponse.value()
        # self.ZoomFactorMotion =   10**self.tweaks.ZoomFactorMotion.value()

        self.interpolationMode = self.tweaks.interpolationMode.currentText()
    self.tweaks.buttonBox.accepted.connect(setValues)
    self.tweakDialog.show()

    # self.NoOfPointsInResponseAndAction
    # self.NoOfPointsInVector
    # self.NoOfPointsInMotion
    # self.NoOfPointsInCurvedSegments

    # self.ZoomFactorAction
    # self.ZoomFactorResponse
    # self.ZoomFactorMotion

    # self.interpolationMode