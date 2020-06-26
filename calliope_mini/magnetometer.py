# source/microbit/calliopemagnetometer.cpp

from typing import Tuple


class CalliopeMagnetometer:
    """
    Calliope Mini has a BMX055 sensor which is capable to measure the
    magnetic field in a range of typical 1300μT (x- and y-axis)
    respectively ±2500μT (z-axis).
    The magnetic field resolution is about 0.3μT.

    This module allows to access the data.
    """

    def get_x(self: "CalliopeMagnetometer") -> int:
        """
        Return the x-component of the magnetic field measured.

        The x-axis is parallel to the board and points from the USB connector
        (up) to the small connector holes (down).

        The result is a signed integer with 16 bit, i.e. values between -32768
        and 32767.
        """
        return int()

    def get_y(self: "CalliopeMagnetometer") -> int:
        """
        Return the y-component of the magnetic field measured.

        The y-axis is parallel to the board and points from button B (right)
        to button A (left).

        The result is a signed integer with 16 bit, i.e. values between -32768
        and 32767.
        """
        return int()

    def get_z(self: "CalliopeMagnetometer") -> int:
        """
        Return the z-component of the magnetic field measured.

        The z-axis is perpendicular to the board and points from the side
        with buttons, display etc. (top) to the backside (bottom).

        The result is a signed integer with 16 bit, i.e. values between -32768
        and 32767.
        """
        return int()

    def get_values(self: "CalliopeMagnetometer") -> Tuple[int, int, int]:
        """
        Return a tuple with x, y and z components of the magnetic field
        -- see the ``get_x``, ``get_y`` and ``get_z`` methods for more info.

        The result is a tuple with three signed integers with 16 bit, i.e.
        values between -32768 and 32767.
        """
        return (int(), int(), int())
