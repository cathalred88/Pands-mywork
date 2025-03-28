gradebook = {} # initializes an empty dictionary
numberStudents = 0

while : numberStudents != int(input("Enter the number of students: "))

    for _ in range(numberStudents):
        courseName = input("Enter course name: ")
        grade = input("Enter grade: ")
        gradebook.update({courseName: grade})

print(gradebook)