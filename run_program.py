"""
Trevor Amestoy
Cornell University
January, 2023

This script is used for demonstration of Python project structure.
"""

import my_package


def run():
    print('Here is a riddle, maybe the Package can help solve it: \n RIDDLE')

    solved = False
    max_iter = 10
    iter = 0
    while not solved:
        solved = my_package.main_module.main_module_function()
        if solved:
            print('I got it, the answer is "water"!')
        else:
            print('Hmmm... still thinking.')

        # Give up if cant solve it
        iter += 1
        if iter >= max_iter:
            print('I give up!')
            return
    return

# Run the function if this is the main file executed
if __name__ == "__main__":
    run()
