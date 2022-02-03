from Simulation.agent import Agent
from Simulation.environment import Environment
from Simulation.simulation import Simulation
from TreatmentTree.treatmentTree import *

from pprint import pprint

def main(env:Environment, treatment:set[Agent], disease:set[Agent],
    tick:int, end_time:int, simulations:int):
    
    _t_tree = TreatmentTree("")
    for _ in range(simulations):
        _simulation = Simulation(env.copy(), disease=disease, treatment=treatment, end_time=end_time)
        while not _simulation.finish():
            _simulation.simulate(tick=tick)
            _posible_interventions = []
            _posible_interventions.extend(_simulation.detect_new_interventions())
            if _posible_interventions:
                new_tratment = _t_tree.expand_selection(_posible_interventions, _simulation.time)
                _simulation.add_intervention(new_tratment.value)
        _t_tree.back_propagation(_simulation.evaluate_enviroment())
    return _t_tree