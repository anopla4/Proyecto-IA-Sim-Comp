from Language.Automaton.final_state import FinalState
from .token import Token
from Language.Automaton.nfa_to_dfa import transform_nfa_to_dfa
from pprint import pprint
from Language.Lexer.RegularExpression.regex_grammar import (
    E,
    X,
    X1,
    T,
    Y,
    Y1,
    F,
    Z,
    Z1,
    A,
    _i,
    _or,
    _concat,
    _star,
    left_br,
    right_br,
    epsilon,
    productions,
    rules,
)
from Language.Lexer.parser_ll import build_ll_table
from Language.Parsing.Grammar_dsl.dsl_grammar import _t
from Language.Lexer.RegularExpression.automaton_builder import build_entire_automaton


def tokenize_regex_automaton(c):
    ll_table = build_ll_table(
        productions,
        [E, X, X1, T, Y, Y1, F, A, Z, Z1],
        [_i, _or, _concat, left_br, right_br, _star, epsilon],
        E,
    )
    aut = build_entire_automaton(
        ll_table,
        E,
        _t,
        _i,
        {"(": left_br, ")": right_br, "|": _or, "U": _concat, "*": _star},
        rules,
    )
    s = ""

    for j in c:
        if j == "\n":
            s += " "
        elif j == "(" or j == ")" or j == "*":
            s += "\\" + j
        else:
            s += j
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
    return tokens
