# students.py
# reads in student names, modules and grades
# Author Andrew Beatty, transcribed by Cathal Redmond 06 Mar 2025

students = []
def readModules():
    modules ={}
    moduleName = input("\t Enter the first module name (or blank to quit:").strip()
    while moduleName != "":
        module = {}
        module["name"]=moduleName
        #no error handling LOL
        module["grade"]=int(input("\t\tEnter Grade: "))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name: (or blank to quit) ").strip()
    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent ["modules"]= readModules()
    students.append(currentStudent)

#test 

doAdd (students)

doAdd(students)
print (students)
