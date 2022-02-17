from Language.Check.context import Context
from Language.Check.semantic_checker import SemanticChecker
from Language.Check.type import BoolType, MainType
from Language.Check.type_builder import TypeBuilder
from Language.Check.type_collector import TypeCollector
from Language.Lexer.token import Token
from Language.Parsing.Grammar_dsl.dsl_grammar import get_grammar
from Language.Lexer.lexer import tokenize_regex_automaton
from Language.Parsing.build_ast_shift_reduce_parser import build_ast
from Language.Parsing.parserLR1 import ParserLR1
from Language.Check.translator import Translator
from Simulation.Simulation.environment import Environment, Patient
from Simulation.Simulation.parameter import Parameter
from Simulation.Simulation.activation_rule import ActivationRule
from Simulation.Simulation.symptom import Symptom
from Simulation.Simulation.intervention import Intervention


def main(text):
    G, t = get_grammar()
    parser = ParserLR1(G)

    tokens = tokenize_regex_automaton(text, t)
    tokens.append(Token("$", (G.EOF, 0)))
    l = [i.type[0] for i in tokens]
    result, actions = parser.parse(l)
    # print()
    ast = build_ast(actions, result, tokens, G)
    context = Context()
    type_c = TypeCollector(context)
    type_c.visit(ast)

    type_b = TypeBuilder(context)
    type_b.visit(ast)

    checker = SemanticChecker(context)
    checker.visit(ast)

    t = Translator()
    code = t.visit(ast)

    print("==========")
    print(code)
    print("=========")

    errors = type_c.errors + type_b.errors + checker.errors
    print(errors)
    try:
        exec(code)
    except Exception as ex:
        print(ex)


main(
    """Parameter p_plaqueta = new Parameter("plaqueta", 18, 25, 50, -20, 80); \n 
    Parameter fiebre = new Parameter("fiebre", 36.5, 35, 36.9, 34.5, 43); \n
    Patient p = new Patient([p_plaqueta]); \n 
    RandVarEffect fiebre_action = { 0.3 -> effect fiebre p 1; 0.45 ->  effect fiebre p 1.4; 0.25 -> effect fiebre p 1.8}; \n 
    Symptom fiebre = { activation_conditions : [new ActivationRule({p_plaqueta : {-19,16}}, {0,19})]; effect_time : 72; repetition : 8; action : fiebre_action;} """
)
