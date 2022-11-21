# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generateReport.ui'
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
        Dialog.resize(400, 188)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.author = QLineEdit(Dialog)
        self.author.setObjectName(u"author")
        self.author.setMaxLength(50)

        self.gridLayout.addWidget(self.author, 0, 1, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.organization = QLineEdit(Dialog)
        self.organization.setObjectName(u"organization")
        self.organization.setMaxLength(50)

        self.gridLayout.addWidget(self.organization, 1, 1, 1, 2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.address = QLineEdit(Dialog)
        self.address.setObjectName(u"address")
        self.address.setMaxLength(50)

        self.gridLayout.addWidget(self.address, 2, 1, 1, 2)

        self.filePath = QLineEdit(Dialog)
        self.filePath.setObjectName(u"filePath")

        self.gridLayout.addWidget(self.filePath, 3, 0, 1, 2)

        self.Browse = QPushButton(Dialog)
        self.Browse.setObjectName(u"Browse")

        self.gridLayout.addWidget(self.Browse, 3, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generate Report", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Author", None))
        self.author.setText(QCoreApplication.translate("Dialog", u"Samrachana Araniko", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Organization", None))
        self.organization.setText(QCoreApplication.translate("Dialog", u"The Coding Company", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Addresss", None))
        self.address.setText(QCoreApplication.translate("Dialog", u"Pokhara, Nepal", None))
        self.filePath.setText(QCoreApplication.translate("Dialog", u"./reports.html", None))
        self.Browse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
    # retranslateUi

