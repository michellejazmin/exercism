def is_isogram(string):
    word = string.lower()
    allowed_characters = {' ', '-'}
    return not any(letter not in allowed_characters and letter in word[:index]
                   for index, letter in enumerate(word))
