def repeat_string(string, n):
# Repeat string n times, space-separated.
    return " ".join([string] * n)


def is_long_word(word, length=5):
# Check if word is at least as long as 'length'.
    return len(word) >= length


def format_sentence(phrase):
# Make a sentence with capital letter and a full stop.
    sentence = phrase.strip()
    sentence = sentence[0].upper() + sentence[1:]
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


# Check if repeat_string works
assert repeat_string("hello", 3) == "hello hello hello"

# Check if Car sets fuel correctly
from car import Car
assert Car("Test", 50).fuel == 50
assert Car("Test2", 0).fuel == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
