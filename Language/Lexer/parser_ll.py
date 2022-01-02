from Language.Parsing.terminal import Terminal
from ..Parsing.epsilon import Epsilon
from ..Parsing.first import first
from ..Parsing.follow import follow


def build_ll_table(productions, non_terminals, terminals, symbol):
    _first = first(non_terminals, productions, terminals)
    _follow = follow(symbol, non_terminals, productions, _first)
    ll_table = {nt: {t: None for t in terminals} for nt in non_terminals}
    for nt in non_terminals:
        for p in productions[nt]:
            w = p.right_side[0]
            if not isinstance(w, Epsilon):
                if isinstance(w, Terminal):
                    if ll_table[nt][w] != None:
                        raise Exception("Ambiguity")
                    ll_table[nt][w] = p
                else:
                    for t in _first[w]:
                        if ll_table[nt][t] != None:
                            raise Exception("Ambiguity")
                        ll_table[nt][t] = p
            else:
                for t in _follow[nt]:
                    if ll_table[nt][t] != None:
                        raise Exception("Ambiguity")
                    ll_table[nt][t] = p
    return ll_table
