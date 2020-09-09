"""
Importing this file will modify sys.path.
Since pep8 has rule E402 that states, that imports should be at the top of a
file, but this modification is necessary before includes happen, include it
first.
"""

from sys import path
import os


this_directory = os.path.dirname(os.path.realpath(__file__))
try:
    index_of_this_directory_in_path = path.index(this_directory)
    path.pop(index_of_this_directory_in_path)
    path.append(this_directory)
except ValueError:
    print(("Note: Current directory {} "
           "not found in path {}.").format(this_directory, path))
