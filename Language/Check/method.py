class Method:
    def __init__(self, name, return_type, parameters, parameters_type) -> None:
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
        self.parameters_types = parameters_type

    def __str__(self):
        params = ", ".join(
            f"{n}:{t.name}" for n, t in zip(self.parameters, self.parameters_types)
        )
        return f"[method] {self.name}({params}): {self.return_type.name};"

    def __eq__(self, other):
        return (
            other.name == self.name
            and other.return_type == self.return_type
            and other.parameters_type == self.parameters_types
        )
