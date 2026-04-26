def is_isogram(string):
    word = string.lower()
    allowed_characters = {' ', '-'}
    for index, letter in enumerate(word):
        if letter not in allowed_characters and letter in word[:index]:
            return False
    return True
