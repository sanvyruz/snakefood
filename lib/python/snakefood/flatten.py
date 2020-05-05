"""
Read a snakefood dependencies file and output the list of all files.
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
from os.path import join

from six import print_

from snakefood.depends import read_depends, flatten_depends




def main():
    import optparse
    parser = optparse.OptionParser(__doc__.strip())
    opts, args = parser.parse_args()

    depends = read_depends(sys.stdin)
    for droot, drel in flatten_depends(depends):
        print_(join(droot, drel))
