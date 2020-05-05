from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# Fully qualified module
from future import standard_library
standard_library.install_aliases()
from project import bar

# Fully qualified package
from project import sub1

# Not found.
from project import alien_sym


