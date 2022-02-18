from typing import Dict, Tuple

from .simulation import Simulation
from .environment import Environment
from .symptom import Symptom
from .intervention import Intervention
from Simulation.FuzzyEngine.fuzzy_engine import FuzzyEngine
from Simulation.FuzzyEngine.rule import Rule

class FuzzySimulation(Simulation):

    def __init__(self, env: Environment, disease: set[Symptom], treatment: set[Intervention], 
        end_time: int, fuzzy_engine:FuzzyEngine):
        super().__init__(env, disease, treatment, end_time=end_time)

        self._fuzzy_engine = fuzzy_engine

    def simulate(self, tick:int):
        '''
        Simulate a time tick
        '''
        self._simulation_time+=tick
        _still_active_symptom:list[Tuple[int,Symptom]] = []
        _action_rules:list[Rule] = []
        for act_time, symptom in self._active_symptoms:
            act_time+=tick
            if act_time == symptom.repetition:
                _action_rules.extend(symptom.action(self._simulation_time, self._env))
                #self._env = symptom.action(self._simulation_time, self._env)
                if not symptom.finish_action():
                    _still_active_symptom.append((0, symptom))
                else:
                    self._inactive_symptoms.add(symptom)
            else:
                _still_active_symptom.append((act_time, symptom))
        self._active_symptoms = _still_active_symptom
        _still_active_intervention:list[Tuple[int,Intervention]] = []
        for act_time, intervention in self._active_intervention:
            act_time+=tick
            if act_time == intervention.repetition:
                _action_rules.extend(intervention.action(self._simulation_time, self._env))
                #self._env = intervention.action(self._simulation_time, self._env)
                if not intervention.finish_action():
                    _still_active_intervention.append((0, intervention))
                else:
                    self._interventions_supply_count[intervention.name]+=1
                    if self._interventions_supply_count[intervention.name] < intervention.supply:
                        self._inactive_intervention.add(intervention)
            else:
                _still_active_intervention.append((act_time, intervention))
        self._env = self._fuzzy_engine.fuzzy_engine(self._env, _action_rules)
        self._active_intervention = _still_active_intervention
        _new_symptoms = self.detect_new_symptoms()
        self._active_symptoms.extend([(0,s) for s in _new_symptoms])
        self._inactive_symptoms.difference_update(_new_symptoms)