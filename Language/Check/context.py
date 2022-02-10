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

    def get_function_to_override(self, method, t, name, base_type_name):
        if t == None:
            return
        if name in t.functions:
            m = t.functions[name]
            if len(m.parameters) != len(method.parameters):
                raise SemanticError(WRONG_SIGNATURE % (method.name, base_type_name))
            for i, t in enumerate(method.parameters_types):
                if not m.parameters_type[i] == t:
                    self.errors.append(WRONG_SIGNATURE % (method.name, base_type_name))
                    break
            if not method.return_type == m.return_type:
                self.errors.append(WRONG_SIGNATURE % (method.name, base_type_name))
        self.get_function_to_override(t.parent, name)
