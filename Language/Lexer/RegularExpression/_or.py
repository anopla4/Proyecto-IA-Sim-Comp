from .binary_expression import BinaryExpression


class Or(BinaryExpression):
    def __init__(self, left_expr, right_expr) -> None:
        super().__init__("|", 3, left_expr, right_expr)
