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
    def __init__(self, lex) -> None:
        super().__init__(lex)


class CallNode(AtomicNode):
    def __init__(self, lex, argums, obj=None) -> None:
        super().__init__(lex)
        self.arguments = argums
        self.obj = obj


class InstanceNode(AtomicNode):
    def __init__(self, idc, argums) -> None:
        super().__init__(idc)
        self.arguments = argums


class VariableNode(AtomicNode):
    def __init__(self, lex) -> None:
        super().__init__(lex)


class StringNode(AtomicNode):
    def __init__(self, lex) -> None:
        super().__init__(lex)


class DictNode(ExpressionNode):
    def __init__(self, items) -> None:
        super().__init__()
        self.items = items


class ItemNode(ExpressionNode):
    def __init__(self, key, val) -> None:
        super().__init__()
        self.key = key
        self.val = val


class TupleNode(ExpressionNode):
    def __init__(self, items) -> None:
        super().__init__()
        self.items = items


class ListNode(ExpressionNode):
    def __init__(self, items) -> None:
        super().__init__()
        self.items = items


class BinaryNode(ExpressionNode):
    def __init__(self, left, right, symbol) -> None:
        super().__init__()
        self.left = left
        self.right = right
        self.symbol = symbol


class ByNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "*")


class DivideNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "/")


class PlusNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "+")


class MinusNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "-")


class EqualsNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "==")


class NotEqualsNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "!=")


class GreaterNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, ">")


class LesserNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "<")


class AndNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "and")


class OrNode(BinaryNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "or")


class UnaryNode(ExpressionNode):
    def __init__(self, expr, symbol) -> None:
        super().__init__()
        self.expr = expr
        self.symbol = symbol


class NotNode(UnaryNode):
    def __init__(self, expr) -> None:
        super().__init__(expr, "not")


class RuleNode(ExpressionNode):
    def __init__(self, condition, destination, then_var, then_val) -> None:
        self.condition = condition
        self.destination = destination
        self.then_var = then_var
        self.then_val = then_val


class ProbFunctionValueNode(ExpressionNode):
    def __init__(self, num, val) -> None:
        super().__init__()
        self.num = num
        self.val = val


class ProbabilityFunctionNode(ExpressionNode):
    def __init__(self, values) -> None:
        super().__init__()
        self.values = values


class EffectNode(ExpressionNode):
    def __init__(self, par, env, e) -> None:
        super().__init__()
        self.par = par
        self.env = env
        self.e = e


class EffectRuleNode(ExpressionNode):
    def __init__(self, e) -> None:
        super().__init__()
        self.e = e
