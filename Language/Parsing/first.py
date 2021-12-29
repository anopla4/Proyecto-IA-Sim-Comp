from epsilon import Epsilon
from non_terminal import NonTerminal
from terminal import Terminal


def symbol_first(alph_sym, productions, firsts):
    if firsts[alph_sym]:
        return
    for p in productions[alph_sym]:
        new_symbol = p.right_side[0]
        if isinstance(new_symbol, Terminal) or isinstance(new_symbol, Epsilon):
            firsts[alph_sym].append(new_symbol)
        elif isinstance(new_symbol, NonTerminal):
            symbol_first(new_symbol, productions, firsts)
            firsts[alph_sym] += firsts[new_symbol]
            if (
                len(list(filter(lambda x: isinstance(x, Epsilon), firsts[alph_sym])))
                > 0
            ):
                new_symbol = p.right_side[1]
                symbol_first(new_symbol, productions, firsts)
                firsts[alph_sym] += firsts[new_symbol]


def first(symbols, productions):
    res = {item: [] for item in symbols}
    for s in symbols:
        symbol_first(s, productions, res)
    return {i.symbol: [j.symbol for j in res[i]] for i in res}
