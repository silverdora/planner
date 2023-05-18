from models import Category, InputTask, Task

categories = []

tasks = []


def create_category(cat: str) -> Category:
    new_category = Category(id=len(categories), name=cat)
    categories.append(new_category)
    return new_category


def find_category(cat: int) -> Category:
    for category in categories:
        if cat == Category.id:
            return category
        raise ValueError


def create_task(params: InputTask) -> Task:
    new_task = Task(name=params.text,
                    creating_of_habit=params.create_habit,
                    category=find_category(params.category),
                    beginning_planned=params.start,
                    finishing_planned=params.end,
                    beginning_real=None,
                    finishing_real=None,
                    completed=False)
    tasks.append(new_task)
    return new_task
