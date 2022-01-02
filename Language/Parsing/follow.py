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
            for i in range(len(rs) - 1):
                a = rs[i]
                if not isinstance(a, NonTerminal):
                    continue
                z = rs[i + 1]
                x = p.left_side
                add_to_follow = [
                    item for item in first[z] if not isinstance(item, Epsilon)
                ]
                for item in add_to_follow:
                    if item not in follows[a]:
                        follows[a].append(item)
                        changed = True
                if len([item for item in first[z] if isinstance(item, Epsilon)]) > 0:
                    for item in follows[x]:
                        if item not in follows[a]:
                            follows[a].append(item)
                            changed = True
                if i + 1 == len(rs) - 1 and isinstance(z, NonTerminal):
                    for item in follows[x]:
                        if item not in follows[z]:
                            follows[z].append(item)
                            changed = True


def follow(s, symbols, productions, first):
    res = {item: [] for item in symbols}
    symbol_follow(productions, res, first)
    res[s].append(Dollar())
    return res
