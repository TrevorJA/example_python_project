"""
Trevor Amestoy
Cornell University
January, 2023
"""

import unittest

from context import my_package

# Define a test suite targeting specific functionality
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_that_riddle_is_solved(self):
        solved = my_package.main_module.main_module_function()
        self.assertTrue(solved)


if __name__ == '__main__':
    unittest.main()
