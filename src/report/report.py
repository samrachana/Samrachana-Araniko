from sampleDatas import resource_path
from numpy import array, cross, nanmax, nanmin, vstack
from numpy.linalg import norm
from pandas import DataFrame
from sdPy.functionDefinitions import dictInArr, rowPos, unit, apply
from datetime import datetime as dt

joinThings = lambda tag,attrs,content : "<"+tag+ " " + attrs+" "+">"+content+"</"+tag+">"
breakLine = joinThings('hr','','')
pageBreak = joinThings('p',"class='pb'",'...')

final = "</div></body></html>"
styleSheet = ""
with open('./report/style.min.css', 'r') as file:
    styleSheet = file.read().replace('\n', '')
from sampleDatas import resource_path
RP = lambda x: '/'.join(resource_path(x).split('\\'))
initial = "<!DOCTYPE html><html><head><meta charset = 'utf-8'>\
            <title class='title'>Samrachana-Araniko | Structure Analysis Report</title>" + \
                joinThings('style','',styleSheet)+\
                    "</head><body><div class='container'>"

from sdPy.segmentMethods import segPlotData2, segEqn
from sdPy.loadMethods import loadPlotData2, loadPlotData4
from sdPy.supportMethods import supportPlotData2

C = ['purple','green','red','blue']

def svgPlot(points,**attributes):
    d = f"M {points[0][0]} {points[0][1]} {' '.join(['L '+str(x).replace('. ',' ').replace('.]',']')[1:-1] for x in points[1:]])}"
    attributes = ' '.join([f'{x}="{attributes[x]}"' for x in attributes])
    return f"<path d='{d}' {attributes}></path>".replace("___",'').replace('__',':').replace('_','-')

def svgAnnotate(text,coord,**attributes):
    font_size = attributes['font_size']
    attributes = ' '.join([f'{x}="{attributes[x]}"' for x in attributes])
    return svgPlot(vstack((
                coord - array([font_size*len(text)/4,font_size/2]),
                coord + array([font_size*len(text)/4,-font_size/2]),
                coord + array([font_size*len(text)/4,font_size/2]),
                coord + array([-font_size*len(text)/4,font_size/2]),
                coord - array([font_size*len(text)/4,font_size/2])
            )),fill='white',stroke='none',opacity=0.5) + \
                f"<text x='{coord[0]}' y='{coord[1]}' text-anchor = 'middle' transform = 'scale(1,-1) translate(0.05,{0.25-2*coord[1]})' \
                    {attributes}>{text}</text>".replace("___",'').replace('__',':').replace('_','-') 

def svgArrow(start,end,width,**attributes):
    xv = unit(end-start)
    yv = array([-xv[1],xv[0]])
    return svgPlot(vstack((
        start+(width*yv)/4,
        end-width*xv+(width*yv)/4,
        end-width*(xv-yv),
        end,
        end-width*(xv+yv),
        end-width*xv-(width*yv)/4,
        start-(width*yv)/4,
        start+(width*yv)/4
    )),**attributes)

def svgArc(start,xRad,yRad,rot,large_Arc,sweep,end,**attributes):
    attributes = ' '.join([f'{x}="{attributes[x]}"' for x in attributes])
    return f'''<path d = 'M {start[0]} {start[1]} A {xRad} {yRad} {rot} {large_Arc} {sweep} {end[0]} {end[1]}' {attributes}></path>'''.replace("___",'').replace('__',':').replace('_','-')

