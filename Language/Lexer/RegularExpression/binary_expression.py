from ..expression import Expression


class BinaryExpression(Expression):
    def __init__(self, regex, priority, left_expr, right_expr) -> None:
        super().__init__(regex, priority)
        self.left_expr = left_expr
        self.right_expr = right_expr

    def build_automaton(self, left_automaton, right_automaton):
        pass
