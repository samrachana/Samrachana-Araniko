# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectTable.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.segmentsTable = QtWidgets.QTableWidget(self.tab)
        self.segmentsTable.setAcceptDrops(True)
        self.segmentsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.segmentsTable.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.segmentsTable.setDragEnabled(True)
        self.segmentsTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.segmentsTable.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.segmentsTable.setAlternatingRowColors(True)
        self.segmentsTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.segmentsTable.setObjectName("segmentsTable")
        self.segmentsTable.setColumnCount(14)
        self.segmentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(13, item)
        self.segmentsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.segmentsTable.horizontalHeader().setStretchLastSection(True)
        self.segmentsTable.verticalHeader().setCascadingSectionResizes(True)
        self.segmentsTable.verticalHeader().setSortIndicatorShown(True)
        self.segmentsTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.segmentsTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.loadsTable = QtWidgets.QTableWidget(self.tab_2)
        self.loadsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.loadsTable.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.loadsTable.setDragEnabled(True)
        self.loadsTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.loadsTable.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.loadsTable.setAlternatingRowColors(True)
        self.loadsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.loadsTable.setObjectName("loadsTable")
        self.loadsTable.setColumnCount(6)
        self.loadsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(5, item)
        self.loadsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.loadsTable.horizontalHeader().setSortIndicatorShown(True)
        self.loadsTable.horizontalHeader().setStretchLastSection(True)
        self.loadsTable.verticalHeader().setCascadingSectionResizes(True)
        self.loadsTable.verticalHeader().setSortIndicatorShown(True)
        self.loadsTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.loadsTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.supportsTable = QtWidgets.QTableWidget(self.tab_3)
        self.supportsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.supportsTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.supportsTable.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.supportsTable.setObjectName("supportsTable")
        self.supportsTable.setColumnCount(5)
        self.supportsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(4, item)
        self.supportsTable.horizontalHeader().setStretchLastSection(True)
        self.supportsTable.verticalHeader().setCascadingSectionResizes(True)
        self.supportsTable.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_4.addWidget(self.supportsTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 24))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionBulk_Update = QtWidgets.QAction(MainWindow)
        self.actionBulk_Update.setObjectName("actionBulk_Update")
        self.menuTools.addAction(self.actionImport)
        self.menuTools.addAction(self.actionBulk_Update)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Object Table"))
        self.segmentsTable.setSortingEnabled(True)
        item = self.segmentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.segmentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.segmentsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "From"))
        item = self.segmentsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "To"))
        item = self.segmentsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Through"))
        item = self.segmentsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Material"))
        item = self.segmentsTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Section"))
        item = self.segmentsTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "E"))
        item = self.segmentsTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "G"))
        item = self.segmentsTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Area"))
        item = self.segmentsTable.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Ixx"))
        item = self.segmentsTable.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Iyy"))
        item = self.segmentsTable.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "J"))
        item = self.segmentsTable.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Axis Vector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Segments"))
        self.loadsTable.setSortingEnabled(True)
        item = self.loadsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.loadsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Parent"))
        item = self.loadsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Degree"))
        item = self.loadsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "From"))
        item = self.loadsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "To"))
        item = self.loadsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Normal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Loads"))
        self.supportsTable.setSortingEnabled(True)
        item = self.supportsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.supportsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        item = self.supportsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.supportsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Normal"))
        item = self.supportsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Settlements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Supports"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionBulk_Update.setText(_translate("MainWindow", "Bulk Update"))
