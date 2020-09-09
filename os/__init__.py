"""
The os module provides a way to get basic information about the files in the
simple file system on the Calliope Mini and the Calliope Mini itself.

The os module only has the functions
- remove(filename: str)
- listdir() -> List[str]:
- size(filename: str) -> int:
- uname()

Since there is a "real" os module in your python installation, your IDE will
propose functions that are not available in MicroPython.


To read from/write to those files, use e.g. ``open(filename, "r")``.
"""

from typing import List, Tuple


def remove(filename: str) -> None:
    """
    Remove the file with the given filename.
    """


def listdir() -> List[str]:
    """
    Return a list of all known files on the filesystem.
    """
    return []


def size(filename: str) -> int:
    """
    Return the size of the given file in bytes.
    """
    return int()


def uname() -> Tuple[str, str, str, str, str]:
    """
    Return a tuple with named entries that contains information about the
    system and the MicroPython version running on it.
    """
    ...
