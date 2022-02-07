from Grammar import Grammar
from buildLRAutomaton import build_lr0_automaton
from first import first
from follow import follow
from non_terminal import NonTerminal
from terminal import Terminal

class ShiftReduceParser:
    SHIFT = "Shift"
    REDUCE = "Reduce"
    OK = "OK"
    
    def __init__(self,G):
        self.G = G
        self.goto = {}
        self.action = {}
        self.build_parser_table()
    
    def build_parser_table(self):
        Augmented_G = Grammar.augment(G)
        automaton = build_lr0_automaton(Augmented_G)

        firsts = first(G.characters,G.productions, G.terminals)
        follows = follow(G.start_symbol, G.characters, G.productions, firsts)

        for i,state in enumerate(automaton.q):
            for item in state:
                if item.IsReduceItem:
                    if item.production.left_side == G.start_symbol:
                        assert (i,G.EOF) not in self.action or self.action[(i,G.EOF)] == (ShiftReduceParser.OK, None), 'Shift-Reduce or Reduce-Reduce conflict'
                        self.action[(i,G.EOF)] = (ShiftReduceParser.OK, None)
                    for symbol in follow[item.production.left_side]:
                        assert (i,symbol) not in self.action or self.action[(i,symbol)] == (ShiftReduceParser.REDUCE, item.production), 'Shift-Reduce or Reduce-Reduce conflict'
                        self.action[(i,symbol)] = (ShiftReduceParser.REDUCE, item.production)
                else:
                    next_symbol = item.next_symbol
                    next_state_index = automaton.q.index(automaton.transition_function[(state,next_symbol)])
                    if isinstance(next_symbol, Terminal):
                        assert (i,next_symbol) not in self.action or self.action[(i,next_symbol)] == (ShiftReduceParser.SHIFT, next_state_index), 'Shift-Reduce conflict!!!'
                        self.action[(i,next_symbol)] = (ShiftReduceParser.SHIFT, next_state_index)
                    else:
                        assert (i,next_symbol) not in self.goto or self.goto[(i,next_symbol)] == next_state_index, 'Shift-Reduce or Reduce-Reduce conflict!!!'
                        self.goto[(i,next_symbol)] = next_state_index

    def __call__(self, w):
        stack = [0,]
        result = []
        actions = []
        index = 0

        while True:
            state = stack[-1]
            lookahead = w[index]

            if (state,lookahead) not in self.action:
                return None
            
            action, tag = self.action[(state,lookahead)]

            if action ==  ShiftReduceParser.SHIFT:
                stack.append(tag)
                actions.append(action)
                cursor += 1
            elif action == ShiftReduceParser.REDUCE:
                for _ in range(len(tag.right_side)):
                    stack.pop()
                stack.append(self.goto[stack[-1],tag.left_side])
                actions.append(action)
                result.append(tag)
            elif action == ShiftReduceParser.OK:
                return result,actions
            else:
                return ValueError("Not valid action")

                