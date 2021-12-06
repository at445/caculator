import sys
from antlr4 import *
from python.caculatorLexer import caculatorLexer
from python.caculatorParser import caculatorParser
from caculatorImpVisitor import caculatorImpVisitor

if __name__ == "__main__":
    # inputString = " 12*(1+(1+1)*2)   \n \
    #                 c = (1-2)*3+(1+1+1)/1 \n \
    #                 d = (-2)*3+(1+1+1)/1 \n \
    #                 d\nc\n192\n"
    inputString = "192\n \
                12*(1+(1+1)*2) \n   \
                    c = (-2)*3+(1+1+1)/1 \n \
                    print(c) \n \
                    1.2+12*2\n \
                    1.2+(-12)*2\n \
                    print(d) \
                    c = 1.22+(-12)*2 \
                    print(c) \n \
                    "
    input = InputStream(inputString)
    lexer = caculatorLexer(input)
    tokens = CommonTokenStream(lexer)
    paser = caculatorParser(tokens)
    ptree = paser.prog()
    visitor = caculatorImpVisitor()
    visitor.visit(ptree)