from PySide2 import QtCore
# from rbindings import R
from sdPy.segmentMethods import actionData,responseData,trussActionData,trussResponseData



class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished = QtCore.Signal()
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(int)
class WorkerThread2(QtCore.QRunnable):

    def __init__(self,robj,structure,matrix,no=20,trussMode=False,shear=False,inextensible=True):
        super(WorkerThread2, self).__init__()
        self.robj=robj
        self.structure=structure
        self.matrix=matrix
        self.NoOfPoints=no
        self.trussMode=trussMode
        self.shear=shear
        self.inextensible=inextensible
        # self.finished=QtCore.Signal()
        self.signals = WorkerSignals()    
    @QtCore.Slot()
    def run(self):
        # actiondata=actionData(self.robj,self.structure,self.matrix['action']) 
        if not self.trussMode:
            actiondata=actionData(self.robj,self.matrix['simplified'],self.matrix['actionRaw'],self.NoOfPoints)       
            responsedata= responseData(self.robj,self.matrix,self.shear,self.inextensible,self.NoOfPoints)       
        else:
            actiondata=trussActionData(self.robj,self.matrix['simplified'],self.matrix['actionRaw'])       
            responsedata= trussResponseData(self.robj,self.matrix)             
        self.signals.result.emit([actiondata,responsedata])
        self.signals.finished.emit() 


class WorkerThread(QtCore.QRunnable):

    def __init__(self,function,df,analysisParameters=None):
        super(WorkerThread, self).__init__()
        self.df=df
        self.function=function
        self.analysisParameters=analysisParameters
        self.signals = WorkerSignals()    
    @QtCore.Slot()
    def run(self):
        try: 

            if self.analysisParameters:
                matrix=self.function(self.df,
                inextensible=self.analysisParameters['inextensible'],
                shear=self.analysisParameters['shear'],
                simplified=self.analysisParameters['simplify'],
                simFac=self.analysisParameters['structureAnalysisAccuracy'])
            else:
                matrix=self.function(self.df)       
            self.signals.result.emit(matrix)
            self.signals.finished.emit()
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            # self.host.statusbar.showMessage(str(e),5000)
            self.signals.result.emit(None)
            self.signals.finished.emit()         



class MultiThread(QtCore.QRunnable):

    def __init__(self,function,indexedParameters,parameters,keys):
        super(MultiThread, self).__init__()
        self.function=function
        self.indexedParameters=indexedParameters
        self.parameters=parameters
        self.keys=keys
        self.signals = WorkerSignals()    
    @QtCore.Slot()
    def run(self):
        try: 
            print(self.keys)
            output={}
            # output={i:self.function(*[x[i] for x in self.indexedParameters],
            # *self.parameters) for i in self.keys }
            for i in self.keys:
                output[i]=self.function(*[x[i] for x in self.indexedParameters],*self.parameters)
                print(i)
            self.signals.result.emit(output)
            self.signals.finished.emit()
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            # self.host.statusbar.showMessage(str(e),5000)
            self.signals.result.emit(None)
            self.signals.finished.emit()         



class Apply(QtCore.QRunnable):

    def __init__(self,function,keys,parameters):
        super(Apply, self).__init__()
        self.function=function
        self.keys=keys
        self.parameters=parameters
        self.signals = WorkerSignals()    
    @QtCore.Slot()
    def run(self):
        matrix={}
        try: 
            for i in self.keys:
                matrix[i]=self.function(self.parameters[0][i],*self.parameters[1:])       
            self.signals.result.emit(matrix)
            self.signals.finished.emit()
        except Exception as e:
            print(e)
            # self.host.statusbar.showMessage(str(e),5000)
            self.signals.result.emit(None)
            self.signals.finished.emit()    


#axial, sheary, shearz, twist, bendy, bendz
# axial, deflecty, deflectz, twist, slopey, slopez 