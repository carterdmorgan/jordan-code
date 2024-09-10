from datetime import datetime as dt

class Task:
    def __init__(self, name: str, duration: int, deadline: str, completed = False) -> None:
        # tasks begin as soon as they are added
        self.name = name
        self.duration = duration
        # convert deadline from 'YYYY-MM-DD HH:MM' to datetime object
        self.deadline = dt.strptime(deadline, '%Y-%m-%d %H:%M')
        self.completed = completed

class TaskScheduler:

    STATUS_MESSAGE = {
        
    }

    def __init__(self, tasks = None) -> None:
        if tasks is None:
            tasks = {}
        self.tasks = tasks

    def validate_task(self, task = None):
        if task is None:
            raise ValueError('No task by that name')

    def add_task(self, name: str, duration: int, deadline: str):
        added_task = Task(name, duration, deadline)
        self.tasks[name] = added_task

    def check_status(self, name: str):
        current_task = self.tasks.get(name, None)
        try:
            self.validate_task(current_task)
            if current_task.completed is False:
                return 'In progress'
            elif current_task.completed is True:
                return 'Completed'
            else:
                return 'Not started'
        except ValueError as e:
            print({e})
    
    def complete_task(self, name: str):
        current_task = self.tasks.get(name, None)
        try:
            self.validate_task(current_task)
            current_task.completed = True
            self.tasks.pop(name)
        except ValueError as e:
            print({e})
            
    def get_overdue_tasks(self, current_time: str):
        current_datetime = dt.strptime(current_time, '%Y-%m-%d %H:%M')
        overdue_tasks = []
        for value in self.tasks.values():
            if value.deadline < current_datetime:
                overdue_tasks.append(value.name)
        return overdue_tasks


def main():
    schedule1 = TaskScheduler()

    schedule1.add_task('clean house', 2, "2024-09-10 12:00")
    print(schedule1.tasks)

    print(schedule1.check_status('clean house'))
    print(schedule1.check_status('wash car'))

    schedule1.complete_task('clean house')
    print(schedule1.tasks)

    schedule1.complete_task('wash car')
    print(schedule1.tasks)

    schedule1.add_task('clean house', 2, "2024-09-10 12:00")
    print(schedule1.get_overdue_tasks("2024-09-12 12:00"))

    print('end of line')






main()