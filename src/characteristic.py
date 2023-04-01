from stack import Stack
from abc import ABC, abstractmethod

class Characteristic:
    def __init__(self) -> None:
        pass

    def apply(self, base):
        return base
    
class ComplexCharacteristic(Characteristic):
    def __init__(self, default_value: str = None) -> None:
        self.variants = {}
        self.value = default_value

    def add_variant(self, key: str, characteristic: Characteristic):
        self.variants[key] = characteristic

    def set_value(self, value):
        self.value = value
        
    def apply(self, base):
        if self.value in self.variants.keys():
            characteristic = self.variants[self.value]
            
            return characteristic.apply(base)
            
        else:
            return base
        
class CharacteristicStack(Stack, Characteristic):
    def __init__(self) -> None:
        super().__init__()

    def apply(self, base):
        for key, characteristic in self.members.items():
            base = characteristic.apply(base)
            print("Applied", key)
        return base

    def set_characteristic(self, key: str, value: str):
        self.members[key].set_value(value)
    
