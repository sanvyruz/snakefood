from __future__ import absolute_import

# Fully qualified module
import project.bar

# Fully qualified package
import project.sub1

# Relative module
from . import bli

# Relative package
from . import sub2

# Not found.
import project.alien
import project.alien.alien2

# More than one level and relative.
from . import sub1.test
 
