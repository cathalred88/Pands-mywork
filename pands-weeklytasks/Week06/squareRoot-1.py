# squareRoot.py
# this script allows the user to enter a floating point number, and performs a calculation to estimate it's square root. 
# Author: Cathal Redmond
# Reference materail / Sources: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ 
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo


## Definition of functions
# readNum Function : this reads in the intiail number
def readNum(message = "Enter a floating point number: ") :
    num = False
    while (not num):
        try: 
            num = float(input(message))
        except ValueError:
            print ("That was not a number, ", end="")
    return num


# sqrt function : this performs calculation to estimate square root 
# this function needs to do sequential actions: accept an input value, then enter into a loop of: perform  operation , then check for condition to be satisfied, to initialise break of loop and return of value. 
def sqrt(message = "perfroming first estimate: ") :
    candidate = inputValue
    errorEstimate = 10 ** (-10) 
    cycleCount = 0
    squareRootValue = inputValue

    while abs(candidate - squareRootValue * squareRootValue) > errorEstimate :
        squareRootValue = (squareRootValue + candidate / squareRootValue) / 2
        cycleCount = cycleCount + 1 
        #print({cycleCount})

    return squareRootValue



## Execution of operations
# This is where the program calls together the functions to perform the squareroot task required. 
inputValue = readNum()
computedValue = sqrt(inputValue)
tolerance = 0.0001 

print("Square root of {} is estimated to be {}. ".format(inputValue,computedValue))
