from ..non_terminal import NonTerminal
from ..terminal import Terminal
from ..production import Production
from ..Node.declaration_nodes import *
from ..Node.expression_nodes import *
from ..Node.statement_nodes import *
from ..Node.program_node import ProgramNode
from ..Grammar import Grammar

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
def_rand_var, def_effect = NonTerminal.get_non_terminals("<def-rand-var> <def-effect>")
expr, arith, term, factor, atom = NonTerminal.get_non_terminals(
    "<expr> <arith> <term> <factor> <atom>"
)
func_call, arg_list = NonTerminal.get_non_terminals("<func-call> <arg-list>")
prob_func, prob_func_list, rule = NonTerminal.get_non_terminals(
    "<prob-func> <prob-func-list> <rule>"
)
for_, if_, if_else = NonTerminal.get_non_terminals("<for> <if> <if-else>")
(
    bool_expr,
    compare_expr,
    comparison_operator,
    compare_factor,
) = NonTerminal.get_non_terminals(
    "<bool-expr> <compare-expr> <comparison-operator> <compare-factor>"
)

non_terminals = [
    # program,
    # elements_list,
    # statement,
    # simple_statement,
    # statement_list,
    # def_class,
    # class_statements,
    body_statements,
    # def_attr,
    # def_func,
    # func_statements,
    # def_var,
    # assignment,
    # def_agent,
    # param,
    # param_list,
    # instance,
    # def_rand_var,
    # def_effect,
    expr,
    arith,
    term,
    factor,
    atom,
    # arg_list,
    # prob_func_list,
    # rule,
    # if_,
    # if_else,
    # func_call,
    # for_,
    # prob_func,
    bool_expr,
    compare_expr,
    comparison_operator,
    compare_factor,
]

# terminals

epsilon = Terminal("epsilon")
effect = Terminal("effect")
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
for_kw, if_kw, else_kw = Terminal.get_terminals("for if else")
activation_condition, effect_time, repetition, action = Terminal.get_terminals(
    "activationCondition effectTime repetition action"
)
terminals = [
    epsilon,
    # effect,
    # in_,
    # rule_operator,
    semi,
    equal,
    gt,
    idx,
    # for_kw,
    # activation_condition,
    # is_,
    # arrow,
    colon,
    # comma,
    # dot,
    opar,
    cpar,
    ocur,
    ccur,
    plus,
    minus,
    star,
    div,
    lt,
    equals_b,
    not_equals_b,
    not_,
    and_,
    or_,
    # class_,
    # function_,
    # if_kw,
    # else_kw,
    # effect_time,
    # repetition,
    # action,
]


rules = {}
productions = {}

# # <program>

# p_77 = Production(program, [elements_list])
# rules[p_77] = lambda _, s: ProgramNode(s[1])
# productions[program] = [p_77]

# # <elements-list>

# p_0 = Production(elements_list, [statement, elements_list])
# rules[p_0] = lambda _, s: [s[1]] + s[2]
# p_48 = Production(elements_list, [func_call, elements_list])
# rules[p_48] = lambda _, s: [s[1]] + s[2]
# p_49 = Production(elements_list, [statement])
# rules[p_49] = lambda _, s: [s[1]]
# p_50 = Production(elements_list, [func_call])
# rules[p_50] = lambda _, s: [s[1]]
# productions[elements_list] = [p_0, p_48, p_49, p_50]

# # <statement>

# p_1 = Production(statement, [def_class])
# rules[p_1] = lambda _, s: [s[1]]
# p_2 = Production(statement, [def_func])
# rules[p_2] = lambda _, s: [s[1]]
# p_75 = Production(statement, [def_agent])
# rules[p_75] = lambda _, s: [s[1]]
# p_54 = Production(statement, [simple_statement])
# rules[p_54] = lambda _, s: [s[1]]
# p_3 = Production(statement, [epsilon])
# rules[p_3] = lambda h, s: []
# productions[statement] = [p_1, p_2, p_75, p_54, p_3]

# # <simple-statement>

# p_51 = Production(simple_statement, [if_])
# rules[p_51] = lambda _, s: [s[1]]
# p_52 = Production(simple_statement, [if_else])
# rules[p_52] = lambda _, s: [s[1]]
# p_53 = Production(simple_statement, [for_])
# rules[p_53] = lambda _, s: [s[1]]
# p_56 = Production(simple_statement, [def_var])
# rules[p_56] = lambda _, s: [s[1]]
# p_57 = Production(simple_statement, [assignment])
# rules[p_57] = lambda _, s: [s[1]]
# productions[simple_statement] = [p_51, p_52, p_53, p_56, p_57]

