
"""
 * @author nhphung
"""
# from array import ArrayType
# from cgitb import lookup
# from copyreg import constructor
# from email.policy import default
# from multiprocessing.dummy import Array
# from threading import local
from AST import *
from Visitor import *
from StaticError import *

class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class GetFirst(BaseVisitor, Utils):
    def __init__(self):
        self.globalEnv = {}

    def visitProgram(self, ast, o):
        o = self.globalEnv
        for decl in ast.decl:
            self.visit(decl, o)
        return o
    
    def visitClassDecl(self, ast, o):
        name = ast.classname.name
        if name in o:
            raise Redeclared(Class(), name)
        
        o[name] = {}

        for mem in ast.memlist:
            self.visit(mem, o[name])

    
    def visitAttributeDecl(self, ast, o):
        kind = ast.kind
        if type(kind) == Instance:
            self.visit(ast.decl, ('instance', o))
        elif type(kind) == Static:
            self.visit(ast.decl, ('static', o))

    def visitVarDecl(self, ast, o):
        kind, envi = o
        name = ast.variable.name
        if name in envi:
            raise Redeclared(Attribute(), name)
        envi[name] = ('mutable', self.visit(ast.varType, envi), kind)
        return ('mutable', self.visit(ast.varType, envi), kind)

    def visitConstDecl(self, ast, o):
        kind, envi = o
        name = ast.constant.name
        if name in envi:
            raise Redeclared(Attribute(), name)
        envi[name] = ('immutable', self.visit(ast.constType, envi), kind)

    def visitMethodDecl(self, ast, o):
        if(type(ast.kind) == Instance):
            kind = 'instance'
        elif(type(ast.kind) == Static):
            kind = 'static'
        name = ast.name.name
        params = ast.param
        if name in o:
            raise Redeclared(Method(), name)
        # khac code
        param = list(map(lambda x: self.visit(x, (None, {})), params))
        o[name] = ('method', None, kind, param)

    def visitFloatType(self, ast, o):
        return FloatType()

    def visitIntType(self, ast, o):
        return IntType()

    def visitStringType(self, ast, o):
        return StringType()

    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitArrayType(self, ast, o):
        return ast
    
    def visitVoidType(self, ast, o):
        return VoidType()

    def visitClassType(self, ast, o):
        envi = self.globalEnv
        name = ast.classname.name
                
        if name not in envi:
            raise Undeclared(Class(), name)
        return ClassType(name)
        

        
class MyHelper:
    @ staticmethod
    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    @ staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]

    @ staticmethod
    def isNotNumber(expType):
        return type(expType) not in [IntType, FloatType]




