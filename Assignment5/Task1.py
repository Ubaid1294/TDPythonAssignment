# Task 1: Create a Dictionary of Student Marks
# Problem Statement: Write a Python program that:
# 1. Creates a dictionary where student names are keys and their marks are values.
# 2. Asks the user to input a student's name.
# 3. Retrieves and displays the corresponding marks.
# 4. If the student’s name is not found, display an appropriate message.

Students = {'Alice' : 85,
            'Mike' : 45,
            'Jim' : 55,
            'Jen' : 33,
            'Jenson' : 87}
StudentName = input('Enter Student Name: ')
Marks = Students.get(StudentName)
if StudentName in Students:
    print("{}'s marks: {}".format(StudentName, Marks))
else:
    print("Student not found")
    # print("Student {} not found ".format(StudentName))