# GRAPH_DPI = 2000
# GRAPH_SIZE = (4,4)
def plotOnSegments(segDf, funData, zoomFactor,index,precision,cut=True,location='.'):
    # plt.rcParams['figure.dpi']=GRAPH_DPI
    # plt.rcParams['figure.figsize']=GRAPH_SIZE
    # plt.gca().set_aspect('equal')
    # plt.axis('off')
    table = DataFrame({'Member':[],'Minimum':[],'Maximum':[]})
    wt = min(0.75,0.4*min(apply(lambda x: norm(x['P3']-x['P1']),segDf.Robject)))
    svgHead = ''
    maxCoord = [-99999]*2
    minCoord = [99999]*2
    for i in range(len(segDf)):
        xs, fs, fdata, x = list(funData[i][:,0]), list(funData[i][:,-1]), funData[i][:,1:-1], segDf.Robject[i]
        if cut:
            xs,fs = xs[1:-1],fs[1:-1]
        e = lambda t: segEqn(x['type'],array([0,*x['P1']]),array([0,*x['P3']]),t,array([0,*x['P2']]))[1:]
        P2=e(0.5*norm(x['P3']-x['P1']))
        # wt = min(1,0.4*norm(x['P3']-x['P1']))
        xv = 0.75*unit(x['P3']-x['P1'])*wt
        yv = 0.75*unit(cross(array([1,0,0]),array([0,*xv]))[1:])*wt
        svgHead += svgArrow(P2,P2+xv,width=0.1*wt,stroke_width=0.05*wt,stroke=C[0],opacity=0.25)
        svgHead += svgArrow(P2,P2+yv,width=0.1*wt,stroke_width=0.05*wt,stroke=C[0],opacity=0.25)
        data = segPlotData2(x['type'],x['P1'],x['P3'],1,P2,50)
        svgHead += svgPlot(data,stroke=C[0],stroke_width=0.035,opacity=0.5)
        svgHead += svgPlot(fdata,stroke=C[2],stroke_width=0.05)
        svgHead += svgAnnotate(segDf.Name[i],P2,fill=C[0], opacity=0.75,font_size=0.5*wt)
        minIndex, maxIndex = fs.index(min(fs)), fs.index(max(fs))
        xmin, fmin, xmax, fmax = xs[minIndex], fs[minIndex], xs[maxIndex], fs[maxIndex]
        if cut:
            fdata = fdata[1:-1]
        minLine = array([e(xmin),fdata[minIndex]])
        maxLine = array([e(xmax),fdata[maxIndex]])
        svgHead += svgPlot(minLine,stroke_width=0.065,opacity=0.25,stroke=C[1])
        svgHead += svgAnnotate(str(round(fmin/zoomFactor,precision)),minLine[1],fill=C[2],font_size=0.5*wt)
        svgHead += svgPlot(maxLine,stroke_width=0.065,opacity=0.25,stroke=C[3])
        svgHead += svgAnnotate(str(round(fmax/zoomFactor,precision)),maxLine[1],fill=C[1],font_size=0.5*wt)
        table = table.append({'Member':segDf.Name[i],
                        'Minimum':f'{round(fmin/zoomFactor,precision)} @ {round(xmin,precision)}', 
                        'Maximum':f'{round(fmax/zoomFactor,precision)} @ {round(xmax,precision)}'},ignore_index=True)
        maxCoord = [max([maxCoord[0],nanmax(fdata[:,0])]),max([maxCoord[1],nanmax(fdata[:,1])])]
        minCoord = [min([minCoord[0],nanmin(fdata[:,0])]),min([minCoord[1],nanmin(fdata[:,1])])] 
    # plt.savefig(f'{location}/temp{index}.svg',pad_inches=0,bbox_inches='tight',transparent=True)
    offset = max([3,0.25*min([maxCoord[0]-minCoord[0],maxCoord[1]-minCoord[1]])])
    return f'''<svg style = 'fill:none' transform='translate(0,{(maxCoord[1]-minCoord[1])/2}) scale(1,-1)' \
                        viewBox='{minCoord[0]-offset} {minCoord[1]-offset} {maxCoord[0]-minCoord[0]+2*offset} {maxCoord[1]-minCoord[1]+2*offset}'>'''+\
                            svgHead + '</svg>', table

