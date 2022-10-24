# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segmentDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(602, 309)
        Dialog.setAccessibleName("")
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.p1x = QtWidgets.QDoubleSpinBox(Dialog)
        self.p1x.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p1x.setObjectName("p1x")
        self.gridLayout.addWidget(self.p1x, 1, 2, 1, 1)
        self.p1y = QtWidgets.QDoubleSpinBox(Dialog)
        self.p1y.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p1y.setObjectName("p1y")
        self.gridLayout.addWidget(self.p1y, 1, 3, 1, 2)
        self.p1z = QtWidgets.QDoubleSpinBox(Dialog)
        self.p1z.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p1z.setObjectName("p1z")
        self.gridLayout.addWidget(self.p1z, 1, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.p2x = QtWidgets.QDoubleSpinBox(Dialog)
        self.p2x.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p2x.setObjectName("p2x")
        self.gridLayout.addWidget(self.p2x, 2, 2, 1, 1)
        self.p2y = QtWidgets.QDoubleSpinBox(Dialog)
        self.p2y.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p2y.setObjectName("p2y")
        self.gridLayout.addWidget(self.p2y, 2, 3, 1, 2)
        self.p2z = QtWidgets.QDoubleSpinBox(Dialog)
        self.p2z.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p2z.setObjectName("p2z")
        self.gridLayout.addWidget(self.p2z, 2, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.p3x = QtWidgets.QDoubleSpinBox(Dialog)
        self.p3x.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p3x.setObjectName("p3x")
        self.gridLayout.addWidget(self.p3x, 3, 2, 1, 1)
        self.p3y = QtWidgets.QDoubleSpinBox(Dialog)
        self.p3y.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p3y.setObjectName("p3y")
        self.gridLayout.addWidget(self.p3y, 3, 3, 1, 2)
        self.p3z = QtWidgets.QDoubleSpinBox(Dialog)
        self.p3z.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)

        self.p3z.setObjectName("p3z")
        self.gridLayout.addWidget(self.p3z, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 4, 1, 1)
        self.youngsModulus = QtWidgets.QDoubleSpinBox(Dialog)
        self.youngsModulus.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.youngsModulus.setObjectName("youngsModulus")
        self.gridLayout.addWidget(self.youngsModulus, 5, 0, 1, 2)
        self.shearModulus = QtWidgets.QDoubleSpinBox(Dialog)
        self.shearModulus.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.shearModulus.setObjectName("shearModulus")
        self.gridLayout.addWidget(self.shearModulus, 5, 2, 1, 2)
        self.area = QtWidgets.QDoubleSpinBox(Dialog)
        self.area.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.area.setObjectName("area")
        self.gridLayout.addWidget(self.area, 5, 4, 1, 2)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 4, 1, 1)
        self.ixx = QtWidgets.QDoubleSpinBox(Dialog)
        self.ixx.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.ixx.setObjectName("ixx")
        self.gridLayout.addWidget(self.ixx, 7, 0, 1, 2)
        self.axisVector = QtWidgets.QDoubleSpinBox(Dialog)
        self.axisVector.setStatusTip("")
        self.axisVector.setObjectName("axisVector")
        self.gridLayout.addWidget(self.axisVector, 7, 2, 1, 2)
        self.iyy = QtWidgets.QDoubleSpinBox(Dialog)
        self.iyy.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.iyy.setObjectName("iyy")
        self.gridLayout.addWidget(self.iyy, 7, 4, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 4, 1, 2)
        self.name = QtWidgets.QDoubleSpinBox(Dialog)


        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 2, 1, 3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.name, self.p1x)
        Dialog.setTabOrder(self.p1x, self.p1y)
        Dialog.setTabOrder(self.p1y, self.p1z)
        Dialog.setTabOrder(self.p1z, self.p2x)
        Dialog.setTabOrder(self.p2x, self.p2y)
        Dialog.setTabOrder(self.p2y, self.p2z)
        Dialog.setTabOrder(self.p2z, self.p3x)
        Dialog.setTabOrder(self.p3x, self.p3y)
        Dialog.setTabOrder(self.p3y, self.p3z)
        Dialog.setTabOrder(self.p3z, self.youngsModulus)
        Dialog.setTabOrder(self.youngsModulus, self.shearModulus)
        Dialog.setTabOrder(self.shearModulus, self.area)
        Dialog.setTabOrder(self.area, self.ixx)
        Dialog.setTabOrder(self.ixx, self.axisVector)
        Dialog.setTabOrder(self.axisVector, self.iyy)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Segement Detials"))


        self.p1x.setWhatsThis(_translate("Dialog", "x"))
        self.p1y.setWhatsThis(_translate("Dialog", "y"))
        self.p1z.setWhatsThis(_translate("Dialog", "z"))

        self.p2x.setWhatsThis(_translate("Dialog", "x"))
        self.p2y.setWhatsThis(_translate("Dialog", "y"))
        self.p2z.setWhatsThis(_translate("Dialog", "z"))

        self.p3x.setWhatsThis(_translate("Dialog", "x"))
        self.p3y.setWhatsThis(_translate("Dialog", "y"))
        self.p3z.setWhatsThis(_translate("Dialog", "z"))



        self.youngsModulus.setWhatsThis(_translate("Dialog", "Young\'s Modulus"))
        self.shearModulus.setWhatsThis(_translate("Dialog", "Shear Modulus"))
        self.area.setWhatsThis(_translate("Dialog", "CSA of segment"))



        self.ixx.setWhatsThis(_translate("Dialog", "I about centroid"))
        self.axisVector.setWhatsThis(_translate("Dialog", "Axis of Ixx (x,y,z)"))
        self.iyy.setStatusTip(_translate("Dialog", "Axis of Iyy should be perpendicular to axis of Ixx"))
        self.iyy.setWhatsThis(_translate("Dialog", "I about centroid"))
        self.name.setWhatsThis(_translate("Dialog", "Name of the segment (optional)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
