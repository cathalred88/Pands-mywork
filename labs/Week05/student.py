# sudent.py
# script to store and print grades from multiple courses for students
# Author: Cathal Redmond 2 Mar 2025
# references for "Add User Input To A Dictionary" https://www.geeksforgeeks.org/how-to-add-user-input-to-a-dictionary-in-python/


# need to create a list of students in a dictionary, then  define a coupling between courses and grades
# code from website: 
#studentName = ("tim")
#studentList = {}
#while len(studentName) == 0 :
#    studentName = str(input('Enter student name: '))
#    key = str(input('Enter module name: '))
#    value = str(input('Enter score: '))
#    studentList.update({key: value})

#print("{}".format(studentName))


# first define the dictionary of students
moduleCounter = 0
student = {
    "name":"Mary",
    "modules" : [
        {
            "courseName" : "Programming",
            "grade" : 45
        }
        ,
        {
            "courseName" : "History",
            "grade" : 99
        }
    ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t{} \t:{}".format(module["courseName"],module["grade"]))