# cents.py
# Author Cathal 
import math

amount = float(input("Please enter an amount (in dollars and cents): "))
sign = str('positive') if amount > 0 else str('negative')

# print(type(amount))
# print (amount)
# print(type(sign))
# print (sign)

dollars = (amount//100) if sign == 'positive' else abs(amount)//100
cents = (amount//100) if sign == 'positive' else abs(amount)//100

print ("{} dollars and {} cents".format(dollars,cents))