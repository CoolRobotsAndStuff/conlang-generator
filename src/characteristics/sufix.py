from characteristic import Characteristic


class Sufix(Characteristic):
    def __init__(self, suffix) -> None:
        super().__init__()
        self.suffix: str = suffix

    def apply(self, base):
        return base + self.suffix