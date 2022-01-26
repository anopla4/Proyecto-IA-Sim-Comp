from State import State

def goto(q_p: set(State), transition: str, transition_function: dict):
    go = set()
    for state in q_p:
        if (state,transition) not in transition_function:
            continue
        go.union(set(transition_function[(state,transition)]))
    return go

def epsilon_closure(q_p: set, transition_function: dict):
    return q_p.union(goto(q_p, 'epsilon', transition_function))

def transform_nfa_to_dfa(Q: set, q_init, V: list, F: list, transition_function: dict):
    Q_dfa = set()
    V_dfa = [t for t in V if t != 'epsilon']
    F_dfa = []
    new_state = epsilon_closure(q_init, transition_function)
    transition_function_fda = {}
    q_init_dfa = new_state
    states = [q_init_dfa,]
    while states:
        current_state = states.pop(0)
        for transition in V_dfa:
            goto_ = goto(current_state, transition, transition_function)
            if goto_:
                new_state = epsilon_closure(goto_, transition_function)
                Q_dfa.add(new_state)
                states.append(new_state)
                if new_state.intersection(set(F)):
                    F_dfa.append(new_state)
                transition_function_fda[(current_state,transition)] = new_state
    return Q_dfa, q_init_dfa, V_dfa, F_dfa, transition_function_fda