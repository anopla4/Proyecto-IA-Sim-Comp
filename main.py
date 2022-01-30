from rule import Rule
from agent import Agent
from env import Env
from simulation import Simulation
from treatmentTree import *

from pprint import pprint

def main(env:Env, treatment:set[Agent], disease:set[Agent], disease_rules:set[Rule], treatment_rules:set[Rule],
    tick:int, end_time:int, simulations:int):
    
    _t_tree = TreatmentTree("")
    for _ in range(simulations):
        #_current_time = 0
        _simulation = Simulation(env, disease=disease, treatment=treatment, disease_rules=disease_rules, end_time=end_time)
        #_current_node = _t_tree.root
        while not _simulation.finish():
            _simulation.simulate(tick=tick)
            _posible_interventions = [""]
            _posible_interventions.extend(_simulation.detect_new_interventions(treatment_rules))
            _t_tree.expand_selection(_posible_interventions)
        _t_tree.back_propagation()

    pprint(_t_tree)