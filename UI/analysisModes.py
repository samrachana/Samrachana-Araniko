# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyseModes.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 117)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frameMode = QtWidgets.QRadioButton(Dialog)
        self.frameMode.setChecked(True)
        self.frameMode.setObjectName("frameMode")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.frameMode)
        self.gridLayout.addWidget(self.frameMode, 0, 0, 1, 1)
        self.trussMode = QtWidgets.QRadioButton(Dialog)
        self.trussMode.setObjectName("trussMode")
        self.buttonGroup.addButton(self.trussMode)
        self.gridLayout.addWidget(self.trussMode, 0, 1, 1, 1)
        self.inextensibleMode = QtWidgets.QCheckBox(Dialog)
        self.inextensibleMode.setObjectName("inextensibleMode")
        self.gridLayout.addWidget(self.inextensibleMode, 1, 0, 1, 1)
        self.shearMode = QtWidgets.QCheckBox(Dialog)
        self.shearMode.setStatusTip("")
        self.shearMode.setObjectName("shearMode")
        self.gridLayout.addWidget(self.shearMode, 1, 1, 1, 1)
        self.simplifyMode = QtWidgets.QCheckBox(Dialog)
        self.simplifyMode.setObjectName("simplifyMode")
        self.gridLayout.addWidget(self.simplifyMode, 1, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.trussMode.clicked['bool'].connect(self.inextensibleMode.setDisabled)
        self.trussMode.clicked['bool'].connect(self.shearMode.setDisabled)
        self.frameMode.clicked['bool'].connect(self.inextensibleMode.setEnabled)
        self.frameMode.clicked['bool'].connect(self.shearMode.setEnabled)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Analysis Modes"))
        self.frameMode.setText(_translate("Dialog", "Frame"))
        self.trussMode.setText(_translate("Dialog", "Truss"))
        self.inextensibleMode.setToolTip(_translate("Dialog", "analyse frame assuming the members inextensible"))
        self.inextensibleMode.setWhatsThis(_translate("Dialog", "analyse frame assuming the members inextensible"))
        self.inextensibleMode.setText(_translate("Dialog", "Inextensible"))
        self.shearMode.setToolTip(_translate("Dialog", "analyse frame assuming the shear in all the members"))
        self.shearMode.setWhatsThis(_translate("Dialog", "analyse frame assuming the shear in all the members"))
        self.shearMode.setText(_translate("Dialog", "Shear"))
        self.simplifyMode.setText(_translate("Dialog", "Simplify"))
        self.simplifyMode.setToolTip(_translate("Dialog", "check for intermediate supports and curved members"))
        self.simplifyMode.setWhatsThis(_translate("Dialog", "check for intermediate supports and curved members"))
