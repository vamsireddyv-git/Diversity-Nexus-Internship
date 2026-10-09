class Student:
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 21)
student2 = Student("Priya", 22)

print(student1.name, student1.age)
print(student2.name, student2.age)

student1.name = "Vamsi"
print(student1.name, student1.age)

print(student2.name, student2.age)


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

phone1 = Mobile("Samsung", "A55", 35000)
phone2 = Mobile("Apple", "iPhone 15", 65000)
phone3 = Mobile("OnePlus", "Nord 4", 30000)

phone1.storage = "128GB"
phone2.storage = "256GB"
phone3.storage = "512GB"

print(phone1.brand, phone1.model, phone1.price, phone1.storage)
print(phone2.brand, phone2.model, phone2.price, phone2.storage)
print(phone3.brand, phone3.model, phone3.price, phone3.storage)

phone4 = Mobile("Vivo", "V30") # Intenional error: missing price argument




class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print("Account holder:", self.account_holder)
        print("Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance.")

account = BankAccount("Rahul", 1000)

account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(300)
account.display_balance()
account.deposit(-200)
account.withdraw(2000)
account.display_balance()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

shape1 = Rectangle(10, 5)
shape2 = Rectangle(8, 4)

print("Rectangle 1")
print("Area:", shape1.area())
print("Perimeter:", shape1.perimeter())

print("Rectangle 2")
print("Area:", shape2.area())
print("Perimeter:", shape2.perimeter())



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_employee_id(self):
        print("Employee ID:", self.employee_id)


class Trainer(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_subject(self):
        print("Subject:", self.subject)


employee = Employee("Ananya", 23, "E101")
employee.introduce()
employee.show_employee_id()

trainer = Trainer("Rahul", 30, "Python")
trainer.introduce()
trainer.show_subject()

person = Person("Vamsi", 21)
person.introduce()
person.show_employee_id()