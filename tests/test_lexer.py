import unittest
from src.lexer import lexer

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = lexer

    def test_token_plus(self):
        self.lexer.input('+')
        token = self.lexer.token()
        self.assertEqual(token.type, 'PLUS')
        self.assertEqual(token.value, '+')

    def test_token_minus(self):
        self.lexer.input('-')
        token = self.lexer.token()
        self.assertEqual(token.type, 'MINUS')
        self.assertEqual(token.value, '-')

    def test_token_mult(self):
        self.lexer.input('*')
        token = self.lexer.token()
        self.assertEqual(token.type, 'TIMES')
        self.assertEqual(token.value, '*')

    def test_token_div(self):
        self.lexer.input('/')
        token = self.lexer.token()
        self.assertEqual(token.type, 'DIVIDE')
        self.assertEqual(token.value, '/')

    def test_token_lparen(self):
        self.lexer.input('(')
        token = self.lexer.token()
        self.assertEqual(token.type, 'LPAREN')
        self.assertEqual(token.value, '(')

    def test_token_rparen(self):
        self.lexer.input(')')
        token = self.lexer.token()
        self.assertEqual(token.type, 'RPAREN')
        self.assertEqual(token.value, ')')

    def test_token_number(self):
        self.lexer.input('123')
        token = self.lexer.token()
        self.assertEqual(token.type, 'NUMBER')
        self.assertEqual(token.value, 123)

    def test_token_id(self):
        self.lexer.input('variable')
        token = self.lexer.token()
        self.assertEqual(token.type, 'ID')
        self.assertEqual(token.value, 'variable')

if __name__ == '__main__':
    unittest.main()
