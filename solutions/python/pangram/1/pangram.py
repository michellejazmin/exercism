def is_pangram(sentence):
    letters = {letter for letter in sentence.lower() if letter.isalpha()}
    return len(letters) == 26
