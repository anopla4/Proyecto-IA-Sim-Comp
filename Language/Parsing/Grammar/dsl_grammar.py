from ast import ClassDef
from ..non_terminal import NonTerminal
from ..terminal import Terminal
from ..production import Production
from ..Node.declaration_nodes import *
from ..Node.expression_nodes import *
from ..Node.statement_nodes import *
from ..Node.program_node import ProgramNode

# non terminals
program, elements_list = NonTerminal.get_non_terminals("<program> <elements-list>")
statement, simple_statement, statement_list = NonTerminal.get_non_terminals(
    "<statement> <simple-statement> <statement-list>"
)
def_class, class_statements, body_statements = NonTerminal.get_non_terminals(
    "<def-class> <class-statements> <body-statements>"
)
(
    def_attr,
    def_func,
    func_statements,
    def_var,
    assignment,
) = NonTerminal.get_non_terminals(
    "<def-attr> <def-func> <func-statements> <def-var> <assignment>"
)
def_agent = NonTerminal("<def-agent>")
param, param_list = NonTerminal.get_non_terminals("<param> <param-list>")
instance = NonTerminal("<instance>")
def_rand_var, def_efect = NonTerminal.get_non_terminals("<def-rand-var> <def-efect>")
expr, arith, term, factor, atom = NonTerminal.get_non_terminals(
    "<expr> <arith> <term> <factor> <atom>"
)
func_call, arg_list = NonTerminal.get_non_terminals("<func-call> <arg-list>")
prob_func, prob_func_list, rule, consecuent = NonTerminal.get_non_terminals(
    "<prob-func> <prob-func-list> <rule> <consecuent>"
)
simulation_call = NonTerminal("<sim-call>")
for_, if_, if_else = NonTerminal.get_non_terminals("<for> <if> <if-else>")
(
    bool_expr,
    compare_expr,
    comparison_operator,
    compare_factor,
) = NonTerminal.get_non_terminals(
    "<bool-expr> <compare-expr> <comparison-operator> <compare-factor>"
)

# terminals

epsilon = Terminal("epsilon")
d_rand_var = Terminal.get_terminals("RandVariableEfect")
patient, parameter, intervention, symptom = Terminal.get_terminals(
    "Patient Parameter Intervention Symptom"
)
efect = Terminal("efect")
in_, is_ = Terminal.get_terminals("in is")
rule_operator, arrow = Terminal.get_terminals("=> ->")
semi, colon, comma, dot, opar, cpar, ocur, ccur = Terminal.get_terminals(
    "; : , . ( ) { }"
)
equal, plus, minus, star, div = Terminal.get_terminals("= + - * /")
gt, lt, equals_b, not_equals_b, not_, and_, or_ = Terminal.get_terminals(
    "> < == != not and or"
)
idx, class_, function_ = Terminal.get_terminals("idx class function")
num, int_ = Terminal.get_terminals("num int")
for_kw, if_kw, else_kw = Terminal.get_terminals("for if else")
simulate = Terminal("simulate")
activation_condition, efect_time, repetition, action = Terminal.get_terminals(
    "activationCondition efectTime repetition action"
)

rules = {}

# <program>

p_77 = Production(program, [elements_list])
rules[p_77] = lambda _, s: ProgramNode(s[1])

# <elements-list>

p_0 = Production(elements_list, [statement, elements_list])
rules[p_0] = lambda _, s: [s[1]] + s[2]
p_48 = Production(elements_list, [func_call, elements_list])
rules[p_48] = lambda _, s: [s[1]] + s[2]
p_49 = Production(elements_list, [statement])
rules[p_49] = lambda _, s: [s[1]]
p_50 = Production(elements_list, [func_call])
rules[p_50] = lambda _, s: [s[1]]

# <statement>

p_1 = Production(statement, [def_class])
rules[p_1] = lambda _, s: [s[1]]
p_2 = Production(statement, [def_func])
rules[p_2] = lambda _, s: [s[1]]
p_75 = Production(statement, [def_agent])
rules[p_75] = lambda _, s: [s[1]]
p_54 = Production(statement, [simple_statement])
rules[p_54] = lambda _, s: [s[1]]
p_3 = Production(statement, [epsilon])
rules[p_3] = lambda _: []

