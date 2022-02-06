from .epsilon import Epsilon
from .non_terminal import NonTerminal
from .terminal import Terminal
from ..utils import all_productions


def symbol_first(productions, firsts):
    changed = True
    _productions = all_productions(productions)
    while changed:
        changed = False
        for p in _productions:
            x = p.left_side
            w = p.right_side[0]
            # if isinstance(w, Terminal) or isinstance(w, Epsilon):
            if isinstance(w, Terminal) or w.symbol == "epsilon":
                if w not in firsts[x]:
                    firsts[x].append(w)
                    changed = True
            elif isinstance(w, NonTerminal):
                for item in firsts[w]:
                    if item in firsts[x]:
                        continue
                    firsts[x].append(item)
                    changed = True

                if (
                    # len(list(filter(lambda x: isinstance(x, Epsilon), firsts[x]))) > 0
                    len(list(filter(lambda x: x.symbol == "epsilon", firsts[x]))) > 0
                    and len(p.right_side) > 0
                ):
                    z = p.right_side[1]
                    for item in firsts[z]:
                        if item in firsts[x]:
                            continue
                        firsts[x].append(item)
                        changed = True


def first(symbols, productions, terminals):
    res = {item: [] for item in symbols}
    res = dict(list(res.items()) + [(item, [item]) for item in terminals])
    symbol_first(productions, res)

    return res
