#!/usr/bin/env python

# Module that cannot be found.
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import alien_module_yeah

# Package that cannot be found.
import alien_package.alien_module

# From variants.
from alien_module_yeah import alien_symbol
from alien_package import alien_module
