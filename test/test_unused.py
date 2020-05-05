"""
Test ignoring unused imports.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
from os.path import *
from testsupport import *


_files = ['simple/unused.py']

def test_ignore_unused():
    "Test ignoring unused imports."

    for fn in _files:
        fn = join(data, fn)
        print('Testing ignore unused for: %s' % fn)
        compare_expect(fn.replace('.py', '.expect'), None,
                       'sfood', '--ignore-unused', fn, filterdir=(data, 'ROOT'))
