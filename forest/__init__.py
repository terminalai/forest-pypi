# -*- coding: utf-8 -*-
#from .forest import *
#from .forestdata import *
from .lazy import *


#  set __version__ attribute
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound
