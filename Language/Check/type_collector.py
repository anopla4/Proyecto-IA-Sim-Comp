from inspect import Parameter
import Language.Check.visitor as visitor
from ..Parsing.Node.declaration_nodes import *
from ..Parsing.Node.expression_nodes import *
from ..Parsing.Node.statement_nodes import *
from ..Parsing.Node.program_node import ProgramNode
from .context import Context
from .type import *
from .error import SemanticError


class TypeCollector(object):
    def __init__(self, context, errors=[]):
        self.errors = errors
        self.context = context

    @visitor.on("node")
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node):
        self.context.types["Main"] = MainType()
        self.context.types["Num"] = NumType(self.context.types["Main"])
        self.context.types["int"] = IntType(self.context.types["Num"])
        self.context.types["double"] = DoubleType(self.context.types["Num"])
        self.context.types["String"] = StringType(self.context.types["Main"])
        self.context.types["void"] = VoidType(self.context.types["Main"])
        self.context.types["error"] = ErrorType(self.context.types["Main"])
        self.context.types["Agent"] = AgentType(self.context.types["Main"])
        self.context.types["Symptom"] = SymptomType(self.context.types["Agent"])
        self.context.types["Intervention"] = InterventionType(
            self.context.types["Agent"]
        )
        self.context.types["Parameter"] = ParameterType(self.context.types["Main"])
        self.context.types["Environment"] = EnvironmentType(self.context.types["Main"])
        self.context.types["Patient"] = ParameterType(self.context.types["Environment"])
        self.context.types["RandVarEffect"] = RandVarEffectType(
            self.context.types["Main"]
        )
        self.context.types["ActivationRule"] = ActivationRuleType(
            self.context.types["Main"]
        )
        self.context.types["Dict"] = DictType(self.context.types["Main"])
        self.context.types["List"] = ListType(self.context.types["Main"])
        self.context.types["Tuple"] = TupleType(self.context.types["Main"])
        self.context.types["Bool"] = BoolType(self.context.types["Main"])
        for dec in node.statements:
            self.visit(dec)

    @visitor.when(ClassNode)
    def visit(self, node):
        try:
            self.current_type = self.context.def_type(node.id)
        except SemanticError as ex:
            self.errors.append(ex.text)
