import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'AND',
    'OR',
    'NOT',
    'FIELD',
    'WILDCARDS',
    'REGEXP',
    'FUZZINESS',
    'LRANGE',
    'RRANGE',
    'NUMBER',
    'ALPHABET'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_FIELD = r':'
t_WILDCARDS = r'[?|*]'
t_REGEXP = r'/'
t_FUZZINESS = r'~'
t_LRANGE = r'[\[|{]'
t_RRANGE = r'[\]|}]'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ALPHABET(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = 'A OR B AND (C AND DD*)'

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

