"""
Trevor Amestoy
Cornell University
January, 2023
"""

import random

def subpackage_function():
    print('The subpackage_function is being used now.')
    status = bool(random.getrandbits(1))
    return status
