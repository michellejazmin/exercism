import string

def rotate(text, key):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    cipher = ''
    for character in text:
        if character in lowercase:
            index = lowercase.find(character)
            rotated = lowercase[(index + key) % 26]
            cipher += rotated
        elif character in uppercase:
            index = uppercase.find(character)
            rotated = uppercase[(index + key) % 26]
            cipher += rotated
        else:
            cipher += character
    return cipher