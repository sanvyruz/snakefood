#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import sys, types, imp
from imp import find_module
from pkgutil import ImpImporter
from os.path import *


root = '/home/blais/p/snakefood/test/snakefood'
sys.path.insert(0, root)

## i = ImpImporter(join(root, 'project'))
## mod = i.find_module('bar')
## print mod, mod.get_filename()

## import project.bar

i = ImpImporter()
mod = i.find_module('project')
print(mod, mod.get_filename())

i = ImpImporter(dirname(mod.get_filename()))
mod = i.find_module('bar')
print(mod, mod.get_filename())




