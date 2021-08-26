import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'AND',
    'OR',
    'NOT',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
A OR B AND (C AND D)
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    print(tok.type)
    print(tok.value)
    print(tok.lineno)
    print(tok.lexpos)

