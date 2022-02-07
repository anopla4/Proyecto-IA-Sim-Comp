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
        for declaration in node.declarations:
            self.visit(declaration, scope.create_child())
        return scope

    @visitor.when(ClassNode)
    def visit(self, node, scope):
        self.current_type = self.context.get_type(node.id)
        attributes = self.current_type.attributes
        for attr in attributes:
            if scope.check_attr(attr.name) == None:
                scope.define_var(attr.type, attr.name)
            else:
                self.errors.append(
                    SemanticError(ATTRIBUTE_ALREADY_DEFINED % (attr.name))
                )

        for feature in node.features:
            self.visit(feature, scope)

    @visitor.when(AttrDeclarationNode)
    def visit(self, node, scope):
        pass

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        nscope = scope.create_child()
        self.current_method = self.current_type.get_method(node.id)

        # checking overwriting
        if not self.context.get_function_to_override(
            self.current_method, self.current_type.parent, node.id, self.current_type
        ):
            raise SemanticError(
                WRONG_SIGNATURE % (self.current_method.name, self.current_type.name)
            )
        # defining variables in new scope
        for i, var in enumerate(self.current_method.param_names):
            try:
                nscope.is_local(var, self.current_method.name)
                nscope.define_var(var, self.current_method.param_types[i])
            except SemanticError as ex:
                self.errors.append(ex.text)

        for expr in node.body:
            self.visit(expr, nscope)

        # # checking return type
        # rtype = node.body[-1].computed_type
        # if not rtype.conforms_to(self.current_method.return_type):
        #     self.errors.append(
        #         INCOMPATIBLE_TYPES % (rtype.name, self.current_method.return_type.name)
        #     )

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        try:
            var_type = self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            var_type = ErrorType()

        try:
            scope.check_var(node.id)
            scope.define_var(node.id, var_type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            var_type = ErrorType()
        # todo revisar aqui
        self.visit(node.expr, scope.create_child())
        if not node.expr.computed_type.conforms_to(var_type):
            self.errors.append(
                INCOMPATIBLE_TYPES % (node.expr.computed_type.name, var_type.name)
            )
        node.computed_type = var_type

    @visitor.when(AssignmentNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child())

        var = scope.variables[node.id]
        if var is None:
            self.errors.append(VARIABLE_NOT_DEFINED % (node.id, self.current_type.name))
            var = scope.define_variable(node.id, node.expr.computed_type)

        if not node.expr.computed_type.conforms_to(var.type):
            self.errors.append(
                INCOMPATIBLE_TYPES % (node.expr.computed_type.name, var.type.name)
            )

        node.computed_type = var.type

    @visitor.when(CallNode)
    def visit(self, node, scope):
        # evaluate object
        self.visit(node.obj, scope)
        obj_type = node.obj.computed_type

        try:
            method = obj_type.get_method(node.id)
            if not len(node.args) == len(method.param_types):
                self.errors.append(INVALID_OPERATION % (method.name, obj_type.name))
                node.computed_type = ErrorType()
                return
            for i, arg in enumerate(node.args):
                self.visit(arg, scope)
                if not arg.computed_type.conforms_to(method.param_types[i]):
                    self.errors.append(
                        INCOMPATIBLE_TYPES % (arg.computed_type, method.param_types[i])
                    )
            node.computed_type = method.return_type
        except SemanticError as ex:
            self.errors.append(ex.text)
            node.computed_type = ErrorType()

    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

        if not node.left.computed_type.conforms_to(
            IntType()
        ) or not node.right.computed_type.conforms_to(IntType()):
            self.errors.append(
                INVALID_OPERATION
                % (node.left.computed_type.name, node.right.computed_type.name)
            )
            node.computed_type = ErrorType()
        else:
            node.computed_type = IntType()

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        node.computed_type = IntType()

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        if node.lex == "self":
            node.computed_type = self.current_type
            return

        var = scope.find_variable(node.lex)
        if var is None:
            self.errors.append(
                VARIABLE_NOT_DEFINED % (node.lex, self.current_type.name)
            )
            var = scope.define_variable(node.lex, ErrorType())

        node.computed_type = var.type

    @visitor.when(InstanceNode)
    def visit(self, node, scope):
        try:
            node.computed_type = self.context.get_type(node.lex)
        except SemanticError as ex:
            self.errors.append(ex.text)
            node.computed_type = ErrorType()
