"""
Routines that manipulate, read and convert lists of dependencies.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# This file is part of the Snakefood open source package.
# See http://furius.ca/snakefood/ for licensing details.

from future import standard_library
standard_library.install_aliases()
import sys, logging
from operator import itemgetter



def read_depends(f):
    "Generator for the dependencies read from the given file object."
    for line in f:
        try:
            yield eval(line)
        except Exception:
            logging.warning("Invalid line: '%s'" % line)

def output_depends(depdict):
    """Given a dictionary of (from -> list of targets), generate an appropriate
    output file."""
    # Output the dependencies.
    write = sys.stdout.write
    for (from_root, from_), targets in sorted(iter(depdict.items()),
                                             key=itemgetter(0)):
        for to_root, to_ in sorted(targets):
            write(repr( ((from_root, from_), (to_root, to_)) ))
            write('\n')

def eliminate_redundant_depends(depends):
    "Remove the redundant dependencies."
    alluniq = set()
    outdeps = []
    for dep in depends:
        if dep in alluniq:
            continue
        alluniq.add(dep)
        outdeps.append(dep)
    return outdeps

def flatten_depends(depends):
    """Yield the list of dependency pairs to a single list of (root, relfn)
    pairs, in the order that they appear. The list is guaranteed to be unique
    (we remove duplicates)."""
    seen = set([(None, None)])
    for dep in depends:
        for pair in dep:
            if pair in seen:
                continue
            seen.add(pair)
            yield pair

                 
