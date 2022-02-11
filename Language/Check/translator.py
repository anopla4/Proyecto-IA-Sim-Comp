from . import visitor
from ..Parsing.Node.declaration_nodes import *
from ..Parsing.Node.expression_nodes import *
from ..Parsing.Node.statement_nodes import *
from ..Parsing.Node.program_node import ProgramNode
from .type import *
from .error import *
from .scope import Scope


class Translator(object):
    @visitor.on("node")
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        statements = "\n".join(self.visit(child, tabs) for child in node.statements)
        import1 = "from Simulation.environment import Environment"
        import2 = "from Simulation.parameter import Parameter"
        import3 = "from Simulation.activation_rule import ActivationRule"
        import4 = "from Simulation.symptom import Symptom"
        import5 = "from Simulation.intervention import Intervention"
        return f"{import1}\n{import2}\n{import3}\n{import4}\n{import5}\n{statements}"

    @visitor.when(ClassNode)
    def visit(self, node, tabs=0):
        parent = "" if node.parent is None else f"({node.parent})"
        ans = "\t" * tabs + f"class {node.id}{parent}:"
        features = "\n".join(self.visit(child, tabs + 1) for child in node.statements)
        return f"{ans}\n{features}"

    @visitor.when(AttrDeclarationNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.expr)
        ans = "\t" * tabs + f"{node.id} = {expr}"
        return ans

    @visitor.when(VarDeclarationNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.expr)
        ans = "\t" * tabs + f"{node.id} = {expr}"
        return ans

    @visitor.when(AssignmentNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.expr)
        ans = "\t" * tabs + f"{node.id} = {expr}"
        return ans

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, tabs=0):
        params = ", ".join(param[1] for param in node.params)
        body = "\n".join(self.visit(child, tabs + 1) for child in node.body)
        ans = "\t" * tabs + f"def {node.id}({params}):\n{body}"
        return ans

    @visitor.when(BinaryNode)
    def visit(self, node, tabs=0):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ans = "\t" * tabs + f"{left} {node.symbol} {right}"
        return ans

    @visitor.when(UnaryNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.expr)
        ans = "\t" * tabs + f"{node.symbol} ({expr})"
        return ans

    @visitor.when(VariableNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"{node.lex}"

    @visitor.when(ConstantNumNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"{node.lex}"

    @visitor.when(StringNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f'"{node.lex}"'

    @visitor.when(CallNode)
    def visit(self, node, tabs=0):
        obj = f"{self.visit(node.obj)}." if node.obj != None else ""
        args = ",".join(self.visit(arg) for arg in node.arguments)
        ans = "\t" * tabs + f"{obj}{node.lex}({args})"
        return ans

    @visitor.when(InstanceNode)
    def visit(self, node, tabs=0):
        args = self.visit(node.arguments)
        return "\t" * tabs + f"{node.lex}({args})"

    @visitor.when(RuleNode)
    def visit(self, node, tabs=0):
        condition = ",".join([self.visit(cond) for cond in node.condition])
        dest = self.visit(node.destination)
        then_var = self.visit(node.then_var)
        then_val = self.visit(node.then_val)
        return (
            "\t" * tabs
            + f"Rule({{{condition}}}, destination={dest}, then=({then_var}, {then_val}))"
        )

    @visitor.when(ProbFunctionValueNode)
    def visit(self, node, tabs=0):
        num = "\t" * tabs + f"if p <= {self.visit(node.num)}:"
        value = "\t" * (tabs + 1) + f"return {self.visit(node.val)}"
        return f"{num}\n{value}"

    @visitor.when(ProbabilityFunctionNode)
    def visit(self, node, tabs=0):
        acc = 0
        args = []
        for v in node.values:
            num = self.visit(v.num)
            acc += float(num)
            v.num = ConstantNumNode(str(acc))
            args.append(self.visit(v, tabs + 1))
        args = "\n".join(args)
        return "\t" * tabs + f"def f(p): \n  {args}"

    @visitor.when(EffectNode)
    def visit(self, node, tabs=0):
        param = self.visit(node.par)
        env = self.visit(node.env)
        element = self.visit(node.e)
        condition = "\t" * tabs + f"if {env}.get_parameter({param}):"
        body = "\t" * (tabs + 1) + f"{env}.update_parameter({element}, {param})"
        return f"{condition}\n{body}"

    @visitor.when(EffectRuleNode)
    def visit(self, node, tabs=0):
        pass

    @visitor.when(AgentDefNode)
    def visit(self, node, tabs=0):
        conditions = self.visit(node.conditions)
        ans = (
            "\t" * tabs
            + f"{node.idt}({node.idn}, {conditions}, {node.t}, {node.rep}, f"
        )
        if node.supply != None:
            ans += f"{node.supply})\n"
        else:
            ans += ")\n"
        return ans

    @visitor.when(RandomVariableNode)
    def visit(self, node, tabs=0):
        pass

    @visitor.when(ForNode)
    def visit(self, node, tabs=0):
        stms = "\n".join([self.visit(arg, tabs + 1) for arg in node.body])
        var = self.visit(node.var)
        expr = self.visit(node.expr)
        ans = "\t" * tabs + f"for {var} in {expr}: \n {stms}"
        return ans

    @visitor.when(IfNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.expr)
        stms = "\n".join([self.visit(arg, tabs + 1) for arg in node.body])
        ans = "\t" * tabs + f"if {expr}: \n {stms}"
        return ans

    @visitor.when(IfElseNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.condition_if)
        stms_if = "\n".join([self.visit(arg, tabs + 1) for arg in node.body_if])
        stms_else = "\n".join([self.visit(arg, tabs + 1) for arg in node.body_else])
        ans_if = "\t" * tabs + f"if {expr}: \n {stms_if}"
        ans_else = "\t" * tabs + f"else: \n {stms_else}"
        return f"{ans_if}\n{ans_else}"

    @visitor.when(ItemNode)
    def visit(self, node, tabs=0):
        key = self.visit(node.key)
        value = self.visit(node.val)
        return "\t" * tabs + f"{key}: {value}"

    @visitor.when(DictNode)
    def visit(self, node, tabs=0):
        items = ", ".join([self.visit(i) for i in node.items])
        return "\t" * tabs + f"{{{items}}}"

    @visitor.when(ListNode)
    def visit(self, node, tabs=0):
        items = ", ".join([self.visit(i) for i in node.items])
        return "\t" * tabs + f"[{items}]"

    @visitor.when(TupleNode)
    def visit(self, node, tabs=0):
        items = ", ".join([self.visit(i) for i in node.items])
        return "\t" * tabs + f"({items})"

    @visitor.when(ReturnNode)
    def visit(self, node, tabs=0):
        expr = self.visit(node.expr)
        return "\t" * tabs + f"return {expr}"
