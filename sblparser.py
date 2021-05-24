from sly import Parser
from sbllexer import SblLexer
import copy

SymbolTable = {}
FunctionTable = {}

class SblParser(Parser):
    tokens = SblLexer.tokens

    class BinOp(object):
        def __init__(self, op, left, right):
            self.op = op
            self.left = left
            self.right = right

        def eval(self):
            if self.op == 'orelse':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif type(val1) is not bool or type(val2) is not bool:
                    print("SEMANTIC ERROR")
                    return None
                else:
                    return val1 or val2
            elif self.op == 'andalso':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif type(val1) is not bool or type(val2) is not bool:
                    print("SEMANTIC ERROR")
                    return None
                else:
                    return val1 and val2
            elif self.op == 'not':
                val = self.left.eval()
                if val == None:
                    return None
                elif type(val) is not bool:
                    print("SEMANTIC ERROR")
                    return None
                else:
                    return not val
            elif self.op == '<':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 < val2
            elif self.op == '<=':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 <= val2
            elif self.op == '>':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 > val2
            elif self.op == '>=':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 >= val2
            elif self.op == '==':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 == val2
            elif self.op == '<>':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 != val2
            elif self.op == '::':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not(type(val2) == list):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return [val1] + val2
            elif self.op == 'in':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not(type(val2) == str or type(val2) == list):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 in val2
            elif self.op == '+':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not ((type(val1) == int or type(val1) == float or type(val1) == str or type(val1) == list) or (type(val2) == int or type(val2) == float or type(val2) == str or type(val2) == list)):
                    print ("SEMANTIC ERROR")
                    return None
                elif not (((type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float)) or (type(val1) == str and type(val2) == str) or (type(val1) == list and type(val2) == list)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 + val2
            elif self.op == '-':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not ((type(val1) == int or type(val1) == float) or (type(val2) == int or type(val2) == float)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 - val2
            elif self.op == '*':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not ((type(val1) == int or type(val1) == float) or (type(val2) == int or type(val2) == float)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 * val2
            elif self.op == '/':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif val2 == 0:
                    print ("SEMANTIC ERROR")
                    return None
                elif not ((type(val1) == int or type(val1) == float) or (type(val2) == int or type(val2) == float)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 / val2
            elif self.op == 'div':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif val2 == 0:
                    print ("SEMANTIC ERROR")
                    return None
                elif not ((type(val1) == int or type(val1) == float) or (type(val2) == int or type(val2) == float)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 // val2
            elif self.op == 'mod':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not ((type(val1) == int or type(val1) == float) or (type(val2) == int or type(val2) == float)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 % val2
            elif self.op == '**':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not ((type(val1) == int or type(val1) == float) or (type(val2) == int or type(val2) == float)):
                    print ("SEMANTIC ERROR")
                    return None
                else:
                    return val1 ** val2
            elif self.op == 'INDEX':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not((type(val1) == list and type(val2) == int) or (type(val1) == str and type(val2) == int)):
                    print("SEMANTIC ERROR")
                    return None
                elif not(val2 >= 0 and val2 < len(val1)):
                    print("SEMANTIC ERROR")
                    return None        
                else:
                    return val1[val2]
            elif self.op == 'TUPINDEX':
                val1 = self.left.eval()
                val2 = self.right.eval()
                if val1 == None or val2 == None:
                    return None
                elif not(type(val2) == tuple and type(val1) == int):
                    print("SEMANTIC ERROR")
                    return None
                elif not(val1 >= 1 and val1 < len(val2) + 1):
                    print("SEMANTIC ERROR")
                    return None        
                else:
                    return self.right.eval()[self.left.eval() - 1]
            else:
                return None

    class FunctionDef(object):
        def __init__(self, name, args, block, returnexpr):
            self.name = name
            self.args = args
            self.block = block
            self.returnexpr = returnexpr
        def eval(self):
            FunctionTable[self.name] = (self.args, self.block, self.returnexpr)

    class FunctionCall(object):
        def __init__(self, name, args):
            self.name = name
            self.args = args
        def eval(self):
            if self.name in FunctionTable:
                if len(FunctionTable[self.name][0]) == len(self.args):
                    global SymbolTable
                    outerSymbolTable = copy.deepcopy(SymbolTable)
                    i = 0
                    for arg in FunctionTable[self.name][0]:
                        x = arg.name
                        SymbolTable[x] = self.args[i].eval()
                        i = i + 1
                    FunctionTable[self.name][1].eval()
                    output = FunctionTable[self.name][2].eval()
                    SymbolTable = outerSymbolTable
                    return output
                else:
                    print("SEMANTIC ERROR")
                    return None
            else:
                print("SEMANTIC ERROR")
                return None

    class Statement(object):
        def __init__(self, stmt, next):
            self.stmt = stmt
            self.next = next
        def eval(self):
            self.stmt.eval()
            if not (self.next == None):
                self.next.eval()

    class IfElse(object):
        def __init__(self, expression, ifblock, elseblock):
            self.expression = expression
            self.ifblock = ifblock
            self.elseblock = elseblock
        def eval(self):
            if type(self.expression.eval()) is not bool:
                print("SEMANTIC ERROR")
                return None
            elif self.expression.eval():
                return self.ifblock.eval()
            elif not (self.elseblock == None):
                return self.elseblock.eval()
            else:
                return None

    class While(object):
        def __init__(self, expression, block):
            self.expression = expression
            self.block = block
        def eval(self):
            if type(self.expression.eval()) is not bool:
                print("SEMANTIC ERROR")
                return None
            else:
                whileBool = self.expression.eval()
                while(whileBool):
                    self.block.eval()
                    whileBool = self.expression.eval()
                return None

    class ListAssign(object):
        def __init__(self, listToChange, index, value):
            self.listToChange = listToChange
            self.index = index
            self.value = value
        def eval(self):
            val1 = self.listToChange.eval()
            val2 = self.index.eval()
            if type(val1) is not list or (type(val2) is not int and type(val2) is not float):
                print("SEMANTIC ERROR")
                return None
            else:
                self.listToChange.eval()[self.index.eval()] = self.value.eval()
                return None

    class VarAssign(object):
        def __init__(self, var, value):
            self.var = var
            self.value = value
        def eval(self):
            global SymbolTable
            SymbolTable[self.var] = self.value.eval()
            return None

    class Print(object):
        def __init__(self, value):
            self.value = value
        def eval(self):
            print(self.value.eval())
            return None

    class Var(object):
        def __init__(self, name):
            self.name = name
        def eval(self):
            global SymbolTable
            if self.name in SymbolTable:
                return SymbolTable[self.name]
            else:
                print("SEMANTIC ERROR")
                return None

    class Number(object):
        def __init__(self, value):
            self.value = value
        def eval(self):
            return self.value
    
    class Boolean(object):
        def __init__(self, value):
            self.value = value
        def eval(self):
            return self.value
    
    class String(object):
        def __init__(self, value):
            self.value = value
        def eval(self):
            return self.value

    class List(object):
        def __init__(self, value):
            self.value = value
        def eval(self):
            newlist = []
            for entry in self.value:
                newlist = newlist + [entry.eval()]
            return newlist

    class Tuple(object):
        def __init__(self, value):
            self.value = value
        def eval(self):
            newtup = ()
            for entry in self.value:
                newtup = newtup + (entry.eval(),)
            return newtup

    @_('blocklist')
    def start(self, p):
        return p.blocklist.eval()

    @_('fundef blocklist')
    def blocklist(self, p):
        return self.Statement(p.fundef, p.blocklist)

    @_('fundef empty')
    def blocklist(self, p):
        return self.Statement(p.fundef, None)

    @_('FUN VAR "(" listexprlist ")" ASSIGN block orexpr ";"')
    def fundef(self, p):
        return self.FunctionDef(p.VAR, p.listexprlist, p.block, p.orexpr)

    @_('FUN VAR "(" ")" ASSIGN block orexpr ";"')
    def fundef(self, p):
        return self.FunctionDef(p.VAR, [], p.block, p.orexpr)

    @_('block')
    def fundef(self, p):
        return p.block

    @_('"{" stmtlist "}"')
    def block(self, p):
        return p.stmtlist

    @_('condblock stmtlist')
    def stmtlist(self, p):
        return self.Statement(p.condblock, p.stmtlist)

    @_('condblock empty')
    def stmtlist(self, p):
        return self.Statement(p.condblock, None)

    @_('IF orexpr block ELSE block')
    def condblock(self, p):
        return self.IfElse(p.orexpr, p.block0, p.block1)

    @_('IF orexpr block')
    def condblock(self, p):
        return self.IfElse(p.orexpr, p.block, None)

    @_('WHILE orexpr block')
    def condblock(self, p):
        return self.While(p.orexpr, p.block)

    @_('stmt')
    def condblock(self, p):
        return p.stmt

    @_('indexexpr "[" orexpr "]" ASSIGN orexpr ";"')
    def stmt(self, p):
        return self.ListAssign(p.indexexpr, p.orexpr0, p.orexpr1)
    
    @_('VAR ASSIGN orexpr ";"')
    def stmt(self, p):
        return self.VarAssign(p.VAR, p.orexpr)

    @_('PRINT "(" orexpr ")" ";"')
    def stmt(self, p):
        return self.Print(p.orexpr)

    @_('orexpr')
    def stmt(self, p):
        return p.orexpr

    @_('orexpr OR andexpr')
    def orexpr(self, p):
        return self.BinOp(p[1], p.orexpr, p.andexpr)

    @_('andexpr')
    def orexpr(self, p):
        return p.andexpr

    @_('andexpr AND notexpr')
    def andexpr(self, p):
        return self.BinOp(p[1], p.andexpr, p.notexpr)

    @_('notexpr')
    def andexpr(self, p):
        return p.notexpr

    @_('NOT notexpr')
    def notexpr(self, p):
        return self.BinOp(p[0], p.notexpr, None)

    @_('compexpr')
    def notexpr(self, p):
        return p.compexpr

    @_('conexpr LESS conexpr')
    def compexpr(self, p):
        return self.BinOp(p[1], p.conexpr0, p.conexpr1)

    @_('conexpr LESSEQ conexpr')
    def compexpr(self, p):
        return self.BinOp(p[1], p.conexpr0, p.conexpr1)

    @_('conexpr GREAT conexpr')
    def compexpr(self, p):
        return self.BinOp(p[1], p.conexpr0, p.conexpr1)

    @_('conexpr GREATEQ conexpr')
    def compexpr(self, p):
        return self.BinOp(p[1], p.conexpr0, p.conexpr1)

    @_('conexpr EQ conexpr')
    def compexpr(self, p):
        return self.BinOp(p[1], p.conexpr0, p.conexpr1)

    @_('conexpr NOTEQ conexpr')
    def compexpr(self, p):
        return self.BinOp(p[1], p.conexpr0, p.conexpr1)

    @_('conexpr')
    def compexpr(self, p):
        return p.conexpr

    @_('inexpr CONS conexpr')
    def conexpr(self, p):
        return self.BinOp(p[1], p.inexpr, p.conexpr)

    @_('inexpr')
    def conexpr(self, p):
        return p.inexpr

    @_('inexpr IN addexpr')
    def inexpr(self, p):
        return self.BinOp(p[1], p.inexpr, p.addexpr)

    @_('addexpr')
    def inexpr(self, p):
        return p.addexpr
    
    @_('addexpr PLUS multexpr')
    def addexpr(self, p):
        return self.BinOp(p[1], p.addexpr, p.multexpr)

    @_('addexpr MINUS multexpr')
    def addexpr(self, p):
        return self.BinOp(p[1], p.addexpr, p.multexpr)

    @_('multexpr')
    def addexpr(self, p):
        return p.multexpr

    @_('multexpr TIMES exponexpr')
    def multexpr(self, p):
        return self.BinOp(p[1], p.multexpr, p.exponexpr)

    @_('multexpr DIVIDE exponexpr')
    def multexpr(self, p):
        return self.BinOp(p[1], p.multexpr, p.exponexpr)

    @_('multexpr INTDIV exponexpr')
    def multexpr(self, p):
        return self.BinOp(p[1], p.multexpr, p.exponexpr)

    @_('multexpr MOD exponexpr')
    def multexpr(self, p):
        return self.BinOp(p[1], p.multexpr, p.exponexpr)

    @_('exponexpr')
    def multexpr(self, p):
        return p.exponexpr

    @_('indexexpr EXPON exponexpr')
    def exponexpr(self, p):
        return self.BinOp(p[1], p.indexexpr, p.exponexpr)  

    @_('indexexpr')
    def exponexpr(self, p):
        return p.indexexpr

    @_('indexexpr "[" orexpr "]"')
    def indexexpr(self, p):
        return self.BinOp('INDEX', p.indexexpr, p.orexpr)

    @_('"#" indexexpr funcall')
    def indexexpr(self, p):
        return self.BinOp('TUPINDEX', p.indexexpr, p.funcall)

    @_('funcall')
    def indexexpr(self, p):
        return p.funcall

    @_('VAR "(" listexprlist ")"')
    def funcall(self, p):
        return self.FunctionCall(p.VAR, p.listexprlist)

    @_('VAR "(" ")"')
    def funcall(self, p):
        return self.FunctionCall(p.VAR, [])

    @_('value')
    def funcall(self, p):
        return p.value

    @_("TRUE")
    def value(self, p):
        return self.Boolean(p.TRUE == 'True')

    @_("FALSE")
    def value(self, p):
        return self.Boolean(p.FALSE == 'True')

    @_('INT', 'REAL')
    def value(self, p):
        return self.Number(p[0])

    @_('STRING')
    def value(self, p):
        return self.String(p.STRING)

    @_('VAR')
    def value(self, p):
        return self.Var(p.VAR)

    @_('"(" orexpr ")"')
    def value(self, p):
        return p.orexpr

    @_('storeconstructor')
    def value(self, p):
        return p.storeconstructor

    @_('constructor')
    def storeconstructor(self, p):
        val = p.constructor
        if type(val) == tuple:
            return self.Tuple(val)
        elif type(val) == list:
            return self.List(val)
        else:
            return val

    @_('"(" orexpr "," tupexprlist ")"')
    def constructor(self, p):
        val = p.orexpr
        return (val,) + p.tupexprlist

    @_('"(" orexpr "," ")"')
    def constructor(self, p):
        val = p.orexpr
        return (val,)

    @_('"(" ")"')
    def constructor(self, p):
        return tuple()

    @_('"[" orexpr "," listexprlist "]"')
    def constructor(self, p):
        val = p.orexpr
        return [val] + p.listexprlist

    @_('"[" orexpr "]"')
    def constructor(self, p):
        val = p.orexpr
        return [val]

    @_('"["  "]"')
    def constructor(self, p):
        return list()

    @_('uminus')
    def constructor(self, p):
        return p.uminus

    @_('tupexprlist "," orexpr')
    def tupexprlist(self, p):
        val = p.orexpr
        return p.tupexprlist + (val,)

    @_('orexpr')
    def tupexprlist(self, p):
        val = p.orexpr
        return (val,)

    @_('listexprlist "," orexpr')
    def listexprlist(self, p):
        val = p.orexpr
        return p.listexprlist + [val]

    @_('orexpr')
    def listexprlist(self, p):
        val = p.orexpr
        return [val]

    @_('MINUS INT',
        'MINUS REAL')
    def uminus(self, p):
        return self.Number(-1 * p[1])

    @_('')
    def empty(self, p):
        pass

    def error(self, p):
        print ("SYNTAX ERROR")
        self.restart()