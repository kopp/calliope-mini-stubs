# source/microbit/modmicrobit.cpp


def panic(n: int = 9999) -> None:
    """
    Enter a panic mode.
    To leave this mode, restart the Calliope mini (remove/apply power or press the reset button).
    Pass in an arbitrary integer to indicate a status::

        calliope_mini.panic(255)
    """

def reset() -> None:
    """
    Restart the board.
    """

def sleep(duration_ms: int) -> None:
    """
    Wait for ``duration_ms`` milliseconds. One second is 1000 milliseconds, so::

        calliope_mini.sleep(1000)

    will pause the execution for one second. ``duration_ms`` can be an
    integer or a floating point number.
    """

def running_time() -> int:
    """
    Return the number of milliseconds since the board was switched on or
    restarted.
    """
    return int()

def temperature() -> int:
    """
    Return the temperature of the Calliope Mini in degrees Celcius.
    """
    return int()