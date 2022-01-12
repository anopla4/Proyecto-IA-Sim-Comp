from Language.Parsing.terminal import Terminal
from Language.Parsing.epsilon import Epsilon


class Tree:
    def __init__(self, root) -> None:
        self.root = root


class TreeNode:
    def __init__(self, value, args) -> None:
        self.value = value
        self.children = args


def build_cst(ll_table, s, symbol):
    i = 0
    node = TreeNode(symbol, [])
    cst = Tree(node)
    stack = [node]
    while stack:
        node = stack.pop(-1)
        if i == len(s):
            node = stack.pop(-1)
            p = None
            for terminal in ll_table[node.value]:
                production = ll_table[node.value][terminal]
                if production and isinstance(production.right_side[0], Epsilon):
                    p = production
                    break
            if p != None:
                new_child = TreeNode(p.right_side[0], [])
                node.children.append(new_child)
        else:
            p = [
                ll_table[node.value][terminal]
                for terminal in ll_table[node.value]
                if s[i] == terminal.symbol and ll_table[node.value][terminal] != None
            ][0]
            children = list(reversed(p.right_side))
            for j in range(len(children)):
                new_child = TreeNode(children[j], [])
                node.children.append(new_child)
                if isinstance(children[j], Terminal) and s[i] == children[j].symbol:
                    i += 1
                elif not isinstance(children[j], Epsilon) and children[j].symbol != ")":
                    stack.append(new_child)
        print(f"{node.value.symbol} -> {[a.value.symbol for a in node.children]}")

    return cst
