from ..expression import Expression


class Star(Expression):
    def __init__(self, expr) -> None:
        super().__init__("*", 1)
        self.expr = expr
