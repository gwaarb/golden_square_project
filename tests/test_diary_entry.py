import pytest
from lib.diary_entry import *

"""
If we initialise a new object from the DiaryEntry but pass a non-string 'title' parameter
It will raise an exception
"""
def test_diary_entry_title_not_string():
    with pytest.raises(Exception) as e:
        d_entry = DiaryEntry(123, "Contents of entry")
    e_msg = str(e.value)
    assert e_msg == "No string found in title"
#---------


"""
If we initialise a new object from the DiaryEntry but pass a non-string 'content' parameter
It will raise an exception
"""
def test_diary_entry_content_not_string():
    with pytest.raises(Exception) as e:
        d_entry = DiaryEntry("Today's Date", 123)
    e_msg = str(e.value)
    assert e_msg == "No string found in contents"
#---------


"""
If we initialise a new object from the DiaryEntry but pass an empty string 'title' parameter
It will raise an exception
"""
def test_diary_entry_title_empty_string():
    with pytest.raises(Exception) as e:
        d_entry = DiaryEntry("", "Contents of entry")
    e_msg = str(e.value)
    assert e_msg == "No string found in title"
#---------


"""
If we initialise a new object from the DiaryEntry but pass an empty string 'content' parameter
It will raise an exception
"""
def test_diary_entry_content_empty_string():
    with pytest.raises(Exception) as e:
        d_entry = DiaryEntry("Today's Date", "")
    e_msg = str(e.value)
    assert e_msg == "No string found in contents"
#---------


"""
If we initialise a new object from the DiaryEntry and call count_words
It will return the number of words in the content of our entry
"""
def test_diary_entry_count_words_in_entry():
    d_entry = DiaryEntry("Today's Date", "Today has been an eventful day!")
    result = d_entry.count_words()
    assert result == "6 words in the diary entry content"
#---------


"""
If we initialise a new object from the DiaryEntry and call format
It will return our title and entry formatted nicely
"""
def test_diary_entry_format_entry():
    d_entry = DiaryEntry("Today", "It has been an eventful day!")
    result = d_entry.format()
    assert result == "Today: It has been an eventful day!"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 200 wpm parameter and a 200 word entry
It will return the estimated reading time in minutes
"""
def test_diary_entry_reading_time_at_200_wpm_200_words():
    d_entry = DiaryEntry("Today", "word " * 199)
    result = d_entry.reading_time(200)
    assert result == "Estimated 1 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 200 wpm parameter and a 250 word entry
It will return the estimated reading time in minutes (rounded down)
"""
def test_diary_entry_reading_time_at_200_wpm_250_words():
    d_entry = DiaryEntry("Today", "word " * 299)
    result = d_entry.reading_time(200)
    assert result == "Estimated 1 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 200 wpm parameter and a 300 word entry
It will return the estimated reading time in minutes (rounded up)
"""
def test_diary_entry_reading_time_at_200_wpm_300_words():
    d_entry = DiaryEntry("Today", "word " * 299)
    result = d_entry.reading_time(200)
    assert result == "Estimated 2 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 100 wpm parameter and a 200 word entry
It will return the estimated reading time in minutes
"""
def test_diary_entry_reading_time_at_100_wpm_200_words():
    d_entry = DiaryEntry("Today", "word " * 199)
    result = d_entry.reading_time(100)
    assert result == "Estimated 2 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 500 wpm parameter and a 200 word entry
It will return a minimum estimated reading time 
"""
def test_diary_entry_reading_time_at_500_wpm_200_words():
    d_entry = DiaryEntry("Today", "word " * 199)
    result = d_entry.reading_time(500)
    assert result == "Estimated less than 1 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 200 wpm parameter and a 2000 word entry
It will return the estimated reading time in minutes
"""
def test_diary_entry_reading_time_at_200_wpm_2000_words():
    d_entry = DiaryEntry("Today", "word " * 1999)
    result = d_entry.reading_time(200)
    assert result == "Estimated 10 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_time with a 200 wpm parameter and a 12000 word entry
It will return the estimated reading time in minutes
"""
def test_diary_entry_reading_time_at_200_wpm_12000_words():
    d_entry = DiaryEntry("Today", "word " * 19999)
    result = d_entry.reading_time(200)
    assert result == "Estimated 60 min(s) reading time for the dairy entry"
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_chunk with a 200 wpm parameter, 15 minutes and a 6000 word entry
It will return a string containing an estimated achievable reading chunk
"""
def test_diary_entry_reading_chunk_200_wpm_15_mins_6000_words():
    test_wpm = 200
    test_mins = 15
    test_entry = "word " * 5999
    ex_chunk = "word " * 2999
    d_entry = DiaryEntry("Today", test_entry)
    result = d_entry.reading_chunk(test_wpm, test_mins)
    assert result == "Here is an estimated achievable chunk of reading: " + ex_chunk
#---------


"""
If we initialise a new object from the DiaryEntry and call reading_chunk with a 200 wpm parameter, 15 minutes and a 6000 word entry twice
It will return a string containing an estimated achievable reading chunk
"""
def test_diary_entry_reading_chunk_200_wpm_15_mins_6000_words_twice():
    test_wpm = 200
    test_mins = 15
    test_entry = "word " * 5999
    ex_chunk = "word " * 2999
    d_entry = DiaryEntry("Today", test_entry)
    d_entry.reading_chunk(test_wpm, test_mins)
    result = d_entry.reading_chunk(test_wpm, test_mins)
    assert result == "Here is an estimated achievable chunk of reading: " + ex_chunk
#---------