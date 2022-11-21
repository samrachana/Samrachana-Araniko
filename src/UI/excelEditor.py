# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exceleditor.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 587)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.addRow = QPushButton(self.centralwidget)
        self.addRow.setObjectName(u"addRow")

        self.gridLayout.addWidget(self.addRow, 0, 1, 1, 1)

        self.subtractRow = QPushButton(self.centralwidget)
        self.subtractRow.setObjectName(u"subtractRow")

        self.gridLayout.addWidget(self.subtractRow, 0, 2, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.segmentsTable = QTableWidget(self.tab)
        if (self.segmentsTable.columnCount() < 11):
            self.segmentsTable.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.segmentsTable.setObjectName(u"segmentsTable")
        self.segmentsTable.setDragEnabled(True)
        self.segmentsTable.setDragDropMode(QAbstractItemView.DragDrop)
        self.segmentsTable.setDefaultDropAction(Qt.CopyAction)
        self.segmentsTable.setAlternatingRowColors(True)
        self.segmentsTable.horizontalHeader().setDefaultSectionSize(100)

        self.gridLayout_2.addWidget(self.segmentsTable, 0, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.done = QPushButton(self.tab)
        self.done.setObjectName(u"done")

        self.gridLayout_2.addWidget(self.done, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.loadsTable = QTableWidget(self.tab_2)
        if (self.loadsTable.columnCount() < 6):
            self.loadsTable.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.loadsTable.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        self.loadsTable.setObjectName(u"loadsTable")
        self.loadsTable.setDragEnabled(True)
        self.loadsTable.setDragDropMode(QAbstractItemView.DragDrop)
        self.loadsTable.setDefaultDropAction(Qt.CopyAction)
        self.loadsTable.setAlternatingRowColors(True)
        self.loadsTable.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.loadsTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.supportsTable = QTableWidget(self.tab_3)
        if (self.supportsTable.columnCount() < 6):
            self.supportsTable.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.supportsTable.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.supportsTable.setObjectName(u"supportsTable")
        self.supportsTable.setDragEnabled(True)
        self.supportsTable.setDragDropMode(QAbstractItemView.DragDrop)
        self.supportsTable.setDefaultDropAction(Qt.CopyAction)
        self.supportsTable.setAlternatingRowColors(True)
        self.supportsTable.setSelectionMode(QAbstractItemView.ContiguousSelection)

        self.gridLayout_4.addWidget(self.supportsTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addRow.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.subtractRow.setText(QCoreApplication.translate("MainWindow", u"-", None))
        ___qtablewidgetitem = self.segmentsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.segmentsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"P1", None));
        ___qtablewidgetitem2 = self.segmentsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"P3", None));
        ___qtablewidgetitem3 = self.segmentsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"P2", None));
        ___qtablewidgetitem4 = self.segmentsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"E", None));
        ___qtablewidgetitem5 = self.segmentsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"G", None));
        ___qtablewidgetitem6 = self.segmentsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem7 = self.segmentsTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"I", None));
        ___qtablewidgetitem8 = self.segmentsTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Density", None));
        ___qtablewidgetitem9 = self.segmentsTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"alpha", None));
        ___qtablewidgetitem10 = self.segmentsTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.done.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Segments", None))
        ___qtablewidgetitem11 = self.loadsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem12 = self.loadsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Degree", None));
        ___qtablewidgetitem13 = self.loadsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"P1", None));
        ___qtablewidgetitem14 = self.loadsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"P3", None));
        ___qtablewidgetitem15 = self.loadsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Normal", None));
        ___qtablewidgetitem16 = self.loadsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Parent Segment", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Loads", None))
        ___qtablewidgetitem17 = self.supportsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem18 = self.supportsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem19 = self.supportsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem20 = self.supportsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem21 = self.supportsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Normal", None));
        ___qtablewidgetitem22 = self.supportsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Settlement", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Supports", None))
    # retranslateUi

