from .binary_expression import BinaryExpression


class Concat(BinaryExpression):
    def __init__(self, left_expr, right_expr) -> None:
        super().__init__("U", 2, left_expr, right_expr)
