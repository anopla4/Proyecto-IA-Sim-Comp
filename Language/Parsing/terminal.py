from .alphabet_symbol import AlphabetSymbol


class Terminal(AlphabetSymbol):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    @staticmethod
    def get_terminals(s):
        t = s.split()
        return [Terminal(nt) for nt in t]
