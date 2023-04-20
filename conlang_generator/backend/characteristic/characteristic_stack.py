from abc import ABC, abstractmethod
from typing import Self
from collections import UserString, OrderedDict

from backend.characteristic.characteristic_interface import CharacteristicInterface
from backend.characteristic.complex_characteristic import ComplexCharacteristic



class CharacteristicStack(CharacteristicInterface):
    def __init__(self) -> None:
        self.characteristics = OrderedDict()

    def apply(self, base: UserString) -> UserString:
        for characteristic in self.characteristics.values():
            base = characteristic.apply(base)
        return base

    def set_characteristic(self, key: str, value: str):
        for member_key, member_value in self.characteristics.items():

            if isinstance(member_value, ComplexCharacteristic) and key == member_key:
                member_value.set_value(value)

            elif isinstance(member_value, CharacteristicStack):
                member_value.set_characteristic(key, value)

    def get_string(self, indentation=0, do_number=False):
        final_str = ""
        indent = indentation * "  "
        number = 0
        for member_key, member_value in self.characteristics.items():
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
    
class CharacteristicStackBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._stack = CharacteristicStack()

    def add_characteristic(self, key, characteristic) -> Self:
        self._stack.characteristics[key] = characteristic
        return self

    def get_stack(self) -> CharacteristicStack:
        s = self._stack
        self.reset()
        return s