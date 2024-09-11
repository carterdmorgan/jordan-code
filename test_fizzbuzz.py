import unittest

from fizzbuzz import fizzbuzz

class FizzbuzzTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_fizzbuzz_value_error_negative(self):
        with self.assertRaises(ValueError):
            fizzbuzz(-1)

    def test_fizzbuzz_value_error_large(self):
        with self.assertRaises(ValueError):
            fizzbuzz(pow(10, 26))

    def test_fizzbuzz_valid(self):
        result = fizzbuzz(15)
        self.assertEqual(result, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])