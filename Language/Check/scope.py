from pprint import pprint
from .error import *
from .method import Method
from .variable import Variable

from itertools import islice


class Scope:
    def __init__(self, parent=None) -> None:
        self.variables = {}
        self.functions = {}
        self.attributes = {}
        self.parent = parent
        self.locals = []
        self.children = []

    def create_child(self):
        child = Scope(self)
        self.children.append(child)
        return child

    def define_variable(self, vtype, vname):
        info = Variable(vname, vtype)
        self.locals.append(info)
        self.attributes[vname] = info
        return info

    def find_variable(self, vname, index=None):
        locals = self.locals if index is None else islice(self.locals, index)
        try:
            return next(x for x in locals if x.name == vname)
        except StopIteration:
            return (
                self.parent.find_variable(vname, self.index)
                if self.parent is not None
                else None
            )

    def is_defined(self, vname):
        return self.find_variable(vname) is not None

    def is_local(self, vname):
        return any(True for x in self.locals if x.name == vname)

    def define_func(self, name, return_type, params, params_types):
        self.variables[name] = Method(name, return_type, params, params_types)
        return self.variables[name]

    def find_func(self, func):
        try:
            pprint(self.functions)
            return next(x for x in self.functions if x.name == func)
        except StopIteration:
            return self.parent.find_func(func) if self.parent is not None else None
