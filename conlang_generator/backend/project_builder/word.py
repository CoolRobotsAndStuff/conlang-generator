from backend.characteristic.characteristic_stack import CharacteristicStack
from backend.characteristic.characteristic_stack import CharacteristicStackBuilder
from conlang_generator.backend.project_builder.characteristic.word_type import WordType

from collections import UserString
from typing import Self

class WordBuilder:
    def __init__(self) -> None:
        self.stack_builder = CharacteristicStackBuilder()
        self.reset()
    
    def reset(self):
        self._word = Word()

    def set_base(self, base: UserString) -> Self:
        self._word.base = base
        return self

    def add_word_type(self, word_type: WordType):
        self.stack_builder.add_characteristic("word_type", word_type)
        self._word.characteristics = self.stack_builder.get_stack()
        return self
    
    def get_word(self):
        w = self._word
        self.reset()
        return w

class Word(UserString):
    def __init__(self) -> None:
        self.data = ""
        self.base = UserString("")
        self.characteristics = CharacteristicStack()
        self.exceptions_table = {}

    def set_characteristic_value(self, key, value):
        self.characteristics.set_characteristic(key, value)

    def apply_characteristics(self):
        self.data = self.characteristics.apply(self.base).data
    
    def get_string_representation(self):
        final_str = f"### Word: {self.data} ###\nBase: {self.base.data}\n{str(self.characteristics)}"
        return final_str

    
    