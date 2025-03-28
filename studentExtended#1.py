# studentExtended.py
# Extended Student program - prompt the user to enter multiple student names, modules and grades
# Author: Cathal Redmond 03 Mar 2025
# https://nidhiashtikar.medium.com/python-day-22-using-a-while-loop-with-lists-and-dictionaries-010e742e56db


# Empty dictionary to store gradebook
studentList = {}
gradebook = {}

# Set a flag to indicate that polling is active.
gradePolling_active = True
enteringNewStudent = True

while enteringNewStudent:
    name = input("\nPlease enter student name: ")
    if len(name) == 0: break

    while gradePolling_active: 
        # Prompt for the person's name and response
        module = input("Please enter module name (or leave blank to skip): ")
        if len(module) == 0: break
        grade = input("Please enter grade score: ")  

        # Store the response in the gradebook dictionary
        gradebook[module] = grade
    
    # Store the response in the studentList list
    studentList[name] = module

for name in studentList.items():
    print("\n--- {}'s Report Card ---".format(name))
    for module, grade in gradebook.items():
        print(f"{module} \t\t {grade}%.")  

print(studentList)
print(gradebook)