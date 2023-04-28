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