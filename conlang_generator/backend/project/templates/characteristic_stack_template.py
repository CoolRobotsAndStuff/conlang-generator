from templates.template import Template, TemplateManager
from dataclasses import dataclass

@dataclass
class CharacteristicStackTemplate(Template):
    characteristics = []

class ChatacteristicsStackTemplateManager(TemplateManager):
    def __init__(self) -> None:
        self.set()

    def set(self, template=CharacteristicStackTemplate()):
        self._template = template

    def get(self) -> CharacteristicStackTemplate:
        return super().get()
    