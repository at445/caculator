# Generated from ./caculator.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\32")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\4\3\4\3\4\7\4")
        buf.write("\'\n\4\f\4\16\4*\13\4\5\4,\n\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\7\4\64\n\4\f\4\16\4\67\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2")
        buf.write("\16\17\3\2\f\r\2>\2\t\3\2\2\2\4\31\3\2\2\2\6+\3\2\2\2")
        buf.write("\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13")
        buf.write("\f\3\2\2\2\f\3\3\2\2\2\r\16\7\3\2\2\16\17\7\4\2\2\17\20")
        buf.write("\7\b\2\2\20\21\7\5\2\2\21\32\7\n\2\2\22\32\5\6\4\2\23")
        buf.write("\24\7\b\2\2\24\25\7\6\2\2\25\26\5\6\4\2\26\27\7\n\2\2")
        buf.write("\27\32\3\2\2\2\30\32\7\n\2\2\31\r\3\2\2\2\31\22\3\2\2")
        buf.write("\2\31\23\3\2\2\2\31\30\3\2\2\2\32\5\3\2\2\2\33\34\b\4")
        buf.write("\1\2\34\35\7\4\2\2\35\36\5\6\4\2\36\37\7\5\2\2\37,\3\2")
        buf.write("\2\2 \"\t\2\2\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#(\7\t")
        buf.write("\2\2$%\7\7\2\2%\'\7\t\2\2&$\3\2\2\2\'*\3\2\2\2(&\3\2\2")
        buf.write("\2()\3\2\2\2),\3\2\2\2*(\3\2\2\2+\33\3\2\2\2+!\3\2\2\2")
        buf.write(",\65\3\2\2\2-.\f\5\2\2./\t\3\2\2/\64\5\6\4\6\60\61\f\4")
        buf.write("\2\2\61\62\t\2\2\2\62\64\5\6\4\5\63-\3\2\2\2\63\60\3\2")
        buf.write("\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\7\3")
        buf.write("\2\2\2\67\65\3\2\2\2\t\13\31!(+\63\65")
        return buf.getvalue()


class caculatorParser ( Parser ):

    grammarFileName = "caculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "'='", "'.'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "NEWLINE", 
                      "WS", "MUL", "DIV", "ADD", "SUB" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    INT=7
    NEWLINE=8
    WS=9
    MUL=10
    DIV=11
    ADD=12
    SUB=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(caculatorParser.StatContext)
            else:
                return self.getTypedRuleContext(caculatorParser.StatContext,i)


        def getRuleIndex(self):
            return caculatorParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = caculatorParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << caculatorParser.T__0) | (1 << caculatorParser.T__1) | (1 << caculatorParser.ID) | (1 << caculatorParser.INT) | (1 << caculatorParser.NEWLINE) | (1 << caculatorParser.ADD) | (1 << caculatorParser.SUB))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return caculatorParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FormulasPrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(caculatorParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormulasPrint" ):
                return visitor.visitFormulasPrint(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(caculatorParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class ExplicitPrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(caculatorParser.ID, 0)
        def NEWLINE(self):
            return self.getToken(caculatorParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitPrint" ):
                return visitor.visitExplicitPrint(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(caculatorParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(caculatorParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(caculatorParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = caculatorParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [caculatorParser.T__0]:
                localctx = caculatorParser.ExplicitPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(caculatorParser.T__0)
                self.state = 12
                self.match(caculatorParser.T__1)
                self.state = 13
                self.match(caculatorParser.ID)
                self.state = 14
                self.match(caculatorParser.T__2)
                self.state = 15
                self.match(caculatorParser.NEWLINE)
                pass
            elif token in [caculatorParser.T__1, caculatorParser.INT, caculatorParser.ADD, caculatorParser.SUB]:
                localctx = caculatorParser.FormulasPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.expr(0)
                pass
            elif token in [caculatorParser.ID]:
                localctx = caculatorParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(caculatorParser.ID)
                self.state = 18
                self.match(caculatorParser.T__3)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(caculatorParser.NEWLINE)
                pass
            elif token in [caculatorParser.NEWLINE]:
                localctx = caculatorParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.match(caculatorParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return caculatorParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesisExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(caculatorParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisExpr" ):
                return visitor.visitParenthesisExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(caculatorParser.INT)
            else:
                return self.getToken(caculatorParser.INT, i)
        def ADD(self):
            return self.getToken(caculatorParser.ADD, 0)
        def SUB(self):
            return self.getToken(caculatorParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(caculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(caculatorParser.ExprContext,i)

        def MUL(self):
            return self.getToken(caculatorParser.MUL, 0)
        def DIV(self):
            return self.getToken(caculatorParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a caculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(caculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(caculatorParser.ExprContext,i)

        def ADD(self):
            return self.getToken(caculatorParser.ADD, 0)
        def SUB(self):
            return self.getToken(caculatorParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = caculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [caculatorParser.T__1]:
                localctx = caculatorParser.ParenthesisExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 26
                self.match(caculatorParser.T__1)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(caculatorParser.T__2)
                pass
            elif token in [caculatorParser.INT, caculatorParser.ADD, caculatorParser.SUB]:
                localctx = caculatorParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==caculatorParser.ADD or _la==caculatorParser.SUB:
                    self.state = 30
                    _la = self._input.LA(1)
                    if not(_la==caculatorParser.ADD or _la==caculatorParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 33
                self.match(caculatorParser.INT)
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 34
                        self.match(caculatorParser.T__4)
                        self.state = 35
                        self.match(caculatorParser.INT) 
                    self.state = 40
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = caculatorParser.MulDivExprContext(self, caculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        _la = self._input.LA(1)
                        if not(_la==caculatorParser.MUL or _la==caculatorParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = caculatorParser.AddSubExprContext(self, caculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(_la==caculatorParser.ADD or _la==caculatorParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(3)
                        pass

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




