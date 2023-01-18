"""
Trevor Amestoy
Cornell University
January, 2023
"""

# Import the helpers from the current folder "."
from . import helpers

# Import the subpackage_module
from .subpackage import subpackage_module

def main_module_function():

    print('Here is a riddle, maybe "sample_package" can help solve it:')
    print('\n   What runs but has no feet, roars but has no mouth? \n')

    solved = False
    while not solved:
        print('Lets see if the helper can solve the riddle.')

        # Run the helper function
        status = helpers.helper_function()

        if status:
            print('The helper solved it, the answer is "A River"!')
            solved = True
        else:
            print('The helper could not solve it.')
            print('Maybe the subpackage_module can help.')
            status = subpackage_module.subpackage_function()
            if status:
                print('The subpackage solved it, the answer is "A River"!')
                solved = True
            else:
                print('The subpackage could not solve it...')
    return solved
