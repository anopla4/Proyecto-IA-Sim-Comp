from Language.Parsing.first import symbol_first


class Production:
    def __init__(self, left_side, right_side) -> None:
        self.left_side = left_side
        self.right_side = right_side
    
    def __str__(self) -> str:
        return f"{self.left_side.symbol} -> {''.join([symbol.symbol for symbol in self.right_side])}"