import pytest
from lib.todo import *

"""
1. create instance of Todo object
2. Pass invalid task string | raises exception (x2)
"""
def test_todo_invalid_task():
    with pytest.raises(Exception) as e:
        bad_task = Todo(101)
    e_msg = str(e.value)
    assert e_msg == 'Invalid Task'
    
    with pytest.raises(Exception) as e:
        no_task = Todo('')
    e_msg = str(e.value)
    assert e_msg == 'Invalid Task'
    

"""
1. create instance of Todo object
2. Pass valid task string
3. Mark as completed
4. Mark as completed again | raises exception
"""
def test_todo_mark_done_twice():
    do_once = Todo('do this once.')
    do_once.mark_done()
    with pytest.raises(Exception) as e:
        do_once.mark_done()
    e_msg = str(e.value)
    assert e_msg == 'Task already completed'