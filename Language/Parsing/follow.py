from .epsilon import Epsilon
from .non_terminal import NonTerminal
from .terminal import Terminal
from .dollar import Dollar


def symbol_follow(productions, follows, first):
    changed = True
    while changed:
        changed = False
        all_productions = [i for i in productions.values()]
        _productions = []
        for p in all_productions:
            _productions += p
        for p in _productions:
            non_terminals = [i for i in p.right_side if isinstance(i, NonTerminal)]
            for i in range(len(non_terminals) - 1):
                a = non_terminals[i]
                z = non_terminals[i + 1]
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


def follow(s, symbols, productions, first):
    res = {item: [] for item in symbols}
    symbol_follow(productions, res, first)
    res[s].append(Dollar())
    return res
