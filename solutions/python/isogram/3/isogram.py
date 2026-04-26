def is_isogram(string):
    word = [letter for letter in string.lower() if letter.isalpha()]
    return not any(letter in word[:index] for index, letter in enumerate(word))