def plotGraphs(segDf, lodDf, supDf, nodeMatrix, frameData, axialForceData, shearForceData, bendingMomentData, zoomFactorActions, slopeData, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion, precision,location):
    # plt.rcParams['figure.dpi']=GRAPH_DPI
    # plt.rcParams['figure.figsize']=GRAPH_SIZE
    # plt.gca().set_aspect('equal')
    # plt.axis('off')
    wt = min(0.75,0.4*min(apply(lambda x: norm(x['P3']-x['P1']),segDf.Robject)))
    maxCoord = [-999999]*2
    minCoord = [999999]*2
    svgHead = ''
    for x in segDf.Robject:
        data = segPlotData2(x['type'],x['P1'],x['P3'],1,x['P2'],50)
        maxCoord[0] = nanmax([nanmax(data[:,0]),maxCoord[0]])
        maxCoord[1] = nanmax([nanmax(data[:,1]),maxCoord[1]])
        minCoord[0] = nanmin([nanmin(data[:,0]),minCoord[0]])
        minCoord[1] = nanmin([nanmin(data[:,1]),minCoord[1]])
        svgHead += svgPlot(data,stroke=C[0],stroke_width=0.05)
    for x in lodDf.Robject:
        if x['degree'] > -3:
            data = loadPlotData2(50*x['P1'],50*x['P3'],50*x['parentSegment']['P1'],50*x['parentSegment']['P3'],50*x['parentSegment']['P2'],x['degree'],50*x['peak'],x['normal'],x['parentSegment']['type'],1,1)/50
        else:
            data = loadPlotData4(x['parentSegment'],x['degree'],1)/50
        maxCoord[0] = nanmax([nanmax(data[:,0]),maxCoord[0]])
        maxCoord[1] = nanmax([nanmax(data[:,1]),maxCoord[1]])
        minCoord[0] = nanmin([nanmin(data[:,0]),minCoord[0]])
        minCoord[1] = nanmin([nanmin(data[:,1]),minCoord[1]])
        svgHead += svgPlot(data,stroke=C[2],stroke_width=0.035)
    for x in supDf.Robject:
        if x['type'] == 'Node' or x['type'] == '000':
            pass
        else:
            data = supportPlotData2(x['type'],x['location']*50,1,x['normal'])/50
            maxCoord[0] = nanmax([nanmax(data[:,0]),maxCoord[0]])
            maxCoord[1] = nanmax([nanmax(data[:,1]),maxCoord[1]])
            minCoord[0] = nanmin([nanmin(data[:,0]),minCoord[0]])
            minCoord[1] = nanmin([nanmin(data[:,1]),minCoord[1]])
            svgHead += svgPlot(data,stroke=C[3],stroke_width=0.025)  
    for x in range(1,nodeMatrix.shape[0]+1):
        svgHead += svgAnnotate(str(x),nodeMatrix[x-1]+array([0.2*wt,-0.2*wt]),fill=C[0],font_size=0.6*wt)
    
    offset = max([3,0.25*min([maxCoord[0]-minCoord[0],maxCoord[1]-minCoord[1]])])
 
    svgPlot1 = f'''<svg style = 'fill:none' transform='translate(0,{(maxCoord[1]-minCoord[1])/2}) scale(1,-1)' \
                        viewBox='{minCoord[0]-offset} {minCoord[1]-offset} {maxCoord[0]-minCoord[0]+2*offset} {maxCoord[1]-minCoord[1]+2*offset}'>'''+svgHead+'</svg>'

    # plt.savefig(f'{location}/temp1.svg',pad_inches=0,bbox_inches='tight',transparent=True)
    rxnTbl = frameData['reactions'][:,2:]
    for x in supDf.Robject:
        loc = x['location']
        i = rowPos(loc,nodeMatrix)
        if type(i)!=type(False) and x['type'] not in ['Node','000']:
            svgHead += svgArc(loc+array([0,wt]),wt,wt,0,1,1,loc+array([wt,-0.15*wt]),stroke_width=0.1*wt,stroke=C[1],opacity=0.75)
            svgHead += svgPlot(vstack((
                loc+array([0.8*wt,-0.3*wt]),
                loc+array([wt,-0.1*wt]),
                loc+array([1.2*wt,-0.3*wt]),
                loc+array([0.8*wt,-0.3*wt])
            )),transform=f'rotate(-15, {loc[0]+wt}, {loc[1]-0.3*wt}) translate({-0.025*wt},0)',fill=C[1],stroke='none',opacity=0.75)
            svgHead += svgArrow(loc,loc+array([2*wt,0]),width=0.2*wt,fill=C[1],stroke='none',opacity=0.75)
            svgHead += svgArrow(loc,loc+array([0,2*wt]),width=0.2*wt,fill=C[1],stroke='none',opacity=0.75)
            rxns = rxnTbl[i]
            svgHead += svgAnnotate(f'Fx = {round(rxns[0],precision)}',(loc[0]+2.75*wt,loc[1]-0.5*wt),fill=C[1],font_size=0.6*wt)
            svgHead += svgAnnotate(f'Fy = {round(rxns[1],precision)}',(loc[0]+0.5*wt,loc[1]+2.5*wt),fill=C[1],font_size=0.6*wt)
            svgHead += svgAnnotate(f'M = {round(rxns[2],precision)}',(loc[0],loc[1]-1.5*wt),fill=C[1],font_size=0.6*wt)

    svgPlot2 = f'''<svg style = 'fill:none' transform='translate(0,{(maxCoord[1]-minCoord[1])/2}) scale(1,-1)' \
                        viewBox='{minCoord[0]-0.75*offset} {minCoord[1]-offset} {maxCoord[0]-minCoord[0]+2*offset} {maxCoord[1]-minCoord[1]+2*offset}'>'''+svgHead+'</svg>'

    # plt.savefig(f'{location}/temp2.svg',pad_inches=0,bbox_inches='tight',transparent=True)
    # plt.close()
    
    svgPlot3, afTbl = plotOnSegments(segDf,axialForceData,zoomFactorActions[0],3,precision,True,location)
    svgPlot4, sfTbl = plotOnSegments(segDf,shearForceData,zoomFactorActions[1],4,precision,True,location)
    svgPlot5, bmTbl = plotOnSegments(segDf,bendingMomentData,zoomFactorActions[2],5,precision,True,location)
    svgPlot6, angTbl = plotOnSegments(segDf,slopeData,zoomFactorResponses[0],6,precision,True,location)
    svgPlot7, adTbl = plotOnSegments(segDf,axialDisplacementData,zoomFactorResponses[1],7,precision,True,location)
    svgPlot8, sdTbl = plotOnSegments(segDf,shearDisplacementData,zoomFactorResponses[2],8,precision,True,location)
    svgPlot9, moTbl = plotOnSegments(segDf,motionData,zoomFactorMotion,9,precision,False,location)

    return [svgPlot1,svgPlot2,svgPlot3,svgPlot4,svgPlot5,svgPlot6,svgPlot7,svgPlot8,svgPlot9],\
        [afTbl,sfTbl,bmTbl,angTbl,adTbl,sdTbl,moTbl]

