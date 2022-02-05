from .rule import Rule
from .fuzzy_functions import defuzzing_by_centroid, inference_by_mandami,max_agreg
from Simulation.parameter import Parameter
from Simulation.environment import Environment


def fuzzy_engine(state:Environment, rules:list[Rule]) -> Environment:
    """
    Given a state, it uses fuzzy logic mechanisms to determine the next state.
    """
    fuzzing_state = {} # {variable: {value: membresy_value}}
    membresy_functions = {} # {variable : {value: membresy_function}}
    for param in state.parameters:
        fuzzing_state[param.name] = param.get_defuzzy_values()
        membresy_functions[param.name] = param.membresy_functions
    for param in state.parameters:
        target_rules = [r for r in rules if r.get_target() == param.name]
        if len(target_rules) > 0:
            param.value = __get_var_value(fuzzing_state, param, target_rules)
    return state

#def __defuzzing_by_centroid(agregation_function)->float:
#    pass

def __get_var_value(fuzzing_state, param_target:Parameter, rules:list[Rule]) -> float:
    rules_evaluation = []
    for rule in rules:
        and_ = 1.1
        for cond in rule.and_conditions:
            and_=min(and_, fuzzing_state[cond[0]][cond[1]])
        mem_f = param_target.membresy_functions[rule.then[1]]
        rules_evaluation.append(inference_by_mandami(and_,mem_f))
        #rules_evaluation.append(lambda x: and_ if mem_f(x) > and_ else mem_f(x))
    agregation = max_agreg(rules_evaluation)
    #agregation = lambda x : max([f(x) for f in rules_evaluation])
    l,r = param_target.get_definition_range()
    output = defuzzing_by_centroid(agregation, l,r)
    return output
