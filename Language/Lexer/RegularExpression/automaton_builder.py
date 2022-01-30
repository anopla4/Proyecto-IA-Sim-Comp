from Language.Automaton.automaton import Automaton
from Language.Automaton.state import State
from Language.Automaton.final_state import FinalState
from Language.Lexer.RegularExpression.word import Word
from Language.Lexer.RegularExpression._or import Or
from Language.Lexer.RegularExpression._concat import Concat
from Language.Lexer.RegularExpression._star import Star
from .ast import build_ast

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
    aut.f = FinalState(t)

def build_entire_automaton(ll_table, s, sym, expressions, rules=None):
    automatons = []
    transition_function = []
    characters = []
    final_states = []
    states = []
    for exp in expressions:
        ast = build_ast(ll_table, s, sym, rules)
        _aut = build_automaton_expression(ast, expressions[exp])
        transition_function += _aut.transition_function.items()
        characters += _aut.characters
        states += _aut.states
        final_states.append(_aut.final_state)
        automatons.append(_aut)
    init_state = State()
    states.append(init_state)
    transition_function[(init_state, "epsilon")] = []
    for a in automatons:
        transition_function[(init_state, "epsilon")].append(a.initial_state)
    return Automaton(states, init_state, characters, final_states, dict(transition_function))
