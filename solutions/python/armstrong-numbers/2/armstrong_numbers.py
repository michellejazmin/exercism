def is_armstrong_number(number):
    total = 0
    str_number = str(number)
    for digit in str_number:
        total += int(digit)**len(str_number)
    return total == number
