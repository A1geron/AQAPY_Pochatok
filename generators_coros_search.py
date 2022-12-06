"""HW5. Some generators and coroutine."""
import copy

WORDS = {}


def flatten(arr):
    """Generator that creates a flattened sequence from sequence of sequences"""
    for element in arr:
        for inner_element in element:
            if not bool(element):
                yield []
            yield inner_element


def grep(pattern):
    """Coroutine that accepts a search token and returns a string if it contains that token"""
    while True:
        line = (yield)
        if pattern not in line:
            continue
        yield line


def add_word(word, leaf_key='TERM'):
    """Method that adds a word into a dict of words in a specific way (see examples below)"""
    node = WORDS
    for char in word:
        node = node.setdefault(char, {})
    node.setdefault(leaf_key, word)


def get_words(chars):
    """Returns a list of words which start with passed characters.
    Length of the returned list must be up to 10 words"""
    trimmed_dict = copy.deepcopy(WORDS)
    result = []
    if not trimmed_dict.get(chars[0]):
        return result[0:10]
    for i in chars:
        if trimmed_dict.get(i):
            trimmed_dict = trimmed_dict.pop(i)

    def inner_get(inner_dict):
        for key in inner_dict:
            if isinstance(inner_dict, dict):
                if inner_dict.get('TERM'):
                    result.append(inner_dict['TERM'])
                inner_get(inner_dict[key])
            return

    inner_get(trimmed_dict)
    return result[0:10]


if __name__ == '__main__':
    assert list(flatten([])) == []
    assert list(flatten([[]])) == []
    assert list(flatten([[], []])) == []
    assert list(flatten([[1, 2], [], [3]])) == [1, 2, 3]
    assert list(flatten([[1, 2], [3, 4, 5]])) == [1, 2, 3, 4, 5]

    search = grep('bbq')
    next(search)
    assert search.send('Birthday invitation') is None
    assert search.send('Bring bbq sauce with') == 'Bring bbq sauce with'
    assert search.send('Are you hungry?') is None
    assert search.send("We won't invite you to our BBQ party then") is None
    assert search.send('but you better be quick (bbq) otherwise') == 'but you better be quick (bbq) otherwise'
    search.close()

    add_word('hello')
    assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}}}}}}
    add_word('hell')
    assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}}}}
    add_word('he')
    assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}, 'TERM': 'he'}}}
    # set is used here to ignore order but not to remove duplicates
    # the task doesn't require words to be in specific order
    assert set(get_words('he')) == {'he', 'hell', 'hello'}
    assert get_words('l') == []
    assert set(get_words('hel')) == {'hell', 'hello'}
    assert get_words('hel') == ['hell', 'hello']
