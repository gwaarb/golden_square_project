import pytest
from lib.reading_time import *

"""
If we pass a parameter that is not a string
It will raise an exception
"""
def test_reading_time_empty_string():
    test_parameter = False
    with pytest.raises(Exception) as e:
        reading_time(test_parameter)
    e_msg = str(e.value)
    assert e_msg == "The passed arguement was not Type: String."

#-----------

"""
If we pass an empty string
It will raise an exception 
"""
def test_reading_time_empty_string():
    test_parameter = ''
    with pytest.raises(Exception) as e:
        reading_time(test_parameter)
    e_msg = str(e.value)
    assert e_msg == "The string did not contain any text."

#-----------

"""
If we pass a string containing less than 200 words
It will return a string advising a minimum reading time
"""
def test_reading_time_150_words():
    test_parameter = 'word ' * 149
    result = reading_time(test_parameter)
    assert result == "The reading time for 150 words is less than a minute."

#-----------

"""
If we pass a string containing less than 200 words
It will return a string advising a minimum reading time
"""
def test_reading_time_200_words():
    test_parameter = 'word ' * 199
    result = reading_time(test_parameter)
    assert result == "The reading time for 200 words is 1.00 minute(s)."

#-----------

"""
If we pass a string containing 250 words
It will return a string advising the estimated time in minutes
"""
def test_reading_time_250_words():
    test_parameter = 'word ' * 249
    result = reading_time(test_parameter)
    assert result == "The reading time for 250 words is 1.25 minute(s)."

    #-----------

"""
If we pass a string containing 250 words
It will return a string advising the estimated time in minutes
"""
def test_reading_time_431_words():
    test_parameter = 'word ' * 430
    result = reading_time(test_parameter)
    assert result == "The reading time for 431 words is 2.15 minute(s)."

    #-----------

"""
If we pass a string containing 12000 words
It will return a string advising the estimated time in hours
"""
def test_reading_time_12000_words():
    test_parameter = 'word ' * 11999
    result = reading_time(test_parameter)
    assert result == "The reading time for 12000 words is 1.00 hour(s)."

    #-----------

"""
If we pass a string containing 12000 words
It will return a string advising the estimated time in hours
"""
def test_reading_time_12899_words():
    test_parameter = 'word ' * 12898
    result = reading_time(test_parameter)
    assert result == "The reading time for 12899 words is 1.07 hour(s)."