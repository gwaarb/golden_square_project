import pytest
from unittest.mock import Mock
from lib.diary import *

# Create Diary object with invalid empty content
# Raises exception
def test_invalid_contents_passed():
    with pytest.raises(Exception) as e:
        f_diary = Diary('')
    e_msg = str(e.value)
    assert e_msg == "Invalid contents"

# Create Diary object with valid string and call read
# Returns stored content string
def test_create_and_read_diary():
    f_diary = Diary('blah blah blah')
    assert f_diary.read() == 'blah blah blah'