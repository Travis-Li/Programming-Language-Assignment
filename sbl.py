import sys
from sly import Parser
from sbllexer import SblLexer
from sblparser import SblParser

if __name__ == '__main__':
    lexer = SblLexer()
    parser = SblParser()

    data = open(sys.argv[1],'r').read()

    result = parser.parse(lexer.tokenize(data))