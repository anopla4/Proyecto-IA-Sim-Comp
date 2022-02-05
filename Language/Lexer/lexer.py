from Language.Automaton.final_state import FinalState
from .token import Token
from Language.Automaton.nfa_to_dfa import transform_nfa_to_dfa
from pprint import pprint


def tokenize_regex_automaton(aut, s):
    aut = transform_nfa_to_dfa(aut)
    count = len(s)
    st = aut.initial_state
    tokens = []
    exp = ""
    while count >= 0:
        if count == 0:
            break
        if (
            count > 0
            and st == aut.initial_state
            and s[len(s) - count] == " "
            and (st, " ") not in aut.transition_function
        ):
            count -= 1

        elif count > 0 and (st, s[len(s) - count]) in aut.transition_function:
            st = aut.transition_function[(st, s[len(s) - count])]
            exp += s[len(s) - count]
            count -= 1
        elif isinstance(st, FinalState):
            maximum = 0
            t = None
            for i in st.type:
                if maximum < i[1]:
                    maximum = max(maximum, i[1])
                    t = i
            tokens.append(Token(exp, t))
            st = aut.initial_state
            exp = ""
        else:
            raise Exception("La cadena no pertenece al lenguaje.")
    return tokens
