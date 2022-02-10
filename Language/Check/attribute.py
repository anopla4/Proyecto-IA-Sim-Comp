from unicodedata import name


class Attribute:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def __str__(self):
        return f"[attrib] {self.name} : {self.type.name};"

    def __repr__(self):
        return str(self)
