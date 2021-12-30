from .epsilon import Epsilon
from .non_terminal import NonTerminal
from .terminal import Terminal


def symbol_first(productions, firsts):
    changed = True
    while changed:
        changed = False
        all_productions = [i for i in productions.values()]
        _productions = []
        for p in all_productions:
            _productions += p

        for p in _productions:
            x = p.left_side
            w = p.right_side[0]
            if isinstance(w, Terminal) or isinstance(w, Epsilon):
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
                    len(list(filter(lambda x: isinstance(x, Epsilon), firsts[x]))) > 0
                    and len(p.right_side) > 0
                ):
                    z = p.right_side[1]
                    for item in firsts[z]:
                        if item in firsts[x]:
                            continue
                        firsts[x].append(item)
                        changed = True


def first(symbols, productions):
    res = {item: [] for item in symbols}
    symbol_first(productions, res)
    return res
