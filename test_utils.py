from my_utils import (
    is_even,
    is_prime,
    is_palindrome,
    add_all,
    calculate_average,
    find_factors,
    calculate_grade,
    calculate_total,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    build_profile
)


print("Even:", is_even(10))

print("Prime:", is_prime(7))

print("Palindrome:", is_palindrome(121))

print("Sum:", add_all(10, 20, 30, 40))

print("Average:", calculate_average([10, 20, 30, 40, 50]))

print("Factors:", find_factors(12))

print("Grade:", calculate_grade(85))

print("Total:", calculate_total(100, 3))

print("Celsius to Fahrenheit:", celsius_to_fahrenheit(25))

print("Fahrenheit to Celsius:", fahrenheit_to_celsius(77))

print("Profile:", build_profile(
    name="Vamsi",
    age=21,
    city="Ongole"
))