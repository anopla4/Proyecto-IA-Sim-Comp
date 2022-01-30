from typing import Tuple
from env import Env
from agent import Agent
from rule import Rule

class Simulation(object):
    def __init__(self, env:Env, disease:set[Agent],  treatment:set[Agent], #disease_rules:set[Rule], 
    end_time:int=0):
        self._env = env
        self._all_symptoms = disease
        self._active_intervention:list[Tuple[int,Agent]] = []
        self._inactive_intervention:set[Agent] = treatment.copy()
        self._active_symptoms:list[Tuple[int,Agent]] = []
        self._inactive_symptoms:set[Agent] = disease.copy()
        #self._disease_rules:set[Rule] = disease_rules
        self._simulation_time:int = 0
        self._end_time:int = end_time

    def finish(self) ->bool:
        if self._env.final_state() or self._simulation_time == self._end_time:
            return True
        return False
    
    def check_enviroment(self)->bool:
        #return -1 if not end, 0 if lose, 1 if win
        return -1 if self._env.final_state() else 1 

    def detect_new_symptom(self)->set[Agent]:
        _new_symptoms:set[Agent] = set()
        for symptom in self._inactive_symptoms:
            if symptom.check_activation_conditions(self._current_time, self._env):
                _new_symptoms.add(symptom)
        return _new_symptoms

    def simulate(self, tick:int):
        self._current_time+=tick
        _still_active_symptom:list[Tuple[int,Agent]] = []
        for act_time, symptom in self._active_symptom:
            act_time+=tick
            if act_time == symptom.repetition:
                env = symptom.action(self._simulation_time, env)
            if not symptom.finish_action():
                _still_active_symptom.append((0, symptom))
            else:
                self._inactive_symptoms.add(symptom)
        self._active_symptom = _still_active_symptom
        _still_active_intervention:list[Tuple[int,Agent]] = []
        for act_time, intervention in self._active_intervention:
            act_time+=tick
            if act_time == intervention.repetition:
                env = intervention.action(self._simulation_time, env)
            if not intervention.finish_action():
                _still_active_intervention.append((0, intervention))
            else:
                self._inactive_intervention.add(intervention)
        self._active_intervention = _still_active_intervention
        _new_symptoms = self.detect_new_symptom(env)
        self._active_symptoms.extend([(0,s) for s in _new_symptoms])
        self._inactive_symptoms.difference_update(_new_symptoms)

    def detect_new_interventions(self, treatment_rules:set[Rule]) -> set[Agent]:
        _new_interventions:set[Agent] = set()
        for intervention in self._inactive_intervention:
            if intervention.check_activation_conditions(self._current_time, self._env):
                _new_interventions.add(intervention)
        return _new_interventions

    def add_intervention(self, intervention:Agent):
        self._active_intervention.append((0,intervention))
        self._inactive_intervention.remove(intervention)