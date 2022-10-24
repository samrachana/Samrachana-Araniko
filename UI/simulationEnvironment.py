# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulationEnvironment.ui'
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
        Dialog.resize(394, 367)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.fps = QSpinBox(Dialog)
        self.fps.setObjectName(u"fps")
        self.fps.setValue(20)

        self.gridLayout_2.addWidget(self.fps, 0, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.duration = QSpinBox(Dialog)
        self.duration.setObjectName(u"duration")
        self.duration.setMaximum(1000)
        self.duration.setValue(10)

        self.gridLayout_2.addWidget(self.duration, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.subtractRow = QPushButton(Dialog)
        self.subtractRow.setObjectName(u"subtractRow")
        self.subtractRow.setMaximumSize(QSize(31, 28))
        self.subtractRow.setAutoDefault(False)

        self.gridLayout.addWidget(self.subtractRow, 0, 2, 1, 1)

        self.addRow = QPushButton(Dialog)
        self.addRow.setObjectName(u"addRow")
        self.addRow.setMaximumSize(QSize(31, 28))
        self.addRow.setCheckable(False)
        self.addRow.setAutoDefault(False)

        self.gridLayout.addWidget(self.addRow, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 3, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.pushButton, 4, 2, 1, 1)

        self.next = QPushButton(Dialog)
        self.next.setObjectName(u"next")
        self.next.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.next, 4, 3, 1, 1)

        self.keyFrameTable = QTableWidget(Dialog)
        if (self.keyFrameTable.columnCount() < 3):
            self.keyFrameTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.keyFrameTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.keyFrameTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.keyFrameTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.keyFrameTable.setObjectName(u"keyFrameTable")
        self.keyFrameTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyFrameTable.setAlternatingRowColors(True)
        self.keyFrameTable.setSortingEnabled(True)
        self.keyFrameTable.horizontalHeader().setDefaultSectionSize(120)

        self.gridLayout_2.addWidget(self.keyFrameTable, 3, 0, 1, 4)


        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Simulation Environment", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Frames per second", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Duration", None))
        self.duration.setSuffix(QCoreApplication.translate("Dialog", u"s", None))
        self.subtractRow.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.addRow.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.next.setText(QCoreApplication.translate("Dialog", u"Next", None))
        ___qtablewidgetitem = self.keyFrameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"KeyFrame", None));
        ___qtablewidgetitem1 = self.keyFrameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Time (s)", None));
        ___qtablewidgetitem2 = self.keyFrameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Frame No", None));
    # retranslateUi

