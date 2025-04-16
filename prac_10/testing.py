def repeat_string(string, n):
    """Repeat string n times, space-separated.
    >>> repeat_string("hello", 3)
    'hello hello hello'
    """
    return " ".join([string] * n)


def is_long_word(word, length=5):
    """Determine if the word is at least as long as the specified length.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """Return a sentence with capital and full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an apple.")
    'It is an apple.'
    >>> format_sentence("how are you?")
    'How are you?.'
    """
    sentence = phrase.strip()
    sentence = sentence[0].upper() + sentence[1:]
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


# Run assert test
assert repeat_string("hello", 3) == "hello hello hello"

# Test Car fuel setting
from car import Car
assert Car("Test", 50).fuel == 50
assert Car("Test2", 0).fuel == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
