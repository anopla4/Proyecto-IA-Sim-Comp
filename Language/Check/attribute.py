from unicodedata import name


class Attribute:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
