from .Item import Item
from Language.Automaton.automaton import Automaton
from Language.Automaton.nfa_to_dfa import transform_nfa_to_dfa
from .non_terminal import NonTerminal
from .terminal import Terminal
from Language.Automaton.final_state import FinalState


def build_lr0_automaton(G):
    assert len(G.productions[G.start_symbol]) == 1, "The grammar must be augmented"

    states = set()
    transitions = {}
    characters = set()
    characters.add('epsilon')
    initial_state = Item(G.productions[G.start_symbol][0],0)
    visited = {initial_state : FinalState(initial_state)}
    stack = [initial_state,]
    initial_state = visited[initial_state]
    
    while stack:
        current_state = stack.pop()
        if current_state.IsReduceItem:
            continue
        if current_state in states:
            continue
        states.add(visited[current_state])

        next_symbol = current_state.NextSymbol
        characters.add(next_symbol)
        next_state = current_state.NextItem()

        if (visited[current_state], next_symbol) not in transitions:
            transitions[(visited[current_state], next_symbol)] = []
        if next_state not in visited:
            stack.append(next_state)
            visited[next_state] = FinalState(next_state)
        transitions[(visited[current_state], next_symbol)].append(visited[next_state])

        if isinstance(next_symbol, NonTerminal):
            for symbol in G.productions:
                if symbol == next_symbol:
                    if (visited[current_state],'epsilon') not in transitions:
                            transitions[(visited[current_state], 'epsilon')] = []
                    for production in G.productions[symbol]:
                        next_state = Item(production,0)
                        if next_state not in visited:
                            stack.append(next_state)
                            visited[next_state] = FinalState(next_state)
                        transitions[(visited[current_state], 'epsilon')].append(visited[next_state])    
    
    return transform_nfa_to_dfa(Automaton(list(states),initial_state,characters,list(states),transitions), True)