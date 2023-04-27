class Todo:
    task = ''
    completed = False

    def __init__(self, task):
        if not isinstance(task, str) or not task.strip():
            raise Exception('Invalid task')
        self.task = task
        self.completed = False

    def mark_complete(self):
        if self.completed:
            raise Exception('Task already completed')
        self.completed = True