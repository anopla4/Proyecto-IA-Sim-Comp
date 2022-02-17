from Language.Parsing.Node.declaration_nodes import FuncDeclarationNode
from .error import WRONG_SIGNATURE, SemanticError
from .type import Type


class Context:
    def __init__(self) -> None:
        self.types = {}

    def __str__(self):
        return (
            "{\n\t"
            + "\n\t".join(y for x in self.types.values() for y in str(x).split("\n"))
            + "\n}"
        )

    def __repr__(self):
        return str(self)

    def def_type(self, type):
        if type in self.types:
            raise SemanticError(f"Type {type} is already defined.")
        self.types[type] = Type(type)
        return self.types[type]

    def get_type(self, type_name):
        if type_name not in self.types:
            raise SemanticError(f"Type {type_name} is not defined.")
        return self.types[type_name]

    def check_cyclic_inheritance(self, type, type_parent):
        if type_parent == None:
            return
        if type.name == type_parent.name:
            raise SemanticError("Cyclic inheritance.")
        self.check_cyclic_inheritance(type, type.parent)

    def check_if_return_in_func(self, node):
        if node is None:
            raise False
        if isinstance(node, FuncDeclarationNode):
            return True
        return self.check_if_return_in_func(node.parent)

    def check_type_instance(self, node, type_name):
        if len(self.types[type_name].parameters_types) != len(node.arguments):
            raise SemanticError(
                f"Type {type_name} receives {len(self.types[type_name].parameters_types)} arguments."
            )

    def check_argument_type(self, node, index, type_name):
        t = self.types[type_name].parameters_types[index]
        if t != node.type:
            raise SemanticError(f"Cannot convert {t} into {node.type}.")
