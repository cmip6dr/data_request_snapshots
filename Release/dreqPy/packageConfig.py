"""packageConfig
-------------

Basic information about the package, used by setup.py to populate package metadata.
"""

import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__) )

##DOC_DEFAULT_DIR
DOC_DEFAULT_DIR = os.path.join(PACKAGE_DIR, 'docs')

DOC_DIR = os.environ.get('DRQ_CONFIG_DIR', DOC_DEFAULT_DIR)

__versionComment__ = "Version 01.00.25"
__version__ = "01.00.25"
__title__ = "dreqPy"
__description__ = "CMIP6 Data Request Python API"
__uri__ = "http://proj.badc.rl.ac.uk/svn/exarch/CMIP6dreq/tags/{0}".format(__version__)
__author__ = "Martin Juckes"
__email__ = "martin.juckes@stfc.ac.uk"
__license__ = "BSD"
__copyright__ = "Copyright (c) 2015 Science & Technology Facilities Council (STFC)"

version = __version__