# # <def_class>

# p_4 = Production(def_class, [class_, idx, ocur, class_statements, ccur])
# rules[p_4] = lambda _, s: ClassNode(s[2], s[4])
# p_5 = Production(def_class, [class_, idx, colon, idx, ocur, class_statements, ccur])
# rules[p_5] = lambda _, s: ClassNode(s[2], s[3], s[4])
# productions[def_class] = [p_4, p_5]

# # <class-statements>

# p_6 = Production(class_statements, [simple_statement, class_statements])
# rules[p_6] = lambda _, s: [s[1]] + s[2]
# p_58 = Production(class_statements, [def_func, class_statements])
# rules[p_58] = lambda _, s: [s[1]] + s[2]
# p_7 = Production(class_statements, [def_attr, class_statements])
# rules[p_7] = lambda _, s: [s[1]] + s[2]
# p_55 = Production(class_statements, [epsilon])
# rules[p_55] = lambda h, s: []
# productions[class_statements] = [p_6, p_58, p_7, p_55]

# # <def-agent>

# p_76 = Production(
#     def_agent,
#     [
#         idx,
#         idx,
#         equal,
#         ocur,
#         activation_condition,
#         colon,
#         bool_expr,
#         semi,
#         effect_time,
#         colon,
#         idx,
#         semi,
#         repetition,
#         colon,
#         idx,
#         semi,
#         action,
#         colon,
#         idx,
#         semi,
#     ],
# )
# rules[p_76] = lambda _, s: AgentDefNode(s[1], s[2], s[7], s[11], s[15], s[19])
# productions[def_agent] = [p_76]

# # <def-attr>

# p_8 = Production(def_attr, [idx, idx, equal, expr, semi])
# rules[p_8] = lambda _, s: AttrDeclarationNode(s[1], s[2], s[4])
# productions[def_attr] = [p_8]

# # <def-func>

# p_9 = Production(
#     def_func,
#     [function_, idx, opar, param_list, cpar, arrow, idx, ocur, func_statements, ccur],
# )
# rules[p_9] = lambda _, s: FuncDeclarationNode(s[2], s[4], s[7], s[9])
# productions[def_func] = [p_9]

# # <func-statements>

# p_78 = Production(func_statements, [simple_statement, func_statements])
# rules[p_78] = lambda _, s: [s[1]] + s[2]
# p_79 = Production(func_statements, [epsilon])
# rules[p_79] = lambda h, s: []
# productions[func_statements] = [p_78, p_79]

# # <def-var>

# p_15 = Production(def_var, [idx, idx, equal, expr, semi])
# rules[p_15] = lambda _, s: VarDeclarationNode(s[1], s[2], s[4])
# p_88 = Production(def_var, [def_rand_var])
# rules[p_88] = lambda _, s: [s[1]]
# productions[def_var] = [p_15, p_88]

# # <assignment>

# p_16 = Production(assignment, [idx, equal, expr, semi])
# rules[p_16] = lambda _, s: AssignmentNode(s[1], s[3])
# productions[assignment] = [p_16]

# # <param>

# p_10 = Production(param, [idx, idx])
# rules[p_10] = lambda _, s: (s[1], s[2])
# productions[param] = [p_10]

# # <param-list>

# p_11 = Production(param_list, [param, comma, param_list])
# rules[p_11] = lambda _, s: [s[1]] + s[2]
# p_12 = Production(param_list, [epsilon])
# rules[p_12] = lambda h, s: []
# productions[param_list] = [p_11, p_12]

# <expr>

p_13 = Production(expr, [arith])
rules[p_13] = lambda _, s: s[1]
p_64 = Production(expr, [bool_expr])
rules[p_64] = lambda _, s: s[1]
# p_14 = Production(expr, [prob_func])
# rules[p_14] = lambda _, s: s[1]
# p_17 = Production(expr, [rule])
# rules[p_17] = lambda _, s: s[1]
# p_18 = Production(expr, [def_effect])
# rules[p_18] = lambda _, s: s[1]
# p_19 = Production(expr, [func_call])
# rules[p_19] = lambda _, s: s[1]
# p_63 = Production(expr, [instance])
# rules[p_63] = lambda _, s: s[1]
# productions[expr] = [p_13, p_64, p_14, p_17, p_18, p_19, p_63]
productions[expr] = [p_13, p_64]

