# convert.py
# returns the number rounded down to the closest integer
# Author Cathal Redmond 14 feb 2025 (Happy Valenines day)
import math

number = float(input("Please enter the number (in Dollars and cents): "))
dollars = ((number%100)*100)
absolutedollars = abs(dollars)

cents = (number//100)
absolutecents = abs(cents)

total = int(absolutedollars)+(absolutecents)
print ('The amount in cents is {}'.format(total))