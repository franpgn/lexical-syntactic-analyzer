from ply.yacc import yacc
from lexer import tokens

# -----------------------------------------------------------------------------
# Grammar rules
#   expression : PLUS term expression
#              | MINUS term expression
#              | term
#
#   term       : TIMES term factor
#              | DIVIDE term factor
#              | factor
#
#   factor     : ID
#              | NUMBER
#              | PLUS factor
#              | MINUS factor
#              | LPAREN expression RPAREN
# -----------------------------------------------------------------------------

# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression(p):
    '''
    expression : PLUS term term
               | MINUS term term
    '''
    p[0] = ('binop', p[3], p[2], p[1])

def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : TIMES factor factor
         | DIVIDE factor factor
    '''
    p[0] = ('binop', p[3], p[2], p[1])

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = ('number', p[1])

def p_factor_id(p):
    '''
    factor : ID
    '''
    p[0] = ('id', p[1])

def p_factor_unary(p):
    '''
    factor : PLUS factor
           | MINUS factor
    '''
    p[0] = ('unary', p[2], p[1])

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = ('grouped', p[2])

def p_error(p):
    print("Syntax error in input!")

parser = yacc()

def parse(input):
    ast = parser.parse(input)
    print(ast)
