# This file contains all mathematical functions used in calculator.py

operators = ['+', '-', '*', '/']

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

def takeInput(var):
    temp_var = "blank"
    while True:
        try:
            if var == "first_number":
                temp_var = input("Type in first number value of equation: ")
                if temp_var == 'EXIT':
                    return temp_var
                elif int(temp_var):
                    return int(temp_var)
            elif var == "second_number":
                temp_var = input("Type in second number value of equation: ")
                if temp_var == 'EXIT':
                    return temp_var
                elif int(temp_var):
                    return int(temp_var)
            else:
                temp_var = input("Type in desired mathematical operator (+,-,*,/): ")
                if temp_var == 'EXIT' or temp_var in operators:
                    var = temp_var
                    return var
                else:
                    raise Exception("Invalid character, try again.")
        except:
                print("Invalid character, try again.")

def doMath(x,y,z):

    if z == '+':
        print(x, z, y, "=", add(x,y))
    elif z == '-':
        print(x, z, y, "=", sub(x,y))
    elif z == '*':
        print(x, z, y, "=", mul(x,y))
    elif z == '/':
        print(x, z, y, "=", div(x,y))
    else:
        print("An error has occured")

print("Successfully imported basic math functions.")

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