def plotGraphsTruss(segDf, lodDf, supDf, nodeMatrix, frameData, axialForceData, zoomFactorActions, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion, precision,location):
    # plt.rcParams['figure.dpi']=GRAPH_DPI
    # plt.rcParams['figure.figsize']=GRAPH_SIZE
    wt = min(1,0.4*min(apply(lambda x: norm(x['P3']-x['P1']),segDf.Robject)))
    maxCoord = [-999999]*2
    minCoord = [999999]*2
    svgHead = ''
    for x in segDf.Robject:
        data = segPlotData2(x['type'],x['P1'],x['P3'],1,x['P2'],50)
        maxCoord[0] = nanmax([nanmax(data[:,0]),maxCoord[0]])
        maxCoord[1] = nanmax([nanmax(data[:,1]),maxCoord[1]])
        minCoord[0] = nanmin([nanmin(data[:,0]),minCoord[0]])
        minCoord[1] = nanmin([nanmin(data[:,1]),minCoord[1]])
        svgHead += svgPlot(data,stroke=C[0],stroke_width=0.035)
    for x in lodDf.Robject:
        if x['degree'] > -3:
            data = loadPlotData2(50*x['P1'],50*x['P3'],50*x['parentSegment']['P1'],50*x['parentSegment']['P3'],50*x['parentSegment']['P2'],x['degree'],50*x['peak'],x['normal'],x['parentSegment']['type'],1,1)/50
        else:
            data = loadPlotData4(x['parentSegment'],x['degree'],1)
        maxCoord[0] = nanmax([nanmax(data[:,0]),maxCoord[0]])
        maxCoord[1] = nanmax([nanmax(data[:,1]),maxCoord[1]])
        minCoord[0] = nanmin([nanmin(data[:,0]),minCoord[0]])
        minCoord[1] = nanmin([nanmin(data[:,1]),minCoord[1]])
        svgHead += svgPlot(data,stroke=C[2],stroke_width=0.035)
    for x in supDf.Robject:
        if x['type'] == 'Node' or x['type'] == '000':
            pass
        else:
            data = supportPlotData2(x['type'],x['location']*50,1,x['normal'])/50
            maxCoord[0] = nanmax([nanmax(data[:,0]),maxCoord[0]])
            maxCoord[1] = nanmax([nanmax(data[:,1]),maxCoord[1]])
            minCoord[0] = nanmin([nanmin(data[:,0]),minCoord[0]])
            minCoord[1] = nanmin([nanmin(data[:,1]),minCoord[1]])
            svgHead += svgPlot(data,stroke=C[3],stroke_width=0.025)  
    for x in range(1,nodeMatrix.shape[0]+1):
        svgHead += svgAnnotate(str(x),nodeMatrix[x-1]+array([0.2*wt,-0.2*wt]),fill=C[0],font_size=0.6*wt)
    
    offset = max([3,0.25*min([maxCoord[0]-minCoord[0],maxCoord[1]-minCoord[1]])])
 
    svgPlot1 = f'''<svg style = 'fill:none' transform='translate(0,{(maxCoord[1]-minCoord[1])/2}) scale(1,-1)' \
                        viewBox='{minCoord[0]-offset} {minCoord[1]-offset} {maxCoord[0]-minCoord[0]+2*offset} {maxCoord[1]-minCoord[1]+2*offset}'>'''+svgHead+'</svg>'

    # plt.savefig(f'{location}/temp1.svg',pad_inches=0,bbox_inches='tight',transparent=True)
    rxnTbl = frameData['reactions'][:,4:]
    for x in supDf.Robject:
        loc = x['location']
        i = rowPos(loc,nodeMatrix)
        if type(i)!=type(False) and x['type'] not in ['Node','000']:
            svgHead += svgArrow(loc,loc+array([2*wt,0]),width=0.2*wt,fill=C[1],stroke='none',opacity=0.75)
            svgHead += svgArrow(loc,loc+array([0,2*wt]),width=0.2*wt,fill=C[1],stroke='none',opacity=0.75)
            rxns = rxnTbl[i]
            svgHead += svgAnnotate(f'Fx = {round(rxns[0],precision)}',(loc[0]+2.75*wt,loc[1]-0.5*wt),fill=C[1],font_size=0.6*wt)
            svgHead += svgAnnotate(f'Fy = {round(rxns[1],precision)}',(loc[0]+0.5*wt,loc[1]+2.5*wt),fill=C[1],font_size=0.6*wt)

    svgPlot2 = f'''<svg style = 'fill:none' transform='translate(0,{(maxCoord[1]-minCoord[1])/2}) scale(1,-1)' \
                        viewBox='{minCoord[0]-0.75*offset} {minCoord[1]-offset} {maxCoord[0]-minCoord[0]+2*offset} {maxCoord[1]-minCoord[1]+2*offset}'>'''+svgHead+'</svg>'

    # plt.savefig(f'{location}/temp2.svg',pad_inches=0,bbox_inches='tight',transparent=True)
    # plt.close()
    
    svgPlot3, afTbl = plotOnSegments(segDf,axialForceData,zoomFactorActions[0],3,precision,True,location)
    svgPlot4, adTbl = plotOnSegments(segDf,axialDisplacementData,zoomFactorResponses[1],7,precision,True,location)
    svgPlot5, sdTbl = plotOnSegments(segDf,shearDisplacementData,zoomFactorResponses[2],8,precision,True,location)
    svgPlot6, moTbl = plotOnSegments(segDf,motionData,zoomFactorMotion,9,precision,False,location)

    return [svgPlot1,svgPlot2,svgPlot3,svgPlot4,svgPlot5,svgPlot6],\
        [afTbl,adTbl,sdTbl,moTbl]
   
