# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectsTree.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 566)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setMouseTracking(True)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setIndentation(30)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setFocusPolicy(QtCore.Qt.NoFocus)

        self.segment = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./UI/icons/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.segment.setIcon(0, icon1)

        self.load = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./UI/icons/polyload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load.setIcon(0, icon2)

        self.support = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI/icons/hinge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.support.setIcon(0, icon)
        

        

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.treeWidget.setColumnCount(4)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Object Tree"))
        # self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("Form", "Structure"))
        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "Segments"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "Loads"))        
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "Supports"))

        # self.treeWidget.setSortingEnabled(__sortingEnabled)
