import Language.Check.visitor as visitor
from ..Parsing.Node.declaration_nodes import *
from ..Parsing.Node.expression_nodes import *
from ..Parsing.Node.statement_nodes import *
from ..Parsing.Node.program_node import ProgramNode
from .type import *
from .error import *
from .scope import Scope


class SemanticChecker(object):
    def __init__(self, context, errors=[]) -> None:
        self.context = context
        self.current_type = [context.types["Main"]]
        self.current_method = None
        self.errors = errors

    @visitor.on("node")
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope()
        for declaration in node.statements:
            self.visit(declaration, scope.create_child())
        return scope

    @visitor.when(ClassNode)
    def visit(self, node, scope):
        self.current_type.append(self.context.types[node.id])
        attributes = self.current_type.all_attributes()
        for values in attributes:
            attr, _ = values
            scope.define_variable(attr.name, attr.type)

        for st in node.statements:
            self.visit(st, scope)
        self.current_type.pop(-1)

    @visitor.when(AttrDeclarationNode)
    def visit(self, node, scope):
        pass

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        nscope = scope.create_child()
        self.current_method = self.current_type[-1].get_function(node.id)
        # checking overwriting
        try:
            method = self.current_type[-1].parent.get_function(node.id)
            if not len(self.current_method.parameters_types) == len(
                method.parameters_types
            ):
                self.errors.append(
                    WRONG_SIGNATURE % (node.id, self.current_type[-1].name)
                )
            else:
                for i, t in enumerate(self.current_method.parameters_types):
                    if not method.parameters_types[i] == t:
                        self.errors.append(
                            WRONG_SIGNATURE % (node.id, self.current_type[-1].name)
                        )
                        break
                if not self.current_method.return_type == method.return_type:
                    self.errors.append(
                        WRONG_SIGNATURE % (node.id, self.current_type[-1].name)
                    )
        except:
            pass

        # defining variables in new scope
        for i, var in enumerate(self.current_method.parameters):
            if nscope.is_local(var):
                self.errors.append(
                    LOCAL_ALREADY_DEFINED % (var, self.current_method.name)
                )
            else:
                nscope.define_variable(self.current_method.parameters_types[i], var)

        # checking return type
        types_returned = 0
        for expr in node.body:
            self.visit(expr, nscope)
            if isinstance(expr, ReturnNode):
                types_returned += 1
                if not self.context.types[expr.expr.type].conforms_to(
                    self.context.types[self.current_method.return_type]
                ):
                    self.errors.append(
                        INCOMPATIBLE_TYPES
                        % (expr.expr.type, self.current_method.return_type)
                    )
        if not types_returned and not isinstance(
            self.context.types[self.current_method.return_type],
            VoidType,
        ):
            self.errors.append(
                INCOMPATIBLE_TYPES % ("void", self.current_method.return_type)
            )
        self.current_method = None

    @visitor.when(ReturnNode)
    def visit(self, node, scope):
        self.visit(node.expr)
        try:
            self.context.check_if_return_in_func(node)
        except SemanticError as ex:
            self.errors.append(ex.text)

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        try:
            self.context.get_type(node.type)
            var_type = node.type
        except SemanticError as ex:
            self.errors.append(ex.text)
            var_type = "error"

        if scope.is_defined(node.id):
            self.errors.append(
                LOCAL_ALREADY_DEFINED % (node.id, self.current_method.name)
            )
        else:
            scope.define_variable(node.id, var_type)

        self.visit(node.expr, scope.create_child())
        if not self.context.types[node.expr.type].conforms_to(
            self.context.types[var_type]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (node.expr.type, var_type))
        node.type = var_type

    @visitor.when(AssignmentNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child())

        var = scope.find_variable(node.id)
        if var is None:
            self.errors.append(
                VARIABLE_NOT_DEFINED % (node.id, self.current_type[-1].name)
            )
            var = scope.define_variable(node.id, node.expr.computed_type)

        if not self.context.types[node.expr.type].conforms_to(
            self.context.types[var.type]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (node.expr.type, var.type))

        node.type = var.type

    @visitor.when(CallNode)
    def visit(self, node, scope):
        # evaluate object
        if node.obj != None:
            self.visit(node.obj, scope)
            obj_type = node.obj.type

        try:
            if node.obj == None:
                method = self.context.types["Main"].get_function(node.lex)
            else:
                method = obj_type.get_function(node.lex)
            if not len(node.arguments) == len(method.parameters_types):
                self.errors.append(INVALID_OPERATION % (method.name, obj_type.name))
                node.type = "error"
                return
            for i, arg in enumerate(node.arguments):
                self.visit(arg, scope)
                if not self.context.types[arg.type].conforms_to(
                    self.context.types[method.parameters_types[i]]
                ):
                    self.errors.append(
                        INCOMPATIBLE_TYPES
                        % (
                            arg.type,
                            method.parameters_types[i],
                        )
                    )
            node.type = method.return_type
        except SemanticError as ex:
            self.errors.append(ex.text)
            node.type = "error"

    @visitor.when(NumericBinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

        if not self.context.types[node.left.type].conforms_to(
            self.context.types["Num"]
        ) or not self.context.types[node.right.type].conforms_to(
            self.context.types["Num"]
        ):
            self.errors.append(INVALID_OPERATION % (node.left.type, node.right.type))
            node.type = "error"
        else:
            node.type = "Num"

    @visitor.when(AndNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

        if not self.context.types[node.left.type].conforms_to(
            self.context.types["Bool"]
        ) or not self.context.types[node.right.type].conforms_to(
            self.context.types["Bool"]
        ):
            self.errors.append(INVALID_OPERATION % (node.left.type, node.right.type))
            node.type = "error"
        else:
            node.type = "Bool"

    @visitor.when(OrNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

        if not self.context.types[node.left.type].conforms_to(
            self.context.types["Bool"]
        ) or not self.context.types[node.right.type].conforms_to(
            self.context.types["Bool"]
        ):
            self.errors.append(INVALID_OPERATION % (node.left.type, node.right.type))
            node.type = "error"
        else:
            node.type = "Bool"

    @visitor.when(BooleanBinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)
        node.type = "Bool"

    @visitor.when(NotNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope)

        if not self.context.types[node.expr.type].conforms_to(
            self.context.types["Bool"]
        ):
            self.errors.append(INVALID_OPERATION_UNARY % (node.expr.type))
            node.type = "error"
        else:
            node.type = "Bool"

    @visitor.when(IntNode)
    def visit(self, node, scope):
        node.type = "int"

    @visitor.when(DoubleNode)
    def visit(self, node, scope):
        node.type = "double"

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        var = scope.find_variable(node.lex)
        if var is None:
            self.errors.append(
                VARIABLE_NOT_DEFINED % (node.lex, self.current_type[-1].name)
            )
            var = scope.define_variable(node.lex, self.context.types["error"])

        node.type = var.type

    @visitor.when(InstanceNode)
    def visit(self, node, scope):
        try:
            self.context.get_type(node.lex)
            node.type = node.lex
        except SemanticError as ex:
            self.errors.append(ex.text)
            node.type = "error"
        for i in node.arguments:
            self.visit(i, scope)

    @visitor.when(StringNode)
    def visit(self, node, scope):
        node.type = "String"

    @visitor.when(DictNode)
    def visit(self, node, scope):
        node.type = "Dict"
        for i in node.items:
            self.visit(i, scope)

    @visitor.when(ItemNode)
    def visit(self, node, scope):
        key = node.key
        try:
            scope.find_variable(key)
        except:
            self.errors.append(
                VARIABLE_NOT_DEFINED % (key.lex, self.current_type[-1].name)
            )

    @visitor.when(ListNode)
    def visit(self, node, scope):
        node.type = "List"
        for i in node.items:
            self.visit(i, scope)

    @visitor.when(TupleNode)
    def visit(self, node, scope):
        node.type = "Tuple"
        for i in node.items:
            self.visit(i, scope)

    @visitor.when(BooleanNode)
    def visit(self, node, scope):
        node.type = "Bool"

    @visitor.when(RuleNode)
    def visit(self, node, scope):
        then = node.then
        condition = node.condition
        destination = node.destination
        self.visit(then)
        self.visit(condition)
        self.visit(destination)
        try:
            scope.find_variable(destination.lex)
        except:
            self.errors.append(
                VARIABLE_NOT_DEFINED % (destination.lex, self.current_type[-1].name)
            )

        if not self.context.types[condition.type].conforms_to(
            self.context.types["Dict"]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (condition.type, "Dict"))

        if not self.context.types[then.type].conforms_to(self.context.types["Tuple"]):
            self.errors.append(INCOMPATIBLE_TYPES % (then.type, "Tuple"))

        if not self.context.types[destination.type].conforms_to(
            self.context.types["Environment"]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (destination.type, "Environment"))

    @visitor.when(ProbFunctionValueNode)
    def visit(self, node, scope):
        pass

    @visitor.when(ProbabilityFunctionNode)
    def visit(self, node, scope):
        pass

    @visitor.when(EffectNode)
    def visit(self, node, scope):
        par = node.par
        env = node.env
        e = node.e

        self.visit(par)
        self.visit(env)
        self.visit(e)

        if not self.context.types[par.type].conforms_to(
            self.context.types["Parameter"]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (par.type, "Dict"))

        if not self.context.types[env.type].conforms_to(
            self.context.types["Environment"]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (env.type, "Tuple"))

    @visitor.when(ForNode)
    def visit(self, node, scope):
        body = node.body
        var = node.var
        expr = node.expr
        nscope = scope.create_child()

        self.visit(body, nscope)
        self.visit(var, nscope)
        self.visit(expr, scope)

        if not self.context.types[expr.type].conforms_to(self.context.types["List"]):
            self.errors.append(INCOMPATIBLE_TYPES % (expr.type, "List"))

    @visitor.when(IfNode)
    def visit(self, node, scope):
        expr = node.expr
        body = node.body
        nscope = scope.create_child()
        self.visit(expr, scope)
        self.visit(body, nscope)

        if not self.context.types[expr.type].conforms_to(self.context.types["Bool"]):
            self.errors.append(INCOMPATIBLE_TYPES % (expr.type, "Bool"))

    @visitor.when(IfElseNode)
    def visit(self, node, scope):
        condition_if = node.condition_if
        body_if = node.body_if
        body_else = node.body_else
        nscope = scope.create_child()
        nscope1 = scope.create_child()

        self.visit(condition_if, scope)
        self.visit(body_if, nscope)
        self.visit(body_else, nscope1)

        if not self.context.types[condition_if.type].conforms_to(
            self.context.types["Bool"]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (condition_if.type, "Bool"))

    @visitor.when(AgentDefNode)
    def visit(self, node, scope):
        idt = node.idt
        idn = node.idn
        conditions = node.conditions
        t = node.t
        rep = node.rep
        act = node.act
        supply = node.supply

        self.visit(idt, scope)
        self.visit(idn, scope)
        self.visit(conditions, scope)
        self.visit(t, scope)
        self.visit(rep, scope)

        if not self.context.types[conditions.type].conforms_to(
            self.context.types["List"]
        ):
            self.errors.append(INCOMPATIBLE_TYPES % (conditions.type, "List"))
        if not self.context.types[t.type].conforms_to(self.context.types["Num"]):
            self.errors.append(INCOMPATIBLE_TYPES % (t.type, "Num"))
        if not self.context.types[rep.type].conforms_to(self.context.types["Num"]):
            self.errors.append(INCOMPATIBLE_TYPES % (rep.type, "Num"))
        try:
            f = scope.find_variable(act)
            if f != None and not self.context.types[f.type].conforms_to(
                self.context.types["RandVarEffect"]
            ):
                self.errors.append(INCOMPATIBLE_TYPES % (f.type, "RandVarEffect"))
        except SemanticError as ex:
            self.errors.append(ex.text)

        if supply != None:
            self.visit(supply)
            if not self.context.types[supply.type].conforms_to(
                self.context.types["Num"]
            ):
                self.errors.append(INCOMPATIBLE_TYPES % (supply.type, "Num"))
