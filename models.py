from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Task:
    id: int
    name: str
    creating_of_habit: bool
    category: Category
    beginning_planned: datetime
    finishing_planned: datetime
    beginning_real: Optional[datetime]
    finishing_real: Optional[datetime]
    completed: bool


@dataclass
class InputTask:
    text: str
    create_habit: bool
    category: int
    start: datetime
    end: datetime


@dataclass
class Finalization:
    start: datetime
    end: datetime
