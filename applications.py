from database import ListCategoriesStorage, ListTasksStorage
from models import Category, InputTask, Task, Finalization

categories = ListCategoriesStorage()
tasks = ListTasksStorage()


def create_category(cat: str) -> Category:
    new_category = Category(
        id=None,
        name=cat
    )
    categories.add_new_cat(new_category)
    return new_category


def create_task(params: InputTask) -> Task:
    new_task = Task(
        id=None,
        name=params.text,
        creating_of_habit=params.create_habit,
        category=categories.find_cat(params.category),
        beginning_planned=params.start,
        finishing_planned=params.end,
        beginning_real=None,
        finishing_real=None,
        completed=False,
    )
    tasks.add_new_task(new_task)
    return new_task


def edit_task(num: int, params: InputTask) -> Task:
    task = tasks.find_task(num)
    task.name = params.text
    task.creating_of_habit = params.create_habit
    task.category = params.category
    task.beginning_planned = params.start
    task.finishing_planned = params.end
    tasks.save_task(task)
    return task


def finish(num: int, final_params: Finalization) -> Task:
    task = tasks.find_task(num)
    task.beginning_real = final_params.start
    task.finishing_real = final_params.end
    task.completed = True
    tasks.save_task(task)
    return task


def unfinish(num: int) -> Task:
    task = tasks.find_task(num)
    task.beginning_real = None
    task.finishing_real = None
    task.completed = False
    tasks.save_task(task)
    return task

