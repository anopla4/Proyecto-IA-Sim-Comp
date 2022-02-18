from ..non_terminal import NonTerminal
from ..terminal import Terminal
from ..production import Production
from ..Node.declaration_nodes import *
from ..Node.expression_nodes import *
from ..Node.statement_nodes import *
from ..Node.program_node import ProgramNode
from ..Grammar import Grammar


def get_grammar():
    # non terminals
    program, elements_list = NonTerminal.get_non_terminals("<program> <elements-list>")
    statement, simple_statement = NonTerminal.get_non_terminals(
        "<statement> <simple-statement>"
    )
    def_class, body_statements = NonTerminal.get_non_terminals(
        "<def-class> <body-statements>"
    )
    (
        def_func,
        def_var,
        assignment,
    ) = NonTerminal.get_non_terminals("<def-func> <def-var> <assignment>")
    def_agent = NonTerminal("<def-agent>")
    param, param_list = NonTerminal.get_non_terminals("<param> <param-list>")
    instance = NonTerminal("<instance>")
    def_rand_var, def_effect, def_effect_list = NonTerminal.get_non_terminals(
        "<def-rand-var> <def-effect> <def-effect-list>"
    )
    expr, arith, term, factor, atom = NonTerminal.get_non_terminals(
        "<expr> <arith> <term> <factor> <atom>"
    )
    func_call, arg_list = NonTerminal.get_non_terminals("<func-call> <arg-list>")
    prob_func, prob_func_list, rule = NonTerminal.get_non_terminals(
        "<prob-func> <prob-func-list> <rule>"
    )
    for_, if_, if_else = NonTerminal.get_non_terminals("<for> <if> <if-else>")
    or_expr, and_expr, not_expr, compare_expr = NonTerminal.get_non_terminals(
        "<or-expr> <and-expr> <not-expr> <compare-factor>"
    )
    dict_, dict_items_list, dict_item = NonTerminal.get_non_terminals(
        "<dict> <dict-items-list> <dict-item>"
    )
    return_ = NonTerminal("<return>")
    tuple_, list_ = NonTerminal.get_non_terminals("<tuple> <list>")
    string = NonTerminal("<string>")
    idxs = NonTerminal("<idxs>")
    nums = NonTerminal("<nums>")
    non_terminals = [
        idxs,
        string,
        program,
        elements_list,
        statement,
        return_,
        simple_statement,
        def_class,
        body_statements,
        def_func,
        def_var,
        assignment,
        def_agent,
        param,
        param_list,
        instance,
        def_rand_var,
        def_effect,
        def_effect_list,
        expr,
        arith,
        term,
        factor,
        atom,
        or_expr,
        and_expr,
        not_expr,
        arg_list,
        prob_func_list,
        rule,
        if_,
        if_else,
        func_call,
        for_,
        dict_,
        dict_items_list,
        dict_item,
        tuple_,
        list_,
        prob_func,
        compare_expr,
        nums,
    ]

    # terminals

    epsilon = Terminal("epsilon")
    effect = Terminal("effect")
    return_kw = Terminal("return")
    in_, on, is_ = Terminal.get_terminals("in on is")
    rule_operator, arrow = Terminal.get_terminals("=> ->")
    (
        semi,
        colon,
        comma,
        dot,
        opar,
        cpar,
        ocur,
        ccur,
        quotation_marks,
    ) = Terminal.get_terminals('; : , . ( ) { } " ')
    equal, plus, minus, star, div = Terminal.get_terminals("= + - * /")
    gt, lt, equals_b, not_equals_b, not_, and_, or_ = Terminal.get_terminals(
        "> < == != not and or"
    )
    idx, int_, double_, class_, function_ = Terminal.get_terminals(
        "idx int double class function"
    )
    for_kw, if_kw, else_kw = Terminal.get_terminals("for if else")
    activation_condition, effect_time, repetition, action = Terminal.get_terminals(
        "activationCondition effectTime repetition action"
    )
    supply = Terminal("supply")
    type_ = Terminal("type")
    new_ = Terminal("new")
    osquare_br, csquare_br = Terminal.get_terminals("[ ]")
    false_, true_ = Terminal.get_terminals("false true")
    terminals = [
        false_,
        true_,
        type_,
        new_,
        epsilon,
        effect,
        in_,
        rule_operator,
        quotation_marks,
        semi,
        equal,
        gt,
        idx,
        for_kw,
        activation_condition,
        arrow,
        colon,
        return_kw,
        comma,
        dot,
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
        on,
        class_,
        function_,
        if_kw,
        else_kw,
        effect_time,
        repetition,
        action,
        osquare_br,
        csquare_br,
        supply,
        int_,
        double_,
    ]

    rules = {}
    productions = {}

    # <program>

    p_77 = Production(program, [elements_list])
    rules[p_77] = lambda _, s: ProgramNode(s[1])
    productions[program] = [p_77]

    # <elements-list>

    p_0 = Production(elements_list, [statement, elements_list])
    rules[p_0] = lambda _, s: [s[1]] + s[2]
    p_49 = Production(elements_list, [statement])
    rules[p_49] = lambda _, s: [s[1]]
    productions[elements_list] = [p_0, p_49]

    # <statement>

    p_1 = Production(statement, [def_class])
    rules[p_1] = lambda _, s: s[1]
    p_2 = Production(statement, [def_func])
    rules[p_2] = lambda _, s: s[1]
    p_75 = Production(statement, [def_agent])
    rules[p_75] = lambda _, s: s[1]
    p_54 = Production(statement, [simple_statement])
    rules[p_54] = lambda _, s: s[1]
    productions[statement] = [p_54, p_2, p_1, p_75]

    # <simple-statement>

    p_51 = Production(simple_statement, [if_])
    rules[p_51] = lambda _, s: s[1]
    p_52 = Production(simple_statement, [if_else])
    rules[p_52] = lambda _, s: s[1]
    p_53 = Production(simple_statement, [for_])
    rules[p_53] = lambda _, s: s[1]
    p_97 = Production(simple_statement, [func_call])
    rules[p_97] = lambda _, s: s[1]
    p_56 = Production(simple_statement, [def_var])
    rules[p_56] = lambda _, s: s[1]
    p_57 = Production(simple_statement, [assignment])
    rules[p_57] = lambda _, s: s[1]
    productions[simple_statement] = [p_51, p_52, p_53, p_97, p_57, p_56]

    # <def_class>

    p_4 = Production(def_class, [class_, idx, ocur, statement, ccur])
    rules[p_4] = lambda _, s: ClassNode(s[2].expression, s[4])
    p_5 = Production(def_class, [class_, idx, colon, idx, ocur, statement, ccur])
    rules[p_5] = lambda _, s: ClassNode(s[2].expression, s[3], s[4])
    productions[def_class] = [p_4, p_5]

    # <def-agent>

    p_76 = Production(
        def_agent,
        [
            type_,
            idx,
            equal,
            ocur,
            activation_condition,
            colon,
            list_,
            semi,
            effect_time,
            colon,
            nums,
            semi,
            repetition,
            colon,
            nums,
            semi,
            action,
            colon,
            idx,
            semi,
            ccur,
        ],
    )
    rules[p_76] = lambda _, s: AgentDefNode(
        s[1].expression, s[2].expression, s[7], s[11], s[15], s[19].expression
    )
    p_109 = Production(
        def_agent,
        [
            type_,
            idx,
            equal,
            ocur,
            activation_condition,
            colon,
            list_,
            semi,
            effect_time,
            colon,
            nums,
            semi,
            repetition,
            colon,
            nums,
            semi,
            action,
            colon,
            idx,
            semi,
            supply,
            colon,
            nums,
            semi,
            ccur,
        ],
    )
    rules[p_109] = lambda _, s: AgentDefNode(
        s[1].expression, s[2].expression, s[7], s[11], s[15], s[19].expression, s[23]
    )
    productions[def_agent] = [p_76, p_109]

    # <def-func>

    p_9 = Production(
        def_func,
        [
            function_,
            idx,
            opar,
            param_list,
            cpar,
            arrow,
            type_,
            ocur,
            body_statements,
            ccur,
        ],
    )
    rules[p_9] = lambda _, s: FuncDeclarationNode(
        s[2].expression, s[4], s[7].expression, s[9]
    )
    productions[def_func] = [p_9]

    # <def-var>

    p_15 = Production(def_var, [type_, idx, equal, expr, semi])
    rules[p_15] = lambda _, s: VarDeclarationNode(
        s[1].expression, s[2].expression, s[4]
    )
    productions[def_var] = [p_15]

    # <assignment>

    p_16 = Production(assignment, [idx, equal, expr, semi])
    rules[p_16] = lambda _, s: AssignmentNode(s[1].expression, s[3])
    productions[assignment] = [p_16]

    # <param>

    p_10 = Production(param, [type_, idx])
    rules[p_10] = lambda _, s: (s[1].expression, s[2].expression)
    productions[param] = [p_10]

    # <param-list>

    p_11 = Production(param_list, [param, comma, param_list])
    rules[p_11] = lambda _, s: [s[1]] + s[3]
    p_98 = Production(param_list, [param])
    rules[p_98] = lambda _, s: [s[1]]
    p_12 = Production(param_list, [epsilon])
    rules[p_12] = lambda h, s: []
    productions[param_list] = [p_11, p_12, p_98]

    # <expr>

    p_64 = Production(expr, [or_expr])
    rules[p_64] = lambda _, s: s[1]
    p_17 = Production(expr, [rule])
    rules[p_17] = lambda _, s: s[1]
    p_63 = Production(expr, [instance])
    rules[p_63] = lambda _, s: s[1]
    p_88 = Production(expr, [def_rand_var])
    rules[p_88] = lambda _, s: s[1]
    productions[expr] = [p_64, p_63, p_17, p_88]

    # <arith>

    p_20 = Production(arith, [term])
    rules[p_20] = lambda _, s: s[1]
    p_21 = Production(arith, [term, plus, arith])
    rules[p_21] = lambda _, s: PlusNode(s[1], s[3])
    p_22 = Production(arith, [term, minus, arith])
    rules[p_22] = lambda _, s: MinusNode(s[1], s[3])

    productions[arith] = [p_20, p_21, p_22]

    # <term>

    p_80 = Production(term, [factor])
    rules[p_80] = lambda _, s: s[1]
    p_81 = Production(term, [factor, star, term])
    rules[p_81] = lambda _, s: ByNode(s[1], s[3])
    p_23 = Production(term, [factor, div, term])
    rules[p_23] = lambda _, s: DivideNode(s[1], s[3])
    productions[term] = [p_80, p_81, p_23]

    # <factor>

    p_24 = Production(factor, [atom])
    rules[p_24] = lambda _, s: s[1]
    p_25 = Production(factor, [opar, or_expr, cpar])
    rules[p_25] = lambda _, s: s[2]
    productions[factor] = [p_24, p_25]

    # <string>
    p_115 = Production(string, [quotation_marks, idxs, quotation_marks])
    rules[p_115] = lambda _, s: StringNode(s[2])
    productions[string] = [p_115]

    # <idxs>
    p_113 = Production(idxs, [idx, idxs])
    rules[p_113] = lambda _, s: s[1].expression + s[2]
    p_114 = Production(idxs, [epsilon])
    rules[p_114] = lambda _, s: ""
    productions[idxs] = [p_113, p_114]
    # <atom>

    p_28 = Production(atom, [idx])
    rules[p_28] = lambda _, s: VariableNode(s[1].expression)
    p_108 = Production(atom, [nums])
    rules[p_108] = lambda _, s: s[1]
    p_112 = Production(atom, [string])
    rules[p_112] = lambda _, s: s[1]
    p_29 = Production(atom, [func_call])
    rules[p_29] = lambda _, s: s[1]
    p_100 = Production(atom, [dict_])
    rules[p_100] = lambda _, s: s[1]
    p_101 = Production(atom, [tuple_])
    rules[p_101] = lambda _, s: s[1]
    p_102 = Production(atom, [list_])
    rules[p_102] = lambda _, s: s[1]
    p_110 = Production(atom, [false_])
    rules[p_110] = lambda _, s: BooleanNode(s[1])
    p_111 = Production(atom, [true_])
    rules[p_111] = lambda _, s: BooleanNode(s[1])
    productions[atom] = [p_28, p_29, p_100, p_102, p_101, p_108, p_110, p_111, p_112]

    # <or-expr>

    p_65 = Production(or_expr, [and_expr, or_, or_expr])
    rules[p_65] = lambda _, s: OrNode(s[1], s[3])
    p_82 = Production(or_expr, [and_expr])
    rules[p_82] = lambda _, s: s[1]
    productions[or_expr] = [p_65, p_82]

    # <and-expr>

    p_89 = Production(and_expr, [not_expr, and_, and_expr])
    rules[p_89] = lambda _, s: AndNode(s[1], s[3])
    p_93 = Production(and_expr, [not_expr])
    rules[p_93] = lambda _, s: s[1]
    productions[and_expr] = [p_89, p_93]

    # <not-expr>

    p_91 = Production(not_expr, [not_, compare_expr])
    rules[p_91] = lambda _, s: NotNode(s[2])
    p_92 = Production(not_expr, [compare_expr])
    rules[p_92] = lambda _, s: s[1]
    productions[not_expr] = [p_91, p_92]

    # <compare-expr>

    p_67 = Production(compare_expr, [arith, equals_b, compare_expr])
    rules[p_67] = lambda _, s: EqualsNode(s[1], s[3])
    p_68 = Production(compare_expr, [arith, not_equals_b, compare_expr])
    rules[p_68] = lambda _, s: NotEqualsNode(s[1], s[3])
    p_69 = Production(compare_expr, [arith, lt, compare_expr])
    rules[p_69] = lambda _, s: LesserNode(s[1], s[3])
    p_83 = Production(compare_expr, [arith, gt, compare_expr])
    rules[p_83] = lambda _, s: GreaterNode(s[1], s[3])
    p_94 = Production(compare_expr, [arith])
    rules[p_94] = lambda _, s: s[1]
    productions[compare_expr] = [p_67, p_68, p_69, p_83, p_94]

    # <func-call>

    p_31 = Production(func_call, [idx, opar, arg_list, cpar])
    rules[p_31] = lambda _, s: CallNode(s[1].expression, s[3])
    p_32 = Production(func_call, [idx, dot, idx, opar, arg_list, cpar])
    rules[p_32] = lambda _, s: CallNode(s[3].expression, s[5], obj=s[1].expression)
    p_33 = Production(func_call, [func_call, dot, idx, opar, arg_list, cpar])
    rules[p_33] = lambda _, s: CallNode(s[3].expression, s[5], obj=s[1])
    productions[func_call] = [p_31, p_32, p_33]

    # <instance>

    p_62 = Production(instance, [new_, type_, opar, arg_list, cpar])
    rules[p_62] = lambda _, s: InstanceNode(s[2].expression, s[4])
    productions[instance] = [p_62]

    # <arg-list>

    p_35 = Production(arg_list, [epsilon])
    rules[p_35] = lambda h, s: []
    p_36 = Production(arg_list, [expr, comma, arg_list])
    rules[p_36] = lambda _, s: [s[1]] + s[3]
    p_37 = Production(arg_list, [expr])
    rules[p_37] = lambda _, s: [s[1]]
    productions[arg_list] = [p_35, p_36, p_37]

    # <def-rand-var>

    p_39 = Production(def_rand_var, [ocur, prob_func_list, ccur])
    rules[p_39] = lambda _, s: ProbabilityFunctionNode(s[2])
    productions[def_rand_var] = [p_39]

    # <prob-func-list>

    p_85 = Production(prob_func_list, [prob_func, semi, prob_func_list])
    rules[p_85] = lambda _, s: [s[1]] + s[3]
    p_86 = Production(prob_func_list, [prob_func])
    rules[p_86] = lambda h, s: [s[1]]
    productions[prob_func_list] = [p_85, p_86]

    # <prob-func>

    p_40 = Production(prob_func, [nums, arrow, def_effect_list])
    rules[p_40] = lambda _, s: ProbFunctionValueNode(s[1], s[3])
    productions[prob_func] = [p_40]

    # <def-effect-list>

    p_18 = Production(def_effect_list, [def_effect, comma, def_effect_list])
    rules[p_18] = lambda _, s: [s[1]] + s[3]
    p_116 = Production(def_effect_list, [def_effect])
    rules[p_116] = lambda _, s: [s[1]]
    productions[def_effect_list] = [p_18, p_116]

    # <def-effect>

    p_41 = Production(def_effect, [effect, idx, idx, nums])
    rules[p_41] = lambda _, s: EffectNode(
        VariableNode(s[2].expression), VariableNode(s[3].expression), s[4]
    )
    productions[def_effect] = [p_41]

    # <rule>

    p_43 = Production(rule, [dict_, on, atom, rule_operator, tuple_])
    rules[p_43] = lambda _, s: RuleNode(s[1], s[3], s[5])
    productions[rule] = [p_43]

    # <dict>

    p_107 = Production(dict_, [ocur, dict_items_list, ccur])
    rules[p_107] = lambda _, s: DictNode(s[2])
    productions[dict_] = [p_107]

    # <dict-items-list>

    p_96 = Production(dict_items_list, [dict_item, comma, dict_items_list])
    rules[p_96] = lambda _, s: [s[1]] + s[3]
    p_106 = Production(dict_items_list, [dict_item])
    rules[p_106] = lambda _, s: [s[1]]
    productions[dict_items_list] = [p_96, p_106]

    # <dict-item>

    p_105 = Production(dict_item, [atom, colon, atom])
    rules[p_105] = lambda _, s: ItemNode(s[1], s[3])
    productions[dict_item] = [p_105]

    # <tuple>

    p_103 = Production(tuple_, [ocur, arg_list, ccur])
    rules[p_103] = lambda _, s: TupleNode(s[2])
    productions[tuple_] = [p_103]

    # <list>

    p_104 = Production(list_, [osquare_br, arg_list, csquare_br])
    rules[p_104] = lambda _, s: ListNode(s[2])
    productions[list_] = [p_104]

    # <for>

    p_45 = Production(
        for_,
        [for_kw, idx, in_, expr, ocur, body_statements, ccur],
    )
    rules[p_45] = lambda _, s: ForNode(s[2], s[4].expression, s[6])
    productions[for_] = [p_45]

    # <if>

    p_46 = Production(if_, [if_kw, expr, ocur, body_statements, ccur])
    rules[p_46] = lambda _, s: IfNode(s[2], s[4])
    productions[if_] = [p_46]

    # <if-else>

    p_87 = Production(
        if_else,
        [
            if_kw,
            expr,
            ocur,
            body_statements,
            ccur,
            else_kw,
            ocur,
            body_statements,
            ccur,
        ],
    )
    rules[p_87] = lambda _, s: IfElseNode(s[2], s[4], s[8])
    productions[if_else] = [p_87]

    # <body_statements>

    p_59 = Production(body_statements, [simple_statement, body_statements])
    rules[p_59] = lambda _, s: [s[1]] + s[2]
    p_95 = Production(body_statements, [return_, body_statements])
    rules[p_95] = lambda h, s: [s[1]] + s[2]
    p_61 = Production(body_statements, [epsilon])
    rules[p_61] = lambda h, s: []
    productions[body_statements] = [p_59, p_61, p_95]

    # <return>

    p_99 = Production(return_, [return_kw, expr])
    rules[p_99] = lambda _, s: ReturnNode(s[2])
    productions[return_] = [p_99]

    # <nums>

    p_111 = Production(nums, [int_])
    rules[p_111] = lambda _, s: IntNode(s[1].expression)
    p_112 = Production(nums, [double_])
    rules[p_112] = lambda _, s: DoubleNode(s[1].expression)
    productions[nums] = [p_111, p_112]

    # all_terminals
    upper = "A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z"
    name = f"({upper}|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_)+({upper}|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_)*"
    num_p = "1|2|3|4|5|6|7|8|9|((1|2|3|4|5|6|7|8|9)+(0|1|2|3|4|5|6|7|8|9)*)"
    num_ = f"0|{num_p}"
    num_n = f"-+({num_p})"
    num_int = f"({num_p})|({num_n})|0"
    num_double = f"({num_int}|(-+0))+.+0*+({num_p})"

    _t = {
        f"{name}|simulate": (
            idx,
            1,
        ),
        f"{num_int}": (int_, 1),
        f"{num_double}": (double_, 3),
        "Tree|RandVarEffect|ActivationRule|Environment|Patient|Parameter|Agent|Intervention|Symptom|int|double|Tuple|Dict|List|void|bool": (
            type_,
            2,
        ),
        "return": (return_kw, 3),
        "new": (new_, 3),
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
        "\+": (plus, 4),
        "-": (minus, 2),
        "\*": (star, 4),
        "[": (osquare_br, 4),
        "]": (csquare_br, 4),
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
        "supply": (supply, 2),
        "on": (on, 2),
        "true": (true_, 2),
        "false": (false_, 2),
        '"': (quotation_marks, 2),
    }

    G = Grammar(non_terminals, terminals, productions, program, rules)
    G.epsilon = epsilon
    return G, _t
