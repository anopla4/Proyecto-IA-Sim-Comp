import Language.Check.visitor as visitor
from ..Parsing.Node.declaration_nodes import *
from ..Parsing.Node.expression_nodes import *
from ..Parsing.Node.statement_nodes import *
from ..Parsing.Node.program_node import ProgramNode
from .type import *
from .error import SemanticError


class TypeBuilder(object):
    def __init__(self, context, errors=[]) -> None:
        self.context = context
        self.current_type = context.types["Main"]
        self.errors = errors

    @visitor.on("node")
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node):
        for dec in node.statements:
            self.visit(dec)

    @visitor.when(ClassNode)
    def visit(self, node):
        self.current_type = self.context.get_type(node.id)

        if node.parent is not None:
            try:
                parent_type = self.context.get_type(node.parent)
                try:
                    self.context.check_cyclic_inheritance(
                        self.current_type, self.current_type.parent
                    )
                    self.current_type.set_parent(parent_type)
                except SemanticError as ex:
                    self.errors.append(ex.text)
            except SemanticError as ex:
                self.errors.append(ex.text)

        for stm in node.statements:
            self.visit(stm)

    @visitor.when(FuncDeclarationNode)
    def visit(self, node):
        param_names = []
        param_types = []
        for param in node.params:
            t_, n = param
            param_names.append(n)
            try:
                self.context.get_type(t_)
                t = t_
            except SemanticError as ex:
                self.errors.append(ex.text)
                t = "error"
            param_types.append(t)
        try:
            self.context.get_type(node.return_type)
            rtype = node.return_type
        except SemanticError as ex:
            self.errors.append(ex.text)
            rtype = "error"

        try:
            self.current_type.set_function(node.id, param_names, param_types, rtype)
        except SemanticError as ex:
            self.errors.append(ex.text)

    @visitor.when(AttrDeclarationNode)
    def visit(self, node):
        try:
            attr_type = self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            attr_type = ErrorType()

        try:
            self.current_type.set_attribute(node.id, attr_type)
        except SemanticError as ex:
            self.errors.append(ex.text)
