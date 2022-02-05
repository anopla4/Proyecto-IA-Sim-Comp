from .alphabet_symbol import AlphabetSymbol


class NonTerminal(AlphabetSymbol):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    @staticmethod
    def get_non_terminals(s):
        t = s.split()
        return [NonTerminal(nt) for nt in t]


class ENonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type


class TNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type


class XNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type


class YNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type


class FNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type


class ZNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type
