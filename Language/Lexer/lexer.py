from Language.Automaton.final_state import FinalState
from .token import Token
from Language.Automaton.nfa_to_dfa import transform_nfa_to_dfa
from Language.Lexer.RegularExpression.regex_grammar import (
    regex_grammar,
)
from Language.Lexer.parser_ll import build_ll_table

from Language.Lexer.RegularExpression.automaton_builder import build_entire_automaton


def tokenize_regex_automaton(c, _t):
    G, _i, left_br, right_br, _or, _concat, _star = regex_grammar()
    ll_table = build_ll_table(
        G.productions,
        G.non_terminals,
        G.terminals,
        G.start_symbol,
    )

    aut = build_entire_automaton(
        ll_table,
        G.start_symbol,
        _t,
        _i,
        {"(": left_br, ")": right_br, "|": _or, "+": _concat, "*": _star},
        G.rules,
    )
    s = ""

    for j in c:
        if j == "\n":
            s += " "
        elif j == "(" or j == ")" or j == "*" or j == "+":
            s += "\\" + j
        else:
            s += j
    aut = transform_nfa_to_dfa(aut)
    count = len(s)
    st = aut.initial_state
    tokens = []
    exp = ""
    h = 0
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
            if count == 0:
                if isinstance(st, FinalState):
                    maximum = 0
                    t = None
                    for i in st.type:
                        if maximum < i[1]:
                            maximum = max(maximum, i[1])
                            t = i
                    tokens.append(Token(exp, t))
                else:
                    raise Exception("La cadena no pertenece al lenguaje.")
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
        h += 1
    return tokens
