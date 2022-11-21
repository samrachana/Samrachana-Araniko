# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newUnitWindow.ui'
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
        Dialog.resize(370, 345)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ENGlengthMagnitude = QLineEdit(self.groupBox_2)
        self.ENGlengthMagnitude.setObjectName(u"ENGlengthMagnitude")
        self.ENGlengthMagnitude.setEnabled(False)
        self.ENGlengthMagnitude.setReadOnly(True)

        self.gridLayout_3.addWidget(self.ENGlengthMagnitude, 1, 3, 1, 2)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)

        self.ENGforceMagnitude = QLineEdit(self.groupBox_2)
        self.ENGforceMagnitude.setObjectName(u"ENGforceMagnitude")
        self.ENGforceMagnitude.setEnabled(False)
        self.ENGforceMagnitude.setReadOnly(True)
        self.ENGforceMagnitude.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.ENGforceMagnitude, 0, 3, 1, 2)

        self.ENGunitOfLength = QComboBox(self.groupBox_2)
        self.ENGunitOfLength.setObjectName(u"ENGunitOfLength")

        self.gridLayout_3.addWidget(self.ENGunitOfLength, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.forceSuffix_2 = QLabel(self.groupBox_2)
        self.forceSuffix_2.setObjectName(u"forceSuffix_2")

        self.gridLayout_3.addWidget(self.forceSuffix_2, 0, 5, 1, 1)

        self.lengthSuffix_2 = QLabel(self.groupBox_2)
        self.lengthSuffix_2.setObjectName(u"lengthSuffix_2")

        self.gridLayout_3.addWidget(self.lengthSuffix_2, 1, 5, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)

        self.ENGunitOfForce = QComboBox(self.groupBox_2)
        self.ENGunitOfForce.setObjectName(u"ENGunitOfForce")

        self.gridLayout_3.addWidget(self.ENGunitOfForce, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 4)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.SIunitOfForce = QComboBox(self.groupBox)
        self.SIunitOfForce.setObjectName(u"SIunitOfForce")

        self.gridLayout_2.addWidget(self.SIunitOfForce, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.SIforceMagnitude = QLineEdit(self.groupBox)
        self.SIforceMagnitude.setObjectName(u"SIforceMagnitude")
        self.SIforceMagnitude.setEnabled(True)
        self.SIforceMagnitude.setReadOnly(True)

        self.gridLayout_2.addWidget(self.SIforceMagnitude, 0, 3, 1, 2)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.forceSuffix = QLabel(self.groupBox)
        self.forceSuffix.setObjectName(u"forceSuffix")

        self.gridLayout_2.addWidget(self.forceSuffix, 0, 5, 1, 1)

        self.SIunitOfLength = QComboBox(self.groupBox)
        self.SIunitOfLength.setObjectName(u"SIunitOfLength")

        self.gridLayout_2.addWidget(self.SIunitOfLength, 1, 1, 1, 1)

        self.lengthSuffix = QLabel(self.groupBox)
        self.lengthSuffix.setObjectName(u"lengthSuffix")

        self.gridLayout_2.addWidget(self.lengthSuffix, 1, 5, 1, 1)

        self.SIlengthMagnitude = QLineEdit(self.groupBox)
        self.SIlengthMagnitude.setObjectName(u"SIlengthMagnitude")
        self.SIlengthMagnitude.setEnabled(True)
        self.SIlengthMagnitude.setReadOnly(True)

        self.gridLayout_2.addWidget(self.SIlengthMagnitude, 1, 3, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)

        self.ENGunits = QRadioButton(Dialog)
        self.ENGunits.setObjectName(u"ENGunits")
        self.ENGunits.setChecked(False)

        self.gridLayout.addWidget(self.ENGunits, 2, 0, 1, 2)

        self.fahrenheit = QRadioButton(Dialog)
        self.temperature = QButtonGroup(Dialog)
        self.temperature.setObjectName(u"temperature")
        self.temperature.addButton(self.fahrenheit)
        self.fahrenheit.setObjectName(u"fahrenheit")

        self.gridLayout.addWidget(self.fahrenheit, 5, 3, 1, 1)

        self.SIunits = QRadioButton(Dialog)
        self.SIunits.setObjectName(u"SIunits")
        self.SIunits.setChecked(True)

        self.gridLayout.addWidget(self.SIunits, 0, 0, 1, 1)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 4)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 4)

        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")

        self.gridLayout.addWidget(self.save, 7, 1, 1, 2)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")

        self.gridLayout.addWidget(self.cancel, 7, 3, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.celsius = QRadioButton(Dialog)
        self.temperature.addButton(self.celsius)
        self.celsius.setObjectName(u"celsius")
        self.celsius.setChecked(True)

        self.gridLayout.addWidget(self.celsius, 5, 2, 1, 1)


        self.retranslateUi(Dialog)
        self.SIunits.toggled.connect(self.groupBox.setEnabled)
        self.ENGunits.toggled.connect(self.groupBox_2.setEnabled)
        self.cancel.clicked.connect(Dialog.reject)
        self.ENGunits.clicked.connect(self.ENGforceMagnitude.setEnabled)
        self.ENGunits.clicked.connect(self.ENGlengthMagnitude.setEnabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Units", None))
        self.groupBox_2.setTitle("")
        self.ENGlengthMagnitude.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.ENGforceMagnitude.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Force", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Length", None))
        self.forceSuffix_2.setText(QCoreApplication.translate("Dialog", u"pdl", None))
        self.lengthSuffix_2.setText(QCoreApplication.translate("Dialog", u"ft", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.groupBox.setTitle("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Force", None))
        self.SIforceMagnitude.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Length", None))
        self.forceSuffix.setText(QCoreApplication.translate("Dialog", u"N", None))
        self.lengthSuffix.setText(QCoreApplication.translate("Dialog", u"m", None))
        self.SIlengthMagnitude.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.ENGunits.setText(QCoreApplication.translate("Dialog", u"Engineering Units", None))
        self.fahrenheit.setText(QCoreApplication.translate("Dialog", u"Fahrenheit", None))
        self.SIunits.setText(QCoreApplication.translate("Dialog", u"SI Units", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Temperature", None))
        self.celsius.setText(QCoreApplication.translate("Dialog", u"Celsius", None))
    # retranslateUi

