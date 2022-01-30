from Item import Item
from Language.Automaton.automaton import Automaton
from Language.Automaton.nfa_to_dfa import transform_nfa_to_dfa
def build_lr0_automaton(self,G):
    assert len([production for production in G.productions if production.left_side == G.start_symbol]) == 1, "The grammar must be augmented"

    states = set()
    transitions = {}
    characters = set()
    characters.add('epsilon')
    initial_state = Item([production for production in G.productions if production.left_side == G.start_symbol][0],0)

    stack = [initial_state,]

    while stack:
        current_state = stack.pop()

        states.add(current_state)

        next_symbol = current_state.NextSymbol
        characters.add(next_symbol)
        next_state = current_state.NextItem()

        if (current_state, next_symbol) not in transitions:
            transitions[(current_state, next_symbol)] = []
        transitions[(current_state, next_symbol)].append(next_state)
        stack.append(next_state)

        if isinstance(next_symbol, NonTerminal):
            for production in G.productions:
                if production.left_side == next_symbol:
                    if (state,'epsilon') not in transitions:
                        transitions[(state, 'epsilon')] = []
                    next_state = Item(production,0)
                    transitions[(state, 'epsilon')].append(next_state)    
                    stack.append(next_state)
    return transform_nfa_to_dfa(Autmaton(list(states),initial_state,characters,list(states),transitions))