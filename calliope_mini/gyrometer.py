# source/microbit/calliopegyrometer.cpp

from typing import Tuple


class CalliopeGyrometer:
    """
    Calliope Mini has a BMX055 sensor which is capable to measure the
    rotation of the device in a range of 125 degrees/second with a
    sensitivity of about 0.004 degrees/second and a tolerance in the order of
    1%.

    This module allows to access the data.
    """
    # Note: the BMX055 has different modi for the gyroscope.
    #       See the init(..) function of BMX055 in
    #       inc/lib/bmx055.h
    #       where the parameters are selected.
    #       Currently, this is 125 degrees/second.
    #       See also the datasheet
    #       https://www.mouser.de/datasheet/2/783/BST-BMX055-DS000-1509552.pdf
    #       and an explanation for LSB/degree/sec here
    #       https://arduino.stackexchange.com/a/14476

    def get_x(self: "CalliopeGyrometer") -> int:
        """
        Return the x-component of the rotation.

        The x-axis is parallel to the board and points from the USB connector
        (up) to the small connector holes (down).

        The value is positive, if the board is rotated around the x-axis
        such that Button A is moved downwards.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_y(self: "CalliopeGyrometer") -> int:
        """
        Return the y-component of the rotation.

        The y-axis is parallel to the board and points from button B (right)
        to button A (left).

        The value is positive, if the board is rotated around the y-axis
        such that the USB connector is moved upwards.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_z(self: "CalliopeGyrometer") -> int:
        """
        Return the z-component of the rotation.

        The z-axis is perpendicular to the board and points from the side
        with buttons, display etc. (top) to the backside (bottom).

        The value is positive, if the board is rotated around the z-axis
        such that the USB connector is moved to the left (in direction of
        Button A).

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_values(self: "CalliopeGyrometer") -> Tuple[int, int, int]:
        """
        Return a tuple with x, y and z components of the rotation
        -- see the ``get_x``, ``get_y`` and ``get_z`` methods for more info.

        The result is a tuple with three signed integers with 16 bit, i.e. values between -32768 and 32767.
        """
        return (int(), int(), int())
