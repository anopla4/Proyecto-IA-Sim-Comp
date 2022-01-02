class Token:
    def __init__(self, regex, priority) -> None:
        self.regex = regex
        self.priority = priority
