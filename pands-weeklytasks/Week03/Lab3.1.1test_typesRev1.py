# test_types.py 
# revision 1
# # Author: Cathal Redmond 12 Feb 2025

# This is a python program/script to test & print the types of variables allowable in python. 


# comment - so i attempted to write this as basicly as i could, forcing each variable to be each desired type. 
# it seems to work, but i can see its not elegant code and can be so much nicer. 
# but i propose that i get the basic functionality working first to test each function, then refine it once i know its working. 
# Revison 1 is running in VS code terminal with no error messages, but i see there are 5 problems highlighted, and the message box says "statements must be seperated by newlines ot semicolons, and points to the "type" function. I will now attempt to fix this in Rev.2"

Integer = int(1) 
Float = float(1.2)
Boolean = bool(True)
String = str("String")
mylist = ["apple", "banana", "carrot"]

print('Variable {} is of type: {} and value {}'.format('Integer', type(Integer), Integer))
print('Variable {} is of type: {} and value {}'.format('Float', type(Float), Float))
print('Variable {} is of type: {} and value {}'.format('Boolean', type(Boolean), Boolean))
print('Variable {} is of type: {} and value {}'.format('String', type(String), String ))
print('Variable {} is of type: {} and value {}'.format('myList', type(mylist), mylist ))