from Language.Lexer.RegularExpression.rule import ProductionRules
from Language.Parsing.epsilon import Epsilon
from Language.Parsing.non_terminal import NonTerminal
from Language.Parsing.terminal import Terminal

# from .regex_grammar import rules


class Node:
    def __init__(
        self, alphabet_symbol, ast=None, tmp=None, children: list = []
    ) -> None:
        self.alphabet_symbol = alphabet_symbol
        self.ast = ast
        self.tmp = tmp
        self.parent = None
        self.children = children
        self.symbol = (
            alphabet_symbol
            if isinstance(alphabet_symbol, NonTerminal)
            else alphabet_symbol.symbol
        )
        self.out_symbol = None


def build_ast(ll_table, s, sym, rules=None):
    i = 0
    root = Node(sym)
    stack = [[root, []]]
    productions_stack = []
    productions_rules_stack = []
    while stack:
        node, children_nodes = stack[-1]
        if (
            isinstance(node.alphabet_symbol, Terminal)
            and s[i] == node.alphabet_symbol.symbol
        ):
            i += 1
            stack.pop(-1)
        node, children_nodes = stack[-1]
        if children_nodes or isinstance(node.alphabet_symbol, Epsilon):
            temp, _ = stack.pop(-1)
            if children_nodes:
                p = productions_stack.pop(-1)
                pr = productions_rules_stack.pop(-1)
                pr.run_attributes_functions(node.out_symbol, "synthesized")
        else:
            if productions_stack:
                p = productions_stack[-1]
                pr = productions_rules_stack[-1]
                pr.run_attributes_functions(node.alphabet_symbol, "inherited")
            p = None
            if i == len(s):
                nt = (
                    node.alphabet_symbol
                    if node.alphabet_symbol.type == None
                    else node.alphabet_symbol.type
                )
                for terminal in ll_table[nt]:
                    production = ll_table[nt][terminal]
                    if production and isinstance(production.right_side[0], Epsilon):
                        p = production
                        ast_node = node
                        ast_node.out_symbol = p.left_side
                        pr = ProductionRules(
                            rules[p].inherited_rules_functions,
                            rules[p].synthesized_rules_functions,
                        )
                        pr.symbols_nodes[p.left_side] = ast_node
                        productions_stack.append(p)
                        productions_rules_stack.append(pr)
                        temp = []
                        for j in p.right_side:
                            ast_node = Node(j)
                            pr.symbols_nodes[j] = ast_node
                            temp.append([ast_node, []])
                            children_nodes.append(ast_node)
                        stack += list(reversed(temp))
                        break
            else:
                nt = (
                    node.alphabet_symbol
                    if node.alphabet_symbol.type == None
                    else node.alphabet_symbol.type
                )
                p = [
                    ll_table[nt][terminal]
                    for terminal in ll_table[nt]
                    if s[i] == terminal.symbol and ll_table[nt][terminal] != None
                ]
                if p:
                    p = p[0]
                    productions_stack.append(p)
                    pr = ProductionRules(
                        rules[p].inherited_rules_functions,
                        rules[p].synthesized_rules_functions,
                    )
                    productions_rules_stack.append(pr)
                    ast_node = node
                    ast_node.out_symbol = p.left_side
                    pr.symbols_nodes[p.left_side] = ast_node
                    temp = []
                    for j in p.right_side:
                        ast_node = Node(j)
                        pr.symbols_nodes[j] = ast_node
                        temp.append([ast_node, []])
                        children_nodes.append(ast_node)
                    stack += list(reversed(temp))
    return root
