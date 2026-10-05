

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_palindrome(value):
    value = str(value)
    return value == value[::-1]


def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def find_factors(number):
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors


def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def calculate_total(price, quantity=1):
    return price * quantity


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def build_profile(**details):
    return details