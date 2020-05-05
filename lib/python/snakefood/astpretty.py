"""Python AST pretty-printer.

This module exports a function that can be used to print a human-readable
version of the AST.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# This file is part of the Snakefood open source package.
# See http://furius.ca/snakefood/ for licensing details.

from future import standard_library
standard_library.install_aliases()
import sys
from ast import AST

from six import print_

__all__ = ('printAst',)


def printAst(ast, indent='  ', stream=sys.stdout, initlevel=0):
    "Pretty-print an AST to the given output stream."
    rec_node(ast, initlevel, indent, stream.write)
    stream.write('\n')

def rec_node(node, level, indent, write):
    "Recurse through a node, pretty-printing it."
    pfx = indent * level
    if isinstance(node, AST):
        write(pfx)
        write(node.__class__.__name__)
        write('(')

        if any(isinstance(child, AST) for child in node.getChildren()):
            for i, child in enumerate(node.getChildren()):
                if i != 0:
                    write(',')
                write('\n')
                rec_node(child, level+1, indent, write)
            write('\n')
            write(pfx)
        else:
            # None of the children as nodes, simply join their repr on a single
            # line.
            write(', '.join(repr(child) for child in node.getChildren()))

        write(')')

    else:
        write(pfx)
        write(repr(node))


def main():
    import optparse
    parser = optparse.OptionParser(__doc__.strip())
    opts, args = parser.parse_args()

    if not args:
        parser.error("You need to specify the name of Python files to print out.")

    import ast, traceback
    for fn in args:
        print_('\n\n%s:\n' % fn)
        try:
            printAst(ast.parse(fn), initlevel=1)
        except SyntaxError:
            _, e, _ = sys.exc_info()
            traceback.print_exc()

if __name__ == '__main__':
    main()
