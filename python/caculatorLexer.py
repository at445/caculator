# Generated from ./caculator.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\6\7-\n\7\r\7\16\7.\3\b\6\b\62\n\b\r\b\16")
        buf.write("\b\63\3\t\5\t\67\n\t\3\t\3\t\3\n\6\n<\n\n\r\n\16\n=\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\3\2\5\4\2C\\c|\3\2\62;\4\2\13\13\"\"\2L\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35")
        buf.write("\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2")
        buf.write("\r,\3\2\2\2\17\61\3\2\2\2\21\66\3\2\2\2\23;\3\2\2\2\25")
        buf.write("A\3\2\2\2\27C\3\2\2\2\31E\3\2\2\2\33G\3\2\2\2\35\36\7")
        buf.write("r\2\2\36\37\7t\2\2\37 \7k\2\2 !\7p\2\2!\"\7v\2\2\"\4\3")
        buf.write("\2\2\2#$\7*\2\2$\6\3\2\2\2%&\7+\2\2&\b\3\2\2\2\'(\7?\2")
        buf.write("\2(\n\3\2\2\2)*\7\60\2\2*\f\3\2\2\2+-\t\2\2\2,+\3\2\2")
        buf.write("\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\16\3\2\2\2\60\62\t\3")
        buf.write("\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\20\3\2\2\2\65\67\7\17\2\2\66\65\3\2\2\2\66\67")
        buf.write("\3\2\2\2\678\3\2\2\289\7\f\2\29\22\3\2\2\2:<\t\4\2\2;")
        buf.write(":\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\b")
        buf.write("\n\2\2@\24\3\2\2\2AB\7,\2\2B\26\3\2\2\2CD\7\61\2\2D\30")
        buf.write("\3\2\2\2EF\7-\2\2F\32\3\2\2\2GH\7/\2\2H\34\3\2\2\2\7\2")
        buf.write(".\63\66=\3\b\2\2")
        return buf.getvalue()


class caculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    ID = 6
    INT = 7
    NEWLINE = 8
    WS = 9
    MUL = 10
    DIV = 11
    ADD = 12
    SUB = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'('", "')'", "'='", "'.'", "'*'", "'/'", "'+'", 
            "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "NEWLINE", "WS", "MUL", "DIV", "ADD", "SUB" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "ID", "INT", "NEWLINE", 
                  "WS", "MUL", "DIV", "ADD", "SUB" ]

    grammarFileName = "caculator.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


