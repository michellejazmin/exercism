def is_armstrong_number(number):
    sum = 0
    str_number = str(number)
    for digit in str_number:
        sum += int(digit)**len(str_number)
    return sum == number
