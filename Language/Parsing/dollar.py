from Language.Parsing.terminal import Terminal
from .alphabet_symbol import AlphabetSymbol


class Dollar(Terminal):
    def __init__(self) -> None:
        super().__init__("$")