extractNodeMatrix = lambda frameData: frameData['response'][:,:2]
extractNodeMatrixTruss = lambda frameData: frameData['response'][:,1:3]

def nodeTable(nodeMatrix):
    nodeDf = DataFrame(nodeMatrix,columns = ['X','Y'])
    nodeDf.index = ['Node '+str(nodeDf.index[x]+1) for x in range(len(nodeDf))]
    return joinThings('div',"class='dataFrame'", nodeDf.to_html(index=True,justify='center')+joinThings('figcaption',"class='caption'","Table 1: Coordinates of Nodes"))

def segmentTable(segments,nodes):
    segments.index = range(len(segments))
    segmentList = [[segments.Name[x]]+list(segments.Robject[x].values())[:-2] for x in range(len(segments))]
    segDf = DataFrame(segmentList,columns=['Name','Type','From','To','Through','E','G','A','I','k','\u03c1','\u03b1'])
    segDf.From = ['Node '+str(rowPos(segDf.From[x],nodes)+1) for x in range(len(segDf))]
    segDf.To = ['Node '+str(rowPos(segDf.To[x],nodes)+1) for x in range(len(segDf))]
    segTbl1 = joinThings('div',"class='dataFrame'",segDf[['Name','Type','From','To','Through']].to_html(index=False,justify='center')+
                joinThings('figcaption',"class='caption'","Table 2A: Members in the Structure [Coordinates]"))
    segTbl2 = joinThings('div',"class='dataFrame'",segDf[['Name','E','G','A','I','k','\u03c1','\u03b1']].to_html(index=False,justify='center')+
                joinThings('figcaption',"class='caption'","Table 2B: Members in the Structure [Properties]"))
    return segTbl1 + segTbl2

def getLoadType(x):
    return 'Temperature' if x==-4 else (
        'Misfit' if x==-3 else(
            'Moment' if x==-2 else(
                'Point' if x==-1 else(
                    'UDL' if x==0 else(
                        'UVL' if x==1 else(
                            f'Poly n={x}'
                        )
                    )
                )
            )
        )
    )

def loadTable(loads,segments):
    loads.index = range(len(loads))
    loadList = [[loads.Name[x]]+list(loads.Robject[x].values())[:-2] for x in range(len(loads))]
    lodDf = DataFrame(loadList,columns=['Name','Type','Acting On','From','To','Normal','Peak'])
    lodDf['Acting On'] = [segments.Name[dictInArr(lodDf['Acting On'][x],segments.Robject)] for x in range(len(lodDf))]
    lodDf['Type'] = [getLoadType(x) for x in lodDf['Type']]
    lodTbl = joinThings('div',"class='dataFrame'",lodDf.to_html(index=False,justify='center')+joinThings('figcaption',
                "class='caption'","Table 3: Loads in the Structure"))
    return lodTbl

def supportTable(supports):
    supports.index = range(len(supports))
    supportList = [[supports.Name[x]]+list(supports.Robject[x].values())[:-1] for x in range(len(supports))]
    supDf = DataFrame(supportList, columns = ['Name','Type','Location','Settlements [d\u03b8, dX, dY]', 'Normal'])
    supTbl = joinThings('div',"class='dataFrame'",supDf.to_html(index=False,justify='center')+joinThings('figcaption',
                "class='caption'","Table 4: Supports in the Structure"))
    return supTbl

def rxnTable(supDf,frameData,nodeMatrix,precision):
    rxns = frameData['reactions'][:,2:]
    supDf.index = range(len(supDf))
    rxnList = [[supDf.Name[x]]+list(rxns[rowPos(supDf.Robject[x]['location'],nodeMatrix)]) for x in range(len(supDf))]
    columns=['Support','Fx (\u2192)','Fy (\u2191)','M (\u21ba)']
    rxnDf = DataFrame(rxnList,columns=columns).round(precision).dropna(0)
    return  joinThings('div',"class='dataFrame'",rxnDf.to_html(index=False,justify='center')+joinThings('figcaption',
                "class='caption'","Table 5: Support Reactions"))

def dispTable(displacementData,precision):
    Names = ['Node '+str(x+1) for x in range(len(displacementData))]
    disDf = DataFrame({'Node':Names,
                        '\u0394x (\u2192)':displacementData[:,2],
                        '\u0394y (\u2191)':displacementData[:,3], 
                        '\u03b8 (\u21ba)': displacementData[:,4] }).round(precision)      
    return  joinThings('div',"class='dataFrame'",disDf.to_html(index=False,justify='center')+joinThings('figcaption',
                    "class='caption'",f"Table 13: Nodal Displacements"))

def rxnTableTruss(supDf,frameData,nodeMatrix,precision):
    rxns = frameData['reactions'][:,4:]
    supDf.index = range(len(supDf))
    rxnList = [[supDf.Name[x]]+list(rxns[rowPos(supDf.Robject[x]['location'],nodeMatrix)]) for x in range(len(supDf))]
    columns=['Support','Fx (\u2192)','Fy (\u2191)']
    rxnDf = DataFrame(rxnList,columns=columns).round(precision).dropna(0)
    return  joinThings('div',"class='dataFrame'",rxnDf.to_html(index=False,justify='center')+joinThings('figcaption',
                "class='caption'","Table 5: Support Reactions"))

