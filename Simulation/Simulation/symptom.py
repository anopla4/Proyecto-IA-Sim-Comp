from .agent import Agent
from typing import List
from .activation_rule import ActivationRule


class Symptom(Agent):
    def __init__(
        self,
        name: str,
        activation_rules: List[ActivationRule],
        efect_time: int,
        repetition: int,
    ) -> None:
        super().__init__(name, activation_rules, efect_time, repetition)
