from Simulation.intervention import Intervention
from Simulation.environment import Environment
from Simulation.simulation import Simulation
from Simulation.symptom import Symptom
from TreatmentTree.treatmentTree import *


def main(env:Environment, treatment:set[Intervention], disease:set[Symptom],
    tick:int, end_time:int, simulations:int):

    _t_tree = TreatmentTree("root")
    for _ in range(simulations):
        _simulation = Simulation(env.copy(), disease=disease, treatment=treatment, end_time=end_time)
        while not _simulation.finish():
            _simulation.simulate(tick=tick)
            _posible_interventions = []
            _posible_interventions.extend(_simulation.detect_new_interventions())
            if _posible_interventions:
                new_tratment = _t_tree.expand_selection(_posible_interventions, _simulation.time)
                new_tratment.update_arrival_state(_simulation.environment_state())
                _simulation.add_intervention(new_tratment.value)
        _t_tree._current.update_final_state(_simulation.environment_state())
        _t_tree.back_propagation(_simulation.evaluate_environment())
    return _t_tree