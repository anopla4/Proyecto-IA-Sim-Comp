from Language.Automaton.automaton import Automaton
from Language.Automaton.final_state import FinalState
from Language.Parsing.Grammar import Grammar
from Language.Parsing.follow import follow
from .Item import Item
from .first import first
from .non_terminal import NonTerminal


def closure(state, firsts, follows, productions, epsilon):
    clos = set(state)

    pending = list(state)
    
    while pending:
        item = pending.pop()
        next_symbol = item.NextSymbol
        if not isinstance(next_symbol, NonTerminal):
            continue
        productions_symbol = productions[next_symbol]
        delta = item.production.right_side[item.pos+1:]
        delta.extend(list(item.lockahead))
        firsts_delta = frozenset()
        stop = False
        index = 0
        while not stop: 
            firsts_delta = firsts_delta.union(frozenset(firsts[delta[index]]))
            index += 1
            if index == len(delta) or isinstance(delta[index], NonTerminal) or not epsilon in follows[delta[index]]:
                stop = True
        for production in productions_symbol:
            new_item = Item(production, 0, firsts_delta)
            if new_item not in clos:
                pending.append(new_item)
                clos.add(new_item)
    return frozenset(clos)

def gotoLR(state, transition):
    items = {item.NextItem() for item in state if transition == item.NextSymbol}
    return frozenset(items)

def build_LR1_automaton(G):
    symbols = list(G.terminals)
    symbols.extend(G.non_terminals)
            
    firsts = first(symbols ,G.productions, G.terminals)
    firsts[G.EOF] = {G.EOF,}  
    follows = follow(G.start_symbol, G.non_terminals, G.productions, firsts, True, G.EOF)

    item = Item(G.productions[G.start_symbol][0], 0, frozenset([G.EOF]))
    items = closure(frozenset([item]), firsts, follows, G.productions, G.epsilon)
    init_state = FinalState(items)
    states = []
    transition_function = {}
    pending = [items]
    visited = {items: init_state}

    while pending:
        items = pending.pop()
        states.append(visited[items])
        for symbol in symbols:
            new_items = gotoLR(items, symbol)
            if new_items:
                closure_ = closure(new_items, firsts, follows, G.productions, G.epsilon)
                if closure_ not in visited:
                    visited[closure_] = FinalState(closure_)
                    pending.append(closure_)
                transition_function[(visited[items], symbol)] = visited[closure_]
    return Automaton(states, init_state, symbols, states, transition_function)

        


