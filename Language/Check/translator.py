import visitor
from ..Parsing.Node.declaration_nodes import *
from ..Parsing.Node.expression_nodes import *
from ..Parsing.Node.statement_nodes import *
from ..Parsing.Node.program_node import ProgramNode
from .type import *
from .error import *
from .scope import Scope


class FormatVisitor(object):
    @visitor.on("node")
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        statements = "\n".join(self.visit(child, tabs) for child in node.statements)
        return f"{statements}"

    @visitor.when(ClassNode)
    def visit(self, node, tabs=0):
        parent = "" if node.parent is None else f"({node.parent})"
        ans = "\t" * tabs + f"class {node.id} {parent}: {{ {node.statements} }}"
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
        params = ", ".join(param for param in node.params_names)
        body = "\n".join(self.visit(child, tabs + 1) for child in node.body)
        ans = "\t" * tabs + f"def {node.id}({params}): {body}"
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
        ans = "\t" * tabs + f"{node.symbol} {expr}"
        return ans

    @visitor.when(VariableNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"{node.lex}"

    @visitor.when(ConstantNumNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"{node.lex}"

    @visitor.when(CallNode)
    def visit(self, node, tabs=0):
        obj = f"{self.visit(node.obj)}." if node.obj != None else ""
        args = ",".join(arg for arg in node.arguments)
        ans = "\t" * tabs + f"{obj}{node.lex}({args})"
        return ans

    @visitor.when(InstanceNode)
    def visit(self, node, tabs=0):
        args = self.visit(node.arguments)
        return "\t" * tabs + f"{node.lex}({args})"

    @visitor.when(RuleNode)
    def visit(self, node, tabs=0):
        expr_l = self.visit(node.left)
        expr_r = self.visit(node.right)
        return "\t" * tabs + f"if {expr_l}: \n\t {expr_r}"

    @visitor.when(ProbFunctionValueNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"if p < {node.num}: \n\t return {node.val}"

    @visitor.when(ProbabilityFunctionNode)
    def visit(self, node, tabs=0):
        acc = 0
        args = []
        for v in node.values:
            v.num = str(acc + int(v.num))
            args.append(self.visitor(v, tabs + 1))
        args = "\n".join(args)
        return "\t" * tabs + f"def f(): \n  {args}"

    @visitor.when(EfectNode)
    def visit(self, node, tabs=0):
        return f"update_parameter({node.par, node.e})"

    @visitor.when(EfectRuleNode)
    def visit(self, node, tabs=0):
        pass

    @visitor.when(AgentDefNode)
    def visit(self, node, tabs=0):
        conditions = self.visitor(node.conditions)
        ans = (
            "\t" * tabs
            + f"{node.idt}({node.idn}, {conditions}, {node.t}, {node.repetition}, {node.action}"
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
        stms = "\n".join([self.visitor(arg, tabs + 1) for arg in node.body])
        ans = "\t" * tabs + f"for {node.var} in {node.expr}: \n {stms}"
        return ans

    @visitor.when(IfNode)
    def visit(self, node, tabs=0):
        expr = self.visitor(node.expr)
        stms = "\n".join([self.visitor(arg, tabs + 1) for arg in node.body])
        ans = "\t" * tabs + f"if {expr}: \n {stms}"
        return ans

    @visitor.when(IfElseNode)
    def visit(self, node, tabs=0):
        expr = self.visitor(node.expr)
        stms_if = "\n".join([self.visitor(arg, tabs + 1) for arg in node.body_if])
        stms_else = "\n".join([self.visitor(arg, tabs + 1) for arg in node.body_else])
        ans = "\t" * tabs + f"if {expr}: \n {stms_if} \n else: \n {stms_else}"
        return ans