def dispTableTruss(displacementData,precision):
    Names = ['Node '+str(x+1) for x in range(len(displacementData))]
    disDf = DataFrame({'Node':Names,
                        '\u0394x (\u2192)':displacementData[:,2],
                        '\u0394y (\u2191)':displacementData[:,3]}).round(precision)      
    return  joinThings('div',"class='dataFrame'",disDf.to_html(index=False,justify='center')+joinThings('figcaption',
                    "class='caption'",f"Table 9: Nodal Displacements"))

section = lambda i,title: joinThings('div',"class='title'",joinThings('p',"class='sectionNo'",str(i))+title)

def generateReport2d(mainDf, frameData, axialForceData, shearForceData, bendingMomentData, zoomFactorActions, slopeData, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion, units=['1N','1m','C'], precision=3, author='Samrachana Araniko',organization='',address='',fileName='./'):
    coverPage = joinThings('div',"class='cover'",
                joinThings('p',"class='aut'",author)+
                joinThings('p',"class='org'",organization)+
                joinThings('p',"class='add'",address)+
                joinThings('p',"class='dt'",str(dt.now())[:-10])+
                joinThings('p',"class='units'",f'<u>Units Used</u><br>Force: {units[0]}<br>Length: {units[1]}<br>Temperature: {units[2]}'))
    
    segDf = mainDf[mainDf.Class=='segment']
    segDf.index=range(len(segDf))
    lodDf = mainDf[mainDf.Class=='load']
    lodDf.index=range(len(lodDf))
    supDf = mainDf[mainDf.Class=='support']
    supDf.index=range(len(supDf))

    nodeMatrix = extractNodeMatrix(frameData)
    plots,tables = plotGraphs(segDf,lodDf,supDf,nodeMatrix,frameData,axialForceData, shearForceData, bendingMomentData, zoomFactorActions, slopeData, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion,precision,fileName)
    afTbl,sfTbl,bmTbl,angTbl,adTbl,sdTbl,moTbl = tables
    mainGraph = joinThings('p',
                "class='text'","This report presents details of structure graphed below, analysed using Samrachana Araniko.")+joinThings('div',
                "class='graph'",plots[0])+joinThings('figcaption',
                "class='caption'","Figure 1: Analysed Structure")+joinThings('p',
                "class='text'",f"The structure [FRAME] contains {len(segDf)} structural member(s) with {len(supDf)} support(s) under {len(lodDf)} different load(s).")
    rxnGraph = joinThings('p',
                "class='text'","The following graph shows reaction forces and moments at all supports.")+joinThings('div',
                "class='graph'",plots[1])+joinThings('figcaption',
                "class='caption'","Figure 2: Support Reactions")+joinThings('p',
                "class='text'","The direction of forces and moments is as shown in the figure for values with positive magnitude, and just opposite otherwise.")
    afdGraph = joinThings('p',
                "class='text'",f"The following graph shows Axial Force Diagram (AFD) of the frame.")+joinThings('div',
                "class='graph'",plots[2])+joinThings('figcaption',
                "class='caption'","Figure 3: Axial Force Diagram")
    sfdGraph = joinThings('p',
                "class='text'",f"The following graph shows Shear Force Diagram (SFD) of the frame.")+joinThings('div',
                "class='graph'",plots[3])+joinThings('figcaption',
                "class='caption'","Figure 4: Shear Force Diagram")
    bmdGraph = joinThings('p',
                "class='text'",f"The following graph shows Bending Moment Diagram (BMD) of the frame.")+joinThings('div',
                "class='graph'",plots[4])+joinThings('figcaption',
                "class='caption'","Figure 5: Bending Moment Diagram")
    angGraph = joinThings('p',
                "class='text'",f"The following graph shows Slope Diagram of the frame.")+joinThings('div',
                "class='graph'",plots[5])+joinThings('figcaption',
                "class='caption'","Figure 7: Slope Diagram")
    adiGraph = joinThings('p',
                "class='text'",f"The following graph shows Axial Displacement Diagram of the frame. [Displacement along axial direction]")+joinThings('div',
                "class='graph'",plots[6])+joinThings('figcaption',
                "class='caption'","Figure 6: Axial Displacement Diagram")
    sdiGraph = joinThings('p',
                "class='text'",f"The following graph shows Shear Displacement Diagram of the frame. [Dislacement along shear direction]")+joinThings('div',
                "class='graph'",plots[7])+joinThings('figcaption',
                "class='caption'","Figure 8: Shear Displacement Diagram")
    motGraph = joinThings('p',
                "class='text'",f"The following graph shows deflected shape of the frame.")+joinThings('div',
                "class='graph'",plots[8])+joinThings('figcaption',
                "class='caption'","Figure 9: Deflected Shape of the Frame")
        
    nodeDetails = joinThings('p',"class='text'",
                    f'The nodes labelled from 1 to {nodeMatrix.shape[0]} are located in the coordinates given below.')+nodeTable(nodeMatrix)
    segDetails = joinThings('p',"class='text'",
                    'The following two tables show details of members in the structure.')+segmentTable(segDf,nodeMatrix)
    lodDetails = joinThings('p',"class='text'",
                    'The following table shows details of loads in the structure.')+loadTable(lodDf,segDf)
    supDetails = joinThings('p',"class='text'",
                    'The following table shows details of supports in the structure.')+supportTable(supDf)
    rxnDetails = joinThings('p',"class='text'",
                    'The following table shows support reactions in the structure.')+rxnTable(supDf,frameData,nodeMatrix,precision)
    afdDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium axial forces at each segment. AFD @ X means the axial force is AFD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",afTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 6: Minimum and Maximum Axial Forces"))
    sfdDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium shear forces at each segment. SFD @ X means the shear force is SFD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",sfTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 7: Minimum and Maximum Shear Forces"))
    bmdDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium bending moments at each segment. BMD @ X means the bending moment is BMD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",bmTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 8: Minimum and Maximum Bending Moments"))
    angDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium slopes at each segment. S @ X means the slope is S at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",angTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 10: Minimum and Maximum Slopes"))
    adiDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium axial displacements at each segment. AD @ X means the axial displacement is AD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",adTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 9: Minimum and Maximum Axial Displacements"))
    sdiDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium shear displacements at each segment. SD @ X means the shear displacement is SD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",sdTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 11: Minimum and Maximum Shear Displacements"))
    motDetails = joinThings('p',"class='text'",
                    'The following table shows nodal displacements in the structure.')+dispTable(frameData['response'],precision)
    moDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium net displacements at each segment. D @ X means the net displacement is D at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",moTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 12: Minimum and Maximum Net Displacements"))

    part1 = section(1,'Structure Layout and Properties')+mainGraph+breakLine+nodeDetails+breakLine+segDetails+breakLine+lodDetails+breakLine+supDetails+breakLine
    part2 = section(2,'Support Reactions')+rxnGraph+breakLine+rxnDetails+breakLine
    part3 = section(3,'Axial Forces')+afdGraph+breakLine+afdDetails+breakLine
    part4 = section(4,'Shear Forces')+sfdGraph+breakLine+sfdDetails+breakLine
    part5 = section(5,'Bending Moments')+bmdGraph+breakLine+bmdDetails+breakLine
    part6 = section(6,'Axial Displacements')+adiGraph+breakLine+adiDetails+breakLine
    part7 = section(7,'Slopes')+angGraph+breakLine+angDetails+breakLine
    part8 = section(8,'Shear Displacements')+sdiGraph+breakLine+sdiDetails+breakLine
    part9 = section(9,'Deflected Shape')+motGraph+breakLine+moDetails+breakLine+motDetails+breakLine
    
    html = initial + coverPage + \
            part1 + pageBreak + \
            part2 + pageBreak + \
            part3 + pageBreak + \
            part4 + pageBreak + \
            part5 + pageBreak + \
            part6 + pageBreak + \
            part7 + pageBreak + \
            part8 + pageBreak + \
            part9 + pageBreak + \
            final

    # try:
    #     from weasyprint import HTML
    #     with open('temp.html','wt',encoding='utf-8') as f:
    #         f.write(html)
    #         f.close()
    #     HTML('temp.html').write_pdf(fileName,zoom=1)
    # except:
    #     pass
    # from_file('./temp.html',fileName)
    # [osRemove(f'temp{x}.svg') for x in range(1,10)]
    return html

