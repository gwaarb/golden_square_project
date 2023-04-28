import pytest
from lib.diary import *

"""
1. Create instance of Diary object
2. Pass invalid Entry object | raises exception
"""
def test_diary_add_invalid_entry():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add_entry('Entry')
    e_msg = str(e.value)
    assert e_msg == 'Invalid Entry'


"""
1. Create instance of Diary object
2. Pass invalid Todo object | raises exception
"""
def test_diary_add_invalid_todo():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add_todo('Todo')
    e_msg = str(e.value)
    assert e_msg == 'Invalid Todo'
    

"""
1. Create instance of Diary object
2. Attempt to see stored entries when none have been stored | raise exception
3. Attempt to see readable entries when none have been stored | raise exception
"""
def test_diary_no_stored_entries():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.see_entries()
    e_msg = str(e.value)
    assert e_msg == 'No stored entries'
    
    with pytest.raises(Exception) as e:
        diary.readable_entries()
    e_msg = str(e.value)
    assert e_msg == 'No stored entries'
    
    with pytest.raises(Exception) as e:
        diary.find_numbers()
    e_msg = str(e.value)
    assert e_msg == 'No stored entries'


"""
1. Create instance of Diary object
2. Attempt to see incomplete todos when none have been stored | raise exception
3. Attempt to see complete todos when none have been stored | raise exception
4. Attempt to mark all todos as completed when none have been stored | raise exception
"""
def test_diary_no_stored_todos():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.incomplete()
    e_msg = str(e.value)
    assert e_msg == 'No stored todos'
    
    with pytest.raises(Exception) as e:
        diary.complete()
    e_msg = str(e.value)
    assert e_msg == 'No stored todos'
    
    with pytest.raises(Exception) as e:
        diary.give_up()
    e_msg = str(e.value)
    assert e_msg == 'No stored todos'