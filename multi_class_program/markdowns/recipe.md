## 1. The Problem(s)
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Class System Design
```python
    class Diary()
        pass
```
Methods:
    - initialise: create instance variables : parameters | self
        entries = [], todos = [], found_contacts = []: Returns NONE
    - add entry: add a new entry object and store it : parameters | self, entry
        Returns NONE
    - review entry: returns on entry based on available reading time: parameters | self, wpm, ft
        Returns entry with most suitable reading time using passed arguements
    - review entries: returns the saved entries: paramaters | self
        Returns list of entries as []
    - add todo: add a new todo object and store it : parameters | self, todo
        Returns NONE
    - review incomplete: returns the todos that are marked as completed = False : parameters | self
        Returns list of todos as []
    - review complete: returns the todos that are marked as completed = True : parameters | self
        Returns list of todos as []
    - give up: marks all todos that are completed = False to completed = True : parameters | self
        Returns NONE
    - check for numbers: checks the diary entries to see if any contacts where stored : parameters | self
        Returns list of contacts as []


```python
    class Entry()
        pass
```
Methods:
    - accessible variables : title String, entry String, contacts List
    - initialise: create instance variables : parameters | self, title, entry, contacts=None
        title String, entry String, contacts = []


```python
    class Todo()
        pass
```
Methods:
    - accessible variables : todo String, completed Boolean
    - initialise: create instance variables : parameters | self, task
        todo String, completed Boolean = False
    - mark completed: changes the instance completed variable to True if False
        Returns NONE

## 3. Examples as Integration Tests
```python
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


"""
1. Initialise new Diary object
2. Initialise 2 new Entry objects
3. Add entries to Diary entries list
4. Use see entries to review stored Entry objects | returns list
5. Use find numbers to retrieve stored mobile numbers in entries | returns string
6. Initialise new Entry object
7. Add Entry to Diary entries list
8. Use see entries to review stored Entry objects | returns list
9. Use find numbers to retrieve stored mobile numbers in entries | returns list
10. Initialise new Entry object
11. Add Entry to Diary entries list
12. Use see entries to review stored Entry objects | returns list
13. Use find numbers to retrieve stored mobile numbers in entries | returns list
"""
def test_diary_find_numbers():
    diary = Diary()
    short_entry = Entry('Quick Update', 'blah ' * 999)
    long_entry = Entry('The Goss', 'blah ' * 4999)
    new_mob_entry = Entry('Met Someone', 'blah ' * 3999, 'Paul: 07xxxxxxxxx')
    diary.add_entry(short_entry)
    diary.add_entry(long_entry)
    result = diary.see_entries()
    assert result == [short_entry, long_entry]
    
    expected = 'No found mobile numbers'
    result = diary.find_numbers()
    assert result == expected
    
    new_mob_entry = Entry('Met Someone', 'blah ' * 3999, 'Paul: 07xxxxxxxxx')
    diary.add_entry(new_mob_entry)
    result = diary.see_entries()
    assert result == [short_entry, long_entry, new_mob_entry]
    
    expected = 'Paul: 07xxxxxxxxx'
    result = diary.find_numbers()
    assert result == [expected]
    
    another_new_mob_entry = Entry('Met Another', 'blah ' * 2999, 'Will: 07xxxxxxxxx')
    diary.add_entry(another_new_mob_entry)
    result = diary.see_entries()
    assert result == [short_entry, long_entry, new_mob_entry, another_new_mob_entry]
    
    second_expected = 'Will: 07xxxxxxxxx'
    result = diary.find_numbers()
    assert result == [expected, second_expected]

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
```

## 4. Examples as Unit Tests
Entry() unit tests
```python
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
```


Todo() unit tests
```python
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
```


Diary() unit tests
```python
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
```

## 5. Behaviour Implementation

Entry()
```python
class Entry():
    title, entry, mob = str, str, str
    def __init__(self, title, entry, mob=''):
        if not isinstance(title, str) or not title.strip():
            raise Exception('Invalid Title')
        if not isinstance(entry, str) or not entry.strip():
            raise Exception('Invalid Entry')
        self.title = title
        self.entry = entry
        self.mob = mob
```

Todo()
```python
class Todo():
    task, completed = str, bool
    def __init__(self, task, done=False):
        if not isinstance(task, str) or not task.strip():
            raise Exception('Invalid Task')
        self.task = task
        self.completed = done
    
    def mark_done(self):
        if self.completed:
            raise Exception('Task already completed')
        self.completed = True
```

Diary()
```python
class Diary():
    def __init__(self):
        self.entries, self.todos = [], []
    
    # entry methods
    def add_entry(self, entry):
        if not isinstance(entry, Entry):
            raise Exception('Invalid Entry')
        self.entries.append(entry)
        
    def any_entries(self):
        if len(self.entries) == 0:
            return False
        return True
    
    def see_entries(self):
        if not self.any_entries():
            raise Exception('No stored entries')
        return self.entries
    
    def readable_entry(self, wpm, ft): # wpm - words per minute, ft - free time (in minutes)
        if not self.any_entries():
            raise Exception('No stored entries')
        e_sorted = sorted([e.entry for e in self.entries], key=len, reverse=True)
        for e in e_sorted:
            e_length = e.split()
            e_reading_time = len(e_length) / wpm
            if e_reading_time <= ft:
                return e
        return 'No readable entries'
        
    def find_numbers(self):
        if not self.any_entries():
            raise Exception('No stored entries')
        found_nums = [e.mob for e in self.entries if len(e.mob) != 0]
        if len(found_nums) == 0:
            return 'No found mobile numbers'
        return found_nums
    
    # todo methods
    def add_todo(self, todo):
        if not isinstance(todo, Todo):
            raise Exception('Invalid Todo')
        self.todos.append(todo)
    
    def any_todos(self):
        if len(self.todos) == 0:
            return False
        return True
    
    def incomplete(self):
        if not self.any_todos():
            raise Exception('No stored todos')
        unfinished = [todo for todo in self.todos if not todo.completed]
        if len(unfinished) == 0:
            return 'No outstanding todos'
        return unfinished
        
    def complete(self):
        if not self.any_todos():
            raise Exception('No stored todos')
        finished = [todo for todo in self.todos if todo.completed]
        if len(finished) == 0:
            return 'No completed todos'
        return finished
    
    def give_up(self):
        if not self.any_todos():
            raise Exception('No stored todos') 
        for todo in self.todos:
            if not todo.completed:
                todo.completed = True
```