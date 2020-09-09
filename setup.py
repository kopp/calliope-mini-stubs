import move_this_directory_in_path  # Import before setuptools:
# Since this folder contains a `random` module which conflicts with the
# system's random module, make sure that the system's module is found when
# using `import random`.
from setuptools import setup


GITHUB_URL = "https://github.com/kopp/calliope-mini-stubs"


setup(
    name="calliope-mini-stubs",
    version="0.1.0",
    author="kopp",
    description=("Provide stubs with documentation for "
                 "MicroPython running on Calliope Mini"),
    long_description="""# CalliopeMini Stubs

Use this library to develop your python programs for the
[Calliope Mini](https://calliope.cc/)
using a state-of-the-art python IDE such as
[Visual Studio Code](https://code.visualstudio.com/)
on your computer.

This library only helps by providing documentation, type annotations and
function signatures.
It does not contain a simulator/emulator and it does not allow to transfer the
developed code to the Calliope Mini.

Make sure to install this only in a local virtual environment as some
libraries overwrite "system" libraries and thus make scripts that are not
intended to run on the Calliope Mini fail.


Please see
[the repository on GitHub]({})
for how a simple step-by-step instruction how to use it.
    """.format(GITHUB_URL),
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    packages=[
        "antigravity",
        "calliope_mini",
        "love",
        "music",
        "os",
        "radio",
        "random",
        "this",
        "utime",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
