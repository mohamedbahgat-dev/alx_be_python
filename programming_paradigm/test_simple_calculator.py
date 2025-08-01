import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,4), 6)
        self.assertEqual(self.calc.add(-2,4), 2)
        self.assertEqual(self.calc.add(-3,-4), -7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,4), -2)
        self.assertEqual(self.calc.subtract(5,- 4), 9)
        self.assertEqual(self.calc.subtract(-2,-2), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,4), 8)
        self.assertEqual(self.calc.multiply(3,- 4), -12)
        self.assertEqual(self.calc.multiply(-2,-2), 4)

    def test_divition(self):
        self.assertEqual(self.calc.divide(6,3), 2)
        self.assertEqual(self.calc.divide(-6,3), -2)
       
        self.assertRaises(ValueError, self.calc.divide, 2, 0)

if __name__ == '__main__':
    unittest.main()