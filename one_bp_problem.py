LONG_TEXT = """asdlknfasldkmfasdfasdf"""
list_of_words = []


def add_word(word):
    """Adds a new word to list of words"""
    list_of_words.append(word)
    list_of_words.sort()
    return


def get_words(chars):
    """Accepts chars and finds all the words which start with the chars.
    Returns a list of those words in ascending order (length must be up to 5)"""
    words_for_output = []
    for i in range(len(list_of_words)):
        find_res = list_of_words[i].find(chars)
        if find_res != -1 and len(words_for_output) < 5:
            words_for_output.append(list_of_words[i])
    return words_for_output


def crop_text(length):
    yield
    """Generator yields a text piece of specified length or less"""


if __name__ == '__main__':
    assert get_words('') == []

    add_word('bat')
    add_word('batman')

    assert get_words('') == ['bat', 'batman']
    assert get_words('bat') == ['bat', 'batman']
    assert get_words('batm') == ['batman']
    assert get_words('x') == []

    add_word('bar')
    add_word('bartender')
    add_word('basket')
    add_word('band')

    assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    text_generator = crop_text(10)
    assert next(text_generator) == "asdlknfasl"
    assert next(text_generator) == "dkmfasdfas"
    assert next(text_generator) == "df"
