from python.caculatorVisitor import caculatorVisitor
from python.caculatorParser import caculatorParser
class caculatorImpVisitor(caculatorVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.idMap = {}
    # Visit a parse tree produced by caculatorParser#explicitPrint.
    def visitExplicitPrint(self, ctx:caculatorParser.ExplicitPrintContext):
        id = ctx.ID().getText()
        if id in self.idMap:
            print("variable {} = {}".format(ctx.ID().getText().strip(), self.idMap.get(id)))
        else:
            print("""Error: cannot find the "variable" {}""".format(id))
        return None

    # Visit a parse tree produced by caculatorParser#implyFormulasPrint.
    def visitFormulasPrint(self, ctx:caculatorParser.FormulasPrintContext):
        value = self.visit(ctx.expr())
        print("formulas {} = {}".format(ctx.getText().strip(), value))
        return self.visitChildren(ctx)
        
    def visitAddSubExpr(self, ctx: caculatorParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.ADD() is not None:
            return left+right
        return left-right
    def visitMulDivExpr(self, ctx: caculatorParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MUL() is not None:
            return left*right
        return left/right
    def visitParenthesisExpr(self, ctx: caculatorParser.ParenthesisExprContext):
        return self.visit(ctx.expr())

    def visitAssign(self, ctx: caculatorParser.AssignContext):
        key = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if key in self.idMap:
            print("warning: the {} will be overwrited".format(key))
        self.idMap[key] = value
        return None
        #return super().visitPrintExpr(ctx)
    def visitFloatExpr(self, ctx: caculatorParser.FloatExprContext):
        ints = ctx.INT()
        ret = ints[0].getText()
        if len(ints) == 2:
            ret += '.' + ints[1].getText()
        sign = ctx.SUB()
        if sign is not None:
            return -float(ret)
        return float(ret)
    