from sly import Lexer
import re

class SblLexer(Lexer):
    tokens = { ASSIGN, VAR, REAL, INT, STRING, EXPON,
            PLUS, MINUS, TIMES, DIVIDE, EQ, NOTEQ, LESS, LESSEQ, GREAT, GREATEQ, 
            CONS, TRUE, FALSE, INTDIV, MOD, NOT, IN, AND, OR, IF, ELSE, WHILE, PRINT, FUN}

    literals = {'(',')','[',']',',','#','{','}',';'}

    ignore = '\t \s'

    @_(r'(\d+\.(\d*)?(e-?\d+)?|\.\d+(e[+-]?\d+)?)')
    def REAL(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t

    @_(r'\"([^\"]*|[^\']*)\"',
      r'\'([^\"]*|[^\']*)\'')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t

    PLUS = r'\+'
    MINUS = r'-'
    EXPON = r'\*\*'
    TIMES = r'\*'
    DIVIDE = r'/'
    EQ = r'=='
    NOTEQ = r'<>'
    LESSEQ = r'<='
    GREATEQ = r'>='
    LESS = r'<'
    GREAT = r'>'
    CONS = r'::'
    ASSIGN = r'='
    
    FUN = r'\bfun\b'
    TRUE = r'\bTrue\b'
    FALSE = r'\bFalse\b'
    INTDIV = r'\bdiv\b'
    MOD = r'\bmod\b'
    NOT = r'\bnot\b'
    IN = r'\bin\b'
    AND = r'\bandalso\b'
    OR = r'\borelse\b'
    IF = r'\bif\b'
    ELSE = r'\belse\b'
    WHILE = r'\bwhile\b'
    PRINT = r'\bprint\b'
    VAR = r'[a-zA-Z][a-zA-Z0-9_]*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        self.index += 1
