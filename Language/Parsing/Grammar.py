from .epsilon import Epsilon
from .dollar import Dollar
from .production import Production
from .non_terminal import NonTerminal


class Grammar:
    def __init__(
        self,
        non_terminals=None,
        terminals=None,
        productions=None,
        start_symbol=None,
        productions_rules=None,
    ):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.epsilon = Epsilon()
        self.EOF = Dollar()
        self.rules = productions_rules

    @staticmethod
    def augment(G):
        S = NonTerminal("S")
        GG_non_terminals = list(G.non_terminals)
        GG_non_terminals.append(S)
        GG_terminals = G.terminals
        GG_productions = dict(G.productions)
        init_production = Production(S, [G.start_symbol])
        GG_productions[S] = [init_production]
        GG_start_symbol = S
        GG_rules = dict(G.rules)
        GG_rules[init_production] = lambda h, s: s[1]
        GG = Grammar(
            GG_non_terminals,
            GG_terminals,
            GG_productions,
            GG_start_symbol,
            productions_rules=GG_rules,
        )
        GG.EOF = G.EOF
        GG.epsilon = G.epsilon
        return GG
