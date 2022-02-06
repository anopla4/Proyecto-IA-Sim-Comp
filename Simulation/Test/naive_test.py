from Simulation.environment import Environment
from Simulation.parameter import Parameter
from Simulation.activation_rule import ActivationRule
from FuzzyEngine.MembresyFunctions.triangular import Triangular
from FuzzyEngine.MembresyFunctions.trapezoidal import Trapezoidal
from .naive_disease_bank import *
from .naive_treatment_bank import *
from FuzzyEngine.fuzzy_engine import FuzzyEngine

def naive_test(simulation_main, tick=1, end_time=168, simulations=5000):
    
    tos_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9,20)}, time_condition=(0,1e9))
    tos = Tos(name="tos",activation_rules=[tos_rule])

    fiebre_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9,18)}, time_condition=(0,1e9))
    fiebre = Fiebre(name='fiebre',activation_rules=[fiebre_rule])

    antibiotico_rule1 = ActivationRule(parameters_conditions={'fiebre':(37, 100)}, time_condition=(0,1e9))
    antibiotico_rule2 = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 8)}, time_condition=(0,1e9))
    antibiotico = Antibiotico(name='antibiotico',activation_rules=[antibiotico_rule1, antibiotico_rule2])

    dipirona_simple_rule1 = ActivationRule(parameters_conditions={'temperatura':(37, 100)}, time_condition=(0,1e9))
    #dipirona_simple_rule2 = ActivationRule(parameters_conditions={'dolor de cabeza':(10, 1000)}, time_condition=(0,1e9))
    dipirona_simple =  DipironaSimple(name='dipirona',activation_rules=[dipirona_simple_rule1])

    calbamol_rule1 = ActivationRule(parameters_conditions={'temperatura':(37.5, 100),'plaqueta':(-1e9, 24)}, 
                                                time_condition=(0,1e9))
    calbamol_rule2 = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 10)}, time_condition=(0,1e9))
    calbamol = Calbamol(name='calbamol',activation_rules=[calbamol_rule1, calbamol_rule2])

    plaquetol_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 22)}, time_condition=(0,1e9))
    plaquetol = Plaquetol(name='plaquetol', activation_rules=[plaquetol_rule])

    jarabe_rule = ActivationRule(parameters_conditions={'tos':(10, 1e9)}, time_condition=(0,1e9))
    jarabe = Jarabe(name='jarabe', activation_rules=[jarabe_rule])

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
    

    environment = Environment(parameters=[p_plaqueta, p_tos, p_temperatura])
    fuzzy_engine = FuzzyEngine(increse_parameter=p_increase, decrese_parameter=p_decrease)
    t_t = simulation_main(env=environment, 
                treatment=set([antibiotico, jarabe, dipirona_simple, calbamol, plaquetol]), 
                disease=set([tos, fiebre]), 
                fuzzy_engine=fuzzy_engine,
                tick=tick, end_time=end_time, simulations=simulations)

    return t_t 