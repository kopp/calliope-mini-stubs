from setuptools import setup


GITHUB_URL = "https://github.com/kopp/calliope-mini-stubs"


setup(
    name="calliope-mini-stubs",
    version="0.0.6",
    author="kopp",
    description="Provide stubs with documentation for the MicroPython running on Calliope Mini",
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



Please see
[the repository on GitHub]({})
for how a simple step-by-step instruction how to use it.
    """.format(GITHUB_URL),
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    packages=["calliope_mini", "radio", "utime"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
