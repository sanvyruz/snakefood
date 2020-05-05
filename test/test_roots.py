"""
Test roots computation.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
from os.path import *
from testsupport import *


def test_roots():
    "Test that the root directories are being calculated correctly."
    for dn in find_dirs(join(data, 'roots')):
        print('Testing roots for: %s' % dn)
        compare_expect(join(dn, '.expect'), None,
                       'sfood', '--print-roots', dn, filterdir=(data, 'ROOT'))
