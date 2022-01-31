from epsilon import Epsilon
from dollar import Dollar
from production import Production
from non_terminal import NonTerminal
from Language.Lexer.RegularExpression.rule import ProductionRules

class Grammar:
    def __init__(self, non_terminals = [], terminals = [], productions = [], start_symbol = None, productions_rules = {}):
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
        GG_productions = list(G.productions)
        init_production = Production(S, G.start_symbol)
        GG_productions.append(init_production)
        GG_start_symbol = S
        GG_rules = dict(G.rules)
        GG_rules[init_production] = ProductionRules(inherited_rules_functions={},
        synthesized_rules_functions={S: {(S, ast): (E, ast)}},)

        return Grammar(GG_non_terminals, GG_terminals, GG_productions, GG_start_symbol, productions_rules = GG_rules)