from Language.Lexer.RegularExpression.word import Word
from Language.Lexer.RegularExpression._or import Or
from Language.Lexer.RegularExpression._concat import Concat
from Language.Lexer.RegularExpression._star import Star

def build_automaton_(ast):
    if ast == None:
        return
    if isinstance(ast, Word):
        return ast.build_automaton()
    if isinstance(ast, Star):
        aut = build_automaton_(ast.expr)
        return ast.build_automaton(aut)
    if isinstance(ast, Or):
        left = build_automaton_(ast.left_expr)
        right = build_automaton_(ast.right_expr)
        return ast.build_automaton(left, right)
    if isinstance(ast, Concat):
        left = build_automaton_(ast.left_expr)
        right = build_automaton_(ast.right_expr)
        return ast.build_automaton(left, right)
    return