from typing import List

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

import applications
from models import Category, InputTask, Task, Finalization

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


@app.put('/tasks/{number}')
def update_task(number: int, params: InputTask) -> Task:
    return applications.edit_task(number, params)


@app.post('/tasks/{number}/done')
def done(number: int, params: Finalization) -> Task:
    return applications.finish(number, params)


@app.delete('/tasks/{number}/done')
def undone(number: int) -> Task:
    return applications.unfinish(number)
