from typing import List

from fastapi import FastAPI

import applications
from models import Category, InputTask, Task

app = FastAPI()


@app.get('/categories')
def all_categories() -> List[Category]:
    return applications.categories


@app.post('/categories')
def create_category(cat: str) -> Category:
    return applications.create_category(cat)


@app.get('/tasks')
def all_tasks() -> List[Task]:
    return applications.tasks


@app.post('/tasks')
def create_a_task(params: InputTask) -> Task:
    return applications.create_task(params)
