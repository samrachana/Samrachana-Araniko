# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagramsWindow.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1077, 679)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.actionDiagramsMenu = QtWidgets.QToolButton(Dialog)
        self.actionDiagramsMenu.setMinimumSize(QtCore.QSize(190, 26))
        self.actionDiagramsMenu.setMaximumSize(QtCore.QSize(190, 26))
        self.actionDiagramsMenu.setCheckable(False)
        self.actionDiagramsMenu.setChecked(False)
        self.actionDiagramsMenu.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.actionDiagramsMenu.setAutoRaise(False)
        self.actionDiagramsMenu.setObjectName("actionDiagramsMenu")
        self.gridLayout.addWidget(self.actionDiagramsMenu, 0, 1, 1, 1)
        self.actionsGraph = QtWidgets.QOpenGLWidget(Dialog)
        self.actionsGraph.setObjectName("actionsGraph")
        self.gridLayout.addWidget(self.actionsGraph, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.responseDiagramsMenu = QtWidgets.QToolButton(Dialog)
        self.responseDiagramsMenu.setMinimumSize(QtCore.QSize(190, 26))
        self.responseDiagramsMenu.setMaximumSize(QtCore.QSize(190, 26))
        self.responseDiagramsMenu.setObjectName("responseDiagramsMenu")
        self.gridLayout.addWidget(self.responseDiagramsMenu, 2, 1, 1, 1)
        self.responsesGraph = QtWidgets.QOpenGLWidget(Dialog)
        self.responsesGraph.setObjectName("responsesGraph")
        self.gridLayout.addWidget(self.responsesGraph, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Diagrams"))
        self.label.setText(_translate("Dialog", "Actions Graph"))
        self.actionDiagramsMenu.setText(_translate("Dialog", "Filter Diagrams"))
        self.label_2.setText(_translate("Dialog", "Response Graph"))
        self.responseDiagramsMenu.setText(_translate("Dialog", "Filter Diagrams"))
