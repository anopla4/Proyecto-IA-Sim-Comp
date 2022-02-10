from .node import Node


class DeclarationNode(Node):
    pass


class ClassNode(DeclarationNode):
    def __init__(self, id, statements, parent=None) -> None:
        super().__init__()
        self.id = id
        self.parent = parent
        self.statements = statements


class VarDeclarationNode(DeclarationNode):
    def __init__(self, idt, idv, expr) -> None:
        super().__init__()
        self.type = idt
        self.id = idv
        self.expr = expr


class FuncDeclarationNode(DeclarationNode):
    def __init__(self, idf, params, return_type, body) -> None:
        super().__init__()
        self.id = idf
        self.params = params
        self.body = body
        self.return_type = return_type
