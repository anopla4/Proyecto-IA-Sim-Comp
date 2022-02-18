from .agent import Agent
from typing import List
from .activation_rule import ActivationRule


class Intervention(Agent):
    def __init__(
        self,
        name: str,
        activation_rules: List[ActivationRule],
        efect_time: int,
        repetition: int,
        action,
        supply: int,
    ) -> None:
        super().__init__(name, activation_rules, efect_time, repetition, action)
        self._supply = supply

    @property
    def supply(self):
        """
        Returns the supply of current intervention
        """
        return self._supply
