from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict

@dataclass
class Template(ABC):
    pass

class TemplateManager(ABC):
    def __init__(self) -> None:
        self.reset()

    def set(self, template = Template()):
        self._template = template

    def get(self):
        return self._template

    def to_data(self) -> dict:
        return asdict(Template)

    def from_data(self, data: dict):
        self._template = Template(**data)

