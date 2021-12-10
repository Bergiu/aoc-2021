import ply.lex as lex
import ply.yacc as yacc
from functools import reduce


FILENAME = "input"
LINT = True


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# LEXER

tokens = [
    'NEWLINE',
    'LROUND',
    'RROUND',
    'LCURLY',
    'RCURLY',
    'LSQUARE',
    'RSQUARE',
    'LANGLE',
    'RANGLE',
]

t_LROUND = r'\('
t_RROUND = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LANGLE = r'<'
t_RANGLE = r'>'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


def t_error(t):
    column = find_column(t.lexer.lexdata, t)
    msg = f"Illegal character: {repr(t.value[0])}"
    form = "{path}:{line}:{column}: ({symbol}) {msg}"
    formatted = form.format(path=FILENAME, line=t.lineno, column=column, symbol=t.type, msg=msg)
    if LINT:
        print(formatted)
        t.lexer.skip(1)
    else:
        raise Exception(formatted)


lexer = lex.lex()


def do_lexing(data):
    lexer.input(data)
    while True:
        i = lexer.token()
        if i is None:
            break
        print(i)


# PARSER

start = 'codeblock'


def p_program1(p):
    '''codeblock : line'''
    line = p[1]
    p[0] = [line]


def p_program2(p):
    '''codeblock : codeblock line'''
    codeblock = p[1]
    line = p[2]
    p[0] = codeblock + [line]


def p_line(p):
    '''line : chunks NEWLINE'''
    chunks = p[1]
    p[0] = chunks


def p_chunks(p):
    '''chunks : chunk'''
    p[0] = p[1]


def p_chunks2(p):
    '''chunks : chunks chunk'''
    p[0] = p[1] + p[2]


def p_chunk_error(p):
    '''chunks : error chunk
    '''
    p[0] = p[2]
    p.parser.errok()


def p_chunk1(p):
    '''chunk : LROUND RROUND
             | LSQUARE RSQUARE
             | LANGLE RANGLE
             | LCURLY RCURLY
    '''
    p[0] = p[1] + p[2]


def p_chunk2(p):
    '''chunk : LROUND chunks RROUND
             | LSQUARE chunks RSQUARE
             | LANGLE chunks RANGLE
             | LCURLY chunks RCURLY
    '''
    p[0] = p[1] + p[2] + p[3]


precedence = (
    ('left', 'LROUND'),
    ('left', 'RROUND'),
    ('left', 'LSQUARE'),
    ('left', 'RSQUARE'),
    ('left', 'LANGLE'),
    ('left', 'RANGLE'),
    ('left', 'LCURLY'),
    ('left', 'RCURLY'),
    ('left', 'NEWLINE'),
)


chunk_errors = []


incomplete = []
corrupted = []
# should be: 3, 5, 6, 8, 9


def p_error(p):
    if p is None:
        raise Exception("Unexpected end of file.")
    msg = f"Syntax error! Error on token: {repr(p.value)} ({p.type})"
    make_error(p, "error", msg)


def make_error(p, type, message):
    column = find_column(p.lexer.lexdata, p)
    form = "{path}:{line}:{column}: {type}: {msg}"
    formatted = form.format(path=FILENAME, line=p.lineno, column=column, type=type, msg=message)
    if p.type == "NEWLINE":
        incomplete.append((p.lineno, column, p.type))
        parser.restart()
    else:
        corrupted.append((p.lineno, column, p.type))
    if LINT:
        print(formatted)
    else:
        raise Exception(formatted)


parser = yacc.yacc()


def do_parsing(text):
    result = parser.parse(text)
    return result


def main(filename):
    data = open(filename).read()
    # do_lexing(data)
    do_parsing(data)
    # reverse order to overwrite with the first item at last
    point_map = {'RROUND': 3, 'RSQUARE': 57, 'RCURLY': 1197, 'RANGLE': 25137}
    corrupted_first = {x: (y, z) for x, y, z in corrupted[::-1]}
    corrupted_tokens = [item[1][1] for item in corrupted_first.items()]
    summe = sum(map(lambda item: point_map[item], corrupted_tokens))
    print(summe)


if __name__ == '__main__':
    main(FILENAME)

