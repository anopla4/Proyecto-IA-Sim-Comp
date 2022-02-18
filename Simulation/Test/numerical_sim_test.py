from ..Simulation.environment import Environment
from ..Simulation.parameter import Parameter
from ..Simulation.activation_rule import ActivationRule
from ..Simulation.symptom import Symptom
from ..Simulation.intervention import Intervention
from .DiseaseBank.numerical_actions import *
from .TreatmentBank.numerical_actions import *

def numerical_sim_test(simulation_main, tick=1, end_time=168, simulations=5000):
    
    p_plaqueta = Parameter('plaqueta', value=18, low_good_limit=25, upp_good_limit=50, low_bad_limit=-20, upp_bad_limit=80)
    p_tos = Parameter('tos', value=10, low_good_limit=0, upp_good_limit=5, low_bad_limit=-20, upp_bad_limit=60)
    p_dolorCabeza = Parameter('dolor de cabeza', value=26, low_good_limit=0, upp_good_limit=15, low_bad_limit=-20, upp_bad_limit=100)
    p_fiebre = Parameter('fiebre', value=36.5, low_good_limit=35, upp_good_limit=36.9, low_bad_limit=34.5, upp_bad_limit=43)

    tos = Symptom(name="tos",
    activation_rules=[ActivationRule(parameters_conditions={p_plaqueta:(-1e9,22)}, time_condition=(0,1e9))],
    efect_time=72, repetition=8, action=tos_action)
    #tos.inner_action = tos_action

    dc = Symptom(name="dolor de cabeza",
    activation_rules=[ActivationRule(parameters_conditions={p_tos:(20, 200)}, time_condition=(0,1e9)),
                    ActivationRule(parameters_conditions={p_fiebre:(37, 200)}, time_condition=(0,1e9))],
    efect_time=72, repetition=4, action=dc_action)
    #dc.inner_action = dc_action
    
    fiebre = Symptom(name="fiebre",
    activation_rules=[ActivationRule(parameters_conditions={p_plaqueta:(-1e9,16)}, time_condition=(0,1e9))],
    efect_time=72, repetition=8, action=fiebre_action)
    #fiebre.inner_action = fiebre_action

    antibiotico = Intervention(name='antibiotico',
    activation_rules=[ActivationRule(parameters_conditions={p_fiebre:(38, 100)}, time_condition=(72,1e9)),
                    ActivationRule(parameters_conditions={p_plaqueta:(-1e9, 8)}, time_condition=(24,1e9))],
    efect_time=36, repetition=12, supply=7, action=antibiotico_action)
    #antibiotico.inner_action = antibiotico_action

    dipirona_simple  = Intervention(name='dipirona simple',
    activation_rules=[ActivationRule(parameters_conditions={p_fiebre:(37, 100)}, time_condition=(0,1e9)),
                    ActivationRule(parameters_conditions={p_dolorCabeza:(10, 1000)}, time_condition=(0,1e9))],
    efect_time=24, repetition=8, supply=10, action=dipirona_simple_action)
    #dipirona_simple.inner_action = dipirona_simple_action

    dipirona_doble  = Intervention(name='dipirona_doble',
    activation_rules=[ActivationRule(parameters_conditions={p_fiebre:(37, 100)}, time_condition=(0,1e9)),
                    ActivationRule(parameters_conditions={p_dolorCabeza:(25, 1e9)}, time_condition=(0,1e9))],
    efect_time=24, repetition=8, supply=10, action=dipirona_doble_action)
    #dipirona_doble.inner_action = dipirona_doble_action

    calbamol  = Intervention(name='calbamol',
    activation_rules=[ActivationRule(parameters_conditions={p_fiebre:(37.5, 100),p_plaqueta:(-1e9, 30)}, 
                                                time_condition=(0,1e9)),
                    ActivationRule(parameters_conditions={p_dolorCabeza:(15, 1e9)}, time_condition=(48,1e9)),
                    ActivationRule(parameters_conditions={p_plaqueta:(-1e9, 10)}, time_condition=(24,1e9))],
    efect_time=48, repetition=6, supply=8, action=calbamol_action)
    #calbamol.inner_action = calbamol_action

    plaquetol = Intervention(name="plaquetol",
    activation_rules=[ActivationRule(parameters_conditions={p_plaqueta:(-1e9, 10)}, time_condition=(24,1e9))],
    efect_time=24, repetition=12, supply=10, action=plaquetol_action)
    ##plaquetol.inner_action = plaquetol_action

    jarabe = Intervention(name="jarabe",
    activation_rules=[ActivationRule(parameters_conditions={p_tos:(10, 1e9)}, time_condition=(24,1e9))],
    efect_time=48, repetition=12, supply=5, action=jarabe_action)
    #jarabe.inner_action = jarabe_action

    environment = Environment(parameters=[p_dolorCabeza, p_plaqueta, p_tos, p_fiebre])

    t_t = simulation_main(env=environment, treatment=set([antibiotico, jarabe, dipirona_simple, dipirona_doble, calbamol, plaquetol]), disease=set([tos, fiebre, dc]), tick=tick, end_time=end_time, simulations=simulations)

    return t_t