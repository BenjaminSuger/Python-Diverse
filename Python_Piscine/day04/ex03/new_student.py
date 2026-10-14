import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student entity"""
    name: str
    surname: str
    active: bool = True
    id: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self) -> None:
        self.login = self.name[0] + self.surname
        self.id = generate_id()
