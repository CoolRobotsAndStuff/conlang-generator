from abc import ABC, abstractmethod
from collections import UserString

class CharacteristicInterface(ABC):
    @abstractmethod
    def apply(self, base: UserString) -> UserString:
        pass
