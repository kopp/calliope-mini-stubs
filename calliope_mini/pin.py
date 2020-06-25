from  typing import Union


class MicroBitDigitalPin:
    """
    A digital pin can output HIGH or LOW voltage by writing logic 1 (HIGH
    voltage) or logic 0 (LOW voltage) to the instance of this class (see
    ``write_digital``) or read an applied voltage (see ``read_digital``).

    Additionally it can generate a PWM signal using ``write_analog`` -- you
    can control the duty cycle by ``write_analog``.
    (See also the ``get/set_analog_period`` commands for how to specify the
    period duration.

    The pins also have built-in pull up/pull down resistors.
    The pull mode for a pin is automatically configured when the pin changes to an
    input mode. Input modes are when you call ``read_analog`` / ``read_digital`` /
    ``is_touched``. The pull mode for these is, respectively, ``NO_PULL``,
    ``PULL_DOWN``, ``PULL_UP``. Only when in ``read_digital`` mode can you call
    ``set_pull`` to change the pull mode from the default.

    Pins are in one of the following modes.
    It is set into this mode automatically and you can use ``get_mode`` to
    query the current mode.
    Note, that not all pins can go into all modes -- for example only
    ``MicroBitTouchPin``s can go into mode ``touch``.

      - unused
      - write_analog
      - read_digital
      - write_digital
      - display -- pin drives LEDs in the display matrix
      - button -- pin is used for button A or B
      - music
      - audio
      - touch
      - i2c -- pin is used in the i2c capable groove connector
      - spi

    """

    NO_PULL: int = 0
    PULL_UP: int = 1
    PULL_DOWN: int = 2

    def read_digital(self) -> int:
        """Return 1 if the pin is high, and 0 if it's low."""
        return int()

    def write_digital(self, value: int) -> None:
        """Set the pin to high if ``value`` is 1, or to low, if it is 0."""
        ...

    def write_analog(self, value: Union[int, float]) -> None:
        """Output a PWM signal on the pin, with the duty cycle proportional to
        the provided ``value``. The ``value`` may be either an integer or a
        floating point number.
        For both integers and floats use values between 0 (0% duty cycle) and 1023 (100% duty).
        """
        ...

    def set_analog_period(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in
        milliseconds.  Values must be between 1 and 1000.
        """
        if not 1 <= period <= 1000:
            raise ValueError("invalid period")

    def set_analog_period_microseconds(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in
        microseconds.  Values must be between 256 and 1000000.
        """
        if not 256 <= period <= 1000000:
            raise ValueError("invalid period")

    def get_analog_period_microseconds(self) -> int:
        """Return the period of the PWM signal in microseconds."""
        return int()

    def set_pull(self, value: int = (NO_PULL or PULL_UP or PULL_DOWN)) -> None:
        """Set the pull state to one of three possible values: ``pin.PULL_UP``,
        ``pin.PULL_DOWN`` or ``pin.NO_PULL`` (where ``pin`` is an instance of
        a pin).
        
        See class ``MicroBitDigitalPin`` for more info.
        """
        ...

    def get_pull(self) -> int:
        """
        Return the pull mode the pin is in (``NO_PULL``, ``PULL_UP``, ``PULL_DOWN``).

        See class ``MicroBitDigitalPin`` for more info.
        """
        return int()

    def get_mode(self) -> str:
        """
        Return the mode the pin is currently in.
        """
        return str()


class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """
    Pins of this class have all capabilities as ``MicroBitDigitalPin``s, and
    additionally they can read an applied analog voltage (i.e. they include
    an analog-to-digital-converter, ADC).
    See ``read_analog``.
    """
    def read_analog(self) -> int:
        """Read the voltage applied to the pin, and return it as an integer
        between 0 (meaning 0V) and 1023 (meaning 3.3V).
        """
        return int()


class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """
    Pins of this class have all capabilities as ``MicroBitAnalogDigitalPin``s, and
    additionally can tell, whether they are touched with a finger or not.
    See ``is_touched``.
    """
    def is_touched(self) -> bool:
        """Return ``True`` if the pin is being touched with a finger, otherwise
        return ``False``.

        This test is done by measuring the capacitance of the pin together with
        whatever is connected to it. Human body has quite a large capacitance,
        so touching the pin gives a dramatic change in reading, which can be
        detected.
        """
        return bool()