# <arith>

p_20 = Production(arith, [term])
rules[p_20] = lambda _, s: s[1]
p_21 = Production(arith, [arith, plus, term])
rules[p_21] = lambda _, s: PlusNode(s[1], s[3])
p_22 = Production(arith, [arith, minus, term])
rules[p_22] = lambda _, s: MinusNode(s[1], s[3])
productions[arith] = [p_20, p_21, p_22]

# <term>

p_80 = Production(term, [factor])
rules[p_80] = lambda _, s: s[1]
p_81 = Production(term, [term, star, factor])
rules[p_81] = lambda _, s: ByNode(s[1], s[3])
p_23 = Production(term, [term, div, factor])
rules[p_23] = lambda _, s: DivideNode(s[1], s[3])
productions[term] = [p_80, p_81, p_23]

# <factor>

p_24 = Production(factor, [atom])
rules[p_24] = lambda _, s: s[1]
p_25 = Production(factor, [opar, arith, cpar])
rules[p_25] = lambda _, s: s[2]
# p_26 = Production(factor, [opar, func_call, cpar])
# rules[p_26] = lambda _, s: s[2]
# productions[factor] = [p_24, p_25, p_26]
productions[factor] = [p_24, p_25]

# <atom>

p_28 = Production(atom, [idx])
rules[p_28] = lambda _, s: s[1]
# p_29 = Production(atom, [func_call])
# rules[p_29] = lambda _, s: s[1]
# productions[atom] = [p_28, p_29]
productions[atom] = [p_28]

# <bool-expr>

p_65 = Production(bool_expr, [bool_expr, and_, compare_expr])
rules[p_65] = lambda _, s: AndNode(s[1], s[3])
p_66 = Production(bool_expr, [bool_expr, or_, compare_expr])
rules[p_66] = lambda _, s: OrNode(s[1], s[3])
p_82 = Production(bool_expr, [compare_expr])
rules[p_82] = lambda _, s: s[1]
productions[bool_expr] = [p_65, p_66, p_82]

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
productions[compare_expr] = [p_70, p_67, p_68, p_69, p_83]

# <compare-factor>

p_84 = Production(compare_factor, [not_, compare_factor])
rules[p_84] = lambda _, s: NotNode(s[2])
p_71 = Production(compare_factor, [idx])
rules[p_71] = lambda _, s: s[1]
# p_72 = Production(compare_factor, [func_call])
# rules[p_72] = lambda _, s: s[1]
# p_73 = Production(compare_factor, [instance])
# rules[p_73] = lambda _, s: s[1]
p_74 = Production(compare_factor, [opar, bool_expr, opar])
rules[p_74] = lambda _, s: s[2]
# productions[compare_factor] = [p_84, p_71, p_72, p_73, p_74]
productions[compare_factor] = [p_84, p_71, p_74]

# # <func-call>

# p_31 = Production(func_call, [idx, opar, arg_list, cpar])
# rules[p_31] = lambda _, s: CallNode(s[1], s[3])
# p_32 = Production(func_call, [idx, dot, idx, opar, arg_list, cpar])
# rules[p_32] = lambda _, s: CallNode(s[3], s[5], obj=s[1])
# p_33 = Production(func_call, [func_call, dot, idx, opar, arg_list, cpar])
# rules[p_33] = lambda _, s: CallNode(s[3], s[5], obj=s[1])
# p_34 = Production(func_call, [instance, dot, idx, opar, arg_list, cpar])
# rules[p_34] = lambda _, s: CallNode(s[3], s[5], obj=s[1])
# productions[func_call] = [p_31, p_32, p_33, p_34]

# # <instance>

# p_62 = Production(instance, [idx, opar, arg_list, cpar])
# rules[p_62] = lambda _, s: InstanceNode(s[1], s[3])
# productions[instance] = [p_62]

# # <arg-list>

# p_35 = Production(arg_list, [epsilon])
# rules[p_35] = lambda h, s: []
# p_36 = Production(arg_list, [atom, comma, arg_list])
# rules[p_36] = lambda _, s: [s[1]] + s[2]
# p_37 = Production(arg_list, [arith, comma, arg_list])
# rules[p_37] = lambda _, s: [s[1]] + s[2]
# productions[arg_list] = [p_35, p_36, p_37]

