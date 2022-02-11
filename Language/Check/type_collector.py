from inspect import Parameter
import visitor
from ..Parsing.Node.declaration_nodes import *
from ..Parsing.Node.expression_nodes import *
from ..Parsing.Node.statement_nodes import *
from ..Parsing.Node.program_node import ProgramNode
from .context import Context
from .type import *
from .error import SemanticError


class TypeCollector(object):
    def __init__(self, errors=[]):
        self.context = None
        self.errors = errors

    @visitor.on("node")
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node):
        self.context = Context()
        self.context["Main"] = MainType()
        self.context.types["int"] = IntType(self.context["Main"])
        self.context.types["void"] = VoidType(self.context["Main"])
        self.context.types["error"] = ErrorType(self.context["Main"])
        self.context.types["Agent"] = AgentType(self.context["Main"])
        self.context.types["Symptom"] = SymptomType(self.context.types["Agent"])
        self.context.types["Intervention"] = InterventionType(
            self.context.types["Agent"]
        )
        self.context.types["Parameter"] = ParameterType(self.context["Main"])
        self.context.types["Environment"] = EnvironmentType(self.context["Main"])
        self.context.types["Parameter"] = ParameterType(
            self.context.types["Environment"]
        )
        self.context.types["RandVarEffect"] = RandVarEffectType(self.context["Main"])
        self.context.types["ActivationRule"] = ActivationRuleType(self.context["Main"])
        self.context.types["Dict"] = DictType(self.context["Main"])
        self.context.types["List"] = ListType(self.context["Main"])
        self.context.types["Tuple"] = TupleType(self.context["Main"])
        for dec in node.declarations:
            self.visit(dec)

    @visitor.when(ClassNode)
    def visit(self, node):
        try:
            self.current_type = self.context.def_type(node.id)
        except SemanticError as ex:
            self.errors.append(ex.text)
