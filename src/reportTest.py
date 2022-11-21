from report.report import generateReport2d,generateReport2dTruss
from sdPy.functionDefinitions import apply, dictInArr, make2d, structify2d, rowPos, unit
from sdPy.structureMethods import frame2d, truss2d
from sdPy.simulationMethods import getRescaledData, makeFunData, vectorDiagramDataForces2Dcomp, vectorDiagramDataMoments2D, vectorDiagramDataAngles2Dcomp, vectorDiagramDataDisps2Dcomp, simulateFrameMotion2D, vectorDiagramDataTrussForces2Dcomp, vectorDiagramDataTrussDisps2Dcomp, simulateTrussMotion2
def testDfFrame():
    AB = ['line',array([3,6]),array([3,11]),'',1,1,1,1,1,1,0]
    BC = ['line',array([3,11]),array([13,11]),array([5,15]),1,1,1,1,1,1,0]
    CD = ['line',array([13,11]),array([13,6]),'',1,1,1,1,1,1,0]
    h1 = ['Hinge',array([3,6]),array([0,0,0]),array([0,1])]
    h2 = ['Hinge',array([13,6]),array([0,0,0]),array([0,1])]
    ul = [0,make2d(BC),array([3,11]),array([13,11]),array([0,-1]),1]
    Name = ['AB','BC','CD','h1','h2','ul']
    Class = ['segment','segment','segment','support','support','load']
    Robject = [make2d(x) for x in [AB,BC,CD,h1,h2,ul]]
    frame = structify2d(Robject)
    frameData = frame2d(frame,False,False,False)
    axialForceData = apply(lambda x: vectorDiagramDataForces2Dcomp(x,frameData,'x',False,False,True,20,1),frame['segments'])
    afScale, axialForceData = getRescaledData(frame['segments'],axialForceData)
    shearForceData = apply(lambda x: vectorDiagramDataForces2Dcomp(x,frameData,'y',False,False,True,20,1),frame['segments'])
    sfScale, shearForceData = getRescaledData(frame['segments'],shearForceData)
    bendingMomentData = apply(lambda x: vectorDiagramDataMoments2D(x,frameData,None,False,False,True,20,1),frame['segments'])
    bmScale, bendingMomentData = getRescaledData(frame['segments'],bendingMomentData)
    slopeData = apply(lambda x: vectorDiagramDataAngles2Dcomp(x,frameData,None,False,False,True,20,1),frame['segments'])
    agScale, slopeData = getRescaledData(frame['segments'],slopeData)
    axialDisplacementData = apply(lambda x: vectorDiagramDataDisps2Dcomp(x,frameData,'x',False,False,True,20,1),frame['segments'])
    adScale, axialDisplacementData = getRescaledData(frame['segments'],axialDisplacementData)
    shearDisplacementData = apply(lambda x: vectorDiagramDataDisps2Dcomp(x,frameData,'y',False,False,True,20,1),frame['segments'])
    sdScale, shearDisplacementData = getRescaledData(frame['segments'],shearDisplacementData)
    motionData = simulateFrameMotion2D(frame,frameData,False,False,20,1)
    motScale, motionData = getRescaledData(frame['segments'],makeFunData(motionData))

    return {'mainDf': DataFrame({'Name':Name,'Class':Class,'Robject':Robject}),
            'frameData': frameData,
            'axialForceData':axialForceData,
            'shearForceData':shearForceData,
            'bendingMomentData':bendingMomentData,
            'zoomFactorActions':[afScale,sfScale,bmScale],
            'slopeData':slopeData,
            'axialDisplacementData':axialDisplacementData,
            'shearDisplacementData':shearDisplacementData,
            'zoomFactorResponses':[agScale,adScale,sdScale],
            'motionData':motionData,
            'zoomFactorMotion':motScale}
def testDfTruss():
    AB = ['line',array([3,3]),array([6,6]),'',1,1,1,1,1,1,0]
    BC = ['line',array([6,6]),array([9,3]),array([5,15]),1,1,1,1,1,1,0]
    CA = ['line',array([9,3]),array([3,3]),'',1,1,1,1,1,1,0]
    h1 = ['Hinge',array([3,3]),array([0,0,0]),array([0,1])]
    h2 = ['Hinge',array([9,3]),array([0,0,0]),array([0,1])]
    pl = [-1,make2d(BC),array([6,6]),array([6,6]),array([0,-1]),1]
    Name = ['AB','BC','CA','h1','h2','pl']
    Class = ['segment','segment','segment','support','support','load']
    Robject = [make2d(x) for x in [AB,BC,CA,h1,h2,pl]]
    frame = structify2d(Robject)
    frameData = truss2d(frame)
    axialForceData = apply(lambda x: vectorDiagramDataTrussForces2Dcomp(x,frameData,'x',False,False,True,20,1),frame['segments'])
    afScale, axialForceData = getRescaledData(frame['segments'],axialForceData)
    axialDisplacementData = apply(lambda x: vectorDiagramDataTrussDisps2Dcomp(x,frameData,'x',False,False,True,20,1),frame['segments'])
    adScale, axialDisplacementData = getRescaledData(frame['segments'],axialDisplacementData)
    shearDisplacementData = apply(lambda x: vectorDiagramDataTrussDisps2Dcomp(x,frameData,'y',False,False,True,20,1),frame['segments'])
    sdScale, shearDisplacementData = getRescaledData(frame['segments'],shearDisplacementData)
    motionData = simulateTrussMotion2(frame,frameData,False,False,20,1)
    motScale, motionData = getRescaledData(frame['segments'],makeFunData(motionData))

    return {'mainDf': DataFrame({'Name':Name,'Class':Class,'Robject':Robject}),
            'frameData': frameData,
            'axialForceData':axialForceData,
            'zoomFactorActions':[afScale,0,0],
            'axialDisplacementData':axialDisplacementData,
            'shearDisplacementData':shearDisplacementData,
            'zoomFactorResponses':[0,adScale,sdScale],
            'motionData':motionData,
            'zoomFactorMotion':motScale}

generateReport2dTruss(**testDfFrame())