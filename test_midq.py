from questions.Q24 import make_3sg_form
from questions.Q25 import make_ing_form
from questions.Q27 import words_length1
from questions.Q28 import find_longest_word



def make_3sg_form():
    result = make_3sg_form('fry')
    expected = 'fries'
    assert result == expected

def make_ing_form():
    result = make_ing_form('lie')
    expected = 'lying'
    assert result == expected


def words_length1():
    result = words_length1(['lol'])
    expected = [3]
    assert result == expected
    
def find_longest_word():
    result = find_longest_word(['This', 'is', 'unacceptable'])
    expected = 12
    assert result == expected
