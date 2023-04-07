from characteristic import Characteristic


class Sufix(Characteristic):
    def apply(self, base):
        return base + self.arguments["sufix"]