#!/usr/bin/python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import sys
from snakefood.depends import read_depends

## def read_depends(f):
##     "Generator for the dependencies read from the given file object."
##     for line in f:
##         try:
##             yield eval(line)
##         except Exception:
##             logging.warning("Invalid line: '%s'" % line)

depends = read_depends (sys.stdin)

for d in depends:

    if (d[0][0].startswith ('/home/nbecker/idma-cdma') and \
        (d[1][0] == None or \
         d[1][0].startswith ('/home/nbecker/idma-cdma'))):
        print(d)
