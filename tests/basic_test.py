"""
Trevor Amestoy
Cornell University
January, 2023
"""

import unittest

from .context import my_package



# Define a test suite targeting specific functionality
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True



if __name__ == '__main__':
    unittest.main()
