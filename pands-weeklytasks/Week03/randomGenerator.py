# randonGenerator.py
# This program generates a (pseudo)random number between 1 and 10, using a module named "random"
# Author Cathal Redmond 13 Feb 2025

import random

upper = int(input("Please enter the upper limit: "))
lower = int(input("Please enter the lower limit: "))
number = random.randint(lower,upper)
print("here is a random number {}".format(number))