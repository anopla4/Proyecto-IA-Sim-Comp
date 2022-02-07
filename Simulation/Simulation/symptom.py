from .agent import Agent
from .activation_rule import ActivationRule

class Symptom(Agent):

    def __init__(self, name: str, activation_rules: list[ActivationRule], 
        efect_time:int, repetition:int) -> None:
        super().__init__(name, activation_rules, efect_time, repetition)