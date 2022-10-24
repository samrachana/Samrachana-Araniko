from math import *
def isfun(index,string):
    l = len(string)
    p = True
    for t in range(index+1,len(string)):
        if string[t] == '(':
            l = t
            break;
        elif not string[t].islower():
            l=len(string)
            break;
    return True if (l!=len(string) and p) else False

PI,TAU,E,INF,NAN = pi,tau,e,inf,nan
D = PI/180
EX,K,MG,G,T = 1e1,1e3,1e6,1e9,1e12
ML,MC,N,P = 1e-3,1e-6,1e-9,1e-12
atana = atan2

class v:
    def __init__(self,*args):
        if not any([isinstance(x,v) for x in args]):
            self.list = list(args)
        else:
            self.list = []
            for x in args:
                try:
                    self.list.append(x.list)
                except:
                    self.list.append(x)
        check = str(self.list)
        if "'" in check:
            raise ValueError('Use Vector Class For Numeric Data Only')
    def __add__(self,val):
        try:
            return v(*a(self.list,val))
        except:
            return v(*a(self.list,val.list))
    def __mul__(self,val):
        try:
            return v(*m(self.list,val))
        except:
            return v(*m(self.list,val.list))
    __rmul__ = lambda self,val: self.__mul__(val)
    def __getitem__(self,x):
        a =  self.list[x]
        return a if (isinstance(a,int) or isinstance(a,float)) else v(*a)
    def __len__(self):
        return len(self.list)
    def __str__(self):
        return str(self.list)
    def mag(self):
        return norm(self.list)
    def pol(self):
        th = atana(self.list[1],self.list[0])
        return v(self.mag(),th)
    def cart(self):
        return self.list[0]*v(cos(self.list[1]),sin(self.list[1]))
    def append(self,val):
        l = self.list.copy()
        l.append(val)
        return v(*l)
    def apply(self,fun):
        if not any([isinstance(x,v) for x in self]):
            r = v(*[fun(t) for t in self])
        else:
            r = v()
            for x in self:
                try:
                    r = r.append(v(*[fun(t) for t in x]))
                except:
                    r = r.append(fun(x))
        return r
    def __round__(self,digits):
        return self.apply(lambda x: round(x,digits))

def context():
    return globals()

def evalString(command,precision=3):
    if '>>>' in command:
        return 'CLEAR TO CONTINUE'
    if '?' in command:
        return str(eval(expr(command),context()))
    a = eval(expr(command),context())
    try:
        a = round(a,precision)
    except:
        try:
            a = round(v(*a),precision)
        except:
            pass
    a = str(a).replace(',','')
    return a

def expr(string):
    string = string.replace('{','(')
    string = string.replace('}',')')
    if string[0]=='?':
        if len(string)==1:
            return 'h()'
        return "h('"+string[1:]+"')"
    FUNCS = ['s','p','q','x']
    s = ''
    if string[0] in FUNCS and string[1]=='(':
        func = string[0]+'('
        args = string[2:-1].split(sep=',')
        for x in args:
            if not x.isnumeric():
                func = func + "'" + x + "',"
            else:
                func = func + x + ","
        func = func[:-1]+")"
        string = func
            
    for i in range(len(string)-1):
        if string[i] == '^':
            s = s + '**'
        elif string[i].isalpha() and string[i+1].isalpha() and not isfun(i,string):
            if string[i].isupper() and string[i+1].isupper():
                s = s + string[i]
            else:
                s = s + string[i] + '*'
        elif (string[i].isnumeric() or string[i]==')') and (string[i+1].isalpha() or string[i+1]=='('):
            s = s + string[i] + '*'
        elif string[i].isupper() and (string[i+1].isnumeric() or string[i+1] in ['+','-']):
            s = s + string[i] + '**'
        elif string[i].islower() and string[i+1].isnumeric():
            s = s + string[i] + '**'
        else:
            s = s + string[i]
    return s + string[-1]

def sign(x):
    return abs(x)/x if x!=0 else 0

def ap(a,l,n):
    d = (l-a)/(n-1)
    return [a+t*d for t in range(n)]

