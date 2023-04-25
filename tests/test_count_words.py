import pytest
from lib.count_words import *

def test_count_words_empty_string():
    with pytest.raises(Exception) as e:
        count_words('')
    e_msg = str(e.value)
    assert e_msg == 'Cannot pass empty string!'

def test_count_words_string():
    result = count_words('Hello world!')
    assert result == 2

def test_count_words_string_with_comma():
    result = count_words('Hello,world!')
    assert result == 2