from PySide2 import QtWidgets,QtGui
def calculator(self):
    if self.calculatorMode and self.actionCalculator.isChecked():
        self.actionCalculator.setChecked(True)
        self.calculator=QtWidgets.QLineEdit()
        self.calculator.setClearButtonEnabled(True)
        self.clabel=QtWidgets.QPushButton()
        self.clabel.setIcon(QtGui.QPixmap('ico\Tools\ToolCalculate.png'))
        self.statusbar.addPermanentWidget(self.clabel)
        self.statusbar.addPermanentWidget(self.calculator)
        self.calculator.setFocus()

        # self.gridLayout.addWidget(self.calculator)
        self.calculatorMode=False
        from solve import evalString
        import pyperclip
        from time import sleep
        self.showCalculator=False
        def data():
            currentText=self.calculator.text()
            output=evalString(currentText,precision=self.precison)
            pyperclip.copy(output)
            self.calculator.setText(f'{currentText}   >>>   {output}')
            self.statusbar.removeWidget(self.calculator)

            self.statusbar.showMessage(f'Output : {output}',)
        def openEditor():
            if self.showCalculator:
                self.calculator=QtWidgets.QLineEdit()
                self.calculator.setClearButtonEnabled(True)
                self.statusbar.addPermanentWidget(self.calculator)
                self.calculator.setFocus()

                self.calculator.returnPressed.connect(data)

                self.showCalculator=False

            else:
                self.statusbar.removeWidget(self.calculator)
                self.showCalculator=True
        self.calculator.returnPressed.connect(data)

        self.clabel.clicked.connect(openEditor)


    else:
        self.actionCalculator.setChecked(False)
        self.calculatorMode=True
        
        self.statusbar.removeWidget(self.calculator)
        self.statusbar.removeWidget(self.clabel)