def dot(a,b):
    return sum([x*y for x,y in zip(a,b)])

def cross(a,b):
    if len(a)==2:
        return a[0]*b[1] - a[1]*b[0]
    else:
        s0 = a[1]*b[2] - a[2]*b[1]
        s1 = a[2]*b[0] - a[0]*b[2]
        s2 = a[0]*b[1] - a[1]*b[0]
        return [s0,s1,s2]

def integration(fun,A,B,ITER=10,TOL=1e-5):
    XS = [A,B]
    error = 100
    iterLim = 0
    quad = 0
    def georgeBool(a,b):
        xs = ap(a,b,5)
        h = xs[1]-xs[0]
        ys = [fun(x) for x in xs]
        return (2*h*dot(ys,[7,32,12,32,7]))/45
    while iterLim < ITER and error > TOL:
        start = XS[:-1]
        stop = XS[1:]
        s = sum([georgeBool(x,y) for x,y in zip(start,stop)])
        error = abs(s-quad)
        quad = s
        iterLim = iterLim+1
        mids = [(x+y)/2 for x,y in zip(start,stop)]
        XS = XS + mids
        XS.sort()
    return quad
        
def grid(fromArr,toArr,size):
    length = len(fromArr)
    arr = []
    for i in range(length):
        arr.append(tuple(ap(fromArr[i],toArr[i],size)))
    brr = []
    for i in range(size**length):
        temp = []
        for j in range(length):
            k = (i//(size**j))%size
            temp.append(arr[j][k])
        brr.append(temp)
    return brr

def norm(vec,MODE='single'):
    mode = MODE
    if mode == 'single':
        from math import sqrt
        return sqrt(sum((x**2 for x in vec)))
    elif mode == 'common':
        from math import sqrt
        dc = sqrt(len(vec))
        dist1 = (sum(vec)/dc)**2
        dist2 = sum((x**2 for x in vec))
        return sqrt(abs(dist2-dist1))
    else:
        raise TypeError('Mode not defined yet')

def derivative(fun,vec,index,ITER=10,STEP=1,TOL=1e-5):
    step = STEP
    vecL = vec.copy()
    vecR = vec.copy()
    err = 100
    i = 0
    derr = 0
    while i < ITER and err > TOL: 
        vecL[index] = vec[index] - step
        vecR[index] = vec[index] + step
        coeff = (fun(vecR) - fun(vecL))/(2*step)
        err = abs(derr-coeff)
        derr = coeff
        step = step/2
        i = i + 1
    return derr

def solveLinear(coeffMat,constVec):
    try:
        order = len(coeffMat)
        augMat = []
        for i in range(order):
            temp = []
            for j in range(order+1):
                temp.append(coeffMat[i][j] if j < order else constVec[i])
            augMat.append(temp)
        for i in range(order):
            pivot = augMat[i][i]
            for j in range(order):
                if i!=j:
                    ratio = augMat[j][i]/pivot
                    for k in range(order+1):
                        augMat[j][k] = augMat[j][k] - ratio*augMat[i][k]
        soln = []
        for i in range(order):
            soln.append(augMat[i][order]/augMat[i][i])
        return soln
    except:
        raise TypeError('Linear System Not solved')

def transpose(x):
    try:
        return list(map(list,zip(*x)))
    except:
        return list(map(list,zip(x)))

def vecOp(fun,a,b):
    return [fun(x,y) for x,y in zip(a,b)]

def matmul(a,b):
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    return [[sum([a[i][k]*b[k][j] for k in range(n)]) for j in range(p)]for i in range(m)]

def invertMat(matrix):
    if len(matrix)==len(matrix[0]):
        order = len(matrix)
        augMat = []
        for i in range(order):
            temp=[]
            for j in range(order*2):
                temp.append(matrix[i][j] if j < order else (1 if i == j - order else 0))
            augMat.append(temp)
        for i in range(order):
            pivot = augMat[i][i]
            for j in range(order):
                if i!=j:
                    ratio = augMat[j][i]/pivot
                    for k in range(order*2):
                        augMat[j][k] = augMat[j][k] - ratio*augMat[i][k]
        soln = []
        for i in range(order):
            temp = []
            for j in range(order,order*2):
                temp.append(augMat[i][j]/augMat[i][i])
            soln.append(temp)
        return soln
    else:
        m = len(matrix)
        n = len(matrix[0])
        if m > n:
            symm = matmul(transpose(matrix),matrix)
            return matmul(invertMat(symm),transpose(matrix))
        else:
            symm = matmul(matrix,transpose(matrix))
            return matmul(transpose(matrix),invertMat(symm))

class System:                
    def __init__(self,*expressions):
        try:
            self.variables = []
            self.expressions = []
            self.functions = []
            for x in expressions:
                x = expr(x)
                self.expressions.append(x)
                for t in range(len(x)):
                    if x[t].islower() and x[t] not in self.variables and not isfun(t,x):
                            self.variables.append(x[t])
            for x in self.expressions:
                self.functions.append(eval('lambda '+','.join(self.variables)+':'+x))
        except:
            raise TypeError('Error occurred in initialization. Expressions may not be valid')

    def evaluate(self,x,index=None):
        if index==None:
            check = []
            for f in self.functions:
                check.append(eval('f('+','.join([str(t) for t in x])+')'))
        else:
            f = self.functions[index]
            check = eval('f('+','.join([str(t) for t in x])+')')
        return check

    def gridRoot(self,ITER=30,STEP=2,TOL=1e-5,normMode='single',**guesses):
        tol,iterations = TOL,ITER
        size = max(2,STEP)
        guesFrom = [guesses[x][0] for x in self.variables]
        guesTo = [guesses[x][1] for x in self.variables]
        error = 100
        iterLim = 0
        while error > tol and iterLim < iterations:
            for x in grid(guesFrom,guesTo,size):
                check = self.evaluate(x)
                tempErr = norm(check,normMode)
                if  tempErr < error:
                    self.solution = {'X': x,'f(X)' : check}
                    error = tempErr
                    if error < tol:
                        break
            size = size + 1
            iterLim = iterLim + 1
        self.method = 'Grid Search ' + normMode.capitalize()
        self.error = error
        self.iterations = iterLim

    def quadrature(self,A,B,ITER=10,TOL=1e-5,FUN=0):
        fun = lambda x: self.evaluate([x],FUN)
        return integration(fun,A,B,ITER,TOL)

    def partial(self,FUN,VAR,ITER=10,STEP=1,TOL=1e-5):
        fun = lambda vec: self.evaluate(vec,FUN)
        return lambda vec : derivative(fun,vec,VAR,ITER,STEP,TOL)

    def jacobian(self,ITER=10,STEP=1,TOL=1e-5,**derivatives):
        iterations,initialStep,tol = ITER,STEP,TOL
        noOfVars = len(self.variables)
        noOfFuns = len(self.functions)
        first = list(range(noOfFuns))
        second = list(range(noOfVars))
        Jacobian = []
        for x in first:
            jacobian = []
            for y in second:
                key = self.variables[y]+str(x+1)
                try:
                    der = expr(derivatives[key])
                    for var in range(noOfVars):
                        der = der.replace(self.variables[var],'vec['+str(var)+']')
                    jacobian.append(eval('lambda vec: ' + der))
                except:
                    jacobian.append(self.partial(x,y,iterations,initialStep,tol))
            Jacobian.append(jacobian)
        self.Jacobian = lambda vec : [[f(vec) for f in fArr] for fArr in Jacobian]
            
    def newtonRoot(self,ITER=100,TOL=1e-5,**guess):
        iterations,tol = ITER, TOL
        self.jacobian()
        error = 100
        iterLim = 0
        if len(guess)==0:
            for x in self.variables:
                guess[x] = len(self.variables)/2
        try:
            soln=[0]*len(self.variables)
            for x in range(len(self.variables)):
                soln[x]=guess[self.variables[x]]
            while error > tol and iterLim < iterations:
                check = self.evaluate(soln)
                error = norm(check)
                iterLim = iterLim+1
                soln = vecOp(lambda x,y: x-y,soln,solveLinear(self.Jacobian(soln),check))
            self.method = 'Newton-Raphson'
            self.iterations = iterLim
        except:
            soln=[0]*len(self.variables)
            for x in range(len(self.variables)):
                soln[x]=guess[self.variables[x]]
            while error > tol and iterLim < iterations:
                check = self.evaluate(soln)
                error = norm(check)
                iterLim = iterLim+1
                soln = vecOp(lambda x,y: x-y,soln,transpose(matmul(invertMat(self.Jacobian(soln)),transpose(check)))[0])
            self.method = 'Newton-Raphson LSQ'
            self.iterations = iterLim
        self.solution = {'X':soln,'f(X)':self.evaluate(soln)}
        self.error = error

def getFromArgs(args):
    expressions = []
    conditions = {}
    numerics = []
    for x in args:
        try:
            x = evalString(x)
        except:
            pass
        if isinstance(x,int) or isinstance(x,float):
            numerics.append(x)
        elif '=' in x:
            x.replace(' ','')
            for i in range(len(x)):
                if x[i]=="=":
                    index = i
                    break;
            conditions[x[:index]] = float(evalString(x[index+1:]))
        else:
            expressions.append(x)
    return expressions,conditions,numerics
## CLI functions::

x = expr
i = invertMat
t = transpose
M = matmul

def s(*args):
    expressions,conditions,numerics = getFromArgs(args)
    a = System(*expressions)
    a.newtonRoot(*numerics,**conditions)
    soln = a.solution['X']
    if len(soln)==1:
        soln = soln[0]
    return soln

def p(*args):
    expressions,conditions,numerics = getFromArgs(args)
    a = System(*expressions)
    default = {'VAR':0,'FUN':0,'ITER':10,'STEP':1,'TOL':1e-5}
    for i in conditions.items():
        for x in default.keys():
            if i[0]==x:
                default[x] = int(i[1])
                break;
    fun = a.partial(**default)
    vec = [0]*len(a.variables)
    for i in range(len(a.variables)):
        vec[i] = conditions[a.variables[i]]
    return fun(vec)

def q(*args):
    expressions,conditions,numerics = getFromArgs(args)
    a = System(*expressions)
    return a.quadrature(*numerics,**conditions)    

sl = solveLinear

def a(*args):
    logvec = [str(arg).replace('.','').isnumeric() for arg in args]
    if len(args)==2 and any(logvec):
        mul = args[logvec.index(True)]
        vec = args[0] if mul==args[1] else args[1]
        return [mul+x for x in vec]
    s = [1]*len(args[0])
    for i in range(len(args)):
        s = vecOp(lambda x,y: x+y,s,args[i])
    return s

def m(*args):
    logvec = [str(arg).replace('.','').isnumeric() for arg in args]
    if len(args)==2 and any(logvec):
        mul = args[logvec.index(True)]
        vec = args[0] if mul==args[1] else args[1]
        return [mul*x for x in vec]
    s = [1]*len(args[0])
    for i in range(len(args)):
        s = vecOp(lambda x,y: x*y,s,args[i])
    return s

def h(string=None):
    helpDict = {'basic':"3+(5/{2-1.3}), 2PI+3, sin(cos(PI/2)) GIVES RESP "+evalString('3+(5/{2-1.3})')+", "+evalString('2PI+3')+", "+evalString('sin(cos(PI/2))'),
                'angle':"sin(90D), atana(sqrt(3),1) - 60D, acos(1/2) GIVES RESP "+evalString('sin(90D)')+", "+evalString('atana(sqrt(3),1) - 60D')+", "+evalString('acos(1/2)'),
                'eng':"10K, (1MG)+(2K), (0.5ML)+(2MC) GIVES RESP "+evalString('10K')+", "+evalString('(1MG)+(2K)')+", "+evalString('(0.5ML)+(2MC)'),
                'sci':"EX can be used as scientific notation: 3EX5, 1EX-2 GIVES RESP "+evalString('3EX5')+", "+evalString('1EX-2'),
                'pow10':"CONSTS : EX=10, K=10^3, M=10^6, G=10^9, T=10^12, ML=10^-3, MC=10^-6, N=10^-9, P=10^-12",
                'const':"CONSTS: PI="+evalString('PI')+", E="+evalString('E')+", TAU="+evalString('TAU')+", D="+evalString('D'),
                'vector':"v(1,2,3)+5v(1,2,1)*v(2,1,3), v(1,1).pol(), v(2,PI/4).cart(), v(1,1,sqrt(2)).mag() GIVES RESP "+evalString('v(1,2,3)+5v(1,2,1)*v(2,1,3)')+", "+evalString('v(1,1).pol()')+", "+evalString('v(2,PI/4).cart()')+", "+evalString('v(1,1,sqrt(2)).mag()'),
                'matrix':"i([[1,2],[3,2]]), t([[1,2],[3,2]]), M([[1,4],[2,3]],[[2,1],[2,3]]) GIVES RESP "+evalString('i([[1,2],[3,2]])')+", "+evalString('t([[1,2],[3,2]])')+", "+evalString('M([[1,4],[2,3]],[[2,1],[2,3]])'),
                'solve':"s(x2-4,x=1),s(x2-y2-4xy+9,sin(x2+y2)),x=1,y=3) GIVES RESP "+evalString('s(x2-4,x=1)')+", "+evalString('s(x2-y2-4xy+9,sin(x2+y2))'),
                'linear':"sl([[1,2,5],[4,3,1],[3,2,4]],[3,2,1]) GIVES "+evalString('sl([[1,2,5],[4,3,1],[3,2,4]],[3,2,1])'),
                'derivative':"p(3x2-5exp(x)+sin(x2),x=4), p(3xy-x2-10y+9,VAR=1,x=2,y=3) GIVES RESP "+evalString('p(3x2-5exp(x)+sin(x2),x=4)')+", "+evalString('p(3xy-x2-10y+9,VAR=1,x=2,y=3)'),
                'integration':"q(sin(cos(x)),A=0,B=PI/2) GIVES "+evalString('q(sin(cos(x)),A=0,B=PI/2)'),
                'check':"x(expression) can be used to see expanded form of the expression. x(3xy+5E2) GIVES "+evalString('x(3xy+5E2)'),
                'caution1':"NUMBERS AFTER ALPHABETS ARE RAISED AS POWER. SO TAKE CARE WHILE USING ENG/SCI NOTATION",
                'caution2':"VECTORS, LISTS, TUPLES ARE ALMOST ALWAYS EQUIVALENT AS ARGUMENTS OF FUNCTIONS",
                'caution3':"STEP, ITER, AND TOL ARE INITIAL STEP, ITERATION LIMIT, TOLERANCE IN FUNCTIONS: s(), p(), q()",
                'caution4':"VAR IN PARTIAL DERIVATIVES (p) INDICATES CHANGING VARIABLE. ORDER IS FOLLOWED AS IN EXPRESSION",
                'caution5':"NO OUTPUT MEANS ERROR IN INPUT",
                'caution6':"EXPAND (x) FUNCTION IS USEFUL TO CHECK EXPRESSIONS",
                'caution7':"IF FUNCTION RETURNS ERROR TRY CHANGING INITIAL GUESS(ES)",
                'caution8':"a() AND m() MAY BE USED IN LISTS FOR VECTOR ADDITION/MULTIPLICATION BUT USING '+' AND '*' FOR VECTORS IS RECOMMENDED",
                'caution9':"IT IS RECOMMENDED TO USE '{}' INSTEAD OF '()' FOR DEFINING ORDER OF OPERATIONS",
                'caution10':"ALL FUNCTIONS DEFINED IN PYTHON MODULE : math CAN BE USED"}
    try:
        return helpDict[string]
    except:
        return '?x = HELP || x = [basic angle eng sci pow10 const vector matrix solve linear derivative integration check caution1 caution2 ...caution10]'
