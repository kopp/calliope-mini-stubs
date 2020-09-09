# source/microbit/modrandom.cpp
# see also https://github.com/python/typeshed/blob/master/stdlib/3/random.pyi

"""
This library provides functions to work with random numbers.
It is similar to the "real" random library
(see https://docs.python.org/3/library/random.html)
but only supports
- ``getrandbits``
- ``seed``
- ``randrange``
- ``randint``
- ``choice``
- ``random``
- ``uniform``
"""


from typing import Optional, Sequence, TypeVar

_T = TypeVar("_T")

__all__ = [
    "getrandbits",
    "seed",
    "randrange",
    "randint",
    "choice",
    "random",
    "uniform",
]


def getrandbits(number_of_bits: int) -> int:
    """Return an interger with ``number_of_bits`` random bits."""
    return int()


def seed(seed_value: int = None) -> None:
    """
    Initialize the random number generator.

    If no seed value is supplied, the NRF51822's in built cryptographic
    random number generator is used to generate one.
    """


def randrange(start: int, stop: Optional[int] = None, step: int = 1) -> int:
    """
    Generate an integer in the range ``start`` ... ``stop`` (``stop`` is
    excluded) with given steps (``step=2`` means that only every second
    number in the range is possible.)

    Call this as ``randrange(stop)`` or ``randrange(start, stop)`` or
    ``randrange(start, stop, steps)``.
    """
    return int()


def randint(start: int, stop: int) -> int:
    """
    Return a random integer i such that ``start <= i <= stop``. Alias for
    ``randrange(start, stop+1)``.
    """
    return int()


def choice(sequence: Sequence[_T]) -> _T:
    """
    Return a random element from the sequence.
    If the sequence is empty, raise ``IndexError``.
    """
    return sequence[0]


def random() -> float:
    """Return a random floating point number between 0 and 1 (1 excluded)."""
    return float()


def uniform(start: float, stop: float) -> float:
    """
    Return a random floating point number ``i`` such that ``i`` is between
    ``start`` and ``stop``.

    This computes ``start + (stop - start) * random()``.
    """
    return float()
