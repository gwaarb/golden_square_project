from lib.entry import *
from lib.todo import *

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