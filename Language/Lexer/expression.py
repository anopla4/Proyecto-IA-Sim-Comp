class Expression:
    def __init__(self, regex, priority) -> None:
        self.regex = regex
        self.priority = priority

    def build_automaton(self, *args, **kwargs):
        pass
