def get_char_num(w):
    """
    Returns the number of characters in word w.
    """
    count = 0
    for c in w:
        count = count + 1
    return count

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return map(get_char_num, s.split())

def test_get_char_num():
    word = "Hello"
    assert get_char_num(word) == 5

def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]

test_get_char_num()
test_get_word_lengths()
