"""Provides a function to translate text to Pig Latin."""

def translate(text):
    """Translate text to Pig Latin."""
    VOWELS = {'a', 'e', 'i', 'o', 'u'}
    RULE1 = {'xr', 'yt'}
    translated = []
    
    for word in text.lower().split():
        if word[0] in VOWELS or word[0:2] in RULE1:
            word += "ay"
        else:
            pos = 0    # index of the letter used to split the word 
            i = 0      # iterator
            while pos == 0 and i in range(len(word)):
                if word[i] in VOWELS or word[i] == 'y':
                    pos = i
                i += 1
            if word[pos-1:pos+1] == 'qu':
                word = word[pos+1:] + word[:pos+1] + 'ay'
            else:
                word = word[pos:] + word[:pos] + 'ay'
        translated.append(word)
    return " ".join(translated)
