from .alphabet_symbol import AlphabetSymbol


class Dollar(AlphabetSymbol):
    def __init__(self) -> None:
        super().__init__("$")
