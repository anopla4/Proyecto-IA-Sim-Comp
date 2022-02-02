from shift_reduce_parser import ShiftReduceParser
from Lenguage.Lexer.RegularExpression.rule import ProductionRules


def build_ast(actions, productions, tokens, G):
    if not actions or not productions or not tokens:
        return None
    
    stack = []

    producitons = iter(productions)
    tokens = iter(tokens)

    for action in actions:
        if action == ShiftReduceParser.SHIFT:
            stack.append(next(tokens))
        elif action == ShiftReduceParser.REDUCE:
            production = next(productions)
            tokens_production = [None] + stakc[-len(production.right_side):]
            rule = G.rules[production][0] #sinthetyzed rule

            if len(production.right_side):
                value = rule(None, tokens_production)
                stack[-len(production.right_side):] = value
            else:
                stack.append(rule(None, None))

    if not isinstance(next(token), type(G.EOF)):
        raise "Cadena invalida"
    return stack[0]


    

