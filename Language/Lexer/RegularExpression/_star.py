from Language.Automaton.automaton import Automaton
from ..expression import Expression


class Star(Expression):
    def __init__(self, expr) -> None:
        super().__init__("*", 1)
        self.expr = expr

    def build_automaton(self, _automaton):
        init_state = _automaton.initial_state
        final_states = _automaton.final_state
        states = _automaton.states
        characters = ["epsilon"] + _automaton.characters
        characters = list(set(characters))
        transition_function = dict(_automaton.transition_function.items())
        for fs in final_states:
            transition_function[(fs, "epsilon")] = [init_state]

        return Automaton(states, init_state, characters, final_states, transition_function)
