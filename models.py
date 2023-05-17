from dataclasses import dataclass
from datetime import datetime


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Task:
    name: str
    beginning_planned: datetime
    time_to_do_planned: datetime
    finishing_planned: datetime
    beginning_real: datetime
    time_to_do_real: datetime
    finishing_real: datetime
    completed_button: str


@dataclass
class WheelOfBalance(Task):
    
