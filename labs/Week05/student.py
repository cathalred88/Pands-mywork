# sudent.py
# script to store and print grades from multiple courses for students
# Author: Cathal Redmond 2 Mar 2025

# need to create a list of students in a dictionary, then  define a coupling between courses and grades

# first define the dictionary of students
student = {
    "name":"Mary",
    "modules" : [
        {
            "courseName" : "Programming",
            "grade" : 45
        },
        {
            "courseName" : "History",
            "grade" : 99
        }
    ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t:{} \t:{}".format(module["courseName"],module["grade"]))