# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nodalDisplacements.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1067, 572)
        Form.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMinimumSize(QtCore.QSize(0, 25))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(336, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(335, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(336, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setLineWidth(5)
        self.label_3.setMidLineWidth(5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.displacementTable = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displacementTable.sizePolicy().hasHeightForWidth())
        self.displacementTable.setSizePolicy(sizePolicy)
        self.displacementTable.setMinimumSize(QtCore.QSize(0, 192))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.displacementTable.setFont(font)
        self.displacementTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.displacementTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.displacementTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.displacementTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.displacementTable.setTabKeyNavigation(True)
        self.displacementTable.setProperty("showDropIndicator", False)
        self.displacementTable.setDragDropOverwriteMode(False)
        self.displacementTable.setAlternatingRowColors(True)
        self.displacementTable.setGridStyle(QtCore.Qt.SolidLine)
        self.displacementTable.setObjectName("displacementTable")
        self.displacementTable.setColumnCount(9)
        self.displacementTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(8, item)
        self.displacementTable.horizontalHeader().setCascadingSectionResizes(True)
        self.displacementTable.horizontalHeader().setDefaultSectionSize(115)
        self.displacementTable.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.displacementTable, 2, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMinimumSize(QtCore.QSize(101, 0))
        self.line.setMaximumSize(QtCore.QSize(101, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(299, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(299, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(299, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.forcesTable = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forcesTable.sizePolicy().hasHeightForWidth())
        self.forcesTable.setSizePolicy(sizePolicy)
        self.forcesTable.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.forcesTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.forcesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.forcesTable.setTabKeyNavigation(False)
        self.forcesTable.setProperty("showDropIndicator", False)
        self.forcesTable.setDragDropOverwriteMode(False)
        self.forcesTable.setAlternatingRowColors(True)
        self.forcesTable.setObjectName("forcesTable")
        self.forcesTable.setColumnCount(10)
        self.forcesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(9, item)
        self.forcesTable.horizontalHeader().setDefaultSectionSize(104)
        self.gridLayout.addWidget(self.forcesTable, 5, 0, 1, 2)
        self.label.setBuddy(self.displacementTable)
        self.label_2.setBuddy(self.displacementTable)
        self.label_3.setBuddy(self.displacementTable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Results from Direct Stiffness Method"))
        self.label_8.setText(_translate("Form", "Nodal Displacements"))
        self.label.setText(_translate("Form", "Node Coordinates"))
        self.label_2.setText(_translate("Form", "Translations"))
        self.label_3.setText(_translate("Form", "Rotations"))
        item = self.displacementTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "x"))
        item = self.displacementTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "y"))
        item = self.displacementTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "z"))
        item = self.displacementTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "dx"))
        item = self.displacementTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "dy"))
        item = self.displacementTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "dz"))
        item = self.displacementTable.horizontalHeaderItem(6)
        item.setText(_translate("Form", "rx"))
        item = self.displacementTable.horizontalHeaderItem(7)
        item.setText(_translate("Form", "ry"))
        item = self.displacementTable.horizontalHeaderItem(8)
        item.setText(_translate("Form", "rz"))
        self.label_7.setText(_translate("Form", "Member End Forces"))
        self.label_4.setText(_translate("Form", "Node"))
        self.label_5.setText(_translate("Form", "    Forces"))
        self.label_6.setText(_translate("Form", "Moments"))
        item = self.forcesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Member"))
        item = self.forcesTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "x"))
        item = self.forcesTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "y"))
        item = self.forcesTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "z"))
        item = self.forcesTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "axial"))
        item = self.forcesTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "shear(y)"))
        item = self.forcesTable.horizontalHeaderItem(6)
        item.setText(_translate("Form", "shear(z)"))
        item = self.forcesTable.horizontalHeaderItem(7)
        item.setText(_translate("Form", "twisting"))
        item = self.forcesTable.horizontalHeaderItem(8)
        item.setText(_translate("Form", "bending(y)"))
        item = self.forcesTable.horizontalHeaderItem(9)
        item.setText(_translate("Form", "bending(z)"))
