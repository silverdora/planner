from models import Category, InputTask, Task, Finalization

categories = []

tasks = []


def create_category(cat: str) -> Category:
    new_category = Category(
        id=len(categories),
        name=cat
    )
    categories.append(new_category)
    return new_category


def find_category(cat: int) -> Category:
    for category in categories:
        if cat == category.id:
            return category
    raise ValueError


def create_task(params: InputTask) -> Task:
    new_task = Task(
        id=len(tasks),
        name=params.text,
        creating_of_habit=params.create_habit,
        category=find_category(params.category),
        beginning_planned=params.start,
        finishing_planned=params.end,
        beginning_real=None,
        finishing_real=None,
        completed=False,
    )
    tasks.append(new_task)
    return new_task


def find_task(found_task: int) -> Task:
    for task in tasks:
        if found_task == task.id:
            return task
    raise ValueError


def edit_task(num: int, params: InputTask) -> Task:
    task = find_task(num)
    task.name = params.text
    task.creating_of_habit = params.create_habit
    task.category = params.category
    task.beginning_planned = params.start
    task.finishing_planned = params.end
    return task


def finish(num: int, final_params: Finalization) -> Task:
    task = find_task(num)
    task.beginning_real = final_params.start
    task.finishing_real = final_params.end
    task.completed = True
    return task


def unfinish(num: int) -> Task:
    task = find_task(num)
    task.beginning_real = None
    task.finishing_real = None
    task.completed = False
    return task

