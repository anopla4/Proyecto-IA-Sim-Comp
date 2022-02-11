import visitor
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
        self.current_type = None
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
        attributes = self.current_type.all_attributes()
        for values in attributes:
            attr, _ = values
            scope.define_variable(attr.name, attr.type)

        for st in node.statements:
            self.visit(st, scope)

    @visitor.when(AttrDeclarationNode)
    def visit(self, node, scope):
        pass

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        nscope = scope.create_child()
        self.current_method = self.current_type.get_function(node.id)

        # checking overwriting
        try:
            method = self.current_type.parent.get_function(node.id)
            if not len(self.current_method.parameters_type) == len(
                method.parameters_type
            ):
                self.errors.append(WRONG_SIGNATURE % (node.id, self.current_type.name))
            else:
                for i, t in enumerate(self.current_method.parameters_type):
                    if not method.parameters_type[i] == t:
                        self.errors.append(
                            WRONG_SIGNATURE % (node.id, self.current_type.name)
                        )
                        break
                if not self.current_method.return_type == method.return_type:
                    self.errors.append(
                        WRONG_SIGNATURE % (node.id, self.current_type.name)
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
                nscope.define_variable(var, self.current_method.parameters_type[i])

        # checking return type
        types_returned = 0
        for expr in node.body:
            self.visit(expr, nscope)
            if isinstance(expr, ReturnNode):
                types_returned += 1
                if not expr.expr.type.conforms_to(self.current_method.return_type):
                    self.errors.append(
                        INCOMPATIBLE_TYPES
                        % (expr.expr.type.name, self.current_method.return_type.name)
                    )
        if not types_returned and not isinstance(
            self.current_method.return_type, VoidType
        ):
            self.errors.append(
                INCOMPATIBLE_TYPES % ("void", self.current_method.return_type.name)
            )

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
            var_type = self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            var_type = ErrorType()

        if scope.is_defined(node.id):
            self.errors.append(
                LOCAL_ALREADY_DEFINED % (node.id, self.current_method.name)
            )
        else:
            scope.define_variable(node.id, var_type)

        self.visit(node.expr, scope.create_child())
        if not node.expr.type.conforms_to(var_type):
            self.errors.append(
                INCOMPATIBLE_TYPES % (node.expr.type.name, var_type.name)
            )
        node.type = var_type

    @visitor.when(AssignmentNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child())

        var = scope.find_variable(node.id)
        if var is None:
            self.errors.append(VARIABLE_NOT_DEFINED % (node.id, self.current_type.name))
            var = scope.define_variable(node.id, node.expr.computed_type)

        if not node.expr.type.conforms_to(var.type):
            self.errors.append(
                INCOMPATIBLE_TYPES % (node.expr.type.name, var.type.name)
            )

        node.type = var.type

    @visitor.when(CallNode)
    def visit(self, node, scope):
        # evaluate object
        if node.obj != None:
            self.visit(node.obj, scope)
            obj_type = node.obj.type

        try:
            if node.obj == None:
                method = MainType().get_function(node.id)
            else:
                method = obj_type.get_function(node.id)
            if not len(node.args) == len(method.parameters_types):
                self.errors.append(INVALID_OPERATION % (method.name, obj_type.name))
                node.computed_type = ErrorType()
                return
            for i, arg in enumerate(node.args):
                self.visit(arg, scope)
                if not arg.type.conforms_to(method.parameters_types[i]):
                    self.errors.append(
                        INCOMPATIBLE_TYPES % (arg.type, method.parameters_types[i])
                    )
            node.type = method.return_type
        except SemanticError as ex:
            self.errors.append(ex.text)
            node.type = ErrorType()

    @visitor.when(NumericBinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

        if not node.left.type.conforms_to(NumType()) or not node.right.type.conforms_to(
            NumType()
        ):
            self.errors.append(
                INVALID_OPERATION % (node.left.type.name, node.right.type.name)
            )
            node.type = ErrorType()
        else:
            node.type = NumType()

    @visitor.when(BooleanBinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

        if not node.left.type.conforms_to(
            BoolType()
        ) or not node.right.type.conforms_to(BoolType()):
            self.errors.append(
                INVALID_OPERATION % (node.left.type.name, node.right.type.name)
            )
            node.type = ErrorType()
        else:
            node.type = BoolType()

    @visitor.when(NotNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope)

        if not node.expr.type.conforms_to(BoolType()):
            self.errors.append(INVALID_OPERATION_UNARY % (node.expr.type.name))
            node.type = ErrorType()
        else:
            node.type = BoolType()

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        node.type = NumType()

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        var = scope.find_variable(node.lex)
        if var is None:
            self.errors.append(
                VARIABLE_NOT_DEFINED % (node.lex, self.current_type.name)
            )
            var = scope.define_variable(node.lex, ErrorType())

        node.type = var.type

    @visitor.when(InstanceNode)
    def visit(self, node, scope):
        try:
            node.type = self.context.get_type(node.lex)
        except SemanticError as ex:
            self.errors.append(ex.text)
            node.type = ErrorType()

    @visitor.when(StringNode)
    def visit(self, node, scope):
        node.type = StringType()

    @visitor.when(DictNode)
    def visit(self, node, scope):
        node.type = DictType()

    @visitor.when(ListNode)
    def visit(self, node, scope):
        node.type = ListType()

    @visitor.when(TupleNode)
    def visit(self, node, scope):
        node.type = TupleType()

    @visitor.when(BooleanNode)
    def visit(self, node, scope):
        node.type = BoolType()

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
                VARIABLE_NOT_DEFINED % (destination.lex, self.current_type.name)
            )

        if not condition.type.conforms_to(DictType()):
            self.errors.append(INCOMPATIBLE_TYPES % (condition.type.name, "dict"))

        if not then.type.conforms_to(TupleType()):
            self.errors.append(INCOMPATIBLE_TYPES % (then.type.name, "tuple"))

        if not destination.type.conforms_to(EnvironmentType()):
            self.errors.append(
                INCOMPATIBLE_TYPES % (destination.type.name, "environment")
            )

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

        if not par.type.conforms_to(ParameterType()):
            self.errors.append(INCOMPATIBLE_TYPES % (par.type.name, "dict"))

        if not env.type.conforms_to(EnvironmentType()):
            self.errors.append(INCOMPATIBLE_TYPES % (env.type.name, "tuple"))

    @visitor.when(ForNode)
    def visit(self, node, scope):
        body = node.body
        var = node.var
        expr = node.expr
        nscope = scope.create_child()

        self.visit(body, nscope)
        self.visit(var, nscope)
        self.visit(expr, scope)

        if not expr.type.conforms_to(ListType()):
            self.errors.append(INCOMPATIBLE_TYPES % (expr.type.name, "listt"))

    @visitor.when(IfNode)
    def visit(self, node, scope):
        expr = node.expr
        body = node.body
        nscope = scope.create_child()
        self.visit(expr, scope)
        self.visit(body, nscope)

        if not expr.type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (expr.type.name, "bool"))

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

        if not condition_if.type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (condition_if.type.name, "bool"))

    @visitor.when(AgentDefNode)
    def visit(self, node, scope):
        idt = node.idt
        idn = node.idn
        conditions = node.conditions
        t = self.t
        rep = node.repetition
        act = node.action
        supply = node.supply

        self.visit(idt, scope)
        self.visit(idn, scope)
        self.visit(conditions, scope)
        self.visit(t, scope)
        self.visit(rep, scope)
        self.visit(act, scope)

        if not conditions.type.conforms_to(BoolType()):
            self.errors.append(
                INCOMPATIBLE_TYPES % (conditions.type.name, "ActivationRule")
            )
        if not t.type.conforms_to(NumType()):
            self.errors.append(INCOMPATIBLE_TYPES % (t.type.name, "Num"))
        if not rep.type.conforms_to(NumType()):
            self.errors.append(INCOMPATIBLE_TYPES % (rep.type.name, "Num"))
        try:
            f = scope.find_func(act)
            if not f.type.conforms_to(RandVarEffectType()):
                self.errors.append(INCOMPATIBLE_TYPES % (f.type.name, "RandVarEffect"))
        except:
            self.errors.append(METHOD_NOT_DEFINED % (act))

        if supply != None:
            self.visit(supply)
            if not supply.type.conforms_to(NumType()):
                self.errors.append(INCOMPATIBLE_TYPES % (supply.type.name, "Num"))
