from ast import Num
from dataclasses import is_dataclass
from .node import Node


class ExpressionNode(Node):
    pass


class AtomicNode(ExpressionNode):
    def __init__(self, lex) -> None:
        super().__init__()
        self.lex = lex


class ConstantNumNode(AtomicNode):
    pass


class CallNode(AtomicNode):
    def __init__(self, lex, argums, obj=None) -> None:
        super().__init__(lex)
        self.arguments = argums
        self.obj = obj


class InstanceNode(AtomicNode):
    def __init__(self, idc, argums) -> None:
        super().__init__()
        self.id = idc
        self.arguments = argums


class VariableNode(AtomicNode):
    pass


class BinaryNode(ExpressionNode):
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right = right


class ByNode(BinaryNode):
    pass


class DivideNode(BinaryNode):
    pass


class PlusNode(BinaryNode):
    pass


class MinusNode(BinaryNode):
    pass


class EqualsNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class NotEqualsNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class GreaterNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class LesserNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class AndNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class OrNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class UnaryNode(ExpressionNode):
    def __init__(self, expr) -> None:
        super().__init__()
        self.expr = expr


class NotNode(UnaryNode):
    def __init__(self, expr) -> None:
        super().__init__(expr)


class RuleNode(ExpressionNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ProbFunctionValueNode(ExpressionNode):
    def __init__(self, num, val) -> None:
        super().__init__()
        self.num = num
        self.val = val


class ProbabilityFunctionNode(ExpressionNode):
    def __init__(self, values) -> None:
        super().__init__()
        self.values = values


class EfectNode(ExpressionNode):
    def __init__(self, par, e) -> None:
        super().__init__()
        self.par = par
        self.e = e


class EfectRuleNode(ExpressionNode):
    def __init__(self, e) -> None:
        super().__init__()
        self.e = e
