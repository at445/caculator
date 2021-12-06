grammar caculator;
/** The start rule; begin parsing here. */
prog: stat+;
stat: 'print' '(' ID ')' NEWLINE    # explicitPrint
    | expr                          # FormulasPrint
    | ID '=' expr NEWLINE           # assign
    | NEWLINE                       # blank
    ;

expr: '(' expr ')'                  # ParenthesisExpr
    | expr ('*'|'/') expr           # MulDivExpr
    | expr ('+'|'-') expr           # AddSubExpr
    | (ADD | SUB)? INT('.' INT)*    # FloatExpr
    ;

ID : [a-zA-Z]+ ; // match identifiers 
INT : [0-9]+ ; // match integers
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS : [ \t]+ -> skip ; // toss out whitespace
MUL : '*' ; // assigns token name to '*' used above in grammar
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;