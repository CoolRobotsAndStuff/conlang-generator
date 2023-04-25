from backend.characteristic.simple_characteristic import SimpleCharacteristic, SimpleCharacteristicBuilder


class SufixBuilder(SimpleCharacteristicBuilder):
    def __init__(self) -> None:
        super().__init__()

    def reset(self):
        self._characteristic = Sufix()

class Sufix(SimpleCharacteristic):
    def apply(self, base):
        return base + self.arguments["sufix"]