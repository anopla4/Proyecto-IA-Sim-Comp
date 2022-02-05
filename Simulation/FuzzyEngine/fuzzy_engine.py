from .variable import Variable
#from action import Action
from .rule import Rule
from .fuzzy_functions import defuzzing_by_centroid, inference_by_mandami,max_agreg

class State:
    def State(self, variables:list[Variable]):
        self.variables = variables

    def get_var_by_name(self, var_name:str) -> Variable:
        for v in self.variables:
            if v.name == var_name:
                return v
        return None


def fuzzy_engine(state:State, rules:list[Rule]) -> State:
    """
    Dado un estado, utiliza los mecanismos de la lógica difusa para determinar el siguiente estado
    """
    fuzzing_state = {} # {variable: {value: membresy_value}}
    membresy_functions = {} # {variable : {value: membresy_function}}
    for var in state.variables:
        fuzzing_state[var.name] = var.get_defuzzy_values()
        membresy_functions[var.name] = var.membresy_functions
    for var in state.variables:
        target_rules = [r for r in rules if r.get_target() == var.name]
        if len(target_rules) > 0:
            var.value = __get_var_value(fuzzing_state, var, target_rules)
    return state

def __defuzzing_by_centroid(agregation_function)->float:
    pass

def __get_var_value(fuzzing_state, var_target:Variable, rules:list[Rule]) -> float:
    rules_evaluation = []
    for rule in rules:
        and_ = 1.1
        for cond in rule.and_conditions:
            and_=min(and_, fuzzing_state[cond[0]][cond[1]])
        mem_f = var_target.membresy_functions[rule.then[1]]
        rules_evaluation.append(inference_by_mandami(and_,mem_f))
        #rules_evaluation.append(lambda x: and_ if mem_f(x) > and_ else mem_f(x))
    agregation = max_agreg(rules_evaluation)
    #agregation = lambda x : max([f(x) for f in rules_evaluation])
    output = __defuzzing_by_centroid(agregation)
    return output
