# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)
        self.buildingName = QtWidgets.QLineEdit(self.centralwidget)
        self.buildingName.setObjectName("buildingName")
        self.gridLayout_6.addWidget(self.buildingName, 0, 2, 1, 3)
        self.building = QtWidgets.QRadioButton(self.centralwidget)
        self.building.setChecked(True)
        self.building.setObjectName("building")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.building)
        self.gridLayout_6.addWidget(self.building, 1, 0, 1, 2)
        self.frame2d = QtWidgets.QRadioButton(self.centralwidget)
        self.frame2d.setObjectName("frame2d")
        self.buttonGroup.addButton(self.frame2d)
        self.gridLayout_6.addWidget(self.frame2d, 1, 3, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 2, 4, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.roomHeight = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.roomHeight.setSingleStep(1.0)
        self.roomHeight.setProperty("value", 3.0)
        self.roomHeight.setObjectName("roomHeight")
        self.gridLayout_2.addWidget(self.roomHeight, 2, 1, 1, 1)
        self.roomBreadth = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.roomBreadth.setSingleStep(1.0)
        self.roomBreadth.setProperty("value", 4.0)
        self.roomBreadth.setObjectName("roomBreadth")
        self.gridLayout_2.addWidget(self.roomBreadth, 1, 1, 1, 1)
        self.roomLength = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.roomLength.setProperty("value", 5.0)
        self.roomLength.setObjectName("roomLength")
        self.gridLayout_2.addWidget(self.roomLength, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 3, 4, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 4, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 4, 4, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 0, 1, 2)
        self.columnMaterial = QtWidgets.QComboBox(self.frame_3)
        self.columnMaterial.setObjectName("columnMaterial")
        self.gridLayout_3.addWidget(self.columnMaterial, 0, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 1, 0, 1, 2)
        self.columnSection = QtWidgets.QComboBox(self.frame_3)
        self.columnSection.setObjectName("columnSection")
        self.gridLayout_3.addWidget(self.columnSection, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.columnYoungModulus = QtWidgets.QLineEdit(self.frame_3)
        self.columnYoungModulus.setObjectName("columnYoungModulus")
        self.gridLayout_3.addWidget(self.columnYoungModulus, 2, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.columnShearModulus = QtWidgets.QLineEdit(self.frame_3)
        self.columnShearModulus.setObjectName("columnShearModulus")
        self.gridLayout_3.addWidget(self.columnShearModulus, 3, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)
        self.columnArea = QtWidgets.QLineEdit(self.frame_3)
        self.columnArea.setObjectName("columnArea")
        self.gridLayout_3.addWidget(self.columnArea, 4, 1, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)
        self.columnIyy = QtWidgets.QLineEdit(self.frame_3)
        self.columnIyy.setObjectName("columnIyy")
        self.gridLayout_3.addWidget(self.columnIyy, 5, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 6, 0, 1, 1)
        self.columnIzz = QtWidgets.QLineEdit(self.frame_3)
        self.columnIzz.setObjectName("columnIzz")
        self.gridLayout_3.addWidget(self.columnIzz, 6, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 7, 0, 1, 1)
        self.columnTorsionConstant = QtWidgets.QLineEdit(self.frame_3)
        self.columnTorsionConstant.setObjectName("columnTorsionConstant")
        self.gridLayout_3.addWidget(self.columnTorsionConstant, 7, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 8, 0, 1, 1)
        self.columnShapeFactor = QtWidgets.QLineEdit(self.frame_3)
        self.columnShapeFactor.setObjectName("columnShapeFactor")
        self.gridLayout_3.addWidget(self.columnShapeFactor, 8, 1, 1, 2)
        self.gridLayout_6.addWidget(self.frame_3, 5, 0, 1, 4)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_30 = QtWidgets.QLabel(self.frame_4)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 2)
        self.beamMaterial = QtWidgets.QComboBox(self.frame_4)
        self.beamMaterial.setObjectName("beamMaterial")
        self.gridLayout_4.addWidget(self.beamMaterial, 0, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame_4)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 1, 0, 1, 2)
        self.beamSection = QtWidgets.QComboBox(self.frame_4)
        self.beamSection.setObjectName("beamSection")
        self.gridLayout_4.addWidget(self.beamSection, 1, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)
        self.beamYoungModulus = QtWidgets.QLineEdit(self.frame_4)
        self.beamYoungModulus.setObjectName("beamYoungModulus")
        self.gridLayout_4.addWidget(self.beamYoungModulus, 2, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 3, 0, 1, 1)
        self.beamShearModulus = QtWidgets.QLineEdit(self.frame_4)
        self.beamShearModulus.setObjectName("beamShearModulus")
        self.gridLayout_4.addWidget(self.beamShearModulus, 3, 1, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)
        self.beamArea = QtWidgets.QLineEdit(self.frame_4)
        self.beamArea.setObjectName("beamArea")
        self.gridLayout_4.addWidget(self.beamArea, 4, 1, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 5, 0, 1, 1)
        self.beamIyy = QtWidgets.QLineEdit(self.frame_4)
        self.beamIyy.setObjectName("beamIyy")
        self.gridLayout_4.addWidget(self.beamIyy, 5, 1, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 6, 0, 1, 1)
        self.beamIzz = QtWidgets.QLineEdit(self.frame_4)
        self.beamIzz.setObjectName("beamIzz")
        self.gridLayout_4.addWidget(self.beamIzz, 6, 1, 1, 2)
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 7, 0, 1, 1)
        self.beamTorsionConstant = QtWidgets.QLineEdit(self.frame_4)
        self.beamTorsionConstant.setObjectName("beamTorsionConstant")
        self.gridLayout_4.addWidget(self.beamTorsionConstant, 7, 1, 1, 2)
        self.label_24 = QtWidgets.QLabel(self.frame_4)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 8, 0, 1, 1)
        self.beamShapeFactor = QtWidgets.QLineEdit(self.frame_4)
        self.beamShapeFactor.setObjectName("beamShapeFactor")
        self.gridLayout_4.addWidget(self.beamShapeFactor, 8, 1, 1, 2)
        self.gridLayout_6.addWidget(self.frame_4, 5, 4, 1, 2)
        self.addSupport = QtWidgets.QCheckBox(self.centralwidget)
        self.addSupport.setObjectName("addSupport")
        self.gridLayout_6.addWidget(self.addSupport, 6, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 0, 0, 1, 3)
        self.addToBuilding = QtWidgets.QCheckBox(self.frame_5)
        self.addToBuilding.setObjectName("addToBuilding")
        self.gridLayout_5.addWidget(self.addToBuilding, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 1, 1, 1, 1)
        self.origin = QtWidgets.QLineEdit(self.frame_5)
        self.origin.setEnabled(False)
        self.origin.setObjectName("origin")
        self.gridLayout_5.addWidget(self.origin, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 7, 0, 1, 5)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setObjectName("cancel")
        self.gridLayout_6.addWidget(self.cancel, 8, 1, 1, 2)
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setObjectName("generate")
        self.gridLayout_6.addWidget(self.generate, 8, 3, 1, 2)
        self.generateAndOpen = QtWidgets.QPushButton(self.centralwidget)
        self.generateAndOpen.setObjectName("generateAndOpen")
        self.gridLayout_6.addWidget(self.generateAndOpen, 8, 5, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.buildingLength = QtWidgets.QSpinBox(self.frame)
        self.buildingLength.setMinimum(1)
        self.buildingLength.setProperty("value", 3)
        self.buildingLength.setObjectName("buildingLength")
        self.gridLayout.addWidget(self.buildingLength, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.buildingBreadth = QtWidgets.QSpinBox(self.frame)
        self.buildingBreadth.setMinimum(1)
        self.buildingBreadth.setProperty("value", 2)
        self.buildingBreadth.setObjectName("buildingBreadth")
        self.gridLayout.addWidget(self.buildingBreadth, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.buildingHeight = QtWidgets.QSpinBox(self.frame)
        self.buildingHeight.setMinimum(1)
        self.buildingHeight.setProperty("value", 3)
        self.buildingHeight.setObjectName("buildingHeight")
        self.gridLayout.addWidget(self.buildingHeight, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 3, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancel.clicked.connect(MainWindow.close)
        self.addToBuilding.clicked['bool'].connect(self.origin.setEnabled)
        self.frame2d.clicked['bool'].connect(self.buildingBreadth.setDisabled)
        self.frame2d.clicked['bool'].connect(self.roomBreadth.setDisabled)
        self.building.clicked['bool'].connect(self.buildingBreadth.setEnabled)
        self.building.clicked['bool'].connect(self.roomBreadth.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generate Building"))
        self.label_27.setText(_translate("MainWindow", "Name"))
        self.building.setText(_translate("MainWindow", "3D (Building)"))
        self.frame2d.setText(_translate("MainWindow", "2D (Frame)"))
        self.label.setText(_translate("MainWindow", "Building Dimension"))
        self.label_5.setText(_translate("MainWindow", "Room Dimension"))
        self.label_6.setText(_translate("MainWindow", "Length"))
        self.label_7.setText(_translate("MainWindow", "Breadth"))
        self.label_8.setText(_translate("MainWindow", "Height"))
        self.label_9.setText(_translate("MainWindow", "Column Properties"))
        self.label_10.setText(_translate("MainWindow", "Beam Properties"))
        self.label_28.setText(_translate("MainWindow", "Material"))
        self.label_29.setText(_translate("MainWindow", "Section"))
        self.label_12.setText(_translate("MainWindow", "E"))
        self.columnYoungModulus.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "G"))
        self.columnShearModulus.setText(_translate("MainWindow", "1"))
        self.label_13.setText(_translate("MainWindow", "Area"))
        self.columnArea.setText(_translate("MainWindow", "1"))
        self.label_15.setText(_translate("MainWindow", "Iyy"))
        self.columnIyy.setText(_translate("MainWindow", "1"))
        self.label_14.setText(_translate("MainWindow", "Izz"))
        self.columnIzz.setText(_translate("MainWindow", "1"))
        self.label_16.setText(_translate("MainWindow", "J"))
        self.columnTorsionConstant.setText(_translate("MainWindow", "1"))
        self.label_17.setText(_translate("MainWindow", "k"))
        self.columnShapeFactor.setText(_translate("MainWindow", "1.5"))
        self.label_30.setText(_translate("MainWindow", "Material"))
        self.label_31.setText(_translate("MainWindow", "Section"))
        self.label_18.setText(_translate("MainWindow", "E"))
        self.beamYoungModulus.setText(_translate("MainWindow", "1"))
        self.label_19.setText(_translate("MainWindow", "G"))
        self.beamShearModulus.setText(_translate("MainWindow", "1"))
        self.label_20.setText(_translate("MainWindow", "Area"))
        self.beamArea.setText(_translate("MainWindow", "1"))
        self.label_21.setText(_translate("MainWindow", "Iyy"))
        self.beamIyy.setText(_translate("MainWindow", "1"))
        self.label_22.setText(_translate("MainWindow", "Izz"))
        self.beamIzz.setText(_translate("MainWindow", "1"))
        self.label_23.setText(_translate("MainWindow", "J"))
        self.beamTorsionConstant.setText(_translate("MainWindow", "1"))
        self.label_24.setText(_translate("MainWindow", "k"))
        self.beamShapeFactor.setText(_translate("MainWindow", "1.5"))
        self.addSupport.setText(_translate("MainWindow", "Support"))
        self.label_26.setText(_translate("MainWindow", "Add to other Building/Fram"))
        self.addToBuilding.setText(_translate("MainWindow", "add"))
        self.label_25.setText(_translate("MainWindow", "Origin"))
        self.origin.setText(_translate("MainWindow", "(0,0,0)"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.generateAndOpen.setText(_translate("MainWindow", "Generate and Open"))
        self.frame.setStatusTip(_translate("MainWindow", "Length = No of rooms along length, Breadth= No of rooms along breadth, Height = No of floors"))
        self.label_2.setText(_translate("MainWindow", "Length"))
        self.label_3.setText(_translate("MainWindow", "Breadth"))
        self.label_4.setText(_translate("MainWindow", "Height"))
