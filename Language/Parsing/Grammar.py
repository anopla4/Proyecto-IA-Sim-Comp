from epsilon import Epsilon
from dollar import Dollar

class Grammar:
    def __init__(self, attributes):
        self.non_terminals = []
        self.terminals = []
        self.productions = []
        self.start_symbol = None
        self.epsilon = Epsilon()
        self.EOF = Dollar()