# <simple-statement>

p_51 = Production(statement, [if_])
rules[p_51] = lambda _, s: [s[1]]
p_52 = Production(statement, [if_else])
rules[p_52] = lambda _, s: [s[1]]
p_53 = Production(statement, [for_])
rules[p_53] = lambda _, s: [s[1]]
p_56 = Production(statement, [def_var])
rules[p_56] = lambda _, s: [s[1]]
p_57 = Production(statement, [assignment])
rules[p_57] = lambda _, s: [s[1]]


# <def_class>

p_4 = Production(def_class, [class_, idx, ocur, class_statements, ccur])
rules[p_4] = lambda _, s: ClassNode(s[2], s[4])
p_5 = Production(def_class, [class_, idx, colon, idx, ocur, class_statements, ccur])
rules[p_5] = lambda _, s: ClassNode(s[2], s[3], s[4])

# <class-statements>

p_6 = Production(class_statements, [simple_statement, class_statements])
rules[p_6] = lambda _, s: [s[1]] + s[2]
p_58 = Production(class_statements, [def_func, class_statements])
rules[p_58] = lambda _, s: [s[1]] + s[2]
p_7 = Production(class_statements, [def_attr, class_statements])
rules[p_7] = lambda _, s: [s[1]] + s[2]
p_55 = Production(class_statements, [epsilon])
rules[p_55] = lambda _: []


# <def-agent>

p_76 = Production(
    def_agent,
    [
        idx,
        idx,
        equal,
        ocur,
        activation_condition,
        colon,
        bool_expr,
        semi,
        efect_time,
        colon,
        idx,
        semi,
        repetition,
        colon,
        idx,
        semi,
        action,
        colon,
        idx,
        semi,
    ],
)
rules[p_76] = lambda _, s: AgentDefNode(s[1], s[2], s[7], s[11], s[15], s[19])

# <def-attr>

p_8 = Production(def_attr, [idx, idx, equal, expr, semi])
rules[p_8] = lambda _, s: AttrDeclarationNode(s[1], s[2], s[4])

# <def-func>

p_9 = Production(
    def_func,
    [function_, idx, opar, param_list, cpar, arrow, idx, ocur, func_statements, ccur],
)
rules[p_9] = lambda _, s: FuncDeclarationNode(s[2], s[4], s[7], s[9])

# <func-statements>

p_78 = Production(func_statements, [simple_statement, func_statements])
rules[p_78] = lambda _, s: [s[1]] + s[2]
p_79 = Production(func_statements, [epsilon])
rules[p_78] = lambda _: []

# <def-var>

p_15 = Production(def_var, [idx, idx, equal, expr, semi])
rules[p_15] = lambda _, s: VarDeclarationNode(s[1], s[2], s[4])
p_15 = Production(def_var, [def_rand_var])
rules[p_15] = lambda _, s: [s[1]]

# <assignment>

p_16 = Production(assignment, [idx, equal, expr, semi])
rules[p_16] = lambda _, s: AssignmentNode(s[1], s[3])

# <param>

p_10 = Production(param, [idx, idx])
rules[p_10] = lambda _, s: (s[1], s[2])

# <param-list>

p_11 = Production(param_list, [param, comma, param_list])
rules[p_11] = lambda _, s: [s[1]] + s[2]
p_12 = Production(param_list, [epsilon])
rules[p_12] = lambda _: []


# <expr>

p_13 = Production(expr, [arith])
rules[p_13] = lambda _, s: s[1]
p_64 = Production(expr, [bool_expr])
rules[p_64] = lambda _, s: s[1]
p_14 = Production(expr, [prob_func])
rules[p_14] = lambda _, s: s[1]
p_17 = Production(expr, [rule])
rules[p_17] = lambda _, s: s[1]
p_18 = Production(expr, [def_efect])
rules[p_18] = lambda _, s: s[1]
p_19 = Production(expr, [func_call])
rules[p_19] = lambda _, s: s[1]
p_63 = Production(expr, [instance])
rules[p_63] = lambda _, s: s[1]


