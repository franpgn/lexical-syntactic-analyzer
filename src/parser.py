from ply.yacc import yacc
from lexer import tokens

# Functions for each rule of the grammar
def p_expression(p):
    '''
    expression : PLUS expression term
               | MINUS expression term
               | DIVIDE expression term
    '''
    p[0] = (f"{p[2]}, {p[3]}, {p[1]}")

def p_expression_times(p):
    '''
    expression : TIMES expression term
    '''
    p[0] = (f"{p[3]}, {p[2]}, {p[1]}")

def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = (f"{p[1]}")

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = str(p[1])

def p_factor_id(p):
    '''
    factor : ID
    '''
    p[0] = (f"{p[1]}")

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = (f"{p[2]}")

def p_error(p):
    print(f"Syntax error")

parser = yacc()

def parse(input):
    result = parser.parse(input)
    if ( result != None ):
        result = result.replace(",", "")
    return result
