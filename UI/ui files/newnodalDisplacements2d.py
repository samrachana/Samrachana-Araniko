# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newnodalDisplacements2d.ui'
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
        MainWindow.resize(705, 296)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.responseTab = QWidget()
        self.responseTab.setObjectName(u"responseTab")
        self.gridLayout_2 = QGridLayout(self.responseTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.displacementTable = QTableWidget(self.responseTab)
        if (self.displacementTable.columnCount() < 5):
            self.displacementTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.displacementTable.setObjectName(u"displacementTable")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displacementTable.sizePolicy().hasHeightForWidth())
        self.displacementTable.setSizePolicy(sizePolicy)
        self.displacementTable.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.displacementTable.setFont(font)
        self.displacementTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.displacementTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.displacementTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.displacementTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.displacementTable.setTabKeyNavigation(True)
        self.displacementTable.setProperty("showDropIndicator", False)
        self.displacementTable.setDragDropOverwriteMode(False)
        self.displacementTable.setAlternatingRowColors(True)
        self.displacementTable.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.displacementTable.setGridStyle(Qt.SolidLine)
        self.displacementTable.setSortingEnabled(True)
        self.displacementTable.horizontalHeader().setCascadingSectionResizes(True)
        self.displacementTable.horizontalHeader().setDefaultSectionSize(130)
        self.displacementTable.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.displacementTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.responseTab, "")
        self.actionsTab = QWidget()
        self.actionsTab.setObjectName(u"actionsTab")
        self.gridLayout_3 = QGridLayout(self.actionsTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.forcesTable = QTableWidget(self.actionsTab)
        if (self.forcesTable.columnCount() < 6):
            self.forcesTable.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.forcesTable.setObjectName(u"forcesTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.forcesTable.sizePolicy().hasHeightForWidth())
        self.forcesTable.setSizePolicy(sizePolicy1)
        self.forcesTable.setMinimumSize(QSize(0, 0))
        self.forcesTable.setMaximumSize(QSize(1200, 16777215))
        self.forcesTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.forcesTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.forcesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.forcesTable.setTabKeyNavigation(False)
        self.forcesTable.setProperty("showDropIndicator", False)
        self.forcesTable.setDragDropOverwriteMode(False)
        self.forcesTable.setAlternatingRowColors(True)
        self.forcesTable.horizontalHeader().setDefaultSectionSize(104)
        self.forcesTable.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.forcesTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.actionsTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reactionTable = QTableWidget(self.tab)
        if (self.reactionTable.columnCount() < 5):
            self.reactionTable.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.reactionTable.setObjectName(u"reactionTable")
        sizePolicy.setHeightForWidth(self.reactionTable.sizePolicy().hasHeightForWidth())
        self.reactionTable.setSizePolicy(sizePolicy)
        self.reactionTable.setMinimumSize(QSize(0, 0))
        self.reactionTable.setFont(font)
        self.reactionTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.reactionTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.reactionTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.reactionTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reactionTable.setTabKeyNavigation(True)
        self.reactionTable.setProperty("showDropIndicator", False)
        self.reactionTable.setDragDropOverwriteMode(False)
        self.reactionTable.setAlternatingRowColors(True)
        self.reactionTable.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.reactionTable.setGridStyle(Qt.SolidLine)
        self.reactionTable.setSortingEnabled(True)
        self.reactionTable.horizontalHeader().setCascadingSectionResizes(True)
        self.reactionTable.horizontalHeader().setDefaultSectionSize(130)
        self.reactionTable.horizontalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.reactionTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Results from Direct Stiffness Method", None))
        ___qtablewidgetitem = self.displacementTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem1 = self.displacementTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem2 = self.displacementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"dx", None));
        ___qtablewidgetitem3 = self.displacementTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"dy", None));
        ___qtablewidgetitem4 = self.displacementTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"slope", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.responseTab), QCoreApplication.translate("MainWindow", u"Nodal Displacements", None))
        ___qtablewidgetitem5 = self.forcesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Member", None));
        ___qtablewidgetitem6 = self.forcesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem7 = self.forcesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem8 = self.forcesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Axial Force", None));
        ___qtablewidgetitem9 = self.forcesTable.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Shear Force", None));
        ___qtablewidgetitem10 = self.forcesTable.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Bending Moment", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actionsTab), QCoreApplication.translate("MainWindow", u"Member End Forces", None))
        ___qtablewidgetitem11 = self.reactionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem12 = self.reactionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem13 = self.reactionTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Fx", None));
        ___qtablewidgetitem14 = self.reactionTable.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Fy", None));
        ___qtablewidgetitem15 = self.reactionTable.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"M", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Reactions", None))
    # retranslateUi

