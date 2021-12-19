tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE', 'POW', 'EQUALS', 
    'LPAREN','RPAREN',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POW     = r'\^'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"
t_ignore_comment = r'\#(.|\\\n)*\n'
t_ignore_newlineslash = r'\\\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
from os import error
import re
import ply.lex as lex
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('nonassoc', 'POW'),
    ('right','UMINUS'),
    )

# Constants
P = 1234577 # Z_p

# My method in Algebraic number field
from math import floor

def divide(a, b):
    return floor(a/b)

def modulo(a, b):
    return a - divide(a, b) * b

def multiply(a, b):
    result = 0
    while b > 0:
        if b % 2 == 1:
            result = (result + a) % P
        a = (a * 2) % P
        b /= 2
    return modulo(result, P)

def pp(a, b):
    # power function
    result = a
    for i in range(1, b):
        result = multiply(result, a)
    return result

def reci(a):
    u = 1
    w = a
    x = 0
    z = P
    while w != 0:
        if w < z:
            q = u
            u = x
            x = q
            q = w
            w = z
            z = q
        q = int(w / z)
        u -= q * x
        w -= q * z

    if x < 0:
        x += P
    return x

def NWD(a, b):
    while a != b:
       if a > b:
           a -= b
       else:
           b -= a
    return a


# dictionary of names
names = { }
rpn = [] # reverse polnish notation
error = 0

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    global error
    rpntext = ""
    for element in rpn:
        rpntext += element + " "
    rpn.clear()
    
    if error == 0:
        print("{}\n= {}".format(rpntext, t[1]))
    else:
        print("Bład")
    error = 0

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POW pwr'''
    if t[2] == '+':
        rpn.append("+")
        t[0] = modulo(t[1]+t[3], P)
    elif t[2] == '-':
        rpn.append("-")
        t[0] = modulo(t[1]-t[3], P)
    elif t[2] == '*':
        rpn.append("*")
        t[0] = t[1] * t[3] % P
    elif t[2] == '/':
        rpn.append("/")
        if t[3] == 0:
            global error
            error = 1
            t[0] = 0
            return 
        t[0] = t[1] * reci(t[3]) % P
    elif t[2] == '^':
        rpn.append('^')
        t[0] = pow(t[1], t[3], P)
    
def p_pwr_neg(t):
    ''' pwr : MINUS pwr %prec UMINUS'''
    rpn[len(rpn)-1] = str((P-1)-t[2])
    t[0] = -t[2]

def p_pwr_num(t):
    ''' pwr : NUMBER '''
    rpn.append(str(int(t[1]) % P))
    t[0] = int(t[1]) % P
    
def p_pwr_group(t):
    ''' pwr : LPAREN pwr2 RPAREN'''
    t[0] = t[2]
    
def p_pwr2_num(t):
    ''' pwr2 : NUMBER '''
    rpn.append(str(int(t[1]) % P))
    t[0] = int(t[1]) % P
    
def p_pwr2_divide(t):
    ''' pwr2 : pwr2 DIVIDE pwr2'''
    global error, P
    if t[3] == 0:
        error = 1
        t[0] = 1
        return
    else:
        if NWD(t[3], P - 1) == 1:
            P -= 1
            rpn[len(rpn) - 1] = str(reci(t[3]))
            t[0] = t[1] * reci(t[3])
            P += 1
        else:
            t[0] = 1
            error = 1

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    while P - t[2] < 0:
        t[2] += P
    rpn[len(rpn) - 1] = str(modulo(P - t[2], P))
    t[0] = modulo(P - t[2], P)

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    rpn.append(str(modulo(t[1], P)))
    t[0] = modulo(t[1], P)

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input()   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
