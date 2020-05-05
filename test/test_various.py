"""
Various tests.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
from os.path import *
from testsupport import *


_files = [
    'simple/stdlib.py',
    'simple/invalid.py',
    'simple/notfound.py',
    'project/foo_import.py',
    'project/foo_from.py',
    'project/sub1/sub11/relative_from.py',
    ]

def test_various():
    "Test ignoring unused imports."

    for fn in _files:
        fn = join(data, fn)
        print('Testing for: %s' % fn)
        compare_expect(fn.replace('.py', '.expect'), None,
                       'sfood', fn, filterdir=(data, 'ROOT'))
