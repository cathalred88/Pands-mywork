# bank.py
# This program prompts the user to enter 2 values as integer numbers in cents, then adds the numbers and displays their sum. 
# author: Cathal Redmond 5 Feb 2025

amount1 = int(input("Please enter amount1 (in cent):"))
amount2 = int(input("Please enter amount2 (in cent):"))
sum = (amount1 + amount2) 
print(f"The sum of these is €{sum//100}.{sum%100}")