# <arith>

p_20 = Production(arith, [term])
rules[p_20] = lambda _, s: s[1]
p_21 = Production(arith, [arith, plus, term])
rules[p_21] = lambda _, s: PlusNode(s[1], s[3])
p_22 = Production(arith, [arith, minus, term])
rules[p_22] = lambda _, s: MinusNode(s[1], s[3])

# <term>

p_80 = Production(term, [factor])
rules[p_80] = lambda _, s: s[1]
p_81 = Production(term, [term, star, factor])
rules[p_81] = lambda _, s: ByNode(s[1], s[3])
p_23 = Production(term, [term, div, factor])
rules[p_23] = lambda _, s: DivideNode(s[1], s[3])

# <factor>

p_24 = Production(factor, [atom])
rules[p_24] = lambda _, s: s[1]
p_25 = Production(factor, [opar, arith, cpar])
rules[p_25] = lambda _, s: s[2]
p_26 = Production(factor, [opar, func_call, cpar])
rules[p_26] = lambda _, s: s[2]


# <atom>

p_27 = Production(atom, [num])
rules[p_27] = lambda _, s: s[1]
p_28 = Production(atom, [idx])
rules[p_28] = lambda _, s: s[1]
p_29 = Production(atom, [func_call])
rules[p_29] = lambda _, s: s[1]

# <bool-expr>

p_65 = Production(bool_expr, [bool_expr, and_, compare_expr])
rules[p_65] = lambda _, s: AndNode(s[1], s[3])
p_66 = Production(bool_expr, [bool_expr, or_, compare_expr])
rules[p_66] = lambda _, s: OrNode(s[1], s[3])
p_82 = Production(bool_expr, [compare_expr])
rules[p_82] = lambda _, s: s[1]

# <compare-expr>

p_70 = Production(compare_expr, [compare_factor])
rules[p_70] = lambda _, s: s[1]
p_67 = Production(compare_expr, [compare_expr, equals_b, compare_factor])
rules[p_67] = lambda _, s: EqualsNode(s[1], s[3])
p_68 = Production(compare_expr, [compare_expr, not_equals_b, compare_factor])
rules[p_68] = lambda _, s: NotEqualsNode(s[1], s[3])
p_69 = Production(compare_expr, [compare_expr, lt, compare_factor])
rules[p_69] = lambda _, s: LesserNode(s[1], s[3])
p_83 = Production(compare_expr, [compare_expr, gt, compare_factor])
rules[p_83] = lambda _, s: GreaterNode(s[1], s[3])

# <compare-factor>

p_84 = Production(compare_factor, [not_, compare_factor])
rules[p_84] = lambda _, s: NotNode(s[2])
p_71 = Production(compare_factor, [idx])
rules[p_71] = lambda _, s: s[1]
p_72 = Production(compare_factor, [func_call])
rules[p_72] = lambda _, s: s[1]
p_73 = Production(compare_factor, [instance])
rules[p_73] = lambda _, s: s[1]
p_74 = Production(compare_factor, [opar, bool_expr, opar])
rules[p_74] = lambda _, s: s[2]


# <func-call>

p_31 = Production(func_call, [idx, opar, arg_list, cpar])
rules[p_31] = lambda _, s: CallNode(s[1], s[3])
p_32 = Production(func_call, [idx, dot, idx, opar, arg_list, cpar])
rules[p_32] = lambda _, s: CallNode(s[3], s[5], obj=s[1])
p_33 = Production(func_call, [func_call, dot, idx, opar, arg_list, cpar])
rules[p_33] = lambda _, s: CallNode(s[3], s[5], obj=s[1])
p_34 = Production(func_call, [instance, dot, idx, opar, arg_list, cpar])
rules[p_34] = lambda _, s: CallNode(s[3], s[5], obj=s[1])
# p_47 = Production(func_call, [simulation_call])

# <instance>

p_62 = Production(instance, [idx, opar, arg_list, cpar])
rules[p_62] = lambda _, s: InstanceNode(s[1], s[3])

# <arg-list>

