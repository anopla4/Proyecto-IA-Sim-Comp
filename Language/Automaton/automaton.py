class Automaton:
    def __init__(self, states, initial_state, characters, final_state, transition_function) -> None:
        self.q = states
        self.initial_state = initial_state
        self.v = characters
        self.f = final_state
        self.transition_function = transition_function
