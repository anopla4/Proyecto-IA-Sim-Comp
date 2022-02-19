from Simulation.Simulation.intervention import Intervention
from Simulation.Simulation.environment import Environment
from Simulation.Simulation.simulation import Simulation
from Simulation.Simulation.fuzzy_simulation import FuzzySimulation
from Simulation.Simulation.symptom import Symptom
from Simulation.TreatmentTree.treatmentTree import *
from Simulation.FuzzyEngine.fuzzy_engine import FuzzyEngine


def simulate(
    env: Environment,
    treatment: list[Intervention],
    disease: list[Symptom],
    tick: int,
    end_time: int,
    simulations: int,
    fuzzy_engine: FuzzyEngine = None,
):
    treatment = set(treatment)
    disease = set(disease)
    _t_tree = TreatmentTree("root")
    for _ in range(simulations):
        _simulation = None
        if fuzzy_engine != None:
            _simulation = FuzzySimulation(
                env.copy(),
                disease=disease,
                treatment=treatment,
                end_time=end_time,
                fuzzy_engine=fuzzy_engine,
            )
        else:
            _simulation = Simulation(
                env.copy(), disease=disease, treatment=treatment, end_time=end_time
            )
        while not _simulation.finish():
            _simulation.simulate(tick=tick)
            _posible_interventions = []
            _posible_interventions.extend(_simulation.detect_new_interventions())
            if _posible_interventions:
                new_tratment = _t_tree.expand_selection(
                    _posible_interventions, _simulation.time
                )
                new_tratment.update_arrival_state(_simulation.environment_state())
                _simulation.add_intervention(new_tratment.value)
        _t_tree._current.update_final_state(_simulation.environment_state())
        _t_tree.back_propagation(_simulation.evaluate_environment())
    _t_tree.calculate_probability()
    _t_tree.prunning()
    return _t_tree
