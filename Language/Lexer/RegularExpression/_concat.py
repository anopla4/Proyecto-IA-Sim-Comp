from .binary_expression import BinaryExpression
from Language.Automaton.automaton import Automaton


class Concat(BinaryExpression):
    def __init__(self, left_expr, right_expr) -> None:
        super().__init__("U", 2, left_expr, right_expr)

    def build_automaton(self, left_automaton, right_automaton):
        init_state = left_automaton.initial_state
        final_state = right_automaton.f
        states = left_automaton.states + right_automaton.states
        characters = (
            ["epsilon"] + left_automaton.characters + right_automaton.characters
        )
        characters = list(set(characters))
        transition_function = dict(
            list(left_automaton.transition_function.items())
            + list(right_automaton.transition_function.items())
        )
        final_states_left = left_automaton.f
        initial_state_right = right_automaton.initial_state
        for fs in final_states_left:
            transition_function[(fs, "epsilon")] = [initial_state_right]

        return Automaton(
            states, init_state, characters, final_state, transition_function
        )
