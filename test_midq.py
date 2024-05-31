from question.Q24 import make_3sg_form
from question.Q25 import make_ing_form
from question.Q27 import words_length1
from question.Q28 import find_longest_word


def test_make_3sg_form():
    result = make_3sg_form('fry')
    expected = 'fries'
    assert result == expected


def test_make_ing_form():
    result = make_ing_form('lie')
    expected = 'lying'
    assert result == expected


def test_words_length1():
    result = words_length1(['lol'])
    expected = [3]
    assert result == expected


def test_find_longest_word():
    result = find_longest_word(['This', 'is', 'unacceptable'])
    expected = 12
    assert result == expected
