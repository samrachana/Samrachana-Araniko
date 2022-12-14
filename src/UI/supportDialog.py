# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supportDialog.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class SupportUi_Dialog(object):
    def setupUi(self, Dialog):
        reg_ex = QtCore.QRegExp("[0-9]+.?[0-9]{,5}")
        input_validator = QtGui.QRegExpValidator(reg_ex)
        Dialog.setObjectName("Dialog")
        Dialog.resize(636, 262)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 5)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.px = QtWidgets.QLineEdit(Dialog)
        self.px.setValidator(input_validator)
        self.px.setText("")
        self.px.setObjectName("px")
        self.gridLayout.addWidget(self.px, 2, 1, 1, 1)
        self.py = QtWidgets.QLineEdit(Dialog)
        self.py.setValidator(input_validator)
        self.py.setText("")
        self.py.setObjectName("py")
        self.gridLayout.addWidget(self.py, 2, 2, 1, 1)
        self.pz = QtWidgets.QLineEdit(Dialog)
        self.pz.setText("")
        self.pz.setObjectName("pz")
        self.gridLayout.addWidget(self.pz, 2, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.dx = QtWidgets.QLineEdit(Dialog)
        self.dx.setValidator(input_validator)
        self.dx.setObjectName("dx")
        self.gridLayout.addWidget(self.dx, 4, 1, 1, 1)
        self.dy = QtWidgets.QLineEdit(Dialog)
        self.dy.setValidator(input_validator)
        self.dy.setObjectName("dy")
        self.gridLayout.addWidget(self.dy, 4, 2, 1, 1)
        self.dz = QtWidgets.QLineEdit(Dialog)
        self.dz.setText("")
        self.dz.setObjectName("dz")
        self.gridLayout.addWidget(self.dz, 4, 4, 1, 1)
        self.rx = QtWidgets.QLineEdit(Dialog)
        self.rx.setValidator(input_validator)
        self.rx.setObjectName("rx")
        self.gridLayout.addWidget(self.rx, 5, 1, 1, 1)
        self.ry = QtWidgets.QLineEdit(Dialog)
        self.ry.setValidator(input_validator)
        self.ry.setObjectName("ry")
        self.gridLayout.addWidget(self.ry, 5, 2, 1, 1)
        self.rz = QtWidgets.QLineEdit(Dialog)
        self.rz.setText("")
        self.rz.setObjectName("rz")
        self.gridLayout.addWidget(self.rz, 5, 4, 1, 1)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.nx = QtWidgets.QLineEdit(Dialog)
        self.nx.setValidator(input_validator)
        self.nx.setObjectName("nx")
        self.gridLayout.addWidget(self.nx, 8, 1, 1, 1)
        self.ny = QtWidgets.QLineEdit(Dialog)
        self.ny.setValidator(input_validator)
        self.ny.setObjectName("ny")
        self.gridLayout.addWidget(self.ny, 8, 2, 1, 1)
        self.nz = QtWidgets.QLineEdit(Dialog)
        self.nz.setText("")
        self.nz.setObjectName("nz")
        self.gridLayout.addWidget(self.nz, 8, 4, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.px)
        Dialog.setTabOrder(self.px, self.py)
        Dialog.setTabOrder(self.py, self.pz)
        Dialog.setTabOrder(self.pz, self.dx)
        Dialog.setTabOrder(self.dx, self.dy)
        Dialog.setTabOrder(self.dy, self.dz)
        Dialog.setTabOrder(self.dz, self.rx)
        Dialog.setTabOrder(self.rx, self.ry)
        Dialog.setTabOrder(self.ry, self.rz)
        Dialog.setTabOrder(self.rz, self.nx)
        Dialog.setTabOrder(self.nx, self.ny)
        Dialog.setTabOrder(self.ny, self.nz)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Support Detials"))
        self.label.setText(_translate("Dialog", "Type"))
        self.comboBox.setItemText(0, _translate("Dialog", "Fixed"))
        self.comboBox.setItemText(1, _translate("Dialog", "Hinge"))
        self.comboBox.setItemText(2, _translate("Dialog", "Roller"))
        self.comboBox.setItemText(3, _translate("Dialog", "Internal Hinge"))
        self.label_5.setText(_translate("Dialog", "Position"))
        self.px.setPlaceholderText(_translate("Dialog", "x"))
        self.py.setPlaceholderText(_translate("Dialog", "y"))
        self.pz.setPlaceholderText(_translate("Dialog", "z"))
        self.dx.setPlaceholderText(_translate("Dialog", "dx"))
        self.dy.setPlaceholderText(_translate("Dialog", "dy"))
        self.dz.setPlaceholderText(_translate("Dialog", "dz"))
        self.rx.setPlaceholderText(_translate("Dialog", "rx"))
        self.ry.setPlaceholderText(_translate("Dialog", "ry"))
        self.rz.setPlaceholderText(_translate("Dialog", "rz"))
        self.label_6.setText(_translate("Dialog", "Normal"))
        self.nx.setPlaceholderText(_translate("Dialog", "x"))
        self.ny.setPlaceholderText(_translate("Dialog", "y"))
        self.nz.setPlaceholderText(_translate("Dialog", "z"))
        self.label_7.setText(_translate("Dialog", "Settlement"))
        self.label_2.setText(_translate("Dialog", "Only for roller "))
