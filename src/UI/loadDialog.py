# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadDialog.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        reg_ex = QtCore.QRegExp("[0-9]+.?[0-9]{,5}")
        input_validator = QtGui.QRegExpValidator(reg_ex)
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 352)
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/polyload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.n1 = QtWidgets.QLineEdit(Dialog)
        self.n1.setValidator(input_validator)
        self.n1.setObjectName("n1")
        self.horizontalLayout.addWidget(self.n1)
        self.n2 = QtWidgets.QLineEdit(Dialog)
        self.n2.setValidator(input_validator)
        self.n2.setObjectName("n2")
        self.horizontalLayout.addWidget(self.n2)
        self.n3 = QtWidgets.QLineEdit(Dialog)
        self.n3.setText("")
        self.n3.setObjectName("n3")
        self.horizontalLayout.addWidget(self.n3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 9, 1, 1, 4)
        self.finalSlider = QtWidgets.QSlider(Dialog)
        self.finalSlider.setMaximum(999999)
        self.finalSlider.setSingleStep(1000)
        self.finalSlider.setPageStep(100)
        self.finalSlider.setSliderPosition(999999)
        self.finalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.finalSlider.setInvertedAppearance(False)
        self.finalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.finalSlider.setTickInterval(0)
        self.finalSlider.setObjectName("finalSlider")
        self.gridLayout_2.addWidget(self.finalSlider, 6, 1, 1, 3)
        self.peak = QtWidgets.QLineEdit(Dialog)
        self.peak.setValidator(input_validator)
        self.peak.setObjectName("peak")
        self.gridLayout_2.addWidget(self.peak, 2, 3, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.parentSegment = QtWidgets.QComboBox(Dialog)
        self.parentSegment.setObjectName("parentSegment")
        self.gridLayout_2.addWidget(self.parentSegment, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 10, 3, 1, 2)
        self.finalBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.finalBox.setDecimals(3)
        self.finalBox.setMaximum(999.999)
        self.finalBox.setSingleStep(0.001)
        self.finalBox.setProperty("value", 999.999)
        self.finalBox.setObjectName("finalBox")
        self.gridLayout_2.addWidget(self.finalBox, 6, 4, 1, 1)
        self.degree = QtWidgets.QSpinBox(Dialog)
        self.degree.setMinimum(-2)
        self.degree.setProperty("value", -1)
        self.degree.setObjectName("degree")
        self.gridLayout_2.addWidget(self.degree, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.p1x = QtWidgets.QLineEdit(self.groupBox)
        self.p1x.setValidator(input_validator)
        self.p1x.setObjectName("p1x")
        self.gridLayout.addWidget(self.p1x, 0, 1, 1, 1)
        self.p1y = QtWidgets.QLineEdit(self.groupBox)
        self.p1y.setValidator(input_validator)
        self.p1y.setObjectName("p1y")
        self.gridLayout.addWidget(self.p1y, 0, 2, 1, 1)
        self.p1z = QtWidgets.QLineEdit(self.groupBox)
        self.p1z.setValidator(input_validator)
        self.p1z.setObjectName("p1z")
        self.gridLayout.addWidget(self.p1z, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.p3x = QtWidgets.QLineEdit(self.groupBox)
        self.p3x.setValidator(input_validator)
        self.p3x.setObjectName("p3x")
        self.gridLayout.addWidget(self.p3x, 1, 1, 1, 1)
        self.p3y = QtWidgets.QLineEdit(self.groupBox)
        self.p3y.setValidator(input_validator)
        self.p3y.setObjectName("p3y")
        self.gridLayout.addWidget(self.p3y, 1, 2, 1, 1)
        self.p3z = QtWidgets.QLineEdit(self.groupBox)
        self.p3z.setValidator(input_validator)
        self.p3z.setObjectName("p3z")
        self.gridLayout.addWidget(self.p3z, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 7, 0, 1, 5)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 5)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 2, 1)
        self.initialBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.initialBox.setDecimals(3)
        self.initialBox.setMaximum(999.999)
        self.initialBox.setSingleStep(0.001)
        self.initialBox.setObjectName("initialBox")
        self.gridLayout_2.addWidget(self.initialBox, 4, 4, 2, 1)
        self.initialSlider = QtWidgets.QSlider(Dialog)
        self.initialSlider.setMaximum(999999)
        self.initialSlider.setSingleStep(1000)
        self.initialSlider.setPageStep(100)
        self.initialSlider.setOrientation(QtCore.Qt.Horizontal)
        self.initialSlider.setObjectName("initialSlider")
        self.gridLayout_2.addWidget(self.initialSlider, 5, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 3, 1, 2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 9, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.parentSegment, self.name)
        Dialog.setTabOrder(self.name, self.degree)
        Dialog.setTabOrder(self.degree, self.peak)
        Dialog.setTabOrder(self.peak, self.n1)
        Dialog.setTabOrder(self.n1, self.n2)
        Dialog.setTabOrder(self.n2, self.n3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Load Detials"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_9.setText(_translate("Dialog", "To"))
        self.n1.setPlaceholderText(_translate("Dialog", "x"))
        self.n2.setPlaceholderText(_translate("Dialog", "y"))
        self.n3.setPlaceholderText(_translate("Dialog", "z"))
        self.peak.setText(_translate("Dialog", "2"))
        self.label.setText(_translate("Dialog", "Parent Segment"))
        self.groupBox.setTitle(_translate("Dialog", "Coordinates"))
        self.label_4.setText(_translate("Dialog", "Initial Point"))
        self.p1x.setPlaceholderText(_translate("Dialog", "x"))
        self.p1y.setPlaceholderText(_translate("Dialog", "y"))
        self.p1z.setPlaceholderText(_translate("Dialog", "z"))
        self.label_3.setText(_translate("Dialog", "Terminal Point"))
        self.p3x.setPlaceholderText(_translate("Dialog", "x"))
        self.p3y.setPlaceholderText(_translate("Dialog", "y"))
        self.p3z.setPlaceholderText(_translate("Dialog", "z"))
        self.label_7.setText(_translate("Dialog", "Peak"))
        self.label_8.setText(_translate("Dialog", "From"))
        self.label_6.setText(_translate("Dialog", "Degree"))
        self.name.setPlaceholderText(_translate("Dialog", "optional"))
        self.label_5.setText(_translate("Dialog", "Normal"))
