# div.py
# This program asks the user to enter two numbers, then divides the second number by the first number, and then display the result as a number and a remainder.
# Author Cathal Redmond 13 Feb 2025.

value1 = int(input("please enter the first number: "))
value2 = int(input("please enter the second number: "))
div = (value1//value2)
remainder = (value1%value2)
print("{} divided by {} is {} remainder {}".format(value1,value2,div,remainder))