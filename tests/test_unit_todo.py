import pytest
from lib.todo_list import *

"""
1. Create a new Todo object with an empty string => raises exception
2. Create a new Todo object with non-string data type => raises exception
"""
def test_todo_invalid_task():
    with pytest.raises(Exception) as e:
        bad_todo = Todo('')
    e_msg = str(e.value)
    assert e_msg == 'Invalid task'
    
    with pytest.raises(Exception) as e:
        bad_todo = Todo(101)
    e_msg = str(e.value)
    assert e_msg == 'Invalid task'
#------

"""
1. Create a new Todo object
2. Call mark_complete twice => raise exception
"""
def test_todo_mark_completed_twice():
    test = Todo('do this once.')
    test.mark_complete()
    with pytest.raises(Exception) as e:
        test.mark_complete()
    e_msg = str(e.value)
    assert e_msg == 'Task already completed'
#------