# # <def-rand-var>

# p_39 = Production(def_rand_var, [idx, idx, equal, ocur, prob_func_list, ccur])
# rules[p_39] = lambda _, s: RandomVariableNode(s[2], s[5])
# productions[def_rand_var] = [p_39]

# # <prob-func-list>

# p_85 = Production(prob_func_list, [prob_func, prob_func_list])
# rules[p_85] = lambda _, s: [s[1]] + s[2]
# p_86 = Production(prob_func_list, [epsilon])
# rules[p_86] = lambda h, s: []
# productions[prob_func_list] = [p_85, p_86]

# # <prob-func>

# p_40 = Production(prob_func, [idx, arrow, def_effect])
# rules[p_40] = lambda _, s: ProbFunctionValueNode(s[1], s[3])
# productions[prob_func] = [p_40]

# # <def-effect>

# p_41 = Production(def_effect, [effect, idx, idx, idx])
# rules[p_41] = lambda _, s: EffectNode(s[2], s[3], s[4])
# p_42 = Production(def_effect, [rule])
# rules[p_42] = lambda _, s: EffectRuleNode(s[1])
# productions[def_effect] = [p_41, p_42]

# # <rule>

# p_43 = Production(rule, [bool_expr, rule_operator, assignment])
# rules[p_43] = lambda _, s: RuleNode(s[1], s[3])
# productions[rule] = [p_43]

# <for>

# p_45 = Production(
#     for_,
#     [for_kw, idx, in_, expr, ocur, body_statements, ccur],
# )
# rules[p_45] = lambda _, s: ForNode(s[2], s[4], s[6])
# productions[for_] = [p_45]

# <if>

# p_46 = Production(if_, [if_kw, expr, ocur, body_statements, ccur])
# rules[p_46] = lambda _, s: IfNode(s[2], s[4])
# productions[if_] = [p_46]

# <if-else>

# p_87 = Production(
#     if_,
#     [if_kw, expr, ocur, body_statements, ccur, else_kw, ocur, body_statements, ccur],
# )
# rules[p_87] = lambda _, s: IfElseNode(s[2], s[4], s[8])
# productions[if_else] = [p_87]


# <body_statements>

# p_59 = Production(body_statements, [simple_statement, body_statements])
# rules[p_59] = lambda _, s: [s[1]] + s[2]
# p_60 = Production(body_statements, [func_call, body_statements])
# rules[p_60] = lambda _, s: [s[1]] + s[2]
p_61 = Production(body_statements, [epsilon])
rules[p_61] = lambda h, s: []
# productions[body_statements] = [p_59, p_60, p_61]
productions[body_statements] = [p_61]


# all_terminals
name = "(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_)*"
num = "0|1|2|3|4|5|6|7|8|9|((1|2|3|4|5|6|7|8|9)U(0|1|2|3|4|5|6|7|8|9)*)"


_t = {
    f"{name}|{num}|RandVariableEffect|Patient|Parameter|Intervention|Symptom|int|double|simulate": (
        idx,
        1,
    ),
    "for": (for_kw, 2),
    "if": (if_kw, 2),
    "else": (else_kw, 2),
    "effect": (effect, 2),
    "in": (in_, 2),
    "is": (is_, 2),
    "=>": (rule_operator, 3),
    "->": (arrow, 3),
    ";": (semi, 4),
    ":": (colon, 4),
    ",": (comma, 4),
    ".": (dot, 4),
    "\(": (opar, 4),
    "\)": (cpar, 4),
    "{": (ocur, 4),
    "}": (ccur, 4),
    "=": (equal, 4),
    "+": (plus, 4),
    "-": (minus, 4),
    "\*": (star, 4),
    "/": (div, 4),
    ">": (gt, 4),
    "<": (lt, 4),
    "==": (equals_b, 4),
    "!=": (not_equals_b, 4),
    "not": (not_, 4),
    "and": (and_, 4),
    "or": (or_, 4),
    "class": (class_, 4),
    "function": (function_, 4),
    "activation_conditions": (activation_condition, 2),
    "effect_time": (effect_time, 2),
    "repetition": (repetition, 2),
    "action": (action, 2),
}

G = Grammar(non_terminals, terminals, productions, expr, rules)
G.epsilon = epsilon
