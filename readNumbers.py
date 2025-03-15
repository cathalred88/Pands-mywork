# readNumbers.py
# allows for numbers to be entered and checked that the input is of correct type
# Author: Andrew Beaty - copied into Python by Cathal Redmond 05 March 2025 

def readNum(message = "Enter a number: ") :
    num = False
    while (not num):
        try: 
            num = int(input(message))
        except ValueError:
            print ("That was not a number, ", end="")
    return num

num1 = readNum()
num2 = readNum("Please enter second number ")

answer = num1 * num2

print(f"answer is {answer}")