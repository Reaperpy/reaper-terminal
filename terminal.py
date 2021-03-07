from commands.printcommand import printcmd
from commands.math import *

command = ""

while True:
    try:
        command = input("> ")
        if command == "print":
            printcmd()
        if command == "add":
            add(int(input("Enter a number: ")), int(input("Enter another number: ")))
        if command == "subtract":
            subtract(int(input("Enter a number: ")), int(input("Enter another number: ")))
        if command == "multiply":
            multiply(int(input("Enter a number: ")), int(input("Enter another number: ")))
        if command == "divfloat":
            divide_float(int(input("Enter a number: ")), int(input("Enter another number: ")))
        if command == "divint":
            divide_int(int(input("Enter a number: ")), int(input("Enter another number: ")))

    except ValueError:
        print("Please enter a valid value.")
    except ZeroDivisionError:
        print("You can't divide by 0!")
