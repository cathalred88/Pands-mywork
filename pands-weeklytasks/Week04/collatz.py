# collatz.py
# script to determine the next number in the collatz conjecture sequence. 
# Author Cathal Redmond 19 feb 2025

# set initial value
x = int(input("Please enter a positive integer: "))
initialValue = x
# initialize cycleCounter at zero
cycleCount = int(0)

# initialize oneCounter to zero
oneCounter = int(0)

print('Initial value set to: {}'. format(x)) 


while oneCounter < 1:
    print("Cycle count : {}".format(cycleCount))
    cycleCount = cycleCount + 1

    if x == 1:
        oneCounter = oneCounter + 1

    if (x % 2) == 0:
        print('{} is Even: Divide by 2\n'.format(x))
        x = x/2 
    else: 
        print ("{} is Odd: Multiply by 3 & add 1\n".format(x))
        x = (x*3)+1 

print("{} collatz sequence converges to 1 after {} cycles".format(initialValue,cycleCount))