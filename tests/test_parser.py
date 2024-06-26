import unittest
from src.parser import parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = parser

    def test_simple_addition(self):
        result = self.parser.parse('( + 1 2 )')
        self.assertEqual(result, '1 2 +')

    def test_simple_subtraction(self):
        result = self.parser.parse('( - 3 4 )')
        self.assertEqual(result, '3 4 -')

    def test_simple_multiplication(self):
        result = self.parser.parse('( * 5 6 )')
        self.assertEqual(result, '5 6 *')

    def test_simple_division(self):
        result = self.parser.parse('( / 7 8 )')
        self.assertEqual(result, '7 8 /')

    def test_nested_expression(self):
        result = self.parser.parse('( * ( + 1 2 ) 3 )')
        self.assertEqual(result, '1 2 + 3 *')

    def test_invalid_syntax(self):
        result = self.parser.parse('( + 1 )')
        self.assertFalse(result, "Syntax error in input!")


if __name__ == '__main__':
    unittest.main()
