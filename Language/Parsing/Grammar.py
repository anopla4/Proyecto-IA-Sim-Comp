from epsilon import Epsilon
from dollar import Dollar

class Grammar:
    def __init__(self, non_terminals = [], terminals = [], productions = [], start_symbol = None, productions_rules = {}):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.epsilon = Epsilon()
        self.EOF = Dollar()
        self.rules = productions_rules