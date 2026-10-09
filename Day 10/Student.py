class Student:
    def __init__(self, name, roll_number, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"


class GraduateStudent(Student):
    def __init__(self, name, roll_number, marks, specialization):
        super().__init__(name, roll_number, marks)
        self.specialization = specialization

    def display_details(self):
        super().display_details()
        print("Specialization:", self.specialization)


students = [
    Student("Rahul", 1, 85),
    Student("Priya", 2, 92),
    Student("Arjun", 3, 38),
    Student("Ananya", 4, 76),
    GraduateStudent("Vamsi", 5, 88, "Cyber Security")
]

for student in students:
    student.display_details()
    print("Result:", student.result())
    print()

highest_student = max(students, key=lambda student: student.marks)

print("Student with the highest marks:")
highest_student.display_details()
print("Result:", highest_student.result())