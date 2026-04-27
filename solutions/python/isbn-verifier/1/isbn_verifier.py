def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    digits = []
    for char in isbn[:-1]:
        if char.isdigit():
            digits.append(int(char))
        else:
            return False
    check_digit = isbn[-1]
    if check_digit.isdigit():
        digits.append(int(check_digit))
    elif check_digit.upper() == 'X':
        digits.append(10)
    else:
        return False
    total = 0
    for index, digit in enumerate(digits):
        total += (digit * (10 - index))
    return total % 11 == 0
