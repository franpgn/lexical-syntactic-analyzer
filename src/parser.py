import ply.yacc as yacc
from lexer import tokens

def p_expression_plus(p):
    'expression : LPAREN PLUS expression expression RPAREN'
    p[0] = f"{p[3]} {p[4]} +"

def p_expression_minus(p):
    'expression : LPAREN MINUS expression expression RPAREN'
    p[0] = f"{p[3]} {p[4]} -"

def p_expression_mult(p):
    'expression : LPAREN MULT expression expression RPAREN'
    p[0] = f"{p[3]} {p[4]} *"

def p_expression_div(p):
    'expression : LPAREN DIV expression expression RPAREN'
    p[0] = f"{p[3]} {p[4]} /"

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('LISP > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(f"Postfix: {result}")
