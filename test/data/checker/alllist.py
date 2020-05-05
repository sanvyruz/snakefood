#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
__all__ = ('mod1', 'mod2', 'mod3', 'sym1')

import mod1
import mod2, mod3
from mod4 import sym1



