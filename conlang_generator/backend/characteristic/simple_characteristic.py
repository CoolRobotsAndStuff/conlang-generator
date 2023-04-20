from abc import ABC, abstractmethod
from typing import Self
from collections import UserString

from backend.characteristic.characteristic_interface import CharacteristicInterface

class SimpleCharacteristic(CharacteristicInterface):
    def __init__(self) -> None:
        self.arguments = {}

    def apply(self, base: UserString) -> UserString:
        return base
    

class SimpleCharacteristicBuilder(ABC):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self):
        self._characteristic = SimpleCharacteristic()

    def set_argument(self, key, value) -> Self:
        self._characteristic.arguments[key] = value
        return self

    def get_characteristic(self) -> SimpleCharacteristic:
        c = self._characteristic
        self.reset()
        return c