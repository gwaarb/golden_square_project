from lib.diary import *
from lib.entry import *
from lib.todo import *

#------------------Entry integration function testing------------------
"""
1. Initialise new Diary object
2. Initialise new Entry object
3. Add Entry to Diary entries list
4. Use see entries to review stored Entry objects | returns list
5. Initialise another new Entry object
6. Add Entry to Diary entries list
7. Use see entries to review stored Entry objects
"""
def test_diary_add_entries():
    diary = Diary()
    test_entry = Entry('Today', 'Was a good day.')
    diary.add_entry(test_entry)
    result = diary.see_entries()
    assert result == [test_entry]
    
    test_entry_2 = Entry('Yesterday', 'Was a terrible day.')
    diary.add_entry(test_entry_2)
    result = diary.see_entries()
    assert result == [test_entry, test_entry_2]


"""
1. Initialise new Diary object
2. Initialise 2 new Entry objects
3. Add entries to Diary entries list
4. Use see entries to review stored Entry objects | returns list
5. Use readible entry to find the next feasible entry read based on wpm and ft | returns string (x4)
"""
def test_diary_readable_entries():
    diary = Diary()
    short_entry = Entry('Quick Update', 'blah ' * 999)
    long_entry = Entry('The Goss', 'blah ' * 4999)
    diary.add_entry(short_entry)
    diary.add_entry(long_entry)
    result = diary.see_entries()
    assert result == [short_entry, long_entry]
    
    expected = short_entry.entry
    result = diary.readable_entry(200, 5)
    assert result == expected
    
    expected = 'No readable entries'
    result = diary.readable_entry(100, 1)
    assert result == expected
    
    expected = short_entry.entry
    result = diary.readable_entry(100, 10)
    assert result == expected
    
    expected = long_entry.entry
    result = diary.readable_entry(500, 20)
    assert result == expected

#------------------Todo integration function testing------------------
"""
1. Initialise new Diary object
2. Initialise new Todo object
3. Add Todo to Diary todo list
4. Use incomplete to review incomplete Todo tasks | returns list
5. Initialise 2 new Todo objects
6. Add new Todos to Diary todo list
7. Use incomplete to review incomplete todo tasks | returns list
"""
def test_diary_add_todos():
    diary = Diary()
    todo = Todo('Walk the plants.')
    diary.add_todo(todo)
    result = diary.incomplete()
    assert result == [todo]
    
    todo2 = Todo('Water the dog.')
    todo3 = Todo('Unite the people.')
    diary.add_todo(todo2)
    diary.add_todo(todo3)
    result = diary.incomplete()
    assert result == [todo, todo2, todo3]


"""
1. Initialise new Diary object
2. Initialise new Todo object
3. Add Todo to Diary todo list
4. Set Todo to completed
5. Use complete to review completed tasks | returns list
6. Initialise 2 new Todo objects
7. Add Todos to Diary todo list
8. Set third Todo to completed
9. Use complete to review completed tasks | returns list
10. Use incomplete to review incomplete tasks | returns list
"""
def test_diary_mark_completed():
    diary = Diary()
    todo = Todo('Walk the plants.')
    diary.add_todo(todo)
    todo.mark_done()
    result = diary.complete()
    assert result == [todo]
    
    todo2 = Todo('Water the dog.')
    todo3 = Todo('Unite the people.')
    diary.add_todo(todo2)
    diary.add_todo(todo3)
    todo3.mark_done()
    result = diary.complete()
    assert result == [todo, todo3]
    
    result = diary.incomplete()
    assert result == [todo2]


"""
1. Initialise new Diary object
2. Initialise 3 new Todo objects
3. Add Todos to Diary todo list
4. Use complete to review completed tasks | returns string
5. Use incomplete to review incompleted tasks | returns list
6. Use give up to mark all tasks as completed 
7. Use incomplete to review incompleted tasks | returns string
8. Use complete to review incompleted tasks | returns list
"""
def test_diary_mark_all_completed():
    diary = Diary()
    todo = Todo('Walk the plants.')
    todo2 = Todo('Water the dog.')
    todo3 = Todo('Unite the people.')
    diary.add_todo(todo)
    diary.add_todo(todo2)
    diary.add_todo(todo3)
    result = diary.complete()
    assert result == 'No completed todos'
    
    result = diary.incomplete()
    assert result == [todo, todo2, todo3]
    
    diary.give_up()
    result = diary.incomplete()
    assert result == 'No outstanding todos'
    
    result = diary.complete()
    assert result == [todo, todo2, todo3]