def generateReport2dTruss(mainDf, frameData, axialForceData, zoomFactorActions, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion, units=['1N','1m','C'], precision=3, author='Samrachana Araniko',organization='The Coding Company',address='tcc.com',fileName='./report.pdf'):
    coverPage = joinThings('div',"class='cover'",
                joinThings('p',"class='aut'",author)+
                joinThings('p',"class='org'",organization)+
                joinThings('p',"class='add'",address)+
                joinThings('p',"class='dt'",str(dt.now())[:-10])+
                joinThings('p',"class='units'",f'<u>Units Used</u><br>Force: {units[0]}<br>Length: {units[1]}<br>Temperature: {units[2]}'))
    
    segDf = mainDf[mainDf.Class=='segment']
    segDf.index=range(len(segDf))
    lodDf = mainDf[mainDf.Class=='load']
    lodDf.index=range(len(lodDf))
    supDf = mainDf[mainDf.Class=='support']
    supDf.index=range(len(supDf))
    
    nodeMatrix = extractNodeMatrixTruss(frameData)
    plots,tables = plotGraphsTruss(segDf,lodDf,supDf,nodeMatrix,frameData,axialForceData, zoomFactorActions, axialDisplacementData, shearDisplacementData, zoomFactorResponses, motionData, zoomFactorMotion,precision,fileName)
    afTbl,adTbl,sdTbl,moTbl = tables
    
    mainGraph = joinThings('p',
                "class='text'","This report presents details of structure graphed below, analysed using Samrachana Araniko.")+joinThings('div',
                "class='graph'",plots[0])+joinThings('figcaption',
                "class='caption'","Figure 1: Analysed Structure")+joinThings('p',
                "class='text'",f"The structure [TRUSS] contains {len(segDf)} structural member(s) with {len(supDf)} support(s) under {len(lodDf)} different load(s).")
    rxnGraph = joinThings('p',
                "class='text'","The following graph shows reaction forces at all supports.")+joinThings('div',
                "class='graph'",plots[1])+joinThings('figcaption',
                "class='caption'","Figure 2: Support Reactions")+joinThings('p',
                "class='text'","The direction of forces is as shown in the figure for values with positive magnitude, and just opposite otherwise.")
    afdGraph = joinThings('p',
                "class='text'",f"The following graph shows Axial Force Diagram (AFD) of the truss.")+joinThings('div',
                "class='graph'",plots[2])+joinThings('figcaption',
                "class='caption'","Figure 3: Axial Force Diagram")
    adiGraph = joinThings('p',
                "class='text'",f"The following graph shows Axial Displacement Diagram of the truss. [Displacement along axial direction]")+joinThings('div',
                "class='graph'",plots[3])+joinThings('figcaption',
                "class='caption'","Figure 4: Axial Displacement Diagram")
    sdiGraph = joinThings('p',
                "class='text'",f"The following graph shows Shear Displacement Diagram of the truss. [Dislacement along shear direction]")+joinThings('div',
                "class='graph'",plots[4])+joinThings('figcaption',
                "class='caption'","Figure 5: Shear Displacement Diagram")
    motGraph = joinThings('p',
                "class='text'",f"The following graph shows deflected shape of the truss.")+joinThings('div',
                "class='graph'",plots[5])+joinThings('figcaption',
                "class='caption'","Figure 6: Deflected Shape of the Frame")
        
    nodeDetails = joinThings('p',"class='text'",
                    f'The nodes labelled from 1 to {nodeMatrix.shape[0]} are located in the coordinates given below.')+nodeTable(nodeMatrix)
    segDetails = joinThings('p',"class='text'",
                    'The following two tables show details of members in the structure.')+segmentTable(segDf,nodeMatrix)
    lodDetails = joinThings('p',"class='text'",
                    'The following table shows details of loads in the structure.')+loadTable(lodDf,segDf)
    supDetails = joinThings('p',"class='text'",
                    'The following table shows details of supports in the structure.')+supportTable(supDf)
    rxnDetails = joinThings('p',"class='text'",
                    'The following table shows support reactions in the structure.')+rxnTableTruss(supDf,frameData,nodeMatrix,precision)
    afdDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium axial forces at each segment. AFD @ X means the axial force is AFD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",afTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 6: Minimum and Maximum Axial Forces"))
    adiDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium axial displacements at each segment. AD @ X means the axial displacement is AD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",adTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 7: Minimum and Maximum Axial Displacements"))
    sdiDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium shear displacements at each segment. SD @ X means the shear displacement is SD at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",sdTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 8: Minimum and Maximum Shear Displacements"))
    motDetails = joinThings('p',"class='text'",
                    'The following table shows nodal displacements in the structure.')+dispTableTruss(frameData['response'][:,1:],precision)
    moDetails = joinThings('p',"class='text'",
                    'The following table shows maximum and minium net displacements at each segment. D @ X means the net displacement is D at distance X along axis of segment [FROM \u2192 TO]. [refer Table 2A]')+\
                        joinThings('div',"class='dataFrame'",moTbl.round(precision).to_html(index=False,justify='center')+joinThings('figcaption',
                                    "class='caption'","Table 10: Minimum and Maximum Net Displacements"))

    part1 = section(1,'Structure Layout and Properties')+mainGraph+breakLine+nodeDetails+breakLine+segDetails+breakLine+lodDetails+breakLine+supDetails+breakLine
    part2 = section(2,'Support Reactions')+rxnGraph+breakLine+rxnDetails+breakLine
    part3 = section(3,'Axial Forces')+afdGraph+breakLine+afdDetails+breakLine
    part4 = section(4,'Axial Displacements')+adiGraph+breakLine+adiDetails+breakLine
    part5 = section(5,'Shear Displacements')+sdiGraph+breakLine+sdiDetails+breakLine
    part6 = section(6,'Deflected Shape')+motGraph+breakLine+moDetails+breakLine+motDetails+breakLine
    
    html = initial + coverPage + \
            part1 + pageBreak + \
            part2 + pageBreak + \
            part3 + pageBreak + \
            part4 + pageBreak + \
            part5 + pageBreak + \
            part6 + pageBreak + \
            final

    # try:
    #     from weasyprint import HTML
    #     with open('temp.html','wt',encoding='utf-8') as f:
    #         f.write(html)
    #         f.close()
    #     HTML('temp.html').write_pdf(fileName,zoom=1)
    # except:
    #     pass
    # from_file('./temp.html',fileName)
    # osRemove('temp.html')
    # [osRemove(f'temp{x}.svg') for x in range(1,10)]
    return html
