# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'liveLoadDefinition.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(567, 346)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.liveLoadsTable = QTableWidget(Dialog)
        if (self.liveLoadsTable.columnCount() < 6):
            self.liveLoadsTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.liveLoadsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.liveLoadsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.liveLoadsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.liveLoadsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.liveLoadsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.liveLoadsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.liveLoadsTable.setObjectName(u"liveLoadsTable")
        self.liveLoadsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.liveLoadsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.liveLoadsTable.setSortingEnabled(True)
        self.liveLoadsTable.horizontalHeader().setVisible(True)
        self.liveLoadsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.liveLoadsTable.horizontalHeader().setMinimumSectionSize(50)
        self.liveLoadsTable.horizontalHeader().setDefaultSectionSize(90)
        self.liveLoadsTable.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout.addWidget(self.liveLoadsTable, 1, 0, 1, 9)

        self.done = QPushButton(Dialog)
        self.done.setObjectName(u"done")
        self.done.setAutoDefault(False)

        self.gridLayout.addWidget(self.done, 2, 8, 1, 1)

        self.back = QPushButton(Dialog)
        self.back.setObjectName(u"back")
        self.back.setAutoDefault(False)

        self.gridLayout.addWidget(self.back, 2, 0, 1, 1)

        self.nextFrame = QPushButton(Dialog)
        self.nextFrame.setObjectName(u"nextFrame")
        self.nextFrame.setAutoDefault(False)

        self.gridLayout.addWidget(self.nextFrame, 0, 8, 1, 1)

        self.previousFrame = QPushButton(Dialog)
        self.previousFrame.setObjectName(u"previousFrame")
        self.previousFrame.setAutoDefault(False)

        self.gridLayout.addWidget(self.previousFrame, 0, 7, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.reset = QPushButton(Dialog)
        self.reset.setObjectName(u"reset")
        self.reset.setAutoDefault(False)

        self.gridLayout.addWidget(self.reset, 0, 3, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton, 2, 7, 1, 1)

        self.keyFrames = QComboBox(Dialog)
        self.keyFrames.setObjectName(u"keyFrames")

        self.gridLayout.addWidget(self.keyFrames, 0, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        self.done.clicked.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Live Load Definition", None))
        ___qtablewidgetitem = self.liveLoadsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Loads", None));
        ___qtablewidgetitem1 = self.liveLoadsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Degree", None));
        ___qtablewidgetitem2 = self.liveLoadsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"P1", None));
        ___qtablewidgetitem3 = self.liveLoadsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"P3", None));
        ___qtablewidgetitem4 = self.liveLoadsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Peak", None));
        ___qtablewidgetitem5 = self.liveLoadsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Normal", None));
        self.done.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.nextFrame.setText(QCoreApplication.translate("Dialog", u">>>", None))
        self.previousFrame.setText(QCoreApplication.translate("Dialog", u"<<<", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"KeyFrames", None))
        self.reset.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

