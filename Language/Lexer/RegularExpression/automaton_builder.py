from Language.Automaton.automaton import Automaton
from Language.Automaton.State import State
from Language.Automaton.final_state import FinalState
from Language.Lexer.RegularExpression.word import Word
from Language.Lexer.RegularExpression._or import Or
from Language.Lexer.RegularExpression._concat import Concat
from Language.Lexer.RegularExpression._star import Star
from .ast import build_ast
from ..tokenizer import tokenize


def build_automaton_(ast):
    if ast == None:
        return
    if isinstance(ast, Word):
        return ast.build_automaton()
    if isinstance(ast, Star):
        aut = build_automaton_(ast.expr)
        return ast.build_automaton(aut)
    if isinstance(ast, Or):
        left = build_automaton_(ast.left_expr)
        right = build_automaton_(ast.right_expr)
        return ast.build_automaton(left, right)
    if isinstance(ast, Concat):
        left = build_automaton_(ast.left_expr)
        right = build_automaton_(ast.right_expr)
        return ast.build_automaton(left, right)
    return


def build_automaton_expression(ast, t):
    aut = build_automaton_(ast)
    transition_function = {}
    f = []
    new_states = {st: None for st in aut.states}
    for i in aut.states:
        if i in aut.f:
            new_final_state = FinalState()
            new_final_state.type.add(t)
            f.append(new_final_state)
            new_states[i] = new_final_state
        else:
            new_states[i] = i
    for (item, c), value in aut.transition_function.items():
        new_item = new_states[item]
        new_value = [new_states[i] for i in value]
        transition_function[(new_item, c)] = new_value
    aut.transition_function = transition_function
    aut.f = f
    aut.states = new_states.values()
    aut.initial_state = new_states[aut.initial_state]
    return aut


def build_entire_automaton(ll_table, sym, expressions, word_type, types, rules=None):
    automatons = []
    transition_function = []
    characters = []
    final_states = []
    states = []
    for exp in expressions:
        t = tokenize(exp, word_type, types)
        ast = build_ast(ll_table, t, sym, rules)

        _aut = build_automaton_expression(ast.ast, expressions[exp])
        transition_function += list(_aut.transition_function.items())
        characters += _aut.characters
        states += _aut.states
        final_states += _aut.f
        automatons.append(_aut)
    init_state = State()
    states.append(init_state)
    transition_function = dict(transition_function)
    transition_function[(init_state, "epsilon")] = []
    for a in automatons:
        transition_function[(init_state, "epsilon")].append(a.initial_state)
    return Automaton(
        states, init_state, set(characters), final_states, transition_function
    )
