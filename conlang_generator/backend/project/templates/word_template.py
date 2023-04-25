from backend.project.templates.template import Template, TemplateManager
from dataclasses import dataclass

class WordTemplateManager(TemplateManager):
    def __init__(self) -> None:
        super().__init__()

@dataclass
class WordTemplate(Template):
    base : str
    characteristics : list
    exceptions_table : dict
    tags : list




    