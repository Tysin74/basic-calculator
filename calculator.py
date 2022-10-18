# Imports functions from functions.py
# Runs a menu function until user inputs exit command
# Takes inputs individually and then calculates answer

from functions import *

print("Basic Calculator V1 loaded.")
while True:
    x = "first_number"
    y = "second_number"
    z = "operator"

    # First input taken
    x = takeInput(x)
    if x == 'EXIT':
        break

    # Second input taken
    y = takeInput(y)
    if y == 'EXIT':
        break

    # Third input taken
    z = takeInput(z)
    if z == 'EXIT':
        break
    
    # Compute answer
    doMath(x,y,z)

print("Program terminated.")