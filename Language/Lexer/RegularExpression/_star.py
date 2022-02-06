from pprint import pprint
from Language.Automaton.automaton import Automaton
from ..expression import Expression
from Language.Automaton.state import State


class Star(Expression):
    def __init__(self, expr) -> None:
        super().__init__("*", 1)
        self.expr = expr

    def build_automaton(self, _automaton: Automaton):
        init_state = State()
        final_state = State()
        final_states = [final_state]
        states = _automaton.states + [init_state, final_state]
        characters = ["epsilon"] + _automaton.characters
        characters = list(set(characters))
        transition_function = dict(_automaton.transition_function.items())
        transition_function[(init_state, "epsilon")] = [
            final_state,
            _automaton.initial_state,
        ]
        for fs in _automaton.f:
            transition_function[(fs, "epsilon")] = [
                final_state,
                _automaton.initial_state,
            ]
        return Automaton(
            states, init_state, characters, final_states, transition_function
        )
