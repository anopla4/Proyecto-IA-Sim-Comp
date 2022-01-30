from Language.Automaton.final_state import FinalState
from .token import Token
from Language.Automaton.nfa_to_dfa import transform_nfa_to_dfa

def tokenize_regex_automaton(aut, s):
    aut = transform_nfa_to_dfa(aut)
    count = len(s)
    st = aut.initial_state
    tokens = []
    exp = ""
    while(count):
        if (st, s[len(s)-count]) in aut.transition_function:
            st = aut.transition_function[(st, s[len(s)-count])]
            exp += s[len(s) - count]
            count -= 1
        elif isinstance(st, FinalState):
            tokens.append(Token(exp, st.type))
            exp = ""
            st = aut.initial_state
        else:
            raise Exception("La cadena no pertenece al lenguaje.")

