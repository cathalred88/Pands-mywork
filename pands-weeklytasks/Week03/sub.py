# Sub.py
# This program asks the user to enter two numbers, then subtracts the second number from the first number, and then display an explanatory message and the result of the operation. 
# Author Cathal Redmond 13 Feb 2025. 

value1 = int(input("Enter first number:"))
value2 = int(input("Enter second number:"))
sub = (value1 - value2)

print('{} minus {} equals {}'.format(value1,value2,sub))