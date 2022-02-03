from Simulation.environment import Environment
from Simulation.parameter import Parameter
from Simulation.rule import Rule
from .disease_bank import *
from .treatment_bank import *

def high_probability_to_win_Test(simulation_main, tick=1, end_time=168, simulations=5000):
    
    tos_rule = Rule(parameters_conditions={'plaqueta':(-1e9,22)}, time_condition=(0,1e9), then='tos')
    tos = Tos(name="tos",activation_rules=[tos_rule])

    dc_rule1 = Rule(parameters_conditions={'tos':(20, 200)}, time_condition=(0,1e9), then='dolor de cabeza')
    dc_rule2 = Rule(parameters_conditions={'fiebre':(37, 200)}, time_condition=(0,1e9), then='dolor de cabeza')
    dc = DolorCabeza(name='dolor de cabeza',activation_rules=[dc_rule1, dc_rule2])

    fiebre_rule = Rule(parameters_conditions={'plaqueta':(-1e9,16)}, time_condition=(0,1e9), then='fiebre')
    fiebre = Fiebre(name='fiebre',activation_rules=[fiebre_rule])


    antibiotico_rule1 = Rule(parameters_conditions={'fiebre':(38, 100)}, time_condition=(72,1e9), then='antibiotico')
    antibiotico_rule2 = Rule(parameters_conditions={'plaqueta':(-1e9, 8)}, time_condition=(24,1e9), then='antibiotico')
    antibiotico = Antibiotico(name='antibiotico',activation_rules=[antibiotico_rule1, antibiotico_rule2])

    dipirona_simple_rule1 = Rule(parameters_conditions={'fiebre':(37, 100)}, time_condition=(0,1e9), then='dipirona simple')
    dipirona_simple_rule2 = Rule(parameters_conditions={'dolor de cabeza':(10, 1000)}, time_condition=(0,1e9), then='dipirona simple')
    dipirona_simple =  DipironaSimple(name='dipirona simple',activation_rules=[dipirona_simple_rule1, dipirona_simple_rule2])

    dipirona_doble_rule1 = Rule(parameters_conditions={'fiebre':(37, 100)}, time_condition=(0,1e9), then='dipirona doble')
    dipirona_doble_rule2 = Rule(parameters_conditions={'dolor de cabeza':(25, 1e9)}, time_condition=(0,1e9), then='dipirona doble')
    dipirona_doble =  DipironaDoble(name='dipirona doble',activation_rules=[dipirona_doble_rule1, dipirona_doble_rule2])

    calbamol_rule1 = Rule(parameters_conditions={'fiebre':(37.5, 100),'plaqueta':(-1e9, 30)}, 
                                                time_condition=(0,1e9), then='calbamol')
    calbamol_rule2 = Rule(parameters_conditions={'dolor de cabeza':(15, 1e9)}, time_condition=(48,1e9), then='calbamol')
    calbamol_rule3 = Rule(parameters_conditions={'plaqueta':(-1e9, 10)}, time_condition=(24,1e9), then='calbamol')
    calbamol = Calbamol(name='calbamol',activation_rules=[calbamol_rule1, calbamol_rule2, calbamol_rule3])

    plaquetol_rule = Rule(parameters_conditions={'plaqueta':(-1e9, 20)}, time_condition=(12,1e9), then='plaquetol')
    plaquetol = Plaquetol(name='plaquetol', activation_rules=[plaquetol_rule])

    jarabe_rule = Rule(parameters_conditions={'tos':(10, 1e9)}, time_condition=(24,1e9), then='jarabe')
    jarabe = Jarabe(name='jarabe', activation_rules=[jarabe_rule])

    p_plaqueta = Parameter('plaqueta', value=18, low_good_limit=25, upp_good_limit=50, low_bad_limit=-20, upp_bad_limit=80)
    p_tos = Parameter('tos', value=10, low_good_limit=0, upp_good_limit=5, low_bad_limit=-20, upp_bad_limit=60)
    p_dolorCabeza = Parameter('dolor de cabeza', value=26, low_good_limit=0, upp_good_limit=15, low_bad_limit=-20, upp_bad_limit=100)
    p_fiebre = Parameter('fiebre', value=36.5, low_good_limit=35, upp_good_limit=36.9, low_bad_limit=34.5, upp_bad_limit=43)

    environment = Environment(parameters=[p_dolorCabeza, p_plaqueta, p_tos, p_fiebre])

    t_t = simulation_main(env=environment, treatment=set([antibiotico, jarabe, dipirona_simple, dipirona_doble, calbamol, plaquetol]), disease=set([tos, fiebre, dc]), tick=tick, end_time=end_time, simulations=simulations)

    return t_t