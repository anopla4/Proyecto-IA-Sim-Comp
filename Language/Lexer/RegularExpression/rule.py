from Language.Parsing.non_terminal import NonTerminal


class ProductionRules:
    def __init__(
        self,
        inherited_rules_functions=None,
        synthesized_rules_functions=None,
    ) -> None:
        self.inherited_rules_functions = inherited_rules_functions
        self.synthesized_rules_functions = synthesized_rules_functions
        self.symbols_nodes = {}

    def run_attributes_functions(self, symbol, attr_type):
        functions = (
            self.inherited_rules_functions
            if attr_type == "inherited"
            else self.synthesized_rules_functions
        )
        if symbol in functions:
            functions = functions[symbol]
        else:
            functions = {}
        for arg, body in functions.items():
            _, attribute = arg
            if len(body) > 2 or not isinstance(body[0], NonTerminal):
                obj = body[0]
                args = [
                    getattr(self.symbols_nodes[i], attr) for i, attr in list(body)[1:]
                ]
                val = obj(*args)
            else:
                n = self.symbols_nodes[body[0]]
                attr = body[1]
                val = getattr(n, attr)
            setattr(self.symbols_nodes[symbol], attribute, val)

    def run_synthesized_attributes_functions(self, symbol, symbols_nodes, p):
        node = symbol.alphabet_symbol
        functions = self.synthesized_rules_functions[node]
        for arg, body in functions.items():
            _, attribute = arg
            attribute_synthesized_symbol = body
            if len(attribute_synthesized_symbol) > 1:
                obj = attribute_synthesized_symbol[0]
                args = [
                    (symbols_nodes[i][attr])
                    for i, attr in list(attribute_synthesized_symbol)[1:]
                ]
                val = obj(*args)
            else:
                n = symbols_nodes[attribute_synthesized_symbol[0]]
                attr = attribute_synthesized_symbol[1]
                val = n[attr]
            node[attribute] = val
