def is_paired(input_string):
    SYMBOLS = {'(', ')', '[', ']', '{', '}'}
    resulting_string = ''.join([char for char in input_string if char in SYMBOLS])
    while '{}' in resulting_string or '[]' in resulting_string or '()' in resulting_string:
        resulting_string = resulting_string.replace('{}', '').replace('[]', '').replace('()', '')
    return len(resulting_string) == 0