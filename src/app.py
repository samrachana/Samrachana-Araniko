
from structure3d.st3d import App
from PySide2 import QtWidgets
import sys
import qdarkstyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)   
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2()) 
    MainWindow = QtWidgets.QMainWindow()
    ui = App(MainWindow,app)
    # MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())

    #  self.segment.update(name=segmentName)
    #     self.segment.update(p1=(self.sd.p1x.text(),self.sd.p1y.text(),self.sd.p1z.text()))
    #     self.segment.update(p2=(self.sd.p2x.text(),self.sd.p2y.text(),self.sd.p2z.text()))
    #     self.segment.update(p3=(self.sd.p3x.text(),self.sd.p3y.text(),self.sd.p3z.text()))
    #     self.segment.update(youngsModulus=self.sd.youngsModulus.text())
    #     self.segment.update(shearModulus=self.sd.shearModulus.text())
    #     self.segment.update(area=self.sd.area.text())
    #     self.segment.update(ixx=self.sd.ixx.text())
    #     self.segment.update(axisVector=self.sd.axisVector.text())
    #     self.segment.update(iyy=self.sd.iyy.text())


