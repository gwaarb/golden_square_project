import pytest
from lib.todo_list import *
from lib.todo import *

"""
1. Initialise a new TodoList object
2. Initialise a new Todo object and pass it to the ToDoList.add function 
3. Call the incomplete function on the TodoList object => Returns list of incompleted todos
"""
def test_todolist_add_todo_object():
    todos = TodoList()
    test = Todo("walk the dog.")
    todos.add(test)
    res = todos.incomplete()
    assert res == ['walk the dog. | incomplete']
#------


"""
1. Initialise a new TodoList object
2. Initialise 3 new Todo objects and pass it to the TodoList.add function 
3. Call the incomplete function on the TodoList object => Returns list of incompleted todos
"""
def test_todolist_add_3_todo_objects():
    todos = TodoList()
    test1 = Todo("walk the dog.")
    test2 = Todo("burp the kimchee.")
    test3 = Todo("tell my momma I love her.")
    todos.add(test1)
    todos.add(test2)
    todos.add(test3)
    res = todos.incomplete()
    assert res == ['walk the dog. | incomplete', 'burp the kimchee. | incomplete', 'tell my momma I love her. | incomplete']
#------

"""
1. Initialise a new TodoList object
2. Initialise a new ToDo object and pass it to the TodoList.add function 
3. Call the mark_complete method on the test Todo object
4. Call the complete function on the TodoList object => Returns list of completed todos
5. Call the incomplete function on the TodoList object => Returns string confirming no incomplete tasks
"""
def test_todolist_mark_todo_completed():
    todos = TodoList()
    test = Todo("walk the dog.")
    todos.add(test)
    test.mark_complete()
    
    res = todos.complete()
    assert res == ['walk the dog. | complete']
    
    res = todos.incomplete()
    assert res == 'No outstanding todos'
#------


"""
1. Initialise a new TodoList object
2. Initialise 3 new Todo objects and pass them to the TodoList.add function 
3. Call the mark_complete method on the test1 and test3 Todo object
4. Call the complete function on the TodoList object => Returns list of completed todos
5. Call the incomplete function on the TodoList object => Returns list of incompleted todos
"""
def test_todolist_mark_2_todos_completed():
    todos = TodoList()
    test1 = Todo("walk the dog.")
    test2 = Todo("burp the kimchee.")
    test3 = Todo("tell my momma I love her.")
    todos.add(test1)
    todos.add(test2)
    todos.add(test3)
    test1.mark_complete()
    test3.mark_complete()
    
    res = todos.complete()
    assert res == ['walk the dog. | complete', 'tell my momma I love her. | complete']
    
    res = todos.incomplete()
    assert res == ['burp the kimchee. | incomplete']
#------

"""
1. Initialise a new TodoList object
2. Initialise 3 new Todo objects and pass them to the ToDoList.add function 
3. Call give_up on TodoList object
4. Call the complete function on the todo list object => Returns list of completed todos
5. Call the incomplete function on the todo list object => Returns list of completed todos
"""
def test_todolist_give_up():
    todos = TodoList()
    test1 = Todo("walk the dog.")
    test2 = Todo("burp the kimchee.")
    test3 = Todo("tell my momma I love her.")
    todos.add(test1)
    todos.add(test2)
    todos.add(test3)
    todos.give_up()

    res = todos.incomplete()
    assert res == 'No outstanding todos'
    
    res = todos.complete()
    assert res == ['walk the dog. | complete', 'burp the kimchee. | complete', 'tell my momma I love her. | complete']
#------