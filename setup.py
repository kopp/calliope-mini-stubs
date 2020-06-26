from setuptools import setup


with open("Readme.md", "r") as fh:
    long_description = fh.read()


setup(
    name="calliope-mini-stubs",
    version="0.0.4",
    author="kopp",
    author_email="kopp.michael@yahoo.de",
    description="Provide stubs with documentation for the MicroPython running on Calliope Mini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kopp/calliope-mini-stubs",
    packages=["calliope_mini", "radio", "utime"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
