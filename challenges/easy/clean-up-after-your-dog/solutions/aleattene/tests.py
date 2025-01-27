
""" To start the tests, type from CLI: python tests.py """

import unittest
from solution import clean_up


class TestSolution(unittest.TestCase):

    def test_garden_clean(self):
        self.assertEqual(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 2, 2), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']], 2, 2), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_']], 6, 9), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', '_', '_', '@', '_'],
                                   ['_', '_', '_', '_', '_', '_', '_', '@', '_']], 4, 3), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_']], 6, 0), 'Clean')
        self.assertEqual(clean_up([['@', '_'], ['_', '_'], ['_', '_']], 1, 4,), 'Clean')
        self.assertEqual(clean_up([['_', '_', '@']], 5, 9), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_']], 3, 6), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '@'],
                                   ['_', '_', '_'], ['_', '_', '_']], 7, 3), 'Clean')
        self.assertEqual(clean_up([['_', '@', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '_', '_']], 7, 4), 'Clean')
        self.assertEqual(clean_up([['@', '_', '_', '_', '_'], ['_', '_', '_', '@', '_'],
                                   ['_', '@', '_', '_', '_']], 9, 3), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '@']], 5, 7), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_']], 5, 6), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '@', '_', '_', '_']], 4, 1), 'Clean')
        self.assertEqual(clean_up([['_', '_'], ['_', '_']], 5, 0), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', '_']], 6, 8), 'Clean')
        self.assertEqual(clean_up([['_', '@', '_', '@', '_', '_'], ['_', '_', '_', '_', '_', '_']], 5, 5), 'Clean')
        self.assertEqual(clean_up([['_', '@', '_']], 5, 2), 'Clean')
        self.assertEqual(clean_up([['_', '_']], 7, 3), 'Clean')
        self.assertEqual(clean_up([['_', '_', '@', '@']], 9, 2), 'Clean')
        self.assertEqual(clean_up([['_', '_', '_', '_']], 1, 7), 'Clean')

    def test_garden_no_clean(self):
        self.assertEqual(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 1, 1), 'Cr@p')
        self.assertEqual(clean_up([['@', '@'], ['@', '@'], ['@', '@']], 2, 2), 'Cr@p')
        self.assertEqual(clean_up([['_', '@', '@'], ['_', ' @', '@']], 1, 2), 'Cr@p')
        self.assertEqual(clean_up([['_', '@', '@', '_', '_', '@', '_', '_', '_']], 4, 0), 'Cr@p')
        self.assertEqual(clean_up([['_', '@', '_'], ['_', '@', '_']], 0, 8), 'Cr@p')

    def test_dog_in_garden(self):
        self.assertEqual(clean_up([['_', '_'], ['D', '_'], ['_', '_']], 2, 2), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', 'D', '_', '_', '_', '_'],
                                   ['_', '_', '_', '_', '@', '@', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '_', 'D', '_', '_']], 9, 5), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', 'D', '_', '_', '_', '_', '_', 'D'],
                                   ['_', '_', 'D', '_', '_', '_', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '@', '_', '_', '_']], 4, 4), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', '_', '_', '@'], ['_', '_', '_', '@', 'D', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '_', 'D', '_'], ['_', '_', '_', '_', 'D', '_', '_', '_'],
                                   ['_', '_', '_', '_', 'D', '@', '_', '_']], 1, 6), 'Dog!!')
        self.assertEqual(clean_up([['D', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'],
                                   ['_', '_', '@', '_'], ['_', '_', '_', '_']], 7, 8), 'Dog!!')
        self.assertEqual(clean_up([['@', '_', '_', '_', 'D', '_', '_'],
                                   ['_', '_', '_', '_', '@', '_', '_']], 3, 8), 'Dog!!')
        self.assertEqual(clean_up([['_', 'D', '@', '_', '_', '_', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '_', '@', '_', '_']], 5, 8), 'Dog!!')
        self.assertEqual(clean_up([['_', '@'], ['D', '_']], 1, 1), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_'], ['_', '_', '_', 'D'], ['_', '_', '_', '_'],
                                   ['_', '_', '_', '_']], 1, 4), 'Dog!!')
        self.assertEqual(clean_up([['_', 'D']], 9, 7), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_'], ['_', 'D', 'D', '@'], ['_', '_', '_', '_']], 5, 1), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', '@', '_'],
                                   ['_', 'D', '_', '_', '_', '_', '_'], ['_', '_', '@', '@', '_', '_', '_'],
                                   ['_', '_', '@', '_', '_', '_', '_']], 2, 8), 'Dog!!')
        self.assertEqual(clean_up([['_', '@', '_', '@', '_', '_', '_', '_'], ['_', '_', '_', '@', '_', '_', '_', '@'],
                                   ['_', '_', '_', '@', '_', '_', '_', '@'], ['@', 'D', '@', '_', '_', '_', '_', '_'],
                                   ['@', '_', '_', '@', '_', '_', '_', '_']], 3, 1), 'Dog!!')
        self.assertEqual(clean_up([['@', '_', '_', '_', '_'], ['_', '_', '_', 'D', '_'], ['D', '_', '@', '@', 'D'],
                                   ['_', '_', '_', '@', '_']], 1, 2), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', 'D', '_'], ['_', '_', '_', '@']], 9, 8), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '@', '_', '@', '_', '@', '@'], ['_', '_', '_', '_', 'D', '@', '_', '_'],
                                   ['_', '_', '_', '@', '_', '_', '_', '@'], ['_', '@', '@', '_', '_', '_', '@', 'D'],
                                   ['_', '_', '_', '_', '_', '_', '_', '_']], 6, 9), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '@', 'D']], 3, 7), 'Dog!!')
        self.assertEqual(clean_up([['@', '_', '_', '_', '_', '@', '_', '_'],
                                   ['_', '_', '_', '_', '_', 'D', '_', '_'], ['_', '_', '@', 'D', '_', '_', 'D', '@'],
                                   ['_', '_', '@', '_', '_', 'D', '_', '_']], 0, 4), 'Dog!!')
        self.assertEqual(clean_up([['_', '@', '_', '_', '@', '_', '_', '_', '_'],
                                   ['_', 'D', '_', '_', '_', '_', '@', '_', '@'],
                                   ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                                   ['_', '_', '_', '_', '_', '_', '_', '_', '@']], 9, 0), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '@', 'D', '@'],
                                   ['_', '_', '@', '_', '@', '_', '_'], ['_', '_', '_', '@', '_', '_', '_'],
                                   ['_', '@', '_', '_', '_', '_', '_']], 6, 9), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', '_', '_', '_'],
                                   ['_', '@', '_', 'D', 'D', '_', '_', '_']], 3, 0), 'Dog!!')
        self.assertEqual(clean_up([['_', '@', '@', '_'], ['D', '_', '@', '_']], 8, 8), 'Dog!!')
        self.assertEqual(clean_up([['_', 'D', '_', '_', '_', '_', 'D', '_', '_'],
                                   ['_', '_', '_', '@', 'D', '_', '_', '_', '_'],
                                   ['D', '_', '_', '@', '_', '_', 'D', '_', '@'],
                                   ['_', 'D', '_', '_', '_', '_', '@', '_', 'D'],
                                   ['_', 'D', '@', '_', '_', '_', '_', '@', '_']], 7, 1), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_'], ['_', '_', '_'], ['D', '_', '_']], 9, 1), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', 'D', '_', '_', '_', '@']], 5, 4), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', 'D', '_', 'D', '@'],
                                   ['_', '_', '_', '_', '_', '_', '@'], ['_', '_', '_', '_', '_', '_', '_'],
                                   ['_', 'D', '_', '_', 'D', '_', '_']], 1, 0), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '@', '_'], ['_', '_', '_', '@', '_', '_'],
                                   ['@', '_', '_', '_', '_', 'D'], ['_', '_', '_', '_', '_', 'D']], 5, 0), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', 'D', '_', '_'], ['_', '_', '_', '_', '_', '@', '_', '_'],
                                   ['_', '@', '@', '_', '@', '@', '@', '_'], ['D', '@', '_', '_', '_', '_', '_', '_'],
                                   ['D', '@', '_', '_', '_', 'D', '_', '@']], 9, 7), 'Dog!!')
        self.assertEqual(clean_up([['_', '_', '_', '_', '_', 'D'], ['_', '_', '@', '_', '@', '_']], 8, 3), 'Dog!!')


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
