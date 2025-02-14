# floor.py
# returns the number rounded down to the closest integer
# Author Cathal Redmond 13/14 feb 2025
import math

number = float(input("Enter the number to round down: "))
floor = math.floor(number)
print ('{} rounded down is {}'.format(number,floor))