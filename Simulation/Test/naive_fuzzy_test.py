from Simulation.environment import Environment
from Simulation.symptom import Symptom
from Simulation.intervention import Intervention
from Simulation.parameter import Parameter
from Simulation.activation_rule import ActivationRule
from FuzzyEngine.MembresyFunctions.triangular import Triangular
from FuzzyEngine.MembresyFunctions.trapezoidal import Trapezoidal
from .DiseaseBank.fuzzy_actions import *
from .TreatmentBank.fuzzy_actions import *
from FuzzyEngine.fuzzy_engine import FuzzyEngine

def naive_fuzzy_test(simulation_main, tick=1, end_time=168, simulations=5000):
    
    p_increase = Parameter(
        name = 'increase', value = 0,
        membresy_functions={'low': Triangular(0,0,0.3),
                            'medium':Trapezoidal(0.2,0.3,0.5,0.6),
                            'high':Triangular(0.5,1,1)},
                low_good_limit=0, upp_good_limit=1,
                low_bad_limit=0, upp_bad_limit=1
            )

    p_decrease=Parameter(
        name= 'decrease', value=0,
        membresy_functions={'low': Triangular(0,0,0.3),
                            'medium':Trapezoidal(0.2,0.3,0.5,0.6),
                            'high':Triangular(0.5,1,1)},
                low_good_limit=0, upp_good_limit=1,
                low_bad_limit=0, upp_bad_limit=1
            )

    p_plaqueta = Parameter(
        name='plaqueta', value=14, 
        membresy_functions={'baja':Trapezoidal(0,0,18,24),
                            'media':Trapezoidal(20,22,28,35),
                            'alta':Trapezoidal(32,38,50,50)},
        low_good_limit=20, upp_good_limit=38,
        low_bad_limit=0, upp_bad_limit=50
        )

    p_tos = Parameter(
        name='tos', value=23, 
        membresy_functions={'baja':Triangular(0,0,15),
                            'media':Triangular(9,15,24),
                            'alta':Triangular(15,26,30)},
        low_good_limit=0, upp_good_limit=15,
        low_bad_limit=-1e9, upp_bad_limit=40
        )

    p_temperatura = Parameter(
        name='temperatura', value=37.1, 
        membresy_functions={'baja':Triangular(34,34,36),
                            'media':Triangular(35,36,37),
                            'alta':Trapezoidal(36.8,38,40,42),
                            'muy alta':Triangular(40,44,44)},
        low_good_limit=35, upp_good_limit=36.8,
        low_bad_limit=34, upp_bad_limit=43
    )

    tos_rule = ActivationRule(parameters_conditions={p_plaqueta:(-1e9,20)}, time_condition=(0,1e9))
    tos = Symptom(name="tos",activation_rules=[tos_rule], efect_time=48, repetition=8)
    tos.inner_action = tos_action

    fiebre_rule = ActivationRule(parameters_conditions={p_plaqueta:(-1e9,18)}, time_condition=(0,1e9))
    fiebre = Symptom(name='fiebre',activation_rules=[fiebre_rule], efect_time=48, repetition=12)
    fiebre.inner_action = fiebre_action

    antibiotico_rule1 = ActivationRule(parameters_conditions={p_temperatura:(37, 100)}, time_condition=(0,1e9))
    antibiotico_rule2 = ActivationRule(parameters_conditions={p_plaqueta:(-1e9, 8)}, time_condition=(0,1e9))
    antibiotico = Intervention(name='antibiotico',activation_rules=[antibiotico_rule1, antibiotico_rule2], 
                efect_time=48, repetition=12, supply=6)
    antibiotico.inner_action = antibiotico_action

    dipirona_simple_rule1 = ActivationRule(parameters_conditions={p_temperatura:(37, 100)}, time_condition=(0,1e9))
    dipirona_simple =  Intervention(name='dipirona',activation_rules=[dipirona_simple_rule1],
            efect_time=24, repetition=4, supply=10)
    dipirona_simple.inner_action = dipirona_action

    calbamol_rule1 = ActivationRule(parameters_conditions={p_temperatura:(37.5, 100),p_plaqueta:(-1e9, 24)}, 
                                                time_condition=(0,1e9))
    calbamol_rule2 = ActivationRule(parameters_conditions={p_plaqueta:(-1e9, 10)}, time_condition=(0,1e9))
    calbamol = Intervention(name='calbamol',activation_rules=[calbamol_rule1, calbamol_rule2],
                efect_time=48, repetition=6, supply=8)
    calbamol.inner_action = calbamol_action

    plaquetol_rule = ActivationRule(parameters_conditions={p_plaqueta:(-1e9, 22)}, time_condition=(0,1e9))
    plaquetol = Intervention(name='plaquetol', activation_rules=[plaquetol_rule], 
                    efect_time=24, repetition=6, supply=12)
    plaquetol.inner_action = plaquetol_action

    jarabe_rule = ActivationRule(parameters_conditions={p_tos:(10, 1e9)}, time_condition=(0,1e9))
    jarabe = Intervention(name='jarabe', activation_rules=[jarabe_rule], efect_time=48, repetition=8,
                    supply=6)
    jarabe.inner_action = jarabe_action

    environment = Environment(parameters=[p_plaqueta, p_tos, p_temperatura])
    fuzzy_engine = FuzzyEngine(increse_parameter=p_increase, decrese_parameter=p_decrease)
    t_t = simulation_main(env=environment, 
                treatment=set([antibiotico, jarabe, dipirona_simple, calbamol, plaquetol]), 
                disease=set([tos, fiebre]), 
                tick=tick, end_time=end_time, simulations=simulations,
                fuzzy_engine=fuzzy_engine)

    return t_t 