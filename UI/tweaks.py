# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tweaks.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(408, 360)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.logScale = QCheckBox(Dialog)
        self.logScale.setObjectName(u"logScale")
        self.logScale.setChecked(True)
        self.logScale.setTristate(False)

        self.gridLayout_2.addWidget(self.logScale, 2, 0, 1, 2)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.interpolationMode = QComboBox(Dialog)
        self.interpolationMode.addItem("")
        self.interpolationMode.addItem("")
        self.interpolationMode.addItem("")
        self.interpolationMode.setObjectName(u"interpolationMode")

        self.gridLayout_2.addWidget(self.interpolationMode, 3, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.sectionDesignerAccuracy = QDoubleSpinBox(self.groupBox)
        self.sectionDesignerAccuracy.setObjectName(u"sectionDesignerAccuracy")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionDesignerAccuracy.sizePolicy().hasHeightForWidth())
        self.sectionDesignerAccuracy.setSizePolicy(sizePolicy)
        self.sectionDesignerAccuracy.setDecimals(6)
        self.sectionDesignerAccuracy.setMinimum(90.000000000000000)
        self.sectionDesignerAccuracy.setMaximum(99.999999000000003)
        self.sectionDesignerAccuracy.setValue(99.950000000000003)

        self.gridLayout_3.addWidget(self.sectionDesignerAccuracy, 0, 1, 1, 1)

        self.structureAnalysisAccuracy = QDoubleSpinBox(self.groupBox)
        self.structureAnalysisAccuracy.setObjectName(u"structureAnalysisAccuracy")
        sizePolicy.setHeightForWidth(self.structureAnalysisAccuracy.sizePolicy().hasHeightForWidth())
        self.structureAnalysisAccuracy.setSizePolicy(sizePolicy)
        self.structureAnalysisAccuracy.setDecimals(6)
        self.structureAnalysisAccuracy.setMinimum(90.000000000000000)
        self.structureAnalysisAccuracy.setMaximum(99.999999000000003)
        self.structureAnalysisAccuracy.setValue(99.950000000000003)

        self.gridLayout_3.addWidget(self.structureAnalysisAccuracy, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.NoOfPointsInResponseAndAction = QSpinBox(self.groupBox_2)
        self.NoOfPointsInResponseAndAction.setObjectName(u"NoOfPointsInResponseAndAction")
        self.NoOfPointsInResponseAndAction.setMinimum(5)
        self.NoOfPointsInResponseAndAction.setMaximum(99)
        self.NoOfPointsInResponseAndAction.setValue(20)

        self.gridLayout.addWidget(self.NoOfPointsInResponseAndAction, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.NoOfPointsInVector = QSpinBox(self.groupBox_2)
        self.NoOfPointsInVector.setObjectName(u"NoOfPointsInVector")
        self.NoOfPointsInVector.setMinimum(5)
        self.NoOfPointsInVector.setValue(20)

        self.gridLayout.addWidget(self.NoOfPointsInVector, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.NoOfPointsInMotion = QSpinBox(self.groupBox_2)
        self.NoOfPointsInMotion.setObjectName(u"NoOfPointsInMotion")
        self.NoOfPointsInMotion.setMinimum(5)
        self.NoOfPointsInMotion.setValue(20)

        self.gridLayout.addWidget(self.NoOfPointsInMotion, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.NoOfPointsInCurvedSegments = QSpinBox(self.groupBox_2)
        self.NoOfPointsInCurvedSegments.setObjectName(u"NoOfPointsInCurvedSegments")
        self.NoOfPointsInCurvedSegments.setMinimum(10)
        self.NoOfPointsInCurvedSegments.setMaximum(500)
        self.NoOfPointsInCurvedSegments.setSingleStep(10)
        self.NoOfPointsInCurvedSegments.setValue(100)

        self.gridLayout.addWidget(self.NoOfPointsInCurvedSegments, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tweaks", None))
        self.logScale.setText(QCoreApplication.translate("Dialog", u"Use Logarthmic Scale to plot loads", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Interpolation mode in Simulation", None))
        self.interpolationMode.setItemText(0, QCoreApplication.translate("Dialog", u"Spline", None))
        self.interpolationMode.setItemText(1, QCoreApplication.translate("Dialog", u"Linear", None))
        self.interpolationMode.setItemText(2, QCoreApplication.translate("Dialog", u"Lagrange", None))

        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Accuracy in calculation of curves in ", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Structure Analysis", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Section Designer", None))
        self.sectionDesignerAccuracy.setSuffix(QCoreApplication.translate("Dialog", u"%", None))
        self.structureAnalysisAccuracy.setSuffix(QCoreApplication.translate("Dialog", u"%", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"No of points to consider in plotting", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Actions and Responses Diagram", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Vector Diagrams", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Motion Simulation", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Curved Segments", None))
    # retranslateUi

