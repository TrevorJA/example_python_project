# Example Python Project

## Purpose

This repository is designed as a Python project template, with a focus on project structure. The full blog post written to accompany this repository is available here:


Please feel free to Fork or Download this repository for your own usage.

## Overview
The project is a silly riddle program with no real usefulness other than forming the structure of the project.  The bulk of the work is done in the [`main_module_function()`](https://github.com/TrevorJA/example_python_project/blob/main/sample_package/module.py) which first prints a riddle on the screen, then iteratively uses the `helper_function()` and `subpackage_function()` to try and "solve" the riddle. Both of these functions simply return a random True/False, and are repeatedly called until the riddle is solved (when `status == True`).


## Instructions

### Dependencies

This program only requires the `random` package. If it is not installed already, you can execute:

`pip install random`

### Usage

The program can then be executed from a command line using the [`main.py`](https://github.com/TrevorJA/example_python_project/blob/main/main.py) executable:

```
C:\<your-local-directory>\example_python_project> python main.py
```

The output will first print out the riddle, then print statements indicating which functions are being used to "solve" the riddle.

A normal output should resemble something similar to the below, although there may be more or less print statements depending upon how many times it takes the random generator to produce a "True" solution:

```
Here is a riddle, maybe `sample_package` can help solve it:

   What runs but has no feet, roars but has no mouth?

Lets see if the helper can solve the riddle.
The helper_function is helping!
The helper could not solve it.
Maybe the subpackage_module can help.
The subpackage_function is being used now.
The subpackage solved it, the answer is "A River"!
```
