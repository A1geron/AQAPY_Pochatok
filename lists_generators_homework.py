"""HW4. Some lists and generators"""

LONG_TEXT = """asdlknfasldkmfasdfasdf"""
list_of_words = []
list_of_words_2 = []


def add_word_2(word):
    """Adds a new word to list of words without sorting"""
    list_of_words_2.append(word)


def get_words_2(chars):
    """Accepts chars and finds all the words which start with the chars.
    Returns a list of those words in ascending order (length must be up to 5)"""
    words_for_output = []
    for i, find_res in enumerate(list_of_words_2):
        if find_res.find(chars) != -1:
            words_for_output.append(list_of_words_2[i])
    words_for_output.sort()
    return words_for_output[:5]


def add_word(word):
    """Adds a new word to list of words"""
    list_of_words.append(word)
    list_of_words.sort()


def get_words(chars):
    """Accepts chars and finds all the words which start with the chars.
    Returns a list of those words in ascending order (length must be up to 5)"""
    words_for_output = []
    for i, find_res in enumerate(list_of_words):
        if find_res.find(chars) != -1 and len(words_for_output) < 5:
            words_for_output.append(list_of_words[i])
    return words_for_output


def crop_text(length):
    """Generator yields a text piece of specified length or less"""
    first_index = 0
    last_index = length
    while True:
        yield LONG_TEXT[first_index:last_index]
        first_index += length
        last_index += length


if __name__ == '__main__':
    assert get_words('') == []
    assert get_words_2('') == []

    add_word('bat')
    add_word('batman')

    add_word_2('bat')
    add_word_2('batman')

    assert get_words('') == ['bat', 'batman']
    assert get_words('bat') == ['bat', 'batman']
    assert get_words('batm') == ['batman']
    assert get_words('x') == []

    assert get_words_2('') == ['bat', 'batman']
    assert get_words_2('bat') == ['bat', 'batman']
    assert get_words_2('batm') == ['batman']
    assert get_words_2('x') == []

    add_word('bar')
    add_word('bartender')
    add_word('basket')
    add_word('band')

    add_word_2('bar')
    add_word_2('bartender')
    add_word_2('basket')
    add_word_2('band')

    assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    assert get_words_2('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    text_generator = crop_text(10)
    assert next(text_generator) == "asdlknfasl"
    assert next(text_generator) == "dkmfasdfas"
    assert next(text_generator) == "df"
