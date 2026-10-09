class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Course:", self.course)