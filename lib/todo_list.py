from lib.todo import *

class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise Exception('Valid todo not found')
        self.todo_list.append(todo)
    
    def incomplete(self):
        not_dones = []
        for todo in self.todo_list:
            if not todo.completed:
                not_dones.append(f'{todo.task} | incomplete')
        if len(not_dones) == 0:
            return 'No outstanding todos'
        return not_dones

    def complete(self):
        dones = []
        for todo in self.todo_list:
            if todo.completed:
                dones.append(f'{todo.task} | complete')
        if len(dones) == 0:
            return 'No completed todos'
        return dones

    def give_up(self):
        if len(self.todo_list) == 0:
            return 'No todos stored'
        for todo in self.todo_list:
            if not todo.completed:
                todo.completed = True