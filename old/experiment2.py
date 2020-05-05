#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import types, imp
from imp import find_module
from pkgutil import ImpImporter
from os.path import *

for a in (imp.PY_SOURCE,
          imp.PY_COMPILED,
          imp.C_EXTENSION,
          imp.PY_RESOURCE,
          imp.PKG_DIRECTORY,
          imp.C_BUILTIN,
          imp.PY_FROZEN):
    print(a)


modname = 'signal'
mod = ImpImporter().find_module(modname)
print('mod', mod)
print('filename', mod.get_filename())
print('source', mod.get_source())
print('code', mod.get_code())
print('file', mod.file)
print('etc', mod.etc)
## print 'ispackage', mod.is_package('util')
## print 'data', mod.get_data()

for a in dir(mod):
    v = getattr(mod, a)
    print(a, v)


