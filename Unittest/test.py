import unittest
from Unittest.gcd import *

class Testgcd(unittest.TestCase):

    def test_check_zero(self):
        result = gcd(0,0)
        self.assertEqual(result, 0)

    def test_check_zero_arg1(self):
        result = gcd(0,7)
        self.assertEqual(result, 7)

    def test_check_zero_arg2(self):
        result = gcd(2,0)
        self.assertEqual(result, 2)

    def test_equal_args(self):
        result = gcd(3,3)
        self.assertEqual(result, 3)

    def test_arg1_equal_one(self):
        result = gcd(1,3)
        self.assertEqual(result, 1)

    def test_arg2_equal_one(self):
        result = gcd(3,1)
        self.assertEqual(result, 1)

    def test_args_even(self):
        result = gcd(8,16)
        self.assertEqual(result, 8)

    def test_arg1_even_arg2_odd(self):
        result = gcd(10,5)
        self.assertEqual(result, 5)

    def test_arg1_odd_arg2_even(self):
        result = gcd(5,10)
        self.assertEqual(result, 5)

    def test_args_odd(self):
        result = gcd(1141,57343)
        self.assertEqual(result, 1)

    def test_arg1_even_negative(self):
        result = gcd(-8,16)
        self.assertEqual(result, 8)

    def test_arg2_even_negative(self):
        result = gcd(8,-16)
        self.assertEqual(result, 8)

    def test_return_int(self):
        result = gcd(4,3)
        self.assertTrue(type(result) is int)

    def test_return_not_int(self):
        result = gcd(1.5,3)
        self.assertFalse(type(result) is int)

    def test_exception_typeError(self):
        with self.assertRaises(TypeError):
            gcd("строка", 3)

    def test_without_args(self):
        with self.assertRaises(TypeError):
            gcd()

if __name__ == '__main__':
    unittest.main()


