from templates.template import Template, TemplateManager
from word_template import WordTemplate, WordTemplateManager
from characteristic_stack_template import CharacteristicStackTemplate, ChatacteristicsStackTemplateManager
from dataclasses import dataclass

@dataclass
class ProjectTemplate(Template):
    characteristics: dict
    words: dict

class ProjectTemplateManager(TemplateManager):
    def __init__(self) -> None:
        self.set()
        self.word_template_manager = WordTemplateManager()
        self.characteristics_stack_template_manager = ChatacteristicsStackTemplateManager()

    def set(self, template=ProjectTemplate()):
        self._template = template

    def get(self) -> ProjectTemplate:
        return self._template

    def to_data(self) -> dict:
        # Create words data
        words_data = {}
        for key, word_template in self._template.words:
            self.word_template_manager.set(word_template)
            words_data[key] = self.word_template_manager.to_data()
        
        # Create characteristics data
        characteristics_data = {}
        for key, characteristic_template in self._template.characteristics:
            self.characteristics_stack_template_manager.set(characteristic_template)
            characteristics_data[key] = self.characteristics_stack_template_manager.to_data()
        
        return {"characteristics": characteristics_data, "words": words_data}
    
    def from_data(self, data: dict):
        # Load words
        for key, word_data in data["words"]:
            self.word_template_manager.from_data(word_data)
            self._template.words[key] = self.word_template_manager.get()

        # Load characteristics
        for key, characteristic_data in data["characteristics"]:
            self.characteristics_stack_template_manager.from_data(characteristic_data)
            self._template.characteristics[key] = self.characteristics_stack_template_manager.get()
        





    
    

    


        