# with open("notes.txt", "w") as file:
#     file.write("Python is easy to learn.\n")
#     file.write("I am learning File I/O.\n")
#     file.write("I like Python programming.\n")

# with open("notes.txt", "r") as file:
#     print(file.read())

# with open("notes.txt", "a") as file:
#     file.write("I will practice Python every day.\n")

# with open("notes.txt", "r") as file:
#     print(file.read())


# import csv

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)

#     total_marks = 0
#     count = 0
#     highest_marks = 0
#     highest_student = ""

#     for student in reader:
#         name = student["name"]
#         marks = int(student["marks"])

#         print(name, marks)

#         total_marks += marks
#         count += 1

#         if marks > highest_marks:
#             highest_marks = marks
#             highest_student = name

# average_marks = total_marks / count

# print("Average marks:", average_marks)
# print("Highest marks:", highest_student)
# print("Highest marks:", highest_marks)


# import json

# with open("students.json", "r") as file:
#     students = json.load(file)

# for student in students:
#     print(student["name"])

# total_marks = 0
# highest_marks = 0
# highest_student = ""

# for student in students:
#     marks = student["marks"]
#     total_marks += marks

#     if marks > highest_marks:
#         highest_marks = marks
#         highest_student = student["name"]

# average_marks = total_marks / len(students)

# print("Average marks:", average_marks)
# print("Highest scorer:", highest_student)
# print("Highest marks:", highest_marks)

# new_student = {
#     "name": "Vamsi",
#     "marks": 90
# }

# students.append(new_student)

# with open("students.json", "w") as file:
#     json.dump(students, file, indent=2)


# ValueError Exception 

try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid number.")
    
# File not found Exception

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
    
    
#Key Error

student = {"name": "Rahul", "marks": 85}

try:
    print(student["age"])
except KeyError:
    print("Key not found.")
    

# Division with Zero

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")            