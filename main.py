from ast import ClassDef
from Language.Check.semantic_checker import SemanticChecker
from Language.Check.type_builder import TypeBuilder
from Language.Check.type_collector import TypeCollector
from Language.Lexer.token import Token
from Language.Parsing.Grammar_dsl.dsl_grammar import get_grammar
from Language.Lexer.lexer import tokenize_regex_automaton
from Language.Parsing.Node.declaration_nodes import (
    ClassNode,
    FuncDeclarationNode,
    VarDeclarationNode,
)
from Language.Parsing.Node.expression_nodes import *
from Language.Parsing.Node.program_node import ProgramNode
from Language.Parsing.Node.statement_nodes import *

from Language.Parsing.build_ast_shift_reduce_parser import build_ast
from Language.Parsing.parserLR1 import ParserLR1
from Language.Parsing.shift_reduce_parser import ShiftReduceParser
from Language.Check.translator import Translator


def main(text):
    G, t = get_grammar()
    parser = ParserLR1(G)

    tokens = tokenize_regex_automaton(text, t)
    tokens.append(Token("$", (G.EOF, 0)))
    l = [i.type[0] for i in tokens]

    result, actions = parser.parse(l)

    ast = build_ast(actions, result, tokens, G)

    type_c = TypeCollector()
    type_c.visit()

    type_b = TypeBuilder()
    type_b.visit()

    checker = SemanticChecker()
    checker.visit()

    t = Translator()
    code = t.visit(ast)

    errors = type_c.errors + type_b.errors + checker.errors
    print(errors)
    try:
        exec(code)
    except Exception as ex:
        print(ex.text)
