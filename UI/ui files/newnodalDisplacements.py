# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newnodalDisplacements.ui'
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
        MainWindow.resize(1081, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.responseTab = QWidget()
        self.responseTab.setObjectName(u"responseTab")
        self.gridLayout = QGridLayout(self.responseTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.responseTab)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(336, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(5)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.responseTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(335, 25))
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(5)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.responseTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setMaximumSize(QSize(336, 25))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.StyledPanel)
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setLineWidth(5)
        self.label_3.setMidLineWidth(5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.displacementTable = QTableWidget(self.responseTab)
        if (self.displacementTable.columnCount() < 9):
            self.displacementTable.setColumnCount(9)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.displacementTable.setObjectName(u"displacementTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.displacementTable.sizePolicy().hasHeightForWidth())
        self.displacementTable.setSizePolicy(sizePolicy1)
        self.displacementTable.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.displacementTable.setFont(font1)
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
        self.displacementTable.horizontalHeader().setDefaultSectionSize(115)
        self.displacementTable.horizontalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.displacementTable, 1, 0, 1, 1)

        self.tabWidget.addTab(self.responseTab, "")
        self.actionsTab = QWidget()
        self.actionsTab.setObjectName(u"actionsTab")
        self.gridLayout_2 = QGridLayout(self.actionsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line = QFrame(self.actionsTab)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(101, 0))
        self.line.setMaximumSize(QSize(101, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.label_7 = QLabel(self.actionsTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(299, 0))
        self.label_7.setMaximumSize(QSize(299, 25))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(False)
        self.label_7.setFont(font2)
        self.label_7.setFrameShape(QFrame.StyledPanel)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.actionsTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(299, 0))
        self.label_8.setMaximumSize(QSize(299, 25))
        self.label_8.setFont(font2)
        self.label_8.setFrameShape(QFrame.StyledPanel)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_12 = QLabel(self.actionsTab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(299, 0))
        self.label_12.setMaximumSize(QSize(299, 25))
        self.label_12.setFont(font2)
        self.label_12.setFrameShape(QFrame.StyledPanel)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_12)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.forcesTable = QTableWidget(self.actionsTab)
        if (self.forcesTable.columnCount() < 10):
            self.forcesTable.setColumnCount(10)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.forcesTable.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        self.forcesTable.setObjectName(u"forcesTable")
        sizePolicy.setHeightForWidth(self.forcesTable.sizePolicy().hasHeightForWidth())
        self.forcesTable.setSizePolicy(sizePolicy)
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

        self.gridLayout_2.addWidget(self.forcesTable, 1, 0, 1, 1)

        self.tabWidget.addTab(self.actionsTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.reactionTable = QTableWidget(self.tab)
        if (self.reactionTable.columnCount() < 9):
            self.reactionTable.setColumnCount(9)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.reactionTable.setHorizontalHeaderItem(8, __qtablewidgetitem27)
        self.reactionTable.setObjectName(u"reactionTable")
        sizePolicy1.setHeightForWidth(self.reactionTable.sizePolicy().hasHeightForWidth())
        self.reactionTable.setSizePolicy(sizePolicy1)
        self.reactionTable.setMinimumSize(QSize(0, 0))
        self.reactionTable.setFont(font1)
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
        self.reactionTable.horizontalHeader().setDefaultSectionSize(115)
        self.reactionTable.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.reactionTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.displacementTable)
        self.label_2.setBuddy(self.displacementTable)
        self.label_3.setBuddy(self.displacementTable)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Results from Direct Stiffness Method", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Node Coordinates", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Translations", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rotations", None))
        ___qtablewidgetitem = self.displacementTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem1 = self.displacementTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem2 = self.displacementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"z", None));
        ___qtablewidgetitem3 = self.displacementTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"dx", None));
        ___qtablewidgetitem4 = self.displacementTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"dy", None));
        ___qtablewidgetitem5 = self.displacementTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"dz", None));
        ___qtablewidgetitem6 = self.displacementTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"rx", None));
        ___qtablewidgetitem7 = self.displacementTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ry", None));
        ___qtablewidgetitem8 = self.displacementTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"rz", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.responseTab), QCoreApplication.translate("MainWindow", u"Nodal Displacements", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Node", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"    Forces", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Moments", None))
        ___qtablewidgetitem9 = self.forcesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Member", None));
        ___qtablewidgetitem10 = self.forcesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem11 = self.forcesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem12 = self.forcesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"z", None));
        ___qtablewidgetitem13 = self.forcesTable.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"axial", None));
        ___qtablewidgetitem14 = self.forcesTable.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"shear(y)", None));
        ___qtablewidgetitem15 = self.forcesTable.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"shear(z)", None));
        ___qtablewidgetitem16 = self.forcesTable.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"twisting", None));
        ___qtablewidgetitem17 = self.forcesTable.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"bending(y)", None));
        ___qtablewidgetitem18 = self.forcesTable.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"bending(z)", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actionsTab), QCoreApplication.translate("MainWindow", u"Member End Forces", None))
        ___qtablewidgetitem19 = self.reactionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem20 = self.reactionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem21 = self.reactionTable.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"z", None));
        ___qtablewidgetitem22 = self.reactionTable.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Fx", None));
        ___qtablewidgetitem23 = self.reactionTable.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Fy", None));
        ___qtablewidgetitem24 = self.reactionTable.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Fz", None));
        ___qtablewidgetitem25 = self.reactionTable.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Mx", None));
        ___qtablewidgetitem26 = self.reactionTable.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"My", None));
        ___qtablewidgetitem27 = self.reactionTable.horizontalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Mz", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Reactions", None))
    # retranslateUi

