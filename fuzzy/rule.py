from action import Action


class Rule:
    def Rule(self, 
        var_conditions:list[tuple[str,str]], action_conditions:list[Action], then:tuple[str,str]):
        self.and_conditions = var_conditions
        self.then = then
        self.action_conditions = action_conditions

    def get_target(self)-> str:
        return self.then[0]