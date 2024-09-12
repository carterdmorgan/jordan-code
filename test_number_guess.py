import unittest

from number_guess import compare_lists

class URLTest(unittest.TestCase):

    def setUp(self):
        solution_list = [1, 2, 3, 4]

    def test_compare_lists(self):
        output = compare_lists([2, 3, 4, 5], self.solution_list)
        self.assertEqual(['H', 'H', 'H', 'H',], output)
