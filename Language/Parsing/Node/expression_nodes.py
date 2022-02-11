from ast import Num
from dataclasses import is_dataclass

from Language.Check.type import DictType
from .node import Node


class ExpressionNode(Node):
    def __init__(self, type) -> None:
        super().__init__()
        self.type = type


class AtomicNode(ExpressionNode):
    def __init__(self, lex, type=None) -> None:
        super().__init__(type)
        self.lex = lex


class ConstantNumNode(AtomicNode):
    def __init__(self, lex, type=None) -> None:
        super().__init__(lex, type)


class CallNode(AtomicNode):
    def __init__(self, lex, argums, obj=None, type=None) -> None:
        super().__init__(lex, type)
        self.arguments = argums
        self.obj = obj


class InstanceNode(AtomicNode):
    def __init__(self, idc, argums, type=None) -> None:
        super().__init__(idc, type)
        self.arguments = argums


class VariableNode(AtomicNode):
    def __init__(self, lex, type=None) -> None:
        super().__init__(lex, type)


class StringNode(AtomicNode):
    def __init__(self, lex, type=None) -> None:
        super().__init__(lex, DictType)


class DictNode(ExpressionNode):
    def __init__(self, items, type=None) -> None:
        super().__init__(type)
        self.items = items


class ItemNode(Node):
    def __init__(self, key, val) -> None:
        super().__init__()
        self.key = key
        self.val = val


class TupleNode(ExpressionNode):
    def __init__(self, items, type=None) -> None:
        super().__init__(type)
        self.items = items


class ListNode(ExpressionNode):
    def __init__(self, items, type=None) -> None:
        super().__init__(type)
        self.items = items


class BinaryNode(ExpressionNode):
    def __init__(self, left, right, symbol, type=None) -> None:
        super().__init__(type)
        self.left = left
        self.right = right
        self.symbol = symbol


class NumericBinaryNode(BinaryNode):
    def __init__(self, left, right, symbol, type=None) -> None:
        super().__init__(left, right, symbol, type)


class ByNode(NumericBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "*")


class DivideNode(NumericBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "/")


class PlusNode(NumericBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "+")


class MinusNode(NumericBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "-")


class BooleanBinaryNode(BinaryNode):
    def __init__(self, left, right, symbol, type=None) -> None:
        super().__init__(left, right, symbol, type)


class EqualsNode(BooleanBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "==")


class NotEqualsNode(BooleanBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "!=")


class GreaterNode(BooleanBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, ">")


class LesserNode(BooleanBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "<")


class AndNode(BooleanBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "and")


class OrNode(BooleanBinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "or")


class UnaryNode(ExpressionNode):
    def __init__(self, expr, symbol, type=None) -> None:
        super().__init__(type)
        self.expr = expr
        self.symbol = symbol


class NotNode(UnaryNode):
    def __init__(self, expr) -> None:
        super().__init__(expr, "not")


class RuleNode(ExpressionNode):
    def __init__(self, condition, destination, then, type=None) -> None:
        super().__init__(type)
        self.condition = condition
        self.destination = destination
        self.then = then
        self.type = type


class ProbFunctionValueNode(Node):
    def __init__(self, num, val) -> None:
        super().__init__()
        self.num = num
        self.val = val


class ProbabilityFunctionNode(ExpressionNode):
    def __init__(self, values, type=None) -> None:
        super().__init__(type)
        self.values = values


class EffectNode(ExpressionNode):
    def __init__(self, par, env, e, type=None) -> None:
        super().__init__(type)
        self.par = par
        self.env = env
        self.e = e


class EffectRuleNode(ExpressionNode):
    def __init__(self, e) -> None:
        super().__init__()
        self.e = e


class BooleanNode(ExpressionNode):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
