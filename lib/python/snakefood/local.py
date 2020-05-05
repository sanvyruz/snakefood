"""Code for checking for local names and superfluous import statements.

This code provides searches for local symbols in the AST, assignments and such
things.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# This file is part of the Snakefood open source package.
# See http://furius.ca/snakefood/ for licensing details.

# stdlib imports
from future import standard_library
standard_library.install_aliases()
from builtins import range
from builtins import object
from ast import NodeVisitor, Expr, iter_child_nodes

__all__ = ('get_names_from_ast', 'filter_unused_imports',
           'NamesVisitor', 'AssignVisitor', 'AllVisitor')


def get_names_from_ast(ast):
    "Find all the names being referenced/used."
    vis = NamesVisitor()
    vis.visit(ast)
    dotted_names, simple_names = vis.finalize()
    return (dotted_names, simple_names)


def filter_unused_imports(ast, found_imports):
    """
    Given the ast and the list of found imports in the file, find out which of
    the imports are not used and return two lists: a list of used imports, and a
    list of unused imports.
    """
    used_imports, unused_imports = [], []

    # Find all the names being referenced/used.
    dotted_names, simple_names = get_names_from_ast(ast)

    # Find all the names being exported via __all__.
    vis = AllVisitor()
    vis.visit(ast)
    exported = vis.finalize()

    # Check that all imports have been referenced at least once.
    usednames = set(x[0] for x in dotted_names)
    usednames.update(x[0] for x in exported)
    used_imports = []
    for x in found_imports:
        _, _, lname, lineno, _,  _ = x
        if lname is not None and lname not in usednames:
            unused_imports.append(x)
        else:
            used_imports.append(x)

    return used_imports, unused_imports


class Visitor(NodeVisitor):
    "Base class for our visitors."
    def continue_(self, node):
        for child in iter_child_nodes(node):
            self.visit(child)


class NamesVisitor(Visitor):
    """AST visitor that finds all the identifier references that are defined,
    including dotted references. This includes all free names and names with
    attribute references.
    """
    def __init__(self):
        self.dotted = []
        self.simple = []
        self.attributes = []

    def visit_Name(self, node):
        self.attributes.append(node.id)
        self.attributes.reverse()
        attribs = self.attributes
        for i in range(1, len(attribs)+1):
            self.dotted.append(('.'.join(attribs[0:i]), node.lineno))
        self.simple.append((attribs[0], node.lineno))
        self.attributes = []

    def visit_Attribute(self, node):
        self.attributes.append(node.attr)
        self.continue_(node)

    def finalize(self):
        return self.dotted, self.simple


class AssignVisitor(Visitor):
    """AST visitor that builds a list of all potential names that are being
    assigned to. This is used later to heuristically figure out if a name being
    refered to is never assigned to nor in the imports."""

    def __init__(self):
        self.assnames = []
        self.in_class = False

    def visit_Name(self, node):
        self.assnames.append((node.name, node.lineno))
        self.continue_(node)

    def visit_Class(self, node):
        self.assnames.append((node.name, node.lineno))
        prev, self.in_class = self.in_class, True
        self.continue_(node)
        self.in_class = prev

    def visit_Function(self, node):
        # Avoid method definitions.
        if not self.in_class:
            self.assnames.append((node.name, node.lineno))
        self.continue_(node)

    def finalize(self):
        return self.assnames


class AllVisitor(Visitor):
    """AST visitor that find an __all__ directive and accumulates the list of
    constants in it."""

    def __init__(self):
        self.all = []
        self.in_assign = False
        self.in_all = False

    def visit_Assign(self, node):
        prev, self.in_assign = self.in_assign, True
        self.continue_(node)
        self.in_assign = prev

    def visit_Name(self, node):
        if self.in_assign and node.id == '__all__':
            self.in_all = True
        self.continue_(node)

    def visit_Constant(self, node):
        if self.in_assign and self.in_all:
            self.all.append((node.value, node.lineno))
        self.continue_(node)

    def finalize(self):
        return self.all
