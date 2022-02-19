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
from Simulation.main import simulate
from random import random
from Simulation.TreatmentTree.pyvis_draw import (
    visualize_best_branch_pyvis,
    plot_graph,
)


def main(text):
    print(text)
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
    Parameter p_tos= new Parameter("tos",10, 0, 5,-20,60);\n
    Parameter p_dolorCabeza= new Parameter("dolor de cabeza",26, 0, 15,-20,100);\n
    Parameter p_fiebre = new Parameter("fiebre", 36.5, 35, 36.9, 34.5, 43); \n
    Patient p = new Patient([p_plaqueta, p_tos, p_dolorCabeza, p_fiebre]); \n 
    RandVarEffect fiebre_action = { 0.3 -> effect "fiebre" p 1, effect "plaqueta" p -1.5; 0.45 -> effect "fiebre" p 1.4, effect "plaqueta" p -1.5; 0.25 -> effect "fiebre" p 1.8, effect "plaqueta" p -2, effect "dolo de cabeza" p 3}; \n
    RandVarEffect tos_action = { 0.5 -> effect "tos" p 0.4, effect "plaqueta" p -0.5; 0.5 -> effect "tos" p 0.4, effect "plaqueta" p -0.8}; \n
    RandVarEffect dc_action = { 0.75 -> effect "dolo de cabeza" p 2.5; 0.25 -> effect "dolo de cabeza" p 4.5}; \n
    Symptom fiebre = { activation_conditions : [new ActivationRule({p_plaqueta : {-0.000000001,16}}, {0,100000000})]; effect_time : 72; repetition : 8; action : fiebre_action;}\n
    Symptom tos = { activation_conditions : [new ActivationRule({p_plaqueta : {-0.000000001,22}}, {0,100000000})]; effect_time : 72; repetition : 8; action : tos_action;}\n
    Symptom dolor_cabeza = { activation_conditions : [new ActivationRule({p_tos : {20,200}}, {0,100000000})]; effect_time : 72; repetition : 4; action : dc_action;}\n
    RandVarEffect dipirona_simple_action = { 0.7 -> effect "dolo de cabeza" p -4.4, effect "fiebre" p -1; 0.3 -> effect "fiebre" p 0 };\n
    RandVarEffect dipirona_doble_action = { 0.82 -> effect "dolo de cabeza" p -6.8, effect "fiebre" p -1.5; 0.18 -> effect "fiebre" p 0 };\n
    RandVarEffect calbamol_action = { 0.4 -> effect "dolo de cabeza" p -2, effect "fiebre" p -0.5, effect "plaqueta" p 3; 0.4 -> effect "dolo de cabeza" p -3, effect "fiebre" p -0.5; 0.2 -> effect "fiebre" p 0 };\n
    RandVarEffect jarabe_action = { 0.75 -> effect "tos" p -6; 0.25 -> effect "tos" p 0 };\n
    RandVarEffect antibiotico_action = { 0.5 -> effect "fiebre" p -1.6, effect "tos" p -10, effect "plaqueta" p 2.4; 0.3 -> effect "fiebre" p -1.4, effect "tos" p -6; 0.2 -> effect "fiebre" p -1, effect "plaqueta" p 6};\n
    RandVarEffect plaquetol_action = { 0.5 -> effect "plaqueta" p 2; 0.3 -> effect "plaqueta" p 5; 0.2 -> effect "plaqueta" p 0 };\n
    Intervention antibiotico = { activation_conditions : [new ActivationRule({p_fiebre : {38, 100}}, {72, 1000000000}), new ActivationRule({p_plaqueta : {-1000000000, 8}}, {24, 1000000000})]; effect_time : 36; repetition : 12; action : antibiotico_action; supply : 7; }\n
    Intervention dipirona_simple = { activation_conditions : [new ActivationRule({p_fiebre : {37, 100}}, {0, 1000000000}), new ActivationRule({p_dolorCabeza : {10, 1000}}, {0, 1000000000})]; effect_time : 24; repetition : 8; action : dipirona_simple_action; supply : 10; }\n
    Intervention dipirona_doble = { activation_conditions : [new ActivationRule({p_fiebre : {37, 100}}, {0, 1000000000}), new ActivationRule({p_dolorCabeza : {25, 1000000000}}, {0, 1000000000})]; effect_time : 24; repetition : 8; action : dipirona_doble_action; supply : 10; }\n
    Intervention calbamol = { activation_conditions : [new ActivationRule({p_fiebre : {37.5, 100}, p_plaqueta : {-1000000000, 30}}, {0, 1000000000}), new ActivationRule({p_dolorCabeza : {15, 1000000000}}, {48, 1000000000}), new ActivationRule({p_plaqueta : {-1000000000, 10}}, {24, 1000000000})]; effect_time : 48; repetition : 6; action : calbamol_action; supply : 8; }\n
    Intervention plaquetol = { activation_conditions : [new ActivationRule({p_plaqueta : {-1000000000, 10}}, {24, 1000000000})]; effect_time : 24; repetition : 12; action : plaquetol_action; supply : 10; }\n
    Intervention jarabe = { activation_conditions : [new ActivationRule({p_tos : {10, 1000000000}}, {24, 1000000000})]; effect_time : 48; repetition : 12; action : jarabe_action; supply : 5; }\n
    Tree treatment_tree = simulate(p,[antibiotico, jarabe, dipirona_simple, dipirona_doble, calbamol, plaquetol], [tos, fiebre, dolor_cabeza], 1, 168, 5000);
    plot_graph(treatment_tree)\n
    visualize_best_branch_pyvis(treatment_tree)"""
)
