import unittest
import src.parser as parser

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
        result = self.parser.parse('( * z ( + x y ) )')
        self.assertEqual(result, 'x y + z *')

    def test_triple_nested_expression(self):
        result = self.parser.parse('( / ( * z ( + x y ) ) 2 )')
        self.assertEqual(result, 'x y + z * 2 /')

    def test_invalid_syntax(self):
        with self.assertRaises(AttributeError):
            self.assertFalse(self.parser.parse('( + 1 )'), "Syntax error in input!")


if __name__ == '__main__':
    unittest.main()
