from .shift_reduce_parser import ShiftReduceParser


def build_ast(actions, productions, tokens, G):
    if not actions or not productions or not tokens:
        return None

    stack = []

    productions = iter(productions)
    tokens = iter(tokens)

    for action in actions:
        if action == ShiftReduceParser.SHIFT:
            stack.append(next(tokens))
        elif action == ShiftReduceParser.REDUCE:
            production = next(productions)
            flag = False
            if production.right_side[0] != G.epsilon:
                tokens_production = [None] + stack[-len(production.right_side) :]
                flag = True
            rule = G.rules[production]  # synthesized rule
            l = []
            l.append(object)
            if len(production.right_side) and flag:
                value = rule(None, tokens_production)
                stack[-len(production.right_side) :] = [value]
            else:
                stack.append(rule(None, None))
    if not next(tokens).type[0] == G.EOF:
        raise "Cadena invalida"
    return stack[0]
