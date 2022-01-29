from Language.Automaton.state import State
from Language.Automaton.automaton import Automaton
from .binary_expression import BinaryExpression


class Or(BinaryExpression):
    def __init__(self, left_expr, right_expr) -> None:
        super().__init__("|", 3, left_expr, right_expr)

    def build_automaton(self, left_automaton, right_automaton):
        init_state = State()
        final_state = State()
        states = [init_state, final_state] + left_automaton.states + right_automaton.states
        characters = ["epsilon"] + left_automaton.characters + right_automaton.characters
        characters = list(set(characters))
        transition_function = dict(left_automaton.transition_function.items() + right_automaton.transition_function.items())
        initial_state_left = left_automaton.initial_state
        final_states_left = left_automaton.f
        initial_state_right = right_automaton.initial_state
        final_states_right = right_automaton.f
        init_state.next_states = [initial_state_left, initial_state_right]
        transition_function[(init_state, "epsilon")] = [initial_state_left, initial_state_right]
        for fs in final_states_left:
            transition_function[(fs, "epsilon")] = final_state
        for fs in final_states_right:
            transition_function[(fs, "epsilon")] = final_state

        return Automaton(states, init_state, characters, [final_state], transition_function)