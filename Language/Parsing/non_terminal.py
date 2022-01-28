from .alphabet_symbol import AlphabetSymbol


class NonTerminal(AlphabetSymbol):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    def type_class():
        pass


class ENonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type

    def type_class():
        return ENonTerminal


class TNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type

    def type_class():
        return TNonTerminal


class XNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type

    def type_class():
        return XNonTerminal


class YNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type

    def type_class():
        return YNonTerminal


class FNonTerminal(NonTerminal):
    def __init__(self, symbol, type=None) -> None:
        super().__init__(symbol)
        self.type = type

    def type_class():
        return FNonTerminal


class ZNonTerminal(NonTerminal):
    def __init__(self, symbol, type = None) -> None:
        super().__init__(symbol)
        self.type = type

    def type_class():
        return ZNonTerminal
