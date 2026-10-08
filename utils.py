def clean_name(name):
    return name.strip().title()

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_valid_email(email):
    return "@" in email and "." in email