class StaticChecker(BaseVisitor):


    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, o):
        envi = GetFirst().visit(ast, None)

        program_defined = False
        for decl in ast.decl:
            if(decl.classname.name == "Program"):
                program_defined = True
            self.visit(decl, envi)
        
        if not program_defined:
            raise NoEntryPoint()

        return envi
        # return [self.visit(x, envi) for x in ast.decl]

    def visitClassDecl(self, ast, o):
        envi = {}
        envi['thisClass'] = ast.classname.name
        envi['global'] = o

        
        if ast.parentname is not None:
            if ast.parentname.name == ast.classname.name: # same
                raise Undeclared(Class(), ast.classname.name)
            

            if ast.parentname.name in envi['global']:
                gotCurrClass = False
                for x in envi['global']: # check if parent class exists before current class
                    if x == ast.parentname.name:
                        if gotCurrClass:
                            raise Undeclared(Class(), ast.parentname.name)
                        else:
                            envi['parent'] = ast.parentname.name
                    elif x == ast.classname.name:
                        gotCurrClass = True
            else:
                raise Undeclared(Class(), ast.parentname.name)



            # if ast.parentname.name in envi['global']:
            #     envi['parent'] = ast.parentname.name
            # else:
            #     raise Undeclared(Class(), ast.parentname.name)
        else:
            envi['parent'] = None

        
        
        main_defined = False

        for mem in ast.memlist:
            if(isinstance(mem, MethodDecl)):
                if mem.name.name == 'main' and mem.param == []: # dont have any param
                    main_defined = True
            self.visit(mem, envi)
        
        if main_defined == False and ast.classname.name == "Program": # check only for class Program
            raise NoEntryPoint()

    def visitAttributeDecl(self, ast, o):
        envi = o
        decl = ast.decl
        if isinstance(decl, VarDecl):
            self.visit(decl, (Variable(), envi))
        elif isinstance(decl, ConstDecl):
            self.visit(decl, (Constant(), envi))
    
    def visitMethodDecl(self, ast, o):
        envi = {}
        envi['global'] = o['global']
        envi['thisClass'] = o['thisClass']
        envi['parent'] = o['parent']
        envi['local'] = [{}]

        for param in ast.param:
            self.visit(param, (Parameter(), envi))
        
        for decl in ast.body.inst:
            if(isinstance(decl, VarDecl)):
                self.visit(decl, (Variable(), envi))
            elif(isinstance(decl, ConstDecl)):
                self.visit(decl, (Constant(), envi))
            else: self.visit(decl, (False, envi))
    
    def visitVarDecl(self, ast, o):
        kind, envi = o
        name = ast.variable.name
        varType = self.visit(ast.varType, envi)
        if ast.varInit is not None:
            initVal = self.visit(ast.varInit, envi)

            # if type(initVal[1]) != type(varType):
            #     raise TypeMismatchInConstant(ast)

            if initVal[0] == 'mutable' or initVal[0] == 'immutable' or initVal[0] == 'method':
                if MyHelper.isNotAccess(ast.varInit):
                    raise Undeclared(Identifier(), ast.varInit.name)

            value = initVal[1]    

            if type(varType) == ArrayType and type(value) == ArrayType:
                
                if int(varType.size) != int(value.size):
                    raise TypeMismatchInConstant(ast)
                
                if type(varType.eleType) != type(value.eleType):
                    if not (type(varType.eleType) == FloatType and type(value.eleType) == IntType):
                        raise TypeMismatchInConstant(ast)
            
            if type(varType) != type(value) and MyHelper.isNotAccess(ast.varInit):
                if not (type(varType) == FloatType and type(value) == IntType):
                    raise TypeMismatchInConstant(ast)
        
        if 'local' in envi: # neu ton tai local
            if name in envi['local'][0]:
                raise Redeclared(kind, name)
            envi['local'][0][name] = ('var', varType, None)

        

    def visitConstDecl(self, ast, o):
        kind, envi = o
        name = ast.constant.name

        if ast.value is None:
            raise IllegalConstantExpression(ast.value)
        if MyHelper.isNotConst(ast.value):
            raise IllegalConstantExpression(ast.value) # can fix cho dep

        initVal = self.visit(ast.value, (True, envi)) # check ??
        if initVal[0] == 'mutable' or initVal[0] == 'immutable' or initVal[0] == 'method':
            if MyHelper.isNotAccess(ast.value):
                raise Undeclared(Identifier(), ast.value.name)
        elif initVal[0] == 'var' or initVal[0] == 'mutable': # sai sai ??
            raise IllegalConstantExpression(ast.value)
        
        value =  self.visit(ast.value, envi)[1]
        constType = self.visit(ast.constType, envi)

        if 'local' in envi: # neu ton tai local
            if name in envi['local'][0]:
                raise Redeclared(kind, name)
            
        if type(constType) == ArrayType and type(value) == ArrayType:
            if int(constType.size) != int(value.size):
                raise TypeMismatchInConstant(ast)
            
            if type(constType.eleType) != type(value.eleType):
                if not (type(constType.eleType) == FloatType and type(value.eleType) == IntType):
                    raise TypeMismatchInConstant(ast)
        
        if type(constType) != type(value):
            if not (type(constType) == FloatType and type(value) == IntType):
                raise TypeMismatchInConstant(ast)
            
        if 'local' in envi:
            envi['local'][0][name] = ('const', constType, value)


    def visitAssign(self, ast, o):
        loop, envi = o
        lhs = self.visit(ast.lhs, envi)
        exp = self.visit(ast.exp, envi)

        kindLhs = lhs[0]
        typeLhs = lhs[1]
        kindExp = exp[0]
        typeExp = exp[1]

        if kindLhs == 'const' or kindLhs == 'immutable':
            raise CannotAssignToConstant(ast)
        if kindLhs == 'mutable' or kindLhs == 'instance' or kindLhs == 'method':
            if MyHelper.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
        
        if kindExp == 'mutable' or kindExp == 'instance' or kindExp == 'method':
            if MyHelper.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
        
        if type(typeLhs) == VoidType:
            raise TypeMismatchInStatement(ast)
        
        if type(typeLhs) is ArrayType and type(typeExp) is ArrayType:
            if typeLhs.size != typeExp.size:
                raise TypeMismatchInStatement(ast)

            if type(typeLhs.eleType) != type(typeExp.eleType):
                if not (type(typeLhs.eleType) == FloatType and type(typeExp.eleType) == IntType):
                    raise TypeMismatchInStatement(ast)

        
        
        if type(typeLhs) != type(typeExp):
            # gan cho array
            if type(typeLhs) is ArrayType:
                if type(typeLhs.eleType) != type(typeExp):
                    if not (type(typeLhs.eleType) == FloatType and type(typeExp) == IntType):
                        raise TypeMismatchInStatement(ast)
            else:
                if not (type(typeLhs) == FloatType and type(typeExp) == IntType):
                    raise TypeMismatchInStatement(ast)
        
    def visitId(self, ast, o):
        if(type(o) == tuple):
            testVar, envi = o
        else: envi = o

        if 'local' in envi:
            for local in envi['local']:
                if ast.name in local:
                    return local[ast.name]

        if ast.name in envi['global'][envi['thisClass']]:
            return envi['global'][envi['thisClass']][ast.name]

        if envi['parent'] is not None:
            if ast.name in envi['global'][envi['parent']]:
                return envi['global'][envi['parent']][ast.name]

        raise Undeclared(Identifier(), ast.name)

    def visitBlock(self, ast, o):
        loop, envi = o
        block_envi = {}
        block_envi['thisClass'] = envi['thisClass']
        block_envi['global'] = envi['global']
        block_envi['parent'] = envi['parent']
        block_envi['local'] = [{}] + envi['local']

        for stmt in ast.inst:
            if(isinstance(stmt, VarDecl)):
                self.visit(stmt, (Variable(), block_envi))
            elif(isinstance(stmt, ConstDecl)):
                self.visit(stmt, (Constant(), block_envi))
            else:
                self.visit(stmt, (loop, block_envi))

    def visitUnaryOp(self, ast, o):
        if isinstance(o, tuple): # truong hop assign statement ?
            if MyHelper.isNotConst(ast.body):
                raise IllegalConstantExpression(ast)
            
            expr = self.visit(ast.body, o)
            if expr[0] == 'var' or expr[0] == 'mutable':
                raise IllegalConstantExpression(ast)
        else: # binh thuong ?
            expr = self.visit(ast.body, o)
        
        if expr[0] == 'mutable' or expr[0] == 'immutable' or expr[0] == 'method':
            if MyHelper.isNotAccess(ast.body):
                raise Undeclared(Identifier(), ast.body.name)
        
        if ast.op == '-':
            if(MyHelper.isNotNumber(expr[1])):
                raise TypeMismatchInExpression(ast)
        
        if ast.op == '!':
            if(type(expr[1]) != BoolType):
                raise TypeMismatchInExpression(ast)
        
        return (None, expr[1], None)
    
    def visitBinaryOp(self, ast, o):
        if isinstance(o, tuple): # truong hop assign statement ?
            if MyHelper.isNotConst(ast.left) or MyHelper.isNotConst(ast.right):
                raise IllegalConstantExpression(ast)
            
            left = self.visit(ast.left, o)
            right = self.visit(ast.right, o)

            kindLeft = left[0]
            kindRight = right[0]

            # ????
            if kindLeft == 'var' or kindLeft == 'mutable':
                raise IllegalConstantExpression(ast)
            if kindRight == 'var' or kindRight == 'mutable':
                raise IllegalConstantExpression(ast)

        else:
            left = self.visit(ast.left, o)
            right = self.visit(ast.right, o)

            kindLeft = left[0]
            kindRight = right[0]

        if(kindLeft == 'mutable' or kindLeft == 'immutable' or kindLeft == 'method'):
            if MyHelper.isNotAccess(ast.left):
                raise Undeclared(Identifier(), ast.left.name)
        
        if(kindRight == 'mutable' or kindRight == 'immutable' or kindRight == 'method'):
            if MyHelper.isNotAccess(ast.right):
                raise Undeclared(Identifier(), ast.right.name)

        if ast.op in ['+', '-', '*']:
            if type(left[1]) != ArrayType: # can fix lai
                if MyHelper.isNotNumber(left[1]) or MyHelper.isNotNumber(right[1]):
                    raise TypeMismatchInExpression(ast)
            
            # ep kieu
            if type(left[1]) == FloatType or type(right[1]) == FloatType:
                return (None, FloatType(), None)
            
            return (None, IntType(), None)
        
        if ast.op == '/': # chia cho 0 ?
            if MyHelper.isNotNumber(left[1]) or MyHelper.isNotNumber(right[1]):
                raise TypeMismatchInExpression(ast)
            
            if type(left[1]) == FloatType or type(right[1]) == FloatType:
                return (None, FloatType(), None)
            
            return (None, FloatType(), None) # ket qua phep chia luon la float
        
        if ast.op == '%':
            if not isinstance(left[1], IntType) or not isinstance(right[1], IntType):
                raise TypeMismatchInExpression(ast)
            
            return (None, IntType(), None)

        if ast.op in ['>', '<', '>=', '<=']:
            # if MyHelper.isNotNumber(left[1]) or MyHelper.isNotNumber(right[1]):
            #     raise TypeMismatchInExpression(ast)

            if type(left[1]) != type(right[1]): # check
                raise TypeMismatchInExpression(ast)

            return (None, BoolType(), None)
        
        if ast.op in ['==', '!=']:
            if type(left[1]) == type(right[1]):
                if(type(left[1]) == FloatType or type(left[1]) == IntType):
                    return (None, BoolType(), None)

            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['&&', '||']:
            if type(left[1]) != BoolType or type(right[1]) != BoolType:
                raise TypeMismatchInExpression(ast)
            
            return (None, BoolType(), None)

        if ast.op == '==.': # str compare
            if (type(left[1]) != StringType or type(right[1]) != StringType):
                raise TypeMismatchInExpression(ast)
            
            return (None, BoolType(), None)

        if ast.op == '+.': # str concat
            if (type(left[1]) != StringType or type(right[1]) != StringType):
                raise TypeMismatchInExpression(ast)
            
            return (None, StringType(), None)


    def visitIf(self, ast, o):
        loop, envi = o
        expr = self.visit(ast.expr, envi)
        kindExpr = expr[0]

        if kindExpr == 'mutable' or kindExpr == 'immutable' or kindExpr == 'method':
            if MyHelper.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        
        if not isinstance(expr[1], BoolType):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, (loop, envi))

        if ast.elseStmt != None:
            self.visit(ast.elseStmt, (loop, envi))


    
    def visitFor(self, ast, o):
        loop, envi = o

        forID = self.visit(ast.id, envi)
        expr1 = self.visit(ast.expr1, envi)
        expr2 = self.visit(ast.expr2, envi)
        expr3 = self.visit(ast.expr3, envi)

        kindID = forID[0]
        kindExpr1 = expr1[0]
        kindExpr2 = expr2[0]
        kindExpr3 = expr3[0]

        if kindID == 'mutable' or kindID == 'immutable' or kindID == 'method':
            if MyHelper.isNotAccess(ast.id):
                raise Undeclared(Identifier(), ast.id.name)
        
        if kindExpr1 == 'mutable' or kindExpr1 == 'immutable' or kindExpr1 == 'method':
            if MyHelper.isNotAccess(ast.expr1):
                raise Undeclared(Identifier(), ast.expr1.name)

        if kindExpr2 == 'mutable' or kindExpr2 == 'immutable' or kindExpr2 == 'method':
            if MyHelper.isNotAccess(ast.expr2):
                raise Undeclared(Identifier(), ast.expr2.name)
        
        if kindExpr3 == 'mutable' or kindExpr3 == 'immutable' or kindExpr3 == 'method':
            if MyHelper.isNotAccess(ast.expr3):
                raise Undeclared(Identifier(), ast.expr3.name)

        if kindID == 'const' or kindID == 'immutable':
            raise CannotAssignToConstant(Assign(ast.id,ast.expr1)) # ????????????

        if type(expr1[1]) != IntType or type(expr2[1]) != IntType or type(expr3[1]) != IntType:
            raise TypeMismatchInStatement(ast)
        
        if(MyHelper.isNotNumber(forID[1])):
            raise TypeMismatchInStatement(ast)

        self.visit(ast.loop, (True, envi))

    def visitBreak(self, ast, o):
        loop, envi = o
        if not loop:
            raise MustInLoop(ast)

    def visitContinue(self, ast, o):
        loop, envi = o
        if not loop:
            raise MustInLoop(ast)

    def visitArrayCell(self, ast, o): # a[1][2]
        arr = self.visit(ast.arr, o)
        if not (isinstance(arr[1], ArrayType)):
            raise TypeMismatchInExpression(ast)

        
        idxList = ast.idx
        for idx in idxList:
            kq = self.visit(idx, o)
            
            if not (isinstance(kq[1], IntType)):
                raise TypeMismatchInExpression(ast)

        return (None, arr[1], None)

    def visitNewExpr(self, ast, o):
        envi = o
        name = ast.classname.name

        if name in envi['global']:
            gotCurrClass = False
            for x in envi['global']: # check if parent class exists before current class
                if x == name:
                    if gotCurrClass:
                        raise Undeclared(Class(), name)
                    else:
                        returnEle = (None, ClassType(ast.classname), None)
                elif (x == envi['thisClass']):
                    gotCurrClass = True
        else:
            raise Undeclared(Class(), name)
        
        lenParam = len(ast.param)
        if(lenParam > 0):
            if "Constructor" in envi['global'][name]:
                constructor = envi['global'][name]["Constructor"]
            else:
                raise Undeclared(Method(), "Constructor")
        
        
            paraList = list(map(lambda x: self.visit(x, envi), ast.param))
            if len(paraList) != len(constructor[3]):
                raise TypeMismatchInExpression(ast)
            
            for i in range(len(paraList)):
                if type(paraList[i][1]) != type(constructor[3][i][1]):
                    if not (type(paraList[i][1]) == IntType and type(constructor[3][i][1]) == FloatType):
                        raise TypeMismatchInExpression(ast)

        return returnEle

    def handleAccess(self, ast, o):
        kind, env, name = o
        if ast.name in env['global'][name]:
            return env['global'][name][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(kind, ast.name)


    def visitReturn(self, ast, o):
        loop, envi = o
  
        typeReturn = self.visit(ast.expr, envi)
        if typeReturn[0] == 'mutable' or typeReturn[0] == 'immutable' or typeReturn[0] == 'method':
            if MyHelper.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        

    def visitCallExpr(self, ast, o):
        envi = o
        if(isinstance(ast.obj, SelfLiteral)):
            method =  self.handleAccess(ast.method, (Method(), envi, envi['thisClass']))
            if(method[2] == 'static'):
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj, o)
            except:
                if ast.obj.name in envi['global']:
                    gotCurrClass = False
                    for x in envi['global']: # check if parent class exists before current class
                        if x == ast.obj.name:
                            if gotCurrClass:
                                raise Undeclared(Class(), ast.obj.name)
                            else:
                                nameClass = ast.obj.name
                        elif x == envi['thisClass']:
                            gotCurrClass = True
                else:
                    raise Undeclared(Class(), ast.obj.name)
            
            if(isinstance(nameClass, tuple)):
                if(type(nameClass[1]) != ClassType):
                    raise TypeMismatchInExpression(ast)
                method = self.handleAccess(ast.method, (Method(), envi, nameClass[1].classname.name))

                if method[2] == 'static': # fix lai ???
                    raise IllegalMemberAccess(ast)
                
                if isinstance(method[1], VoidType):
                    raise TypeMismatchInExpression(ast)
                
                if method[0] != 'method':
                    raise TypeMismatchInExpression(ast)

            if(isinstance(nameClass, str)):
                method = self.handleAccess(ast.method, (Method(), envi, nameClass))
                if method[2] == 'instance': # static cua class khac ?
                    raise IllegalMemberAccess(ast)

                if isinstance(method[1], VoidType):
                    raise TypeMismatchInExpression(ast)

                if method[0] != 'method':
                    raise TypeMismatchInExpression(ast)
                
            listParam = list(map(lambda x: self.visit(x, envi), ast.param))
            if len(listParam) != len(method[3]):
                raise TypeMismatchInExpression(ast)
            
            for i in range(len(listParam)):
                if type(listParam[i][1]) != type(method[3][i][1]):
                    if not (type(listParam[i][1]) == IntType and type(method[3][i][1]) == FloatType):
                        raise TypeMismatchInExpression(ast)
            
        return (None, method[1], None)


    def visitCallStmt(self, ast, o):
        loop, envi = o
        if isinstance(ast.obj, SelfLiteral):
            method =  self.handleAccess(ast.method, (Method(), envi, envi['thisClass']))
            if(method[2] == 'static'):
                raise IllegalMemberAccess(ast)
            listParam = list(map(lambda x: self.visit(x, envi), ast.param))

        else:
            try: # object
                nameClass = self.visit(ast.obj, envi)
            except: # ten class
                if ast.obj.name in envi['global']:
                    gotCurrClass = False
                    for x in envi['global']: # check if parent class exists before current class
                        if x == ast.obj.name:
                            if gotCurrClass:
                                raise Undeclared(Class(), ast.obj.name)
                            else:
                                nameClass = ast.obj.name
                        elif x == envi['thisClass']:
                            gotCurrClass = True
                else:
                    raise Undeclared(Class(), ast.obj.name)

            if isinstance(nameClass, tuple):
                if(type(nameClass[1]) != ClassType):
                    raise TypeMismatchInStatement(ast)
                method = self.handleAccess(ast.method, (Method(), envi, nameClass[1].classname.name))

                if method[2] == 'static': # fix lai ???
                    raise IllegalMemberAccess(ast)

                if method[0] != 'method':
                    raise TypeMismatchInStatement(ast)
                
            if isinstance(nameClass, str):
                method = self.handleAccess(ast.method, (Method(), envi, nameClass))
                if method[2] == 'instance': # ten la class thi chi goi dc static
                    raise IllegalMemberAccess(ast)

                if method[0] != 'method':
                    raise TypeMismatchInStatement(ast)

            listParam = list(map(lambda x: self.visit(x, envi), ast.param))
            if len(listParam) != len(method[3]):
                raise TypeMismatchInStatement(ast)
            for i in range(len(listParam)):
                if type(listParam[i][1]) != type(method[3][i][1]):
                    if not (type(listParam[i][1]) == IntType and type(method[3][i][1]) == FloatType):
                        raise TypeMismatchInStatement(ast)

    
    def visitFieldAccess(self, ast, o):
        if(isinstance(o, tuple)):
            testVar, envi = o
        else:
            envi = o
        
        if isinstance(ast.obj, SelfLiteral):
            fieldname = self.handleAccess(ast.fieldname, (Attribute(), envi, envi['thisClass']))
            if fieldname[2] == 'static':
                raise IllegalMemberAccess(ast)

        else:
            try:
                nameClass = self.visit(ast.obj, envi)
            except:
                if ast.obj.name in envi['global']:
                    gotCurrClass = False
                    for x in envi['global']: # check if parent class exists before current class
                        if x == ast.obj.name:
                            if gotCurrClass:
                                raise Undeclared(Class(), ast.obj.name)
                            else:
                                nameClass = ast.obj.name
                        elif x == envi['thisClass']:
                            gotCurrClass = True
                else:
                    raise Undeclared(Class(), ast.obj.name)

            if isinstance(nameClass, tuple):
                if type(nameClass[1]) != ClassType:
                    raise TypeMismatchInExpression(ast)
                
                fieldname = self.handleAccess(ast.fieldname, (Attribute(), envi, nameClass[1].classname.name))
                
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ast)

                if fieldname[2] == 'static':
                    raise IllegalMemberAccess(ast)

            if isinstance(nameClass, str):
                fieldname = self.handleAccess(ast.fieldname, (Attribute(), envi, nameClass))

                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ast)

                if fieldname[2] == 'instance':
                    raise IllegalMemberAccess(ast)
            
        return (fieldname[0], fieldname[1], None)
        

    

    def visitFloatLiteral(self, ast, o):
        return (None, FloatType(), None)

    def visitIntLiteral(self, ast, o):
        return (None, IntType(), None)

    def visitStringLiteral(self, ast, o):
        return (None, StringType(), None)

    def visitBooleanLiteral(self, ast, o):
        return (None, BoolType(), None)

    def visitSelfLiteral(self, ast, o):
        return (None, SelfLiteral(), None)
    
    def visitNullLiteral(self, ast, o):
        return (None, NullLiteral(), None)
    
    
    def visitArrayLiteral(self, ast, o):
        listEle = list(map(lambda x: self.visit(x, o), ast.value))

        arraySize = len(listEle)
        firstEle = listEle[0]

        for ele in listEle[1:]:
            if type(ele[1]) != type(firstEle[1]):
                raise IllegalArrayLiteral(ast) # fixed

        return (None, ArrayType(arraySize, firstEle[1]), None)

    def visitFloatType(self, ast, o):
        return FloatType()

    def visitBoolType(self, ast, o):
        return BoolType()

    def visitIntType(self, ast, o):
        return IntType()

    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitStringType(self, ast, o):
        return StringType()

    def visitArrayType(self, ast, o):
        return ast

    def visitClassType(self, ast, o):
        name = ast.classname.name
        envi = o

        if name in envi['global']:
            gotCurrClass = False
            for x in envi['global']: # check if parent class exists before current class
                if x == name:
                    if gotCurrClass:
                        raise Undeclared(Class(), name)
                    else:
                        break
                elif x == envi['thisClass']:
                    gotCurrClass = True

        return ast




            

    

    

    





    


