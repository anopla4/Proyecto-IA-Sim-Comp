from alphabet_symbol import AlphabetSymbol


class NonTerminal(AlphabetSymbol):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
