from Language.Automaton.state import State
from Language.Automaton.automaton import Automaton
from ..expression import Expression


class Word(Expression):
    def __init__(self, w) -> None:
        super().__init__(w, 1)

    def build_automaton(self):
        initial_state = State()
        last_state = initial_state
        characters = list(self.regex)
        transition_function = {}
        states = [last_state]
        for i in self.regex:
            st = State()
            states.append(st)
            transition_function[(last_state, i)] = [st]
            last_state = st
        a = Automaton(states, initial_state, characters, [last_state], transition_function)
        return a

