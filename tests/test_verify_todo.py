import pytest
from lib.verify_todo import *

"""
If we pass a an arguement that isn't a string
It will raise an exception
"""
def test_verify_todo_not_string():
    with pytest.raises(Exception) as e:
        verify_todo(10)
    e_msg = str(e.value)
    assert e_msg == "No text found"

"""
If we pass a an empty string
It will raise an exception
"""
def test_verify_todo_empty_string():
    with pytest.raises(Exception) as e:
        verify_todo('')
    e_msg = str(e.value)
    assert e_msg == "No text found"

"""
If we pass a string containing "#TODO"
It will return True
"""
def test_verify_todo_TODO_found():
    result = verify_todo('#TODO Wash the dishes')
    assert result == True

"""
If we pass a string containing "#2do"
It will return False
"""
def test_verify_todo_misspelt1_with_hashtag():
    result = verify_todo('#2do Wash the dishes')
    assert result == False

"""
If we pass a string containing "#toodo"
It will return False
"""
def test_verify_todo_misspelt2_with_hashtag():
    result = verify_todo('#toodo Wash the dishes')
    assert result == False

"""
If we pass a string containing "#todo"
It will return False
"""
def test_verify_todo_lowercase_with_hashtag():
    result = verify_todo('#todo Wash the dishes')
    assert result == False

"""
If we pass a string containing "todo"
It will return False
"""
def test_verify_todo_lowercase_without_hashtag():
    result = verify_todo('todo Wash the dishes')
    assert result == False

"""
If we pass a string containing "TODO"
It will return False
"""
def test_verify_todo_uppercase_without_hashtag():
    result = verify_todo('TODO Wash the dishes')
    assert result == False