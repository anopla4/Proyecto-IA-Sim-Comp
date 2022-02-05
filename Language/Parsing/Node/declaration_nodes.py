from .node import Node


class DeclarationNode(Node):
    pass


class ClassNode(DeclarationNode):
    def __init__(self, expr) -> None:
        super().__init__()
        self.expr = expr


class VarDeclarationNode(DeclarationNode):
    def __init__(self, idt, idv, expr) -> None:
        super().__init__()
        self.type = idt
        self.id = idv
        self.expr = expr


class FuncDeclarationNode(DeclarationNode):
    def __init__(self, idf, argums, body) -> None:
        super().__init__()
        self.id = idf
        self.arguments = argums
        self.body = body
