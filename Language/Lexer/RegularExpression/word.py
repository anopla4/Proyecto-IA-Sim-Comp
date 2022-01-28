from ..expression import Expression


class Word(Expression):
    def __init__(self, w) -> None:
        super().__init__(w, 1)
