from typing import Dict, Tuple


class Rule:
    def __init__(
        self,
        parameters_conditions: Dict[str, str],
        destination: str,
        then: Tuple[str, str],
    ):
        self._parameters_conditions = parameters_conditions
        self._destination = destination
        self.then = then

    @property
    def target(self) -> str:
        return self.then[0]

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def conditions(self) -> Dict[str, str]:
        return self._parameters_conditions

    def __str__(self) -> str:
        s = ""
        for param, value in self._parameters_conditions.items():
            s += f"{param}:{value}  "
        s += f" destination:{self._destination}  "
        s += f"target:{self.then[0]}"
        return s
