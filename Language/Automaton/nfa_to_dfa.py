from pprint import pprint
from Language.Automaton.automaton import Automaton
from .state import State
from .final_state import FinalState


def goto(q_p: set(), transition: str, transition_function: dict):
    go = set()
    for state in q_p:
        if (state, transition) not in transition_function:
            continue
        go = go.union(set(transition_function[(state, transition)]))
    return go


def epsilon_closure(q_p: set, transition_function: dict):
    go = goto(q_p, 'epsilon', transition_function)
    sol = q_p.union(go)
    while go:
        go = goto(go, "epsilon", transition_function)
        sol = sol.union(go)
    return sol


def transform_nfa_to_dfa(aut: Automaton):
    q_dfa = []
    v_dfa = [t for t in aut.characters if t != 'epsilon']
    f_dfa = []
    q_init_dfa = epsilon_closure(
        set([aut.initial_state]), aut.transition_function)
    transition_function_fda = {}
    state_number = {1: q_init_dfa}
    states = [1]
    visited_states = [q_init_dfa]
    while states:
        number = states.pop(0)
        current_state = state_number[number]
        visited_states.append(current_state)
        for transition in v_dfa:
            goto_ = goto(current_state, transition, aut.transition_function)
            if goto_:
                new_state = epsilon_closure(goto_, aut.transition_function)
                if new_state not in visited_states:
                    c = len(state_number) + 1
                    q_dfa.append(new_state)
                    states.append(c)
                    transition_function_fda[(number, transition)] = c
                    state_number[c] = new_state
                else:
                    n = [num for num, st in state_number.items() if st ==
                         new_state][0]
                    transition_function_fda[(number, transition)] = n
                if new_state.intersection(set(aut.f)):
                    f_dfa.append(new_state)
    new_states = {state: State() for state in state_number}
    new_transition_function = {}
    new_f = []
    for a, b in transition_function_fda:
        st = transition_function_fda[a, b]
        for i in state_number[st]:
            if isinstance(i, FinalState):
                new_states[st] = FinalState()
                new_states[st].type += i.type
                new_f.append(new_states[st])
                break
    for a, b in transition_function_fda:
        st = transition_function_fda[a, b]
        new_transition_function[new_states[a], b] = new_states[st]
    a = Automaton(new_states.values(),
                  new_states[1], v_dfa, new_f, new_transition_function)
    return a
