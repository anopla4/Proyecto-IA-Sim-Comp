from .epsilon import Epsilon
from .non_terminal import NonTerminal
from .dollar import Dollar
from ..utils import all_productions


def symbol_follow(productions, follows, first):
    changed = True
    while changed:
        changed = False
        _productions = all_productions(productions)
        for p in _productions:
            rs = p.right_side
            for i in range(len(rs)):
                a = rs[i]
                x = p.left_side
                if i < len(rs) - 1 and isinstance(a, NonTerminal):
                    z = rs[i + 1]
                    add_to_follow = [
                        item
                        for item in first[z]
                        if not item.symbol == "epsilon"
                        # item for item in first[z] if not isinstance(item, Epsilon)
                    ]
                    for item in add_to_follow:
                        if item not in follows[a]:
                            follows[a].append(item)
                            changed = True
                    if (
                        # len([item for item in first[z] if isinstance(item, Epsilon)])
                        len([item for item in first[z] if item.symbol == "epsilon"])
                        > 0
                    ):
                        for item in follows[x]:
                            if item not in follows[a]:
                                follows[a].append(item)
                                changed = True
                if i == len(rs) - 1 and isinstance(a, NonTerminal):
                    for item in follows[x]:
                        if item not in follows[a]:
                            follows[a].append(item)
                            changed = True


def follow(s, symbols, productions, first, lr=False, GEOF=None):
    res = {item: [] for item in symbols}
    symbol_follow(productions, res, first)
    if lr:
        for key in res:
            res[key].append(GEOF)
    else:
        res[s].append(Dollar())
    return res
