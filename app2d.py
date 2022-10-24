import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication,QSplashScreen
from PySide2.QtCore import Qt
from sampleDatas import resource_path
from multiprocessing import freeze_support
if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts) 
    freeze_support()
    app = QApplication(sys.argv)  
    
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) 
    pixmap = QPixmap(resource_path("./ico/splash.png"))
    splash = QSplashScreen(pixmap)
    # splash = QSplashScreen(pixmap,Qt.WindowStaysOnTopHint)
    
    splash.showMessage("<h3><font color='blue'>Loading .     5%</font></h3>",Qt.AlignBottom)

    splash.showMessage("<h3><font color='blue'>Loading . . . 10%</font></h3>",Qt.AlignBottom)
    splash.show()

    splash.showMessage("<h3><font color='blue'>Loading .     20%</font></h3>",Qt.AlignBottom)
    from PySide2.QtCore import Signal,QObject,Qt,Slot
    from PySide2.QtWidgets import QMessageBox,QMainWindow
    from threads import WorkerSignals

    splash.showMessage("<h3><font color='blue'>Loading . .   30%</font></h3>",Qt.AlignBottom)

    from structure2d.fileOperations2d import saveFile
    splash.showMessage("<h3><font color='blue'>Loading . . . 40%</font></h3>",Qt.AlignBottom)

    class Signals(QObject):
        def __init__(self):
            self.signals=WorkerSignals()
        @Slot()
        def signal(self):
            self.signals.finished.emit()
    splash.showMessage("<h3><font color='blue'>Loading .     50%</font></h3>",Qt.AlignBottom)
    class MainWindow(QMainWindow):
        def __init__(self, parent=None, arg=None):
            super().__init__(parent=parent)
            self.signals=WorkerSignals()  

        def closeEvent(self,event):
            event.ignore()
            ret = QMessageBox.question(self, "The structure has been modified.\n"," Do you want to save your changes?",
                                QMessageBox.Save | QMessageBox.Discard
                                | QMessageBox.Cancel)
            if ret==QMessageBox.Save:
                Signals.signal(self)
                
                event.accept()
            elif ret==QMessageBox.Discard:
                event.accept()






    splash.showMessage("<h3><font color='blue'>Loading . .   60%</font></h3>",Qt.AlignBottom)

    from getCss import css
    app.setStyleSheet(css('light',app.primaryScreen().availableGeometry().height()))

    splash.showMessage("<h3><font color='blue'>Loading . . . 70%</font></h3>",Qt.AlignBottom)

    MainWindow = MainWindow()
    
    from structure2d.st2d import Window2d
    splash.showMessage("<h3><font color='blue'>Loading .     80%</font></h3>",Qt.AlignBottom)
    if len(sys.argv)>1:
        ui = Window2d(MainWindow,app,sys.argv[1])
    else:
        ui = Window2d(MainWindow,app)

    from PySide2.QtWidgets import QSizePolicy
    
    # MainWindow.showMaximized()
    splash.showMessage("<h3><font color='blue'>Loading . .   99%</font></h3>",Qt.AlignBottom)

    MainWindow.show()
    splash.showMessage("<h3><font color='blue'>Loading . . . 100%</font></h3>",Qt.AlignBottom)


    splash.finish(MainWindow)
    # print(time()-t)
    sys.exit(app.exec_())  


    # def closeEvent(self,event):
    #     event.ignore()
    #     ret = QMessageBox.question(self, "The structure has been modified.\n"," Do you want to save your changes?",
    #                            QMessageBox.Save | QMessageBox.Discard
    #                            | QMessageBox.Cancel)
    #     if ret==QMessageBox.Save:
    #         Signals.signal(self)
            
    #         event.accept()
    #     elif ret==QMessageBox.Discard:
    #         event.accept()
    # @classmethod       




            # msgBox=QMessageBox 
        # msgBox.setText("You have unsaved structure");
        # msgBox.setInformativeText("Do you want to save your changes and Exit?");
        # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel);
        # msgBox.setDefaultButton(QMessageBox.Save)
        # ret = msgBox.exec()
        # if ret==QMessageBox.Save():
        #     save()


        # messageBox=QMessageBox(self,"Close Confirmation")
        # messageBox.question(self,'You have unsaved changes')
        # saveButton=QPushButton('Save and Exit')

        # saveButton.clicked.connect(save)
        # messageBox.addButton(saveButton)
        # messageBox.addButton('Don't Save',QMessageBox.Yes)
        # messageBox.addButton('Cancel',QMessageBox.No)
        # if (QMessageBox.Yes == QMessageBox.question(self, , "Are you sure, you want to Exit?")):
        #     event.accept()