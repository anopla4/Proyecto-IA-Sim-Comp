from typing import Dict
from .rule import Rule
from .fuzzy_functions import defuzzing_by_centroid, inference_by_mandami,max_agreg
from Simulation.parameter import Parameter
from Simulation.environment import Environment

class Fuzzy:

    def __init__(self, increse_parameter:Parameter, decrese_parameter:Parameter) -> None:
        self._increse_parameter = increse_parameter
        self._decrese_parameter = decrese_parameter

    def engine(self, env:Environment, rules:list[Rule]) -> Environment:
        fuzzing_state:Dict[str,Dict[str,float]] = {} # {variable: {value: membresy_value}}
        membresy_functions = {} # {variable : {value: membresy_function}}
        for param in env.parameters:
            fuzzing_state[param.name] = param.get_defuzzy_values()
            membresy_functions[param.name] = param.membresy_functions
        for param in env.parameters:
            destination_rules = [r for r in rules if r.destination == param.name]
            if len(destination_rules) > 0:
                #param.value += self.__get_var_value(fuzzing_state, param, destination_rules)
                param.value += self.__detect_variation(fuzzing_state, param, destination_rules)
        return env

    def __detect_variation(self, fuzzing_state:Dict[str,Dict[str,float]], param_target:Parameter, rules:list[Rule])->float:
        increse_rules = [r for r in rules if r.target == 'increse']
        decrese_rules = [r for r in rules if r.target == 'decrese']
        l,r = param_target.get_definition_range()
        extended = r-l
        increse_value = self.__get_var_value(fuzzing_state, self._increse_parameter, increse_rules, extended)
        decrese_value = self.__get_var_value(fuzzing_state, self._decrese_parameter, decrese_rules, extended)
        return increse_value-decrese_value


    def __get_var_value(fuzzing_state:Dict[str,Dict[str,float]], param_target:Parameter, rules:list[Rule], extended) -> float:
        rules_evaluation = []
        target_membresy_function = param_target.get_extended_membresy_functions(extended)
        for rule in rules:
            and_ = 1.1
            for param, value in rule.conditions.items():
                #print(f'{param}:{value}')
                #a = fuzzing_state[param][value]
                and_=min(and_, fuzzing_state[param][value])
            mem_f = target_membresy_function[rule.then[1]]
            rules_evaluation.append(inference_by_mandami(and_,mem_f))
            #rules_evaluation.append(lambda x: and_ if mem_f(x) > and_ else mem_f(x))
        agregation = max_agreg(rules_evaluation)
        #agregation = lambda x : max([f(x) for f in rules_evaluation])
        l,r = param_target.get_definition_range()
        l *= extended
        r *= extended
        output = defuzzing_by_centroid(agregation, l,r)
        return output


def fuzzy_engine(env:Environment, rules:list[Rule]) -> Environment:
    """
    Given a environment state, it uses fuzzy logic mechanisms to determine the next state.
    """
    fuzzing_state:Dict[str,Dict[str,float]] = {} # {variable: {value: membresy_value}}
    membresy_functions = {} # {variable : {value: membresy_function}}
    for param in env.parameters:
        fuzzing_state[param.name] = param.get_defuzzy_values()
        membresy_functions[param.name] = param.membresy_functions
    for param in env.parameters:
        target_rules = [r for r in rules if r.target == param.name]
        if len(target_rules) > 0:
            param.value = __get_var_value(fuzzing_state, param, target_rules)
    return env


#def __defuzzing_by_centroid(agregation_function)->float:
#    pass

def __get_var_value(fuzzing_state:Dict[str,Dict[str,float]], param_target:Parameter, rules:list[Rule]) -> float:
    rules_evaluation = []
    for rule in rules:
        and_ = 1.1
        for param, value in rule.conditions.items():
            #print(f'{param}:{value}')
            #a = fuzzing_state[param][value]
            and_=min(and_, fuzzing_state[param][value])
        mem_f = param_target.membresy_functions[rule.then[1]]
        rules_evaluation.append(inference_by_mandami(and_,mem_f))
        #rules_evaluation.append(lambda x: and_ if mem_f(x) > and_ else mem_f(x))
    agregation = max_agreg(rules_evaluation)
    #agregation = lambda x : max([f(x) for f in rules_evaluation])
    l,r = param_target.get_definition_range()
    output = defuzzing_by_centroid(agregation, l,r)
    return output
