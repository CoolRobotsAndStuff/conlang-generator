from backend.stack import Stack
from abc import ABC, abstractmethod

class Characteristic:
    def __init__(self, arguments: dict = {}) -> None:
        self.arguments = arguments

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
        return base

    def set_characteristic(self, key: str, value: str):
        for member_key, member_value in self.members.items():
            if isinstance(member_value, ComplexCharacteristic):
                if key == member_key:
                    member_value.set_value(value)

            elif isinstance(member_value, CharacteristicStack):
                member_value.set_characteristic(key, value)

    def get_string(self, indentation=0, do_number=False):
        final_str = ""
        indent = indentation * "  "
        number = 0
        for member_key, member_value in self.members.items():
            if isinstance(member_value, CharacteristicStack):
                final_str +=  f"{number if do_number else ''}- {member_key}:\n"
                final_str += member_value.get_string(indentation + 1)

            elif isinstance(member_value, ComplexCharacteristic):
                final_str +=  f"{indent}{number if do_number else ''}. {member_key}: {member_value.value} \n"
            else:
                final_str +=  f"{indent}{number if do_number else ''}. {member_key}\n"

            number += 1
        
        return final_str


    def __str__(self):
        heading = "---Characteristics---\n"

        return  heading + self.get_string(0, True)
    
