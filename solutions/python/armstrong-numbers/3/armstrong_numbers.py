"""Module providing a function to determine if a number is an Armstrong number."""

def is_armstrong_number(number):
    """Determine if a given number is an Armstrong number."""
    total = 0
    str_number = str(number)
    for digit in str_number:
        total += int(digit)**len(str_number)
    return total == number
