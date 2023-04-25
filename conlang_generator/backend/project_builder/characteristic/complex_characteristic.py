from typing import Self
from collections import UserString, OrderedDict

from backend.characteristic.characteristic_interface import CharacteristicInterface

class ComplexCharacteristic(CharacteristicInterface):
    def __init__(self) -> None:
        self.variants = OrderedDict()
        self.value = None

    def set_value(self, value):
        self.value = value
        
    def apply(self, base: UserString) -> UserString:
        if self.value in self.variants.keys():
            characteristic = self.variants[self.value]
            return characteristic.apply(base)
            
        else:
            return base
        
class ComplexCharacteristicBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._complex_characteristic = ComplexCharacteristic()

    def set_default_value(self, value) -> Self:
        self._complex_characteristic.set_value(value)
        return self
    
    def add_variant(self, key: str, characteristic: CharacteristicInterface) -> Self:
        self._complex_characteristic.variants[key] = characteristic
        return self

    def get_complex_characteristic(self) -> ComplexCharacteristic:
        c = self._complex_characteristic
        self.reset()
        return c