class Automaton:
    def __init__(self, states, initial_state, characters, final_states, transition_function) -> None:
        self.states = states
        self.initial_state = initial_state
        self.characters = characters
        self.f = final_states
        self.transition_function = transition_function
