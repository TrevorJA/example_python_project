"""
Trevor Amestoy
Cornell University
January, 2023

This script is the main executable, calling the main_module_function which does
the rest of the work.
"""

# Import the main package
import package

def run():
    solved = package.main_module_function()
    return solved

# Run the function if this is the main file executed
if __name__ == "__main__":
    run()
