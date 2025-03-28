# student.py
# prompt the user to enter student names, modules and grades
# Author: Cathal Redmond 03 Mar 2025
# https://nidhiashtikar.medium.com/python-day-22-using-a-while-loop-with-lists-and-dictionaries-010e742e56db


# Empty dictionary to store gradebook
gradebook = {}

# Set a flag to indicate that polling is active.
gradePolling_active = True
name = input("\nPlease enter student name: ")

while gradePolling_active: 
    # Prompt for the strudent's module name and grade

    module = input("Please enter module name (or leave blank to skip): ")
    if len(module) == 0: break
    grade = input("Please enter grade score: ")  

    # Store the response in the gradebook dictionary
    gradebook[module] = grade

# Polling is complete, display the results
print("\n--- {}'s Report Card ---".format(name))
for module, grade, in gradebook.items():
    print("{}:\t {}% ".format(module,grade))

print(gradebook)