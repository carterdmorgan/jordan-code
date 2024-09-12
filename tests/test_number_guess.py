import unittest

from number_guess import *

class NumberGuessTest(unittest.TestCase):

    def setUp(self):
        self.solution = '1234'
        self.solution_list = ['1', '2', '3', '4']

    def test_format_solution(self):
        test_solution = format_solution(self.solution)
        self.assertEqual(self.solution, test_solution)

    def test_convert_to_list(self):
        test_solution_list = convert_to_list(self.solution)
        self.assertEqual(self.solution_list, test_solution_list)

    def test_generate_solution(self):
        test_solution_list = generate_solution(self.solution)
        self.assertEqual(self.solution_list, test_solution_list)

    def test_validate_input_digits(self):
        test_user_input_1 = validate_input_digits('3213')
        test_user_input_2 = validate_input_digits('fs5d')
        self.assertTrue(test_user_input_1)
        self.assertFalse(test_user_input_2)

    def test_validate_input_length(self):
        test_user_input_1 = validate_input_length('1234')
        test_user_input_2 = validate_input_length('164478')
        self.assertTrue(test_user_input_1)
        self.assertFalse(test_user_input_2)

    def test_compare_lists(self):
        test_user_input_1 = compare_lists(['1', '2', '3', '4'], self.solution_list)
        test_user_input_2 = compare_lists(['5', '2', '3', '4'], self.solution_list)
        test_user_input_3 = compare_lists(['1', '2', '3', '1'], self.solution_list)
        self.assertEqual(test_user_input_1, ['=', '=', '=', '='])
        self.assertEqual(test_user_input_2, ['H', '=', '=', '='])
        self.assertEqual(test_user_input_3, ['=', '=', '=', 'L'])


if __name__ == "__main__":
    unittest.main()