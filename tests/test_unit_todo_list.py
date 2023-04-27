import pytest
from lib.todo_list import *

"""
1. Initialise a new ToDoList object
2. Initialise a new Todo object
3. Attempt to pass a non-Todo object to the ToDoList.add function => Raise exception
"""
def test_add_invalid_todo():
    todos = TodoList()
    test_arg = 'Invalid todo'
    with pytest.raises(Exception) as e:
        todos.add(test_arg)
    e_msg = str(e.value)
    assert e_msg == 'Valid todo not found'
#------