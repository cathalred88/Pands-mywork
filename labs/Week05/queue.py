# queue.py
# generates a list of random numbers, then takes the first number out of the list and transfers it into a variable named currentlyServing, and prints the updated states of currentlyServing and queue
# Author: Cathal Redmond 01 Mar 2025
# code refs https://www.geeksforgeeks.org/python-random-module/


# import the random module and name it "ran" to easily distinguish it
import random as ran

# ask the user how many random numbers to generate. 
quantityNumbers = int(input("Please enter how many random numbers you wish to generate: "))
print ("OK, generating {} random numbers.".format(quantityNumbers))

# define the list and give it a name. 
queue = []
# generate a list of random number using a for loop, starting at 0 and ending at quantityNumbers. use the append function to add each element 
generateCounter = 0
while generateCounter < quantityNumbers:
    x = ran.randint(0,100)
    queue.append(x)
    generateCounter = generateCounter + 1
print(queue)


# remove the current number from the list group
removeCounter = generateCounter
while removeCounter >0:
    currentNumber = queue[0]
    del queue [0]
    print("The current number is {}, and the Queue is {}.".format(currentNumber,queue))
    removeCounter = removeCounter - 1

# report the list is empty when remove counter reaches zero
if removeCounter == 0:
    print("The queue is empty!")