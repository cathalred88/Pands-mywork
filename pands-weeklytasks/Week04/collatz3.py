# collatz.py
# inputs successive values of collatz conjecture sequence
# Author Cathal Redmond 19 Feb 2025

# instruction: At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# breakdown of these steps 
# take the current value and, 
# if it is even, 
#       divide it by two, 
# but if it is odd, 
#       multiply it by three and add one.

# This problem will need to be broken down into a number of stages or steps - 
# 1. Get the user to enter a positive integer and store that value as the 'initial' value. 
# 2. Enter into a loop that will test the value for even or odd - or the explicit value 4 (as this is the initiator of the internal loop)
# 3. if Branch 1. if the value is even, then divide it by 2 and reset the value to be the result. 
# 4. if Branch 2. if the value is odd, multiply the value by 3 and add 1, and reset the value to the result. 
# 5. iterate the test count by 1 and then test the result in the loop again. 
# 6. conditions for exit from the loop: when the value 4 is reached for the second time. This will require testing the value each time and iterating the count of a '4 checker' only when 4 is achieved. 

# variables to use: 
# x = initial value entered by the user.
# y = result after transform (this value will be changing with each loop) 
# testCycleCounter = number of test cycles performed. 
# fourCount = number of times the value 4 has been returned. (exit when fourCount reaches 2)

x = int(input("Please enter a positive integer to test: "))
print ("Initial test value set to {}\n".format(x))

testCycleCounter = int(0)
oneCounter = int(0)

while oneCounter < 1:
    testCycleCounter = testCycleCounter + 1
    print ("Number of test cycles: {}".format(testCycleCounter))
    print ("Number of four cycles: {}".format(oneCounter))

    if x == 1:
        oneCounter = oneCounter + 1

    if (x % 2) == 0:
       print(f"{x} is even, Divide by 2\n")
       x = x/2 
    else: 
        print(f"{x} is odd, Multiply by 3 & add 1\n")
        x = (x*3)+1
print("Number has entered into cyclical loop after {} cycles".format(testCycleCounter))