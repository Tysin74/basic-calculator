# This file contains all mathematical functions used in calculator.py

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

if __name__ == '__main__':
    print("Running functions.py as main file. This is to test the use of the functions defined in this file.")
    x = int(input("Input a number: "))
    y = int(input("Print a second number: "))
    operator = input("Type a mathematic operator to perform (+,=,*,/): ")
    if operator == '+':
        print(add(x,y))
    elif operator == '-':
        print(sub(x,y))
    elif operator == '*':
        print(mul(x,y))
    elif operator == '/':
        print(div(x,y))
    else:
        print("Invalid symbol given.")