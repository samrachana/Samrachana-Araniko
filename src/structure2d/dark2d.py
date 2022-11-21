#import qdarkstyle
from PySide2.QtGui import QBrush, QColor
from PySide2.QtCore import Qt
from structure2d.drawLoads import editPeakAndNormal
from getCss import css
def darkMode(self,app=None):
    if self.actionDark_Mode.isChecked()==True:
        self.darkMode=True
        brush = QBrush(QColor(40,40,40))
        self.cursorPath='./ico/cursors/dark/'
        # app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.app.setStyleSheet(css('dark',self.app.primaryScreen().availableGeometry().height()))
        self.scene.setBackgroundBrush(brush)      
        self.bgColor=(40,40,40)
        # self.bgColor= (35, 35, 36,255)
        self.segmentColor= (244, 155, 247,255)
        self.loadColor= (245, 171, 171,255)
        self.afdColor= (163, 163, 245,255)
        self.sfdColor= (196, 245, 196,255)
        self.bmdColor= (245, 185, 185,255)
        self.translationColor= (168, 247, 168,255)
        self.rotationColor= (189, 241, 189,255)
        self.rollerColor= (231, 231, 170,255)
        self.hingeColor= (173, 233, 233,255)
        self.fixedColor= (241, 195, 241,255)
        self.internalHingeColor= (211, 250, 211,255)
        self.customSupportColor= (191, 245, 216,255)


    else:
        self.darkMode=False
        brush = QBrush(Qt.white)
        self.cursorPath='./ico/cursors/light/'
        # with open('style.css') as f:
        #     app.setStyleSheet(f.read())  
        self.app.setStyleSheet(css('light',self.app.primaryScreen().availableGeometry().height()))
        self.scene.setBackgroundBrush(brush)  
        self.bgColor=(250,250,250)
        self.segmentColor = (202, 1, 209, 255)
        self.loadColor = (200, 0, 0, 255)
        
        self.afdColor = (0, 0, 250, 255)
        self.sfdColor = (0, 250, 0, 255)
        self.bmdColor = (250, 0, 0, 255)
        self.translationColor = (0, 200, 0, 255)
        self.rotationColor = (0, 200, 0, 255)
        
        self.rollerColor = (200, 200, 0, 255)
        self.hingeColor = (0, 200, 200, 255)
        self.fixedColor = (120, 0, 120, 255)
        self.internalHingeColor = (100, 200, 100, 255)
        self.customSupportColor = (10, 200, 100, 255)
    editPeakAndNormal(self)
