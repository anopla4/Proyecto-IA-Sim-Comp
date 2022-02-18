from collections import OrderedDict
from Language.Check.error import SemanticError
from .attribute import Attribute
from .method import Method


class Type:
    def __init__(self, name, parent=None, functions=None) -> None:
        self.name = name
        self.parameters_types = []
        self.parent = parent
        self.functions = {} if functions == None else functions
        self.attributes = {}

    def get_attribute(self, name: str):
        try:
            return next(attr for attr in self.attributes if attr.name == name)
        except StopIteration:
            if self.parent is None:
                raise SemanticError(
                    f'Attribute "{name}" is not defined in {self.name}.'
                )
            try:
                return self.parent.get_attribute(name)
            except SemanticError:
                raise SemanticError(
                    f'Attribute "{name}" is not defined in {self.name}.'
                )

    def set_attribute(self, name: str, typex):
        try:
            self.get_attribute(name)
        except SemanticError:
            attribute = Attribute(name, typex)
            self.attributes.append(attribute)
            return attribute
        else:
            raise SemanticError(
                f'Attribute "{name}" is already defined in {self.name}.'
            )

    def get_function(self, name: str):
        try:
            return next(
                self.functions[f]
                for f in self.functions
                if self.functions[f].name == name
            )
        except StopIteration:
            if self.parent is None:
                raise SemanticError(f'Method "{name}" is not defined in {self.name}.')
            try:
                return self.parent.get_function(name)
            except SemanticError:
                raise SemanticError(f'Method "{name}" is not defined in {self.name}.')

    def set_function(
        self, name: str, param_names: list, param_types: list, return_type
    ):
        if name in (self.functions[f].name for f in self.functions):
            raise SemanticError(f'Method "{name}" already defined in {self.name}')
        method = Method(name, return_type, param_names, param_types)
        self.functions[name] = method
        return method

    def set_parent(self, parent):
        if self.parent is not None:
            raise SemanticError(f"Parent type is already set for {self.name}.")
        self.parent = parent

    def all_attributes(self, clean=True):
        plain = (
            OrderedDict() if self.parent is None else self.parent.all_attributes(False)
        )
        for attr in self.attributes:
            plain[attr.name] = (attr, self)
        return plain.values() if clean else plain

    def all_methods(self, clean=True):
        plain = OrderedDict() if self.parent is None else self.parent.all_methods(False)
        for method in self.functions:
            plain[method.name] = (method, self)
        return plain.values() if clean else plain

    def conforms_to(self, other):
        return (
            isinstance(other, MainType)
            or other.bypass()
            or self == other
            or self.parent is not None
            and self.parent.conforms_to(other)
        )

    def bypass(self):
        return False

    def __str__(self):
        output = f"type {self.name}"
        parent = "" if self.parent is None else f" : {self.parent.name}"
        output += parent
        output += " {"
        output += "\n\t" if self.attributes or self.functions else ""
        output += "\n\t".join(str(x) for x in self.attributes)
        output += "\n\t" if self.attributes else ""
        output += "\n\t".join(str(x) for x in self.functions)
        output += "\n" if self.functions else ""
        output += "}\n"
        return output

    def __repr__(self):
        return str(self)


class ErrorType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("<error>", parent)

    def conforms_to(self, other):
        return True

    def bypass(self):
        return True

    def __eq__(self, other):
        return isinstance(other, Type)


class MainType(Type):
    def __init__(self, parent=None) -> None:
        functions = {
            "main": Method(
                "main",
                "Tree",
                ["env", "treatment", "disease", "tick", "end_time", "num_sim"],
                ["Environment", "List", "List", "Num", "Num", "Num"],
            ),
            "print": Method("print", "void", ["text"], ["Main"]),
        }
        super().__init__("Main", parent, functions)


class TreeType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("tree", parent)


class NumType(Type):
    def __init__(self, name="num", parent=None) -> None:
        super().__init__(name, parent)

    def __eq__(self, other):
        return other.name == self.name or isinstance(other, NumType)


class IntType(NumType):
    def __init__(self, parent=None) -> None:
        super().__init__("int", parent)

    def __eq__(self, other):
        return other.name == self.name or isinstance(other, IntType)


class DoubleType(NumType):
    def __init__(self, parent=None) -> None:
        super().__init__("int", parent)

    def __eq__(self, other):
        return other.name == self.name or isinstance(other, IntType)


class BoolType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("bool", parent)


class StringType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("string", parent)


class VoidType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("void", parent)

    def conforms_to(self, other):
        raise Exception("Invalid type: void type.")

    def bypass(self):
        return True

    def __eq__(self, other):
        return isinstance(other, VoidType)


class AgentType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Agent", parent)
        self.parameters_types = ["List", "Num", "Num", "RandVarEffect", "Num"]


class SymptomType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Symptom", parent)
        self.parameters_types = ["List", "Num", "Num", "RandVarEffect"]


class InterventionType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Intervention", parent)
        self.parameters_types = ["List", "Num", "Num", "RandVarEffect", "Num"]


class ParameterType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Parameter", parent)
        self.parameters_types = ["String", "Num", "Num", "Num", "Num", "Num"]


class EnvironmentType(Type):
    def __init__(self, name, parent=None) -> None:
        super().__init__(name, parent)
        self.parameters_types = ["List"]


class PatientType(EnvironmentType):
    def __init__(self, parent=None) -> None:
        super().__init__("patient", parent)


class RandVarEffectType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("RandVarEffect", parent)
        self.parameters_types = []


class ActivationRuleType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("ActivationRule", parent)
        self.parameters_types = ["Dict", "Tuple"]


class ListType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("List", parent)
        self.elements_type = None


class DictType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Dict", parent)


class TupleType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("Tuple", parent)


class MembresyFunctionType(Type):
    def __init__(self, parent=None) -> None:
        super().__init__("MembresyFunction", parent)


class TriangularType(MembresyFunctionType):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parameters_types = ["Num", "Num", "Num"]


class TrapezoidalType(MembresyFunctionType):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parameters_types = ["Num", "Num", "Num", "Num"]