p_35 = Production(arg_list, [epsilon])
rules[p_35] = lambda _: []
p_36 = Production(arg_list, [atom, comma, arg_list])
rules[p_36] = lambda _, s: [s[1]] + s[2]
p_37 = Production(arg_list, [arith, comma, arg_list])
rules[p_37] = lambda _, s: [s[1]] + s[2]

# <num>

# p_38 = Production(num, [int_])

# <def-rand-var>

p_39 = Production(def_rand_var, [d_rand_var, idx, equal, ocur, prob_func_list, ccur])
rules[p_39] = lambda _, s: RandomVariableNode(s[2], s[5])

# <prob-func-list>

p_85 = Production(prob_func_list, [prob_func, prob_func_list])
rules[p_85] = lambda _, s: [s[1]] + s[2]
p_86 = Production(prob_func_list, [epsilon])
rules[p_86] = lambda _: []

# <prob-func>

p_40 = Production(prob_func, [idx, arrow, def_efect])
rules[p_40] = lambda _, s: ProbFunctionValueNode(s[1], s[3])

# <def-efect>

p_41 = Production(def_efect, [efect, idx, idx])
rules[p_41] = lambda _, s: EfectNode(s[2], s[3])
p_42 = Production(def_efect, [rule])
rules[p_42] = lambda _, s: EfectRuleNode(s[1])


# <rule>

p_43 = Production(rule, [bool_expr, rule_operator, assignment])
rules[p_43] = lambda _, s: RuleNode(s[1], s[3])

# <consecuent>

# p_87 = Production(consecuent, [idx, is_, idx])
# rules[p_87] = lambda

# <simulation-call>

# p_44 = Production(
#     simulation_call, [simulate, opar, param, param, param, param, param, param, cpar]
# )

# <for>

p_45 = Production(
    for_,
    [for_kw, idx, in_, expr, ocur, body_statements, ccur],
)
rules[p_45] = lambda _, s: ForNode(s[2], s[4], s[6])

# <if>

p_46 = Production(if_, [if_kw, expr, ocur, body_statements, ccur])
rules[p_46] = lambda _, s: IfNode(s[2], s[4])

# <if-else>

p_87 = Production(
    if_,
    [if_kw, expr, ocur, body_statements, ccur, else_kw, ocur, body_statements, ccur],
)
rules[p_87] = lambda _, s: IfElseNode(s[2], s[4], s[8])


# <body_statements>

p_59 = Production(body_statements, [simple_statement, body_statements])
rules[p_59] = lambda _, s: [s[1]] + s[2]
p_60 = Production(body_statements, [func_call, body_statements])
rules[p_60] = lambda _, s: [s[1]] + s[2]
p_61 = Production(body_statements, [epsilon])
rules[p_61] = lambda _: []


# all_terminals
name = "(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_)*"


t = {
    f"{name}|RandVariableEfect|Patient|Parameter|Intervention|Symptom|int|double|simulate": (
        "id",
        1,
    ),
    "for": ("for", 2),
    "if": ("if", 2),
    "else": ("else", 2),
    "efect": ("efect", 2),
    "in": ("in", 2),
    "is": ("is", 2),
    "=>": ("rule_operator", 3),
    "->": ("arrow", 3),
    ";": ("semi", 4),
    ":": ("colon", 4),
    ",": ("comma", 4),
    ".": ("dot", 4),
    "\(": ("opar", 4),
    "\)": ("cpar", 4),
    "{": ("ocur", 4),
    "}": ("ccur", 4),
    # "=": ("equal", 4),
    # "+": ("plus", 4),
    # "-": ("minus", 4),
    # "\*": ("star", 4),
    # "/": ("divide", 4),
    # ">": ("gt", 4),
    # "<": ("lt", 4),
    # "==": ("equals_b", 4),
    # "!=": ("not_equals_b", 4),
    # "not": ("not", 4),
    # "and": ("and", 4),
    # "or": ("or", 4),
    # "class": ("class", 4),
    # "function": ("function", 4),
    # "activation_conditions": ("activation_condition", 2),
    # "efect_time": ("efect_time", 2),
    # "repetition": ("repetition", 2),
    # "action": ("action", 2),
}
