from typing import Dict, Tuple
from .environment import Environment
from .agent import Agent
from FuzzyEngine.fuzzy_engine import FuzzyEngine
from FuzzyEngine.rule import Rule

class Simulation(object):
    def __init__(self, env:Environment, disease:set[Agent],  treatment:set[Agent], 
        fuzzy_engine:FuzzyEngine, end_time:int=0):

        self._env = env
        self._all_symptoms = disease.copy()
        self._active_intervention:list[Tuple[int,Agent]] = []
        self._inactive_intervention:set[Agent] = treatment.copy()
        self._active_symptoms:list[Tuple[int,Agent]] = []
        self._inactive_symptoms:set[Agent] = disease.copy()
        self._simulation_time:int = 0
        self._end_time:int = end_time
        self._fuzzy_engine = fuzzy_engine

    @property
    def time(self)->int:
        return self._simulation_time

    def finish(self) ->bool:
        if self._simulation_time == self._end_time: #or self._env.final_state():
            return True
        return False
    
    def check_environment(self)->int:
        #return -1 if not end, 0 if lose, 1 if win
        return 0 if self._env.final_state() else 1

    def __evaluate_final_state(self)->float:
        val = 0
        for param in self._env.parameters:
            p_max, p_min = param.upp_bad_limit, param.low_bad_limit
            p_center = (param.upp_good_limit - param.low_good_limit)/2*(p_max-p_min)
            p = p_max
            if not param.in_limits:
                p = param.value
            p = p/(p_max-p_min)
            val+= 1/(abs(p-p_center)+1)
        return val

    def evaluate_environment(self)->float:
        if self._env.final_state():
            return self.__evaluate_final_state()
        val = 0
        for param in self._env.parameters:
            if param.in_good_limits:
                val+=1
            else:
                p_max, p_min = param.upp_bad_limit, param.low_bad_limit
                p_center = (param.upp_good_limit - param.low_good_limit)/2*(p_max-p_min)
                p = param.value/(p_max-p_min)
                val+= 1/(abs(p-p_center)+1)
        return val

    def environment_state(self)->Dict[str,float]:
        return self._env.get_params_dict()

    def detect_new_symptom(self)->set[Agent]:
        _new_symptoms:set[Agent] = set()
        for symptom in self._inactive_symptoms:
            if symptom.check_activation_conditions(self._simulation_time, self._env):
                _new_symptoms.add(symptom)
        return _new_symptoms

    def simulate(self, tick:int):
        self._simulation_time+=tick
        _action_rules:list[Rule] = []
        _still_active_symptom:list[Tuple[int,Agent]] = []
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
        _still_active_intervention:list[Tuple[int,Agent]] = []
        for act_time, intervention in self._active_intervention:
            act_time+=tick
            if act_time == intervention.repetition:
                _action_rules.extend(intervention.action(self._simulation_time, self._env))
                #self._env = intervention.action(self._simulation_time, self._env)
                if not intervention.finish_action():
                    _still_active_intervention.append((0, intervention))
                else:
                    self._inactive_intervention.add(intervention)
            else:
                _still_active_intervention.append((act_time, intervention))
        self._env = self._fuzzy_engine.fuzzy_engine(self._env, _action_rules)
        self._active_intervention = _still_active_intervention
        _new_symptoms = self.detect_new_symptom()
        self._active_symptoms.extend([(0,s) for s in _new_symptoms])
        self._inactive_symptoms.difference_update(_new_symptoms)

    def detect_new_interventions(self)-> set[str]:
        _new_interventions:set[str] = set()
        for intervention in self._inactive_intervention:
            if intervention.check_activation_conditions(self._simulation_time, self._env):
                _new_interventions.add(intervention.name)
        return _new_interventions

    def add_intervention(self, new_intervention:str):
        if new_intervention == "":
            return
        temp = None
        for intervention in self._inactive_intervention:
            if intervention.name == new_intervention:
                temp = intervention
                break
        self._active_intervention.append((0,temp))
        self._inactive_intervention.remove(temp)