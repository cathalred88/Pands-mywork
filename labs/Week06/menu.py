# menu.py
# allows for the selection of different module options
# Author Andre Beatty, copied into code by Cathal Redmond 06  Mar 2025

# the array we will store everything in
def displayMenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return(choice)

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent ["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules =[]
    moduleName = input("\t Enter the first module name (or blank to quit:").strip()
    
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        #no error handling LOL
        module["grade"] = int(input("\t\tEnter Grade: "))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name: (or blank to quit) ").strip()
    
    return modules

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules: 
        print(f"\t{module['name']} \t {module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules (currentStudent["modules"]);

# main program
students = []
choice = displayMenu()
while (choice != 'q'):
    #we could do this with lambda functions
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\n\n ***INVALID INPUT*** please select either a, v, or q. ")
    choice = displayMenu()

print(f"you chose {choice}")
#choice = str(input("What would you like to do? \n\t (a) Add new student \n\t (v) View students \n\t (q) Quit \n Type one letter (a/v/q): "))
#print ("You chose {}".format(choice))