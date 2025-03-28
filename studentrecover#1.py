# student.py
# prompt the user to enter student names, modules and grades
# Author: Cathal Redmond 03 Mar 2025


# Empty dictionary to store responses
gradebook = {}

# Set a flag to indicate that polling is active.
polling_active = True
enteringNewStudent = True
name = input("\nPlease enyer student name: ")

while polling_active: 
    # Prompt for the person's name and response

    module = input("Please enter module name: ")
    if len(module) == 0: break
    grade = input("Please enter grade score: ")  
    
    # Store the response in the dictionary
    gradebook[module] = grade
  

# Polling is complete, display the results
#print("\n--- Poll Results ---")
#for name, module, grade, in gradebook.items():
#    print(f"{name} scored {grade}% in {module}.")

print(gradebook)

