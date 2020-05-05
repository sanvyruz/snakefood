"""
A helper module to build simple filter scripts.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import open
from future import standard_library
standard_library.install_aliases()
from six import print_

import sys
from os.path import join


def do_filter(populate_parser=None):
    import optparse
    parser = optparse.OptionParser(__doc__.strip())
    opts, args = parser.parse_args()

    if not args:
        args = ['-']
    for fn in args:
        if fn == '-':
            f = sys.stdin
        else:
            f = open(fn)

        for line in f:
            try:
                yield eval(line)
            except Exception as e:
                print_(e, sys.stderr)
                raise SystemExit
