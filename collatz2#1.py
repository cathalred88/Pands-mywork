# collatz2.py
# formatting collatz file: print the sequence on one line 
# Author: Cathal Redmond 20 feb 2025

import csv

x = int(input("Please enter a positive integer to test: "))
initialNumber = x
print ("Initial test value set to {}\n".format(initialNumber))

testCycleCounter = int(0)
oneCounter = int(0)

while oneCounter < 1:
    testCycleCounter = testCycleCounter + 1
    #print ("Number of test cycles: {}".format(testCycleCounter))
    #print ("Number of four cycles: {}".format(oneCounter))

    if x == 1:
        oneCounter = oneCounter + 1

    if (int(x) % int(2)) == 0:
       #print(f"{x} is even, Divide by 2\n")
       x = int(x/2) 
       print(x)
    else: 
        #print(f"{x} is odd, Multiply by 3 & add 1\n")
        x = (x*int(3))+int(1)
        print (x)

print("\nNumber {} has entered into collatz loop after {} cycles\n".format(initialNumber,testCycleCounter))