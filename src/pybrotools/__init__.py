# Copyright 2024 PYBROTOOLS authors.
# See license.md file for details.
"""pybrotools module -- tools for clinical science projects.

*pybrotools* is a Python package gathering tools for clinical science
activities. Beyond gathering different tools, the objective of this module is
to provide different method or classes to simplify development of new tools and
accelerate development of these tools.
"""

# Import local functions, variables
from pybrotools._init import (
    MODULE_NAME,
    MODULE_PATH,
    __version__,
    __version_info__,
    init_logging,
    module_info,
)

# Declare local functions, variables
__all__ = [
    "MODULE_NAME",
    "MODULE_PATH",
    "__version__",
    "__version_info__",
    "init_logging",
    "module_info",
]
