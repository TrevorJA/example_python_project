"""
Trevor Amestoy
Cornell University
January, 2023
"""
import sys
sys.path.append('..')

import sample_package
import unittest

# Define a test suite targeting specific functionality
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_that_riddle_is_solved(self):
        solved = sample_package.module.main_module_function()
        self.assertTrue(solved)


if __name__ == '__main__':
    unittest.main()
