from PySide2.QtGui import QTextDocument
from report.report import generateReport2d, generateReport2dTruss
from sdPy.functionDefinitions import apply
from sdPy.simulationMethods import simulateFrameMotion2D, simulateTrussMotion2, vectorDiagramDataAngles2Dcomp, vectorDiagramDataMoments2D,vectorDiagramDataForces2D,vectorDiagramDataForces2Dcomp
from sdPy.simulationMethods import fillAnimationFrames, getRescaledData, makeFunData
from sdPy.loadMethods import loadPlotData2
from sdPy.simulationMethods import vectorDiagramDataDisps2Dcomp
from UI.generateReport import Ui_Dialog
from PySide2.QtWidgets import QDialog,QFileDialog
from sdPy.simulationMethods import vectorDiagramDataTrussDisps2Dcomp,simulateTrussMotion2,vectorDiagramDataTrussForces2Dcomp

import os
def generateReport(self):
    if self.structure:
        self.gR=QDialog(parent=self.MainWindow)
        self.gr=Ui_Dialog()
        self.gr.setupUi(self.gR)
        if self.fileName:
            fileName=os.path.splitext(self.fileName)[0]+'.html'
        else:
            fileName='Untitled'+'.html'
        self.gr.filePath.setText(fileName)
        def getFileName():
            fileName, _ = QFileDialog.getSaveFileName(caption="Save File")
            if fileName=='': self.statusbar.showMessage('File not saved, Enter proper file name to save file',2000); return;
            if not fileName.endswith(('.html','htm')):
                fileName=fileName + ".html"
            else:
                fileName= fileName 
            self.gr.filePath.setText(fileName)

        def getAttributes():
            author = self.gr.author.text()
            organization= self.gr.organization.text()
            address= self.gr.address.text()
            fileName = self.gr.filePath.text()
            if not fileName.endswith(('.html','htm')):
                fileName=fileName+'.html'
            else:
                fileName= fileName         
            folderName=os.path.splitext(fileName)[0]
            # try:
            #     os.mkdir(folderName)
            # except:
            #     self.statusbar.showMessage('Error while creating file. Permission denied')
            #     return
          #generateframe 
            frame=self.structure               
            frameData = self.matrix
            shear = self.shearMode
            inextensible= self.inextensibleMode
            simplify= True
            mainDf=self.df[self.df['Flag']==True][['Name','Class','Robject']]
            if self.currentUnit=='SI':
                units=[str(self.force)+'N',
                    str(self.length)+'m',
                    self.temperature]
            else:
                units=[str(self.force)+'pdl',
                    str(self.length)+'ft',
                    self.temperature]                
            precision= self.precison
            self.statusbar.showMessage('Generating Report . . .')
            self.app.processEvents()
            if not self.trussMode:
                axialForceData = apply(lambda x: vectorDiagramDataForces2Dcomp(x,frameData,'x',shear,inextensible,simplify,20,1),frame['segments'])
                afScale, axialForceData = getRescaledData(frame['segments'],axialForceData)
                self.app.processEvents()
                shearForceData = apply(lambda x: vectorDiagramDataForces2Dcomp(x,frameData,'y',shear,inextensible,simplify,20,1),frame['segments'])
                sfScale, shearForceData = getRescaledData(frame['segments'],shearForceData)
                self.app.processEvents()
                bendingMomentData = apply(lambda x: vectorDiagramDataMoments2D(x,frameData,None,shear,inextensible,simplify,20,1),frame['segments'])
                bmScale, bendingMomentData = getRescaledData(frame['segments'],bendingMomentData)
                self.app.processEvents()
                slopeData = apply(lambda x: vectorDiagramDataAngles2Dcomp(x,frameData,None,shear,inextensible,simplify,20,1),frame['segments'])
                agScale, slopeData = getRescaledData(frame['segments'],slopeData)
                self.app.processEvents()
                axialDisplacementData = apply(lambda x: vectorDiagramDataDisps2Dcomp(x,frameData,'x',shear,inextensible,simplify,20,1),frame['segments'])
                adScale, axialDisplacementData = getRescaledData(frame['segments'],axialDisplacementData)
                self.app.processEvents()
                shearDisplacementData = apply(lambda x: vectorDiagramDataDisps2Dcomp(x,frameData,'y',shear,inextensible,simplify,20,1),frame['segments'])
                sdScale, shearDisplacementData = getRescaledData(frame['segments'],shearDisplacementData)
                self.app.processEvents()
                motionData = simulateFrameMotion2D(frame,frameData,shear,inextensible,20,1)
                motScale, motionData = getRescaledData(frame['segments'],makeFunData(motionData))
                self.app.processEvents()
                zoomFactorActions=[afScale,sfScale,bmScale]
                zoomFactorResponses=[agScale,adScale,sdScale]
                zoomFactorMotion = motScale
                self.app.processEvents()
                html=generateReport2d(mainDf, frameData, axialForceData, shearForceData, bendingMomentData, zoomFactorActions, slopeData, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion, units=units, precision=precision, author=author,organization=organization,address=address,fileName=folderName)
                self.app.processEvents()

                


            else:
          #generatetruss

                axialForceData = apply(lambda x: vectorDiagramDataTrussForces2Dcomp(x,frameData,'x',False,False,True,20,1),frame['segments'])
                afScale, axialForceData = getRescaledData(frame['segments'],axialForceData)
                axialDisplacementData = apply(lambda x: vectorDiagramDataTrussDisps2Dcomp(x,frameData,'x',False,False,True,20,1),frame['segments'])
                adScale, axialDisplacementData = getRescaledData(frame['segments'],axialDisplacementData)
                self.app.processEvents()
                shearDisplacementData = apply(lambda x: vectorDiagramDataTrussDisps2Dcomp(x,frameData,'y',False,False,True,20,1),frame['segments'])
                sdScale, shearDisplacementData = getRescaledData(frame['segments'],shearDisplacementData)
                motionData = simulateTrussMotion2(frame,frameData,False,False,20,1)
                motScale, motionData = getRescaledData(frame['segments'],makeFunData(motionData))
                zoomFactorActions=[afScale,0,0]
                zoomFactorResponses=[0,adScale,sdScale]
                zoomFactorMotion = motScale
                self.app.processEvents()
                html=generateReport2dTruss(mainDf, frameData, axialForceData, zoomFactorActions, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion, units=units, precision=precision, author=author,organization=organization,address=address,fileName=folderName)
                self.app.processEvents()

            self.statusbar.showMessage('Report generation completed',5000)

            with open(fileName,'w',encoding='utf8') as f:
                f.write(html)

            import re
            newFileName=re.sub(r'/','\\\\',fileName)
            self.app.processEvents()
            os.system(newFileName)
            self.app.processEvents()
        self.gr.Browse.clicked.connect(getFileName)
        self.gr.buttonBox.accepted.connect(getAttributes)
        self.gR.show()

    else:
        self.statusbar.showMessage('Please analyse the structure first [ALT+A]',5000)