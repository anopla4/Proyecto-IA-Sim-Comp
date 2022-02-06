from Language.Automaton.automaton import Automaton
from .State import State
from pprint import pprint
from .final_state import FinalState


def goto(q_p: set(), transition: str, transition_function: dict):
    go = set()
    for state in q_p:

        if (state, transition) not in transition_function:
            continue
        go = go.union(set(transition_function[(state, transition)]))
    return go


def epsilon_closure(q_p: set, transition_function: dict):
    pending = [
        q_p,
    ]
    closure = q_p
    visited = set()
    while pending:
        st = pending.pop()
        go = goto(st, "epsilon", transition_function)
        closure = closure.union(go)
        for state in go:
            if state not in visited:
                pending.append(set([state]))
                visited.add(state)
    return closure


def transform_nfa_to_dfa(aut: Automaton, lr=False):
    q_dfa = []
    v_dfa = [t for t in aut.characters if t != "epsilon"]
    f_dfa = []
    q_init_dfa = epsilon_closure(set([aut.initial_state]), aut.transition_function)
    transition_function_fda = {}
    state_number = {1: q_init_dfa}
    states = [1]
    visited_states = [q_init_dfa]
    while states:
        number = states.pop(0)
        current_state = state_number[number]
        for transition in v_dfa:
            goto_ = goto(current_state, transition, aut.transition_function)
            if goto_:
                new_state = epsilon_closure(goto_, aut.transition_function)
                if new_state not in visited_states:
                    visited_states.append(new_state)
                    c = len(state_number) + 1
                    q_dfa.append(new_state)
                    states.append(c)
                    transition_function_fda[(number, transition)] = c
                    state_number[c] = new_state
                    inter = new_state.intersection(set(aut.f))
                    if inter and new_state not in f_dfa:
                        f_dfa.append(new_state)
                else:
                    n = [num for num, st in state_number.items() if st == new_state][0]
                    transition_function_fda[(number, transition)] = n
    if lr:
        new_states = [FinalState(state) for state in q_dfa]
        new_transition_function = {
            (new_states[i - 1], transition): new_states[
                transition_function_fda[i, transition] - 1
            ]
            for i, transition in transition_function_fda
        }
        return Automaton(
            new_states, new_states[0], v_dfa, new_states, new_transition_function
        )
    new_states = {state: State() for state in state_number}
    new_transition_function = {}
    final_sets = []
    new_f = []
    c = 0
    for a, b in transition_function_fda:
        c += 1
        st = transition_function_fda[a, b]
        if state_number[st] in f_dfa and state_number[st] not in final_sets:
            final_sets.append(state_number[st])
            new_states[st] = FinalState()
            new_f.append(new_states[st])

        for i in state_number[st]:
            if isinstance(i, FinalState):
                new_states[st].type = new_states[st].type.union(i.type)
    for a, b in transition_function_fda:
        st = transition_function_fda[a, b]
        new_transition_function[new_states[a], b] = new_states[st]
    a = Automaton(
        new_states.values(), new_states[1], v_dfa, new_f, new_transition_function
    )
    return a
