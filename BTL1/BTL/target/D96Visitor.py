# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#inheritance_from.
    def visitInheritance_from(self, ctx:D96Parser.Inheritance_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#inside_decls.
    def visitInside_decls(self, ctx:D96Parser.Inside_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcdecls.
    def visitFuncdecls(self, ctx:D96Parser.FuncdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcdecl.
    def visitFuncdecl(self, ctx:D96Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcdecl1.
    def visitFuncdecl1(self, ctx:D96Parser.Funcdecl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcdecl2.
    def visitFuncdecl2(self, ctx:D96Parser.Funcdecl2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listparam_with_type.
    def visitListparam_with_type(self, ctx:D96Parser.Listparam_with_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listparam.
    def visitListparam(self, ctx:D96Parser.ListparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecls.
    def visitVardecls(self, ctx:D96Parser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_ele.
    def visitVardecl_ele(self, ctx:D96Parser.Vardecl_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_decl.
    def visitArray_decl(self, ctx:D96Parser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#onevar.
    def visitOnevar(self, ctx:D96Parser.OnevarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listvar.
    def visitListvar(self, ctx:D96Parser.ListvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_no_dollar.
    def visitVardecl_no_dollar(self, ctx:D96Parser.Vardecl_no_dollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_no_dollar_ele.
    def visitVardecl_no_dollar_ele(self, ctx:D96Parser.Vardecl_no_dollar_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listvar_no_dollar.
    def visitListvar_no_dollar(self, ctx:D96Parser.Listvar_no_dollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_stmt.
    def visitMember_access_stmt(self, ctx:D96Parser.Member_access_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ret_stmt.
    def visitRet_stmt(self, ctx:D96Parser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmts_list.
    def visitStmts_list(self, ctx:D96Parser.Stmts_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exps_list.
    def visitExps_list(self, ctx:D96Parser.Exps_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_type.
    def visitArr_type(self, ctx:D96Parser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_size.
    def visitArr_size(self, ctx:D96Parser.Arr_sizeContext):
        return self.visitChildren(ctx)



del D96Parser