# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferenceDialog.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 467)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.bgColor = ColorButton(Dialog)
        self.bgColor.setText("")
        self.bgColor.setObjectName("bgColor")
        self.horizontalLayout_2.addWidget(self.bgColor)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.segmentColor = ColorButton(Dialog)
        self.segmentColor.setText("")
        self.segmentColor.setObjectName("segmentColor")
        self.horizontalLayout.addWidget(self.segmentColor)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setLineWidth(2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.segementWidth = QtWidgets.QSpinBox(Dialog)
        self.segementWidth.setMinimum(1)
        self.segementWidth.setProperty("value", 3)
        self.segementWidth.setObjectName("segementWidth")
        self.horizontalLayout.addWidget(self.segementWidth)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_12.setLineWidth(2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setLineWidth(2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_14.setLineWidth(2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setLineWidth(2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setLineWidth(2)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 3, 1, 1)
        self.rollerColor = ColorButton(Dialog)
        self.rollerColor.setText("")
        self.rollerColor.setObjectName("rollerColor")
        self.gridLayout.addWidget(self.rollerColor, 1, 0, 1, 1)
        self.hingeColor = ColorButton(Dialog)
        self.hingeColor.setText("")
        self.hingeColor.setObjectName("hingeColor")
        self.gridLayout.addWidget(self.hingeColor, 1, 1, 1, 1)
        self.fixedColor = ColorButton(Dialog)
        self.fixedColor.setText("")
        self.fixedColor.setObjectName("fixedColor")
        self.gridLayout.addWidget(self.fixedColor, 1, 2, 1, 1)
        self.internalHingeColor = ColorButton(Dialog)
        self.internalHingeColor.setText("")
        self.internalHingeColor.setObjectName("internalHingeColor")
        self.gridLayout.addWidget(self.internalHingeColor, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setLineWidth(2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.loadColor = ColorButton(Dialog)
        self.loadColor.setText("")
        self.loadColor.setObjectName("loadColor")
        self.gridLayout_2.addWidget(self.loadColor, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setLineWidth(2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.sfdColor = ColorButton(Dialog)
        self.sfdColor.setText("")
        self.sfdColor.setObjectName("sfdColor")
        self.gridLayout_2.addWidget(self.sfdColor, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setLineWidth(2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.bmdColor = ColorButton(Dialog)
        self.bmdColor.setText("")
        self.bmdColor.setObjectName("bmdColor")
        self.gridLayout_2.addWidget(self.bmdColor, 4, 1, 1, 1)
        self.afdColor = ColorButton(Dialog)
        self.afdColor.setText("")
        self.afdColor.setObjectName("afdColor")
        self.gridLayout_2.addWidget(self.afdColor, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_17.setLineWidth(2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setLineWidth(2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.translationColor = ColorButton(Dialog)
        self.translationColor.setText("")
        self.translationColor.setObjectName("translationColor")
        self.gridLayout_2.addWidget(self.translationColor, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_11.setLineWidth(2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.rotationColor = ColorButton(Dialog)
        self.rotationColor.setText("")
        self.rotationColor.setObjectName("rotationColor")
        self.gridLayout_2.addWidget(self.rotationColor, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setLineWidth(2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setLineWidth(2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.loadWidth = QtWidgets.QSpinBox(Dialog)
        self.loadWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.loadWidth.setMinimum(1)
        self.loadWidth.setMaximum(10)
        self.loadWidth.setProperty("value", 2)
        self.loadWidth.setObjectName("loadWidth")
        self.gridLayout_2.addWidget(self.loadWidth, 1, 3, 1, 1)
        self.afdWidth = QtWidgets.QSpinBox(Dialog)
        self.afdWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.afdWidth.setMinimum(1)
        self.afdWidth.setMaximum(10)
        self.afdWidth.setProperty("value", 2)
        self.afdWidth.setObjectName("afdWidth")
        self.gridLayout_2.addWidget(self.afdWidth, 2, 3, 1, 1)
        self.sfdWidth = QtWidgets.QSpinBox(Dialog)
        self.sfdWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sfdWidth.setMinimum(1)
        self.sfdWidth.setMaximum(10)
        self.sfdWidth.setProperty("value", 2)
        self.sfdWidth.setObjectName("sfdWidth")
        self.gridLayout_2.addWidget(self.sfdWidth, 3, 3, 1, 1)
        self.bmdWidth = QtWidgets.QSpinBox(Dialog)
        self.bmdWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bmdWidth.setMinimum(1)
        self.bmdWidth.setMaximum(10)
        self.bmdWidth.setProperty("value", 2)
        self.bmdWidth.setObjectName("bmdWidth")
        self.gridLayout_2.addWidget(self.bmdWidth, 4, 3, 1, 1)
        self.translationWidth = QtWidgets.QSpinBox(Dialog)
        self.translationWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.translationWidth.setMinimum(1)
        self.translationWidth.setMaximum(10)
        self.translationWidth.setProperty("value", 2)
        self.translationWidth.setObjectName("translationWidth")
        self.gridLayout_2.addWidget(self.translationWidth, 5, 3, 1, 1)
        self.rotationWidth = QtWidgets.QSpinBox(Dialog)
        self.rotationWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rotationWidth.setMinimum(1)
        self.rotationWidth.setMaximum(10)
        self.rotationWidth.setProperty("value", 2)
        self.rotationWidth.setObjectName("rotationWidth")
        self.gridLayout_2.addWidget(self.rotationWidth, 6, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setLineWidth(2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.label.setText(_translate("Dialog", "Background color"))
        self.label_2.setText(_translate("Dialog", "Segment color"))
        self.label_3.setText(_translate("Dialog", "Segment width"))
        self.label_12.setText(_translate("Dialog", "Supports Color"))
        self.label_13.setText(_translate("Dialog", "Roller"))
        self.label_14.setText(_translate("Dialog", "Hinge"))
        self.label_15.setText(_translate("Dialog", "Fixed"))
        self.label_16.setText(_translate("Dialog", "Internal Hinge"))
        self.label_7.setText(_translate("Dialog", "AFD"))
        self.label_8.setText(_translate("Dialog", "SFD"))
        self.label_9.setText(_translate("Dialog", "BMD"))
        self.label_17.setText(_translate("Dialog", "Load"))
        self.label_10.setText(_translate("Dialog", "Translation"))
        self.label_11.setText(_translate("Dialog", "Rotation"))
        self.label_4.setText(_translate("Dialog", "Diagrams"))
        self.label_5.setText(_translate("Dialog", "Color"))
        self.label_6.setText(_translate("Dialog", "Thickness"))
from pyqtgraph import ColorButton
