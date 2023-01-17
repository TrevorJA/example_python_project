"""
Trevor Amestoy
Cornell University
January, 2023
"""

import random

def helper_function():
    print('The helper_function is helping!')
    status = bool(random.getrandbits(1))
    if status:
        print('The helper solved it!')
        return status
    else:
        return status
