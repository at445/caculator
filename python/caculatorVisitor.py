# Generated from ./caculator.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .caculatorParser import caculatorParser
else:
    from caculatorParser import caculatorParser

# This class defines a complete generic visitor for a parse tree produced by caculatorParser.

class caculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by caculatorParser#prog.
    def visitProg(self, ctx:caculatorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#explicitPrint.
    def visitExplicitPrint(self, ctx:caculatorParser.ExplicitPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#FormulasPrint.
    def visitFormulasPrint(self, ctx:caculatorParser.FormulasPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#assign.
    def visitAssign(self, ctx:caculatorParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#blank.
    def visitBlank(self, ctx:caculatorParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#ParenthesisExpr.
    def visitParenthesisExpr(self, ctx:caculatorParser.ParenthesisExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#FloatExpr.
    def visitFloatExpr(self, ctx:caculatorParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:caculatorParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by caculatorParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:caculatorParser.AddSubExprContext):
        return self.visitChildren(ctx)



del caculatorParser