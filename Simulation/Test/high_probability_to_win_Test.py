from Simulation.environment import Environment
from Simulation.parameter import Parameter
from Simulation.activation_rule import ActivationRule
from FuzzyEngine.MembresyFunctions.triangular import Triangular
from FuzzyEngine.MembresyFunctions.trapezoidal import Trapezoidal
from .disease_bank import *
from .treatment_bank import *
from FuzzyEngine.fuzzy_engine import FuzzyEngine


def high_probability_to_win_Test(simulation_main, tick=1, end_time=168, simulations=5000):
    
    tos_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9,22)}, time_condition=(0,1e9))
    tos = Tos(name="tos",activation_rules=[tos_rule])

    dc_rule1 = ActivationRule(parameters_conditions={'tos':(20, 200)}, time_condition=(0,1e9))
    dc_rule2 = ActivationRule(parameters_conditions={'fiebre':(37, 200)}, time_condition=(0,1e9))
    dc = DolorCabeza(name='dolor de cabeza',activation_rules=[dc_rule1, dc_rule2])

    fiebre_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9,19)}, time_condition=(0,1e9))
    fiebre = Fiebre(name='fiebre',activation_rules=[fiebre_rule])


    antibiotico_rule1 = ActivationRule(parameters_conditions={'fiebre':(38, 100)}, time_condition=(0,1e9))
    antibiotico_rule2 = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 8)}, time_condition=(0,1e9))
    antibiotico = Antibiotico(name='antibiotico',activation_rules=[antibiotico_rule1, antibiotico_rule2])

    dipirona_simple_rule1 = ActivationRule(parameters_conditions={'fiebre':(37, 100)}, time_condition=(0,1e9))
    dipirona_simple_rule2 = ActivationRule(parameters_conditions={'dolor de cabeza':(10, 1000)}, time_condition=(0,1e9))
    dipirona_simple =  DipironaSimple(name='dipirona simple',activation_rules=[dipirona_simple_rule1, dipirona_simple_rule2])

    dipirona_doble_rule1 = ActivationRule(parameters_conditions={'fiebre':(37, 100)}, time_condition=(0,1e9))
    dipirona_doble_rule2 = ActivationRule(parameters_conditions={'dolor de cabeza':(25, 1e9)}, time_condition=(0,1e9))
    dipirona_doble =  DipironaDoble(name='dipirona doble',activation_rules=[dipirona_doble_rule1, dipirona_doble_rule2])

    calbamol_rule1 = ActivationRule(parameters_conditions={'fiebre':(37.5, 100),'plaqueta':(-1e9, 30)}, 
                                                time_condition=(0,1e9))
    calbamol_rule2 = ActivationRule(parameters_conditions={'dolor de cabeza':(15, 1e9)}, time_condition=(0,1e9))
    calbamol_rule3 = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 10)}, time_condition=(0,1e9))
    calbamol = Calbamol(name='calbamol',activation_rules=[calbamol_rule1, calbamol_rule2, calbamol_rule3])

    plaquetol_rule = ActivationRule(parameters_conditions={'plaqueta':(-1e9, 20)}, time_condition=(0,1e9))
    plaquetol = Plaquetol(name='plaquetol', activation_rules=[plaquetol_rule])

    jarabe_rule = ActivationRule(parameters_conditions={'tos':(10, 1e9)}, time_condition=(0,1e9))
    jarabe = Jarabe(name='jarabe', activation_rules=[jarabe_rule])

    #p_plaqueta = Parameter('plaqueta', value=18, low_good_limit=25, upp_good_limit=50, low_bad_limit=-20, upp_bad_limit=80)
    #p_tos = Parameter('tos', value=10, low_good_limit=0, upp_good_limit=5, low_bad_limit=-20, upp_bad_limit=60)
    #p_dolorCabeza = Parameter('dolor de cabeza', value=26, low_good_limit=0, upp_good_limit=15, low_bad_limit=-20, upp_bad_limit=100)
    #p_fiebre = Parameter('fiebre', value=36.5, low_good_limit=35, upp_good_limit=36.9, low_bad_limit=34.5, upp_bad_limit=43)

    p_increase = Parameter(
        name = 'increase', value = 0,
        membresy_functions={'low': Triangular(0,0,0.3),
                            'medium':Trapezoidal(0.2,0.6,0.65,0.9),
                            'high':Triangular(0.45,0.7,1)},
                low_good_limit=0, upp_good_limit=1,
                low_bad_limit=0, upp_bad_limit=1
            )

    p_decrease=Parameter(
        name= 'decrease', value=0,
        membresy_functions={'low':Trapezoidal(0,0,0.2,0.4),
                            'medium':Triangular(0.1,0.4,0.7),
                            'high': Trapezoidal(0.4,0.6,0.7,1)
                            },
                low_good_limit=0, upp_good_limit=1,
                low_bad_limit=0, upp_bad_limit=1
            )

    p_plaqueta = Parameter(
        name='plaqueta', value=12, 
        membresy_functions={'muy baja': Triangular(0,0,8),
                            'baja':Triangular(5,14,18),
                            'estable':Triangular(16,35,35),
                            'alta':Triangular(33,40,48),
                            'muy alta':Triangular(42,60,60)},
        low_good_limit=14, upp_good_limit=38,
        low_bad_limit=-1e9, upp_bad_limit=48
        )

    p_dolorCabeza = Parameter(
        name='dolor de cabeza', value=10, 
        membresy_functions={'bajo':Trapezoidal(0,0,7,10),
                            'medio':Triangular(7,12,20),
                            'alto':Trapezoidal(18,24,28,30),
                            'muy alto':Triangular(28,40,40)},
        low_good_limit=0, upp_good_limit=12,
        low_bad_limit=0, upp_bad_limit=100
    )

    p_tos = Parameter(
        name='tos', value=14, 
        membresy_functions={'baja':Triangular(0,0,15),
                            'media':Triangular(10,26,30),
                            'alta':Trapezoidal(28,36,40,40)},
        low_good_limit=0, upp_good_limit=15,
        low_bad_limit=-1e9, upp_bad_limit=40
        )

    p_temperatura = Parameter(
        name='temperatura', value=37.8, 
        membresy_functions={'baja':Triangular(34,34.8,35.5),
                            'media':Triangular(35,36.2,37.2),
                            'alta':Triangular(36.8,38.5,42),
                            'muy alta':Trapezoidal(40,43, 46,46)},
        low_good_limit=35, upp_good_limit=36.8,
        low_bad_limit=34.5, upp_bad_limit=43
    )
    

    environment = Environment(parameters=[p_dolorCabeza, p_plaqueta, p_tos, p_temperatura])

    print('Initial state---')
    from pprint import pprint
    pprint(environment.get_params_dict())

    fuzzy_engine = FuzzyEngine(increse_parameter=p_increase, decrese_parameter=p_decrease)

    t_t = simulation_main(env=environment, 
                treatment=set([antibiotico, jarabe, dipirona_simple, dipirona_doble, calbamol, plaquetol]), 
                disease=set([tos, fiebre, dc]), 
                fuzzy_engine=fuzzy_engine,
                tick=tick, end_time=end_time, simulations=simulations)

    return t_t