# convert.py
# returns the number rounded down to the closest integer
# Author Cathal Redmond 14 feb 2025 (Happy Valenines day)
import math

signednumber = float(input("Please enter the number (in Dollars and cents): "))
sign = str('positive') if signednumber > 0 else str('negative') #checks the sign of the number and saves it as a string. I making the decision that a bank would need to keep track if a transaction is positive or negative! 
print ('Sign of input amount is : {} '.format(sign)) # prints the sign of the number
cents = (signednumber * 100)
number = int(abs(cents))

#total_in_cents = (number*100)
print ('The amount in cents is {}'.format(number))




# RIP all the different way i tried to force the numbers not to be inaccurate from floating point errors 

#dollars = ((number%100)*100) # seperates the dollar part of the amount
#print (dollars)
#intdollars = int(dollars)
#print(intdollars)
#cents = (number//100) # seperates the cents part of the amount
#intcents = int(cents)
#print (cents)
#print (intcents)

#total = int(intdollars)+(intcents)
