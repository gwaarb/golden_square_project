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