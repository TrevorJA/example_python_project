"""
Trevor Amestoy
Cornell University
January, 2023
"""

from . import main_helpers
from .my_subpackage import subpackage_module

def main_module_function():
    print('The main function, module_function is being used.')
    print('The main function is not enough, lets us the helper!')
    status = main_helpers.helper_function()
    if not status:
        print('The helper could not solve it, lets try the subpackage.')
        status = subpackage_module.subpackage_function()
    return status
