class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name

    def get_task_name(self):
        return self.task_name

    def mark_as_completed(self):
        self.completed = True

    def is_completed(self):
        return self.is_completed