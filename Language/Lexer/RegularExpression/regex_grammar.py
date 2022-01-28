from ...Parsing.non_terminal import (
    NonTerminal,
    ENonTerminal,
    XNonTerminal,
    TNonTerminal,
    YNonTerminal,
    FNonTerminal,
    ZNonTerminal,
)
from ...Parsing.terminal import Terminal
from ...Parsing.production import Production
from ...Parsing.epsilon import Epsilon
from ._or import Or
from ._concat import Concat
from ._star import Star
from .word import Word
from .rule import ProductionRules

ast = "ast"
tmp = "tmp"
E = ENonTerminal("E")
X = XNonTerminal("X")
X1 = XNonTerminal("X1", X)
T = TNonTerminal("T")
Y = YNonTerminal("Y")
Y1 = YNonTerminal("Y1", Y)
F = FNonTerminal("F")
Z = ZNonTerminal("Z")
Z1 = ZNonTerminal("Z1", Z)
A = ZNonTerminal("A")

i = Terminal("i")
_or = Terminal("|")
_concat = Terminal("U")
_star = Terminal("*")
left_br = Terminal("(")
right_br = Terminal(")")
epsilon = Epsilon()
p_0 = Production(E, [T, X])
p_1 = Production(X, [_or, T, X1])
p_2 = Production(X, [epsilon])
p_3 = Production(T, [F, Y])
p_4 = Production(Y, [_concat, F, Y1])
p_5 = Production(Y, [epsilon])
p_6 = Production(F, [A, Z])
p_7 = Production(Z, [_star, Z1])
p_8 = Production(Z, [epsilon])
p_9 = Production(A, [left_br, E, right_br])
p_10 = Production(A, [i])
productions = {
    E: [p_0],
    X: [p_1, p_2],
    T: [p_3],
    Y: [p_4, p_5],
    F: [p_6],
    Z: [p_7, p_8],
    A: [p_9, p_10],
}

rules = {
    p_0: ProductionRules(
        inherited_rules_functions={X: {(X, tmp): (T, ast)}},
        synthesized_rules_functions={E: {(E, ast): (X, ast)}},
    ),
    p_1: ProductionRules(
        inherited_rules_functions={X1: {(X1, tmp): (Or, (X, tmp), (T, ast))}},
        synthesized_rules_functions={X: {(X, ast): (X1, ast)}},
    ),
    p_2: ProductionRules(
        inherited_rules_functions={},
        synthesized_rules_functions={X: {(X, ast): (X, tmp)}},
    ),
    p_3: ProductionRules(
        inherited_rules_functions={Y: {(Y, tmp): (F, ast)}},
        synthesized_rules_functions={T: {(T, ast): (Y, ast)}},
    ),
    p_4: ProductionRules(
        inherited_rules_functions={Y1: {(Y1, tmp): (Concat, (Y, tmp), (F, ast))}},
        synthesized_rules_functions={Y: {(Y, ast): (Y1, ast)}},
    ),
    p_5: ProductionRules(
        inherited_rules_functions={},
        synthesized_rules_functions={Y: {(Y, ast): (Y, tmp)}},
    ),
    p_6: ProductionRules(
        inherited_rules_functions={Z: {(Z, tmp): (A, ast)}},
        synthesized_rules_functions={F: {(F, ast): (Z, ast)}},
    ),
    p_7: ProductionRules(
        inherited_rules_functions={Z1: {(Z1, tmp): (Star, (Z, tmp))}},
        synthesized_rules_functions={Z: {(Z, ast): (Z1, ast)}},
    ),
    p_8: ProductionRules(
        inherited_rules_functions={},
        synthesized_rules_functions={Z: {(Z, ast): (Z, tmp)}},
    ),
    p_9: ProductionRules(
        inherited_rules_functions={},
        synthesized_rules_functions={A: {(A, ast): (E, ast)}},
    ),
    p_10: ProductionRules(
        inherited_rules_functions={},
        synthesized_rules_functions={A: {(A, ast): (Word, (i, "symbol"))}},
    ),
}
symbol = E
