from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

myClassName = ""


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        listdecls = ctx.classdecl()
        result = []
        for decl in listdecls:
            result += self.visit(decl)
        return Program(result)

    def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
        global myClassName
        myClassName = ctx.ID().getText()
        return [ClassDecl(Id(ctx.ID().getText()), self.visit(ctx.inside_decls()) if ctx.inside_decls() else [], Id(ctx.inheritance_from().ID().getText()) if ctx.inheritance_from() else None)]

    
    def visitInside_decls(self, ctx: D96Parser.Inside_declsContext):
        listdecl = ctx.manydecl()
        res = []
        for decl in listdecl:
            res += self.visit(decl)
        return res

    def visitManydecl(self, ctx: D96Parser.ManydeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else: return self.visit(ctx.funcdecl())

    def visitFuncdecl(self, ctx: D96Parser.FuncdeclContext):
        if ctx.funcdecl1():
            return self.visit(ctx.funcdecl1())
        else:
            return self.visit(ctx.funcdecl2())

    def visitFuncdecl1(self, ctx: D96Parser.Funcdecl1Context):
        # funcdecl1: CONSTRUCTOR LP listparam_with_type? RP block_stmt | DESTRUCTOR LP RP block_stmt;
        if ctx.CONSTRUCTOR():
            return [MethodDecl(Instance(), Id("Constructor"), self.visit(ctx.listparam_with_type()) if ctx.listparam_with_type() else [], self.visit(ctx.block_stmt()))]
        else:
            return [MethodDecl(Instance(), Id("Destructor"), [], self.visit(ctx.block_stmt()))]

    def visitFuncdecl2(self, ctx: D96Parser.Funcdecl2Context):
        if ctx.ID() and ctx.ID().getText() == "main" and myClassName == "Program" and not ctx.listparam_with_type():
            return [MethodDecl(Static(), Id("main"), [], self.visit(ctx.block_stmt()))]
        else:
            return [MethodDecl(Instance() if ctx.ID() else Static(), Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.listparam_with_type()) if ctx.listparam_with_type() else [], self.visit(ctx.block_stmt()))]


    
    ############################ STMT ##############################################################################################

    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        # block_stmt: LCB stmts_list RCB;;
        return Block(self.visit(ctx.stmts_list()))

    def visitStmts_list(self, ctx: D96Parser.Stmts_listContext):
        # stmts_list: stmt*;
        liststmt = ctx.stmt()
        kq = []
        for stmt in liststmt:
            ele = self.visit(stmt)
            if isinstance(ele, list):
                kq.extend(ele)
            else:
                kq += [ele]
        return kq

    # stmt
	# : vardecl_stmt
	# | assign_stmt
	# | if_stmt 
	# | for_stmt
	# | break_stmt
	# | continue_stmt
	# | ret_stmt
	# | member_access_stmt
	# | block_stmt
	# ;

    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    
    def visitVardecl_stmt(self, ctx: D96Parser.VardeclContext): # instance (no dollar)
        # vardecl_stmt: (VAR | VAL) listvar_no_dollar (ASSIGN init_list)? SEMI;
        # listvar_no_dollar: ID (COMMA ID)* COLON typ;
        if ctx.VAR():
            if ctx.init_list():
                return [VarDecl(Id(i.getText()), self.visit(ctx.listvar_no_dollar().typ()) if ctx.listvar_no_dollar().typ() else [], self.visit(j)) for i, j in zip(ctx.listvar_no_dollar().ID(), ctx.init_list().exp())]
            else:
                return [VarDecl(Id(i.getText()), self.visit(ctx.listvar_no_dollar().typ()) if ctx.listvar_no_dollar().typ() else [], NullLiteral() if isinstance(self.visit(ctx.listvar_no_dollar().typ()), ClassType) else None) for i in ctx.listvar_no_dollar().ID()]

        elif ctx.VAL():
            if ctx.init_list():
                return [ConstDecl(Id(i.getText()), self.visit(ctx.listvar_no_dollar().typ()) if ctx.listvar_no_dollar().typ() else [], self.visit(j)) for i, j in zip(ctx.listvar_no_dollar().ID(), ctx.init_list().exp())]
            else:
                return [ConstDecl(Id(i.getText()), self.visit(ctx.listvar_no_dollar().typ()) if ctx.listvar_no_dollar().typ() else [], NullLiteral() if isinstance(self.visit(ctx.listvar_no_dollar().typ()), ClassType) else None) for i in ctx.listvar_no_dollar().ID()]


    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        return Assign(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))

    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        # if_stmt: IF LP exp RP block_stmt else_part? | IF LP exp RP block_stmt (ELSE block_stmt);
        if ctx.ELSE():
            return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(0)), self.visit(ctx.block_stmt(1)))
        else:
            return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(0)), self.visit(ctx.else_part()) if ctx.else_part() else None)

    def visitElse_part(self, ctx: D96Parser.Else_partContext):
        # else_part: (ELSEIF LP exp RP block_stmt) else_part | (ELSEIF LP exp RP block_stmt) (ELSE block_stmt)?;
        if ctx.else_part():
            return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(0)), self.visit(ctx.else_part()))
        else:
            return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(0)), self.visit(ctx.block_stmt(1)) if ctx.ELSE() else None)

    def visitFor_stmt(self, ctx: D96Parser.For_stmtContext):
        # for_stmt: FOREACH LP ID IN exp DOTDOT exp (BY exp)? RP block_stmt;
        return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.block_stmt()), self.visit(ctx.exp(2)) if ctx.exp(2) else IntLiteral(1)) # neu ko co by, tang 1

    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return Continue()

    def visitRet_stmt(self, ctx: D96Parser.Ret_stmtContext):
        # ret_stmt: RETURN SEMI | RETURN exp SEMI;
        return Return(self.visit(ctx.exp()) if ctx.exp() else None)

    def visitMember_access_stmt(self, ctx: D96Parser.Member_access_stmtContext):
        # member_access_stmt: exp DOT ID LP exps_list? RP SEMI | ID SCOPE_OP DOLLAR_ID LP exps_list? RP SEMI;
        if ctx.DOT():
            return CallStmt(self.visit(ctx.exp()) if ctx.exp() else SelfLiteral(), Id(ctx.ID().getText()), self.visit(ctx.exps_list()) if ctx.exps_list() else [])
        else:
            return CallStmt(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.exps_list()) if ctx.exps_list() else []) # con chua fix

    






    ############################ EXPRESSION ##############################################################################################

    # listparam_with_type: (listparam) (SEMI listparam)*;
    # listparam: ID (COMMA ID)* COLON typ;
    def visitListparam_with_type(self, ctx: D96Parser.Listparam_with_typeContext):
        listparam = ctx.listparam()
        res = []
        for param in listparam:
            res += self.visit(param)
        return res

    def visitListparam(self, ctx: D96Parser.ListparamContext):
        return [VarDecl(Id(i.getText()), self.visit(ctx.typ()) if ctx.typ() else [], None) for i in ctx.ID()]

    def visitTyp(self, ctx: D96Parser.TypContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.arr_type():
            return self.visit(ctx.arr_type())
        else :
            return ClassType(Id(ctx.getChild(0).getText()))

    def visitArr_type(self, ctx: D96Parser.Arr_typeContext):
        # arr_type: ARRAY LSB typ COMMA arr_size RSB;
        # arr_size: INTEGER_LITERAL;
        return ArrayType(ctx.arr_size().INTEGER_LITERAL().getText(), self.visit(ctx.typ()))

    # *************************************************************************************************************************
    # vardecl: ((VAR | VAL) listvar COLON typ SEMI) | ((VAR | VAL) vardecl_ele SEMI);
    # vardecl_ele: onevar COMMA vardecl_ele COMMA (exp | array_decl) | onevar COLON typ ASSIGN (exp | array_decl);
    # array_decl: ARRAY LP exps_list RP;
    # onevar: ID | DOLLAR_ID;
    # listvar: onevar (COMMA onevar)*;
    
    # def visitVardecl(self, ctx: D96Parser.VardeclContext):
    #     if ctx.listvar():
    #         return self.visit(ctx.listvar())
    #     else:
    #         return self.visit(ctx.vardecl_ele())
    def visitVardecl(self, ctx: D96Parser.VardeclContext):
        if ctx.VAR():
            if ctx.init_list():
                return [AttributeDecl(Instance() if i.ID() else Static(), VarDecl(Id(i.ID().getText()) if i.ID() else Id(i.DOLLAR_ID().getText()), self.visit(ctx.listvar().typ()) if ctx.listvar().typ() else [], self.visit(j))) for i, j in zip(ctx.listvar().onevar(), ctx.init_list().exp())]
            else:
                return [AttributeDecl(Instance() if i.ID() else Static(), VarDecl(Id(i.ID().getText()) if i.ID() else Id(i.DOLLAR_ID().getText()), self.visit(ctx.listvar().typ()) if ctx.listvar().typ() else [], NullLiteral() if isinstance(self.visit(ctx.listvar().typ()), ClassType) else None)) for i in ctx.listvar().onevar()]

        elif ctx.VAL():
            if ctx.init_list():
                return [AttributeDecl(Instance() if i.ID() else Static(), ConstDecl(Id(i.ID().getText()) if i.ID() else Id(i.DOLLAR_ID().getText()), self.visit(ctx.listvar().typ()) if ctx.listvar().typ() else [], self.visit(j))) for i, j in zip(ctx.listvar().onevar(), ctx.init_list().exp())]
            else:
                return [AttributeDecl(Instance() if i.ID() else Static(), ConstDecl(Id(i.ID().getText()) if i.ID() else Id(i.DOLLAR_ID().getText()), self.visit(ctx.listvar().typ()) if ctx.listvar().typ() else [], NullLiteral() if isinstance(self.visit(ctx.listvar().typ()), ClassType) else None)) for i in ctx.listvar().onevar()]
    # def visitListvar(self, ctx: D96Parser.ListvarContext):
    #     return [AttributeDecl(Instance() if i.ID() else Static(), VarDecl(Id(i.ID().getText()) if i.ID() else Id(i.DOLLAR_ID().getText()), self.visit(ctx.typ()) if ctx.typ() else [], None)) for i in ctx.onevar()]


    # def visitVardecl_ele(self, ctx: D96Parser.Vardecl_eleContext):
    #     list_var = []
    #     list_exp = []
    #     if ctx.vardecl_ele():
    #         list_var += ctx.onevar().ID() if ctx.onevar().ID() else ctx.onevar().DOLLAR_ID()
    #         list_exp += ctx.INTEGER_LITERAL()
    #         self.visit(ctx.visitVardecl_ele())
    #     else:
    #         list_var += ctx.onevar().ID() if ctx.onevar().ID() else ctx.onevar().DOLLAR_ID()
    #         list_exp += ctx.INTEGER_LITERAL()
    #         list_exp.reverse()
    #         type_var = ctx.typ()
    #         return [AttributeDecl(Instance() if i.ID() else Static(), VarDecl(Id(i.ID().getText()) if i.ID() else Id(i.DOLLAR_ID().getText()), self.visit(ctx.typ()) if ctx.typ() else [], None)) for i in ctx.onevar()]




    def visitExp(self, ctx: D96Parser.ExpContext):
        # exp: stringExp | stringExp (STR_CONCAT | STR_COMPARE) stringExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stringExp(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.stringExp(0)), self.visit(ctx.stringExp(1)))
    
    def visitStringExp(self, ctx: D96Parser.StringExpContext):
        # stringExp: logicExp | logicExp (EQUAL_TO | NOT_EQUAL | LT | GT | LTE | GTE) logicExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicExp(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.logicExp(0)), self.visit(ctx.logicExp(1)))
    
    def visitLogicExp(self, ctx: D96Parser.LogicExpContext):
        # logicExp: logicExp (AND | OR) addExp | addExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.addExp())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.logicExp()), self.visit(ctx.addExp()))
    
    
    def visitAddExp(self, ctx: D96Parser.AddExpContext):
        # addExp: addExp (ADD | SUB) mulExp | mulExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.mulExp())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.addExp()), self.visit(ctx.mulExp()))
    
    def visitMulExp(self, ctx: D96Parser.MulExpContext):
        # mulExp: mulExp ( MUL | DIV | MOD ) unaryLogicExp | unaryLogicExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryLogicExp())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.mulExp()), self.visit(ctx.unaryLogicExp()))
    
    
    def visitUnaryLogicExp(self, ctx: D96Parser.UnaryLogicExpContext):
        # unaryLogicExp: NOT unaryLogicExp | unarySignExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unarySignExp())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.unaryLogicExp()))
    
    def visitUnarySignExp(self, ctx: D96Parser.UnarySignExpContext):
        # unarySignExp: SUB unarySignExp | indexExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.indexExp())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.unarySignExp()))
    
    def visitIndexExp(self, ctx: D96Parser.IndexExpContext):
        # indexExp: indexExp index_operators | callExp1;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.callExp1())
        else:
            return ArrayCell(self.visit(ctx.indexExp()), self.visit(ctx.index_operators()))

    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        # index_operators: LSB exp RSB | LSB exp RSB index_operators;
        if ctx.index_operators():
            return [self.visit(ctx.exp())] + self.visit(ctx.index_operators())
        else:
            return [self.visit(ctx.exp())]

    def visitCallExp1(self, ctx: D96Parser.CallExp1Context):
        # callExp1: callExp1 DOT ID | callExp1 DOT ID LP exps_list? RP | selfExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.selfExp())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.callExp1()), Id(ctx.ID().getText()))
        else:
            return CallExpr(self.visit(ctx.callExp1()), Id(ctx.ID().getText()), self.visit(ctx.exps_list()) if ctx.exps_list() else [])

    def visitExps_list(self, ctx: D96Parser.Exps_listContext):
        # exps_list: exp (COMMA exp)*;
        listexp = ctx.exp()
        res = []
        for exp in listexp:
            res += [self.visit(exp)]
        return res

    def visitSelfExp(self, ctx: D96Parser.SelfExpContext):
        # selfExp: SELF DOT ID | callExp2;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.callExp2())
        else:
            return FieldAccess(SelfLiteral(), Id(ctx.ID().getText()))

    def visitCallExp2(self, ctx: D96Parser.CallExp2Context):
        # ccallExp2: ID SCOPE_OP DOLLAR_ID  | ID SCOPE_OP DOLLAR_ID LP exps_list? RP | newExp;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.newExp())
        elif ctx.getChildCount() == 3:
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()))
        else:
            return CallExpr(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.exps_list()) if ctx.exps_list() else [])

    def visitNewExp(self, ctx: D96Parser.NewExpContext):
        # newExp: NEW ID LP exps_list? RP | lastExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.lastExpr())
        else:
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exps_list()) if ctx.exps_list() else [])
    
    def visitLastExpr(self, ctx: D96Parser.LastExprContext):
        # lastExpr: literal | array_decl | (ID | DOLLAR_ID) | LP exp RP;
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.array_decl():
            return self.visit(ctx.array_decl())
        elif ctx.exp():
            return self.visit(ctx.exp())
        else:
            return Id(ctx.getChild(0).getText())

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        # literal: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL;
        if ctx.INTEGER_LITERAL():
            myNum = ctx.INTEGER_LITERAL().getText()
            if myNum.startswith('0x') or myNum.startswith('0X'):
                return IntLiteral(int(myNum, 16))
            elif myNum.startswith('0b') or myNum.startswith('0B'):
                return IntLiteral(int(myNum, 2))
            elif myNum.startswith("0") and myNum != "0":
                return IntLiteral(int(myNum, 8))
            else:
                return IntLiteral(int(myNum))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText() == 'True')
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        else: return NullLiteral()

    def visitArray_decl(self, ctx: D96Parser.Array_declContext):
        # array_decl: ARRAY LP exps_list? RP;
        if ctx.exps_list():
            return ArrayLiteral(self.visit(ctx.exps_list()))
        else: return ArrayLiteral([])


    

        
    













