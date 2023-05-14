import os
import math
import time

# Scientific Calculator
def Add(x,y):
    add = int(x+y)
    return add

def Sub(x,y):
    sub = int(x-y)
    return sub

def Mul(x,y):
    mul = int(x*y)
    return mul

def Div(x,y):
    div = int(x/y)
    return div

def DivRem(x,y):
    divrem = int(x%y)
    return divrem

def Power(x,y):
    power = int(x**y)
    return power

def Root(x,y):
    root = int(pow(x, 1/y))
    return root

def Log(x,y):
    log = math.log(num1, num2)
    return log

def Exponential(x):
    exp = math.exp(x)
    return exp

def Absolute (x):
    abso = abs(x)
    return abso

# Programmable Calculator
def hex_conversion(num):
    hexa = hex(int(num))[2:]
    return hexa
    
def oct_conversion(num):
    octal = oct(int(num))[2:]
    return octal

def dec_conversion(num):
    decimal = int(num)
    return decimal

def binary_conversion(num):
    binary = bin(int(num))[2:]
    return binary

def clear_console():
    if os.name == 'nt': # for Windows
        os.system('cls')

while True:
    x = int(input("Please select a calculator:\n1) Scientific Calculator\n2) Programmable Calculator\n"))
    if x == 1:
        print("1) Scientific Calculator")
        print("Please select an operation:")
        print("Add      (+)")
        print("Subtract (-)")
        print("Multiply (*)")
        print("Divide   (/)")
        print("Divide with remainder (%)")
        print("Power    (^)")
        print("Root     (root)")
        print("Logarithm (log)")
        print("Exponential (e)")
        print("Absolute (abs)")
        
        # Get user input for operation choice
        choice = input("Enter an Operation: ")

        # Get user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform selected operation
        if choice == '+':
            print(num1, "+", num2, "=", Add(num1,num2))
        elif choice == '-':
            print(num1, "-", num2, "=", Sub(num1,num2))
        elif choice == '*':
            print(num1, "*", num2, "=", Mul(num1,num2))
        elif choice == '/':
            print(num1, "/", num2, "=", Div(num1,num2))
        elif choice == '%':
            print(num1, "%", num2, "=", DivRem(num1,num2))
        elif choice == '^':
            print(num1, "^", num2, "=", Power(num1,num2))
        elif choice == 'root':
            print(num1, "root", num2, "=", Root(num1,num2))
        elif choice == 'log':
            print("log(", num1, ",", num2, ")=", Log(num1,num2))
        elif choice == 'e':
            print("e^", num1, "=", Exponential(x))
        elif choice == 'abs':
            print("|", num1, "|", "=", Absolute (num1))
        else:
            print("Invalid operation.")
        time.sleep(3)
        clear_console()

    elif x == 2:
        print("2) Programmable Calculator")
        num = input("Enter a number: ")
        # base = int(input("Enter the base of the number: "))
        choice = input("Select an output format (H/O/D/B): ")
        if choice == 'H':
            print("Hexadecimal:", hex_conversion(num))
        elif choice == 'O':
            print("Octal:", oct_conversion(num))
        elif choice == 'D':
            print("Decimal:", dec_conversion(num))
        elif choice == 'B':
            print("Binary:", binary_conversion(num))
        else:
            print("Invalid output format.")

        time.sleep(3)
        clear_console()

    else:
        print("Invalid calculator selection.")
        time.sleep(3)
        clear_console()
