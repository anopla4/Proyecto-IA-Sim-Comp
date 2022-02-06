from .error import *
from .method import Method
from .variable import Variable


class Scope:
    def __init__(self, parent=None) -> None:
        self.variables = {}
        self.functions = {}
        self.attributes = {}
        self.parent = parent

    def create_child(self):
        return Scope(self)

    def get_parent(self):
        return self.parent

    def define_var(self, type, name):
        self.variables[name] = Variable(name, type)

    def check_var(self, var):
        if var in self.functions:
            return self.functions[var]
        return None

    def define_func(self, name, return_type, params, params_types):
        self.variables[name] = Method(name, return_type, params, params_types)

    def check_func(self, func):
        if func in self.functions:
            return self.functions[func]
        return None
