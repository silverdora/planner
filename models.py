from dataclasses import dataclass
from datetime import datetime


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Task:
    name: str
    creating_of_habit: bool
    category: Category
    beginning_planned: datetime
    finishing_planned: datetime
    beginning_real: datetime
    finishing_real: datetime
    completed: bool




