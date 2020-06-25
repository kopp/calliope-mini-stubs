from typing import Union


"""
This library provides functionality to measure time and sleep for a given
duration.

Note: Make sure to import ``utime`` in your code instead of ``time``.
Calliope Mini has an "alias" so that importing ``time`` works on the device
as well, but this screws up the editor support on your computer, as this then
assumes that the built-in module ``time`` is used.
"""


__all__ = [
    "sleep",
    "sleep_ms",
    "sleep_us",
    "ticks_ms",
    "ticks_us",
    "ticks_diff",
    "ticks_add",
]


def sleep(seconds: float) -> None:
    """
    Sleep (i.e. block) for a given number of seconds.
    """
    ...


def sleep_ms(milliseconds: int) -> None:
    """
    Sleep (i.e. block) for a given number of milliseconds.
    """
    ...


def sleep_us(microseconds: int) -> None:
    """
    Sleep (i.e. block) for a given number of microseconds.
    """
    ...


def ticks_ms() -> int:
    """
    Return a tick counter value in milliseconds resolution.

    See ``ticks_us``.
    """
    return int()


def ticks_us() -> int:
    """
    Return some ticks in microseconds resolution.
    You can use these ticks to compute an elapsed time in microseconds by using ``ticks_diff``.
    The tick values themselves do not have a well defined meaning.
    They "wrap around" after some period, so make sure to use the
    ``ticks_diff`` and ``ticks_add`` functions when working with them.
    """
    return int()


def ticks_diff(end: int, start: int) -> int:
    """
    Number of ticks between ``start`` and ``end``.

    Since the ticks can "wrap around", this method is useful to determine,
    how many ticks happened without needing to care, that ``end`` may be
    smaller than ``start``.

    Note: If the counter wrapped around multiple times, this function will
    not be able to know that and thus will assume, that it wrapped once (or
    not at all if ``end > start``).
    """
    return end - start


def ticks_add(ticks: int, delta: Union[int, float]) -> int:
    """
    Computes the tick count, if ``delta`` additional ticks happen after the
    given ``ticks`` (and performs the wrap-around).
    """
    return int(ticks + delta)
