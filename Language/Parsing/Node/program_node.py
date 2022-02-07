from .node import Node


class ProgramNode(Node):
    def __init__(self, statements) -> None:
        super().__init__()
        self.statements = statements
