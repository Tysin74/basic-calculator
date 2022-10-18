# Imports functions from functions.py
# Runs a menu function until user inputs exit command
# Takes inputs individually and then calculates answer

from functions import *

print("Basic Calculator V1 loaded.")
while True:

    # First input taken
    x = input("Type in first number value of equation: ")
    if x == 'EXIT':
        break
    else:
        x = int(x)

    # Second input taken
    y = input("Type in second number value of equation: ")
    if y == 'EXIT':
        break
    else:
        y = int(y)

    # Third input taken
    z = input("Now type desired mathematical operator (+,-,*,/): ")
    if z == 'EXIT':
        break
    else:
        doMath(x,y,z)

print("Program terminated.")