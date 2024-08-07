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
        self.assertEqual(result, '6 5 *')

    def test_simple_division(self):
        result = self.parser.parse('( / 7 8 )')
        self.assertEqual(result, '7 8 /')

    def test_nested_expression(self):
        result = self.parser.parse('( * z ( + x y ) )')
        self.assertEqual(result, 'x y + z *')

    def test_triple_nested_expression(self):
        result = self.parser.parse('( / ( * z ( + x y ) ) 2 )')
        self.assertEqual(result, 'x y + z * 2 /')

    def test_giant_nested_expression(self):
        result = self.parser.parse('( / ( + ( * 7 9 ) ( / ( - 20 4 ) 2 ) ) ( / ( - (* x y ) ( - a b ) ) ( / 100 ( + 5 5 ) ) ) )')
        self.assertEqual(result, '9 7 * 20 4 - 2 / + y x * a b - - 100 5 5 + / / /')

if __name__ == '__main__':
    unittest.main()
