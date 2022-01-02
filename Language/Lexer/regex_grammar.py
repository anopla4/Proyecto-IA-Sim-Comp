from ..Parsing.non_terminal import NonTerminal
from ..Parsing.terminal import Terminal
from ..Parsing.production import Production
from ..Parsing.epsilon import Epsilon

E = NonTerminal("E")
X = NonTerminal("X")
T = NonTerminal("T")
Y = NonTerminal("Y")
F = NonTerminal("F")
Z = NonTerminal("Z")
i = Terminal("i")
_or = Terminal("|")
_concat = Terminal("U")
_star = Terminal("*")
left_br = Terminal("(")
right_br = Terminal(")")
epsilon = Epsilon()
productions = {
    E: [Production(E, [T, X])],
    X: [Production(X, [_or, T, X]), Production(X, [epsilon])],
    T: [Production(T, [F, Y])],
    Y: [Production(Y, [_concat, F, Y]), Production(Y, [epsilon])],
    F: [Production(F, [_star, Z]), Production(F, [epsilon])],
    Z: [Production(Z, [left_br, E, right_br]), Production(Z, [i])],
}
terminals = [i, _or, _concat, _star, left_br, right_br, epsilon]
non_terminals = [E, X, T, Y, F, Z]
symbol = E
