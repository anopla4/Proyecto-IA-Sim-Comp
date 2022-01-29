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
        final_state_left = left_automaton.f
        initial_state_right = right_automaton.initial_state
        final_state_right = right_automaton.f
        init_state.next_states = [initial_state_left, initial_state_right]
        transition_function[(init_state, "epsilon")] = [initial_state_left, initial_state_right]
        final_state_left.next_states.append(final_state)
        transition_function[(final_state_left, "epsilon")] = [final_state]
        final_state_right.next_states.append(final_state)
        transition_function[(final_state_right, "epsilon")] = [final_state]

        return Automaton(states, init_state, characters, final_state, transition_function)