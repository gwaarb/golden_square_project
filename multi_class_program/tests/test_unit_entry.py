import pytest
from lib.entry import *

"""
1. create instance of Entry object
2. Pass invalid title string | raises exception
3. Pass invalid entry string | raises exception
"""
def test_entry_invalid_parameters():
    day_num = 27
    with pytest.raises(Exception) as e:
        bad_title = Entry(day_num, 'My entry for today')
    e_msg = str(e.value)
    assert e_msg == 'Invalid Title'
    
    with pytest.raises(Exception) as e:
        bad_entry = Entry('Today', '')
    e_msg = str(e.value)
    assert e_msg == 'Invalid Entry'