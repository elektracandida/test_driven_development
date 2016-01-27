def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return None


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


test_get_word_lengths()
