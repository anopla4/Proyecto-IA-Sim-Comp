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
    def __init__(self, idf, params_names, return_type, body) -> None:
        # def __init__(self, idf, params_types, params_names, body, return_type) -> None:
        super().__init__()
        self.id = idf
        # self.params_types = params_types
        self.params_names = params_names
        self.body = body
        self.return_type = return_type
