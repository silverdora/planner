from abc import ABC, abstractmethod
from typing import List
from models import Category, Task


class AbstractCategoriesStorage(ABC):
    @abstractmethod
    def get_cats(self) -> List[Category]:
        raise NotImplementedError

    @abstractmethod
    def add_new_cat(self, cat: Category) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_cat(self, id_of_cat: int) -> Category:
        raise NotImplementedError


class AbstractTasksStorage(ABC):
    @abstractmethod
    def get_tasks(self) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def add_new_task(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_task(self, id_of_task: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def save_task(self, task: Task) -> None:
        raise NotImplementedError


class ListCategoriesStorage(AbstractCategoriesStorage):
    def __init__(self):
        self.categories: List[Category] = []

    def get_cats(self) -> List[Category]:
        return self.categories

    def add_new_cat(self, cat: Category) -> None:
        cat.id = len(self.categories)
        self.categories.append(cat)

    def find_cat(self, id_of_cat: int) -> Category:
        for category in self.categories:
            if id_of_cat == category.id:
                return category
        raise ValueError


class ListTasksStorage(AbstractTasksStorage):
    def __init__(self):
        self.tasks: List[Task] = []

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def add_new_task(self, task: Task) -> None:
        task.id = len(self.tasks)
        self.tasks.append(task)

    def find_task(self, id_of_task: int) -> Task:
        for task in self.tasks:
            if id_of_task == task.id:
                return task
        raise ValueError

    def save_task(self, task: Task) -> None:
        pass
