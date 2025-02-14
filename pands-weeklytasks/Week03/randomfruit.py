# randomFruit.py
# This programs selects a random fruit from a list
# Author Cathal Redmond 13 feb 2025

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}".format(fruit))