# accounts.py
# this script is used to allow a user to enter a 10 digit  bank account number, then display only the last 4 digits for privacy. 
# Author Cathal Redmond 15 Feb 2025

accountNumber = str(input("Please enter an account number (any lenght): "))
# this will take the max number of digits alowed by a string 

n= int(input("Number of last digits to display: "))
accountLen = len(accountNumber)
numX = (accountLen - n)



print("X"*numX + accountNumber[-n:])


# RIP the code that didn't make it

#maskLen = (accountLen-4)
#reversedNumber = accountNumber[::-1]
#print(reversedNumber)

#splitNumber = accountNumber.split()
#print (splitNumber)