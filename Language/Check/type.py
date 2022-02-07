from Language.Check.error import METHOD_NOT_DEFINED, SemanticError
from .attribute import Attribute
from .method import Method


class Type:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.functions = {}
        self.attributes = {}
        self.conforms_to_list = []

    def get_attribute(self, attr_name):
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        return None

    def set_attribute(self, attr_name, attr_type):
        if attr_name in self.attributes:
            raise SemanticError(
                f"{self.name} already contains an attribute {attr_name}"
            )
        attr = Attribute(attr_name, attr_type)
        self.attributes[attr_name] = attr

    def get_function(self, function_name):
        if function_name not in self.functions:
            raise SemanticError(METHOD_NOT_DEFINED % (function_name))
        return self.functions[function_name]

    def set_function(self, function_name, function_type):
        if function_name in self.functions:
            raise SemanticError(f"Function {function_name} already defined.")
        f = Method(function_name, function_type)
        self.functions[function_name] = f

    def set_parent(self, parent):
        self.parent = parent

    def conforms_to(self, t):
        return t in self.conforms_to_list


class ErrorType(Type):
    def __init__(self, name, text, parent=None) -> None:
        super().__init__(name, parent)
        self.text = text


class MainType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Main", parent)


class IntType(Type):
    def __init__(self, name, parent=None) -> None:
        super().__init__(name, parent)


class VoidType(Type):
    def __init__(self, name, parent=None) -> None:
        super().__init__(name, parent)


class AgentType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Agent", parent)


class SymptomType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Symptom", parent)


class InterventionType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Intervention", parent)


class ParameterType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Parameter", parent)


class EnvironmentType(Type):
    def __init__(self, name, parent=None) -> None:
        super().__init__(name, parent)


class RandVarEffectType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("RandVarEffect", parent)
