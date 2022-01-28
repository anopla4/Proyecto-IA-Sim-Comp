from .alphabet_symbol import AlphabetSymbol


class Epsilon(AlphabetSymbol):
    def __init__(self) -> None:
        super().__init__("epsilon")
