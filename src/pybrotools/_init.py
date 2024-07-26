# Copyright 2024 PYBROTOOLS authors.
# See license.md file for details.

# Import classes, functions
from importlib.metadata import version
from importlib.util import find_spec
from pathlib import Path
from re import Match, match
from sys import modules, stderr
from typing import cast

from loguru import logger

# Set Python package constants
MODULE_NAME = modules[__name__].__name__.split(".")[0]
"""Name of the Python module."""

MODULE_PATH: str = Path(find_spec(MODULE_NAME).origin).parent
"""Absolute path of the module."""

# Set package version
__version__: str = version(MODULE_NAME)
"""Version of the Python module."""

result = cast(Match[str], match(r"(\d+\.\d+\.\d+).*", __version__))
__version_info__: tuple[str] = tuple(result.group(1).split("."))
"""Version information of the Python module."""

def module_info() -> str:
    """Returns a string containing information about the Python module.

    Returns:
        Information about the module including its name, path, and version.
    """
    txt  = f" Module: {MODULE_NAME}\n"
    txt += f"   Path: {MODULE_PATH}\n"
    txt += f"Version: {__version__}"

    return txt

def init_logging(console: str = "SUCCESS", file: str = "NONE") -> logger:
    """Initialize logging configuration for console and file handlers.

    By convention, the standard logging level are designated by a name in
    uppercase. The equivalent logger function has the same name in lowercase.
    Here is the list of all standard logging levels: "TRACE", "DEBUG", "INFO",
    "SUCCESS", "WARNING", "ERROR", "CRITICAL".

    Parameters:
        console: The logging level for console output. Default is "SUCCESS".
        file: The logging level for file output. Default is "NONE".

    Returns:
        logger: The configured logger handler.
    """
    # Reset logging handlers
    logger.remove()

    # Define logging to a rotating file
    if file != "NONE":
        logger.add(
            "pybrotools.log",
            rotation="5 seconds",
            level=file,
            format="{time:MMMM D, YYYY > HH:mm:ss!UTC} | {level}\n{message}\n",
        )

        log_txt = "Configured logging in `pybrotools.log` file to {file} lvl."
        logger.info(log_txt)

    # Define logging to console
    logger.add(
        stderr,
        level=console,
        format="{time:MMMM D, YYYY > HH:mm:ss!UTC} | {level}\n{message}\n",
    )
    logger.info(f"Configured logging in console to {console} lvl.")

    # Return logger handler
    return logger
