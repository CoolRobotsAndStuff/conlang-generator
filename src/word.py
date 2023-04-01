from characteristic import CharacteristicStack, Characteristic
from word_type import WordType
from copy import copy

class Word():
    def __init__(self, base="", word_type=None) -> None:
        self.base = base
        self.characteristics = CharacteristicStack()
        if word_type is not None:
            self.characteristics.insert_item(0, "word_type", copy(word_type))
        self.exceptions_table = {}
    
    def __str__(self) -> str:
        return self.__apply_characteristics()
    
    def __apply_characteristics(self):
        return self.characteristics.apply(self.base)