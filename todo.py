import logging
_logger = logging.getLogger()

class ToDo:
    def __init__(self) -> None:
        self.task_lst = []
    
    def add(self, task: str) -> None:
        self.task_lst.append([task, True])
        _logger.info(f"Задача {task} успешно добавлена в список")

    def remove(self, task_id: int) -> None:
        try:
            self.task_lst.pop(task_id)
            _logger.info(f"Задача с id {task_id} удалена")
        except IndexError:
            _logger.warning(f"Задачи с id {task_id} не существует")

    def complete(self, task_id: int) -> None:
        try:
            self.task_lst[task_id][1] = False
            _logger.info(f"Задача с id {task_id} теперь завершена!")
        except IndexError:
            _logger.warning(f"Задачи с id {task_id} не существует")

    def show(self) -> None:   
        flag = 0
        for task in self.task_lst:
            if task[1]:
                print(task[0])
                flag = 1
        if not flag:
            print("Дел пока нет")
    
    def show_completed(self) -> None:
        flag = 0
        for task in self.task_lst:
            if not task[1]:
                print(task[0])
                flag = 1
        if not flag:
            print("Пока нет завершённых дел")
