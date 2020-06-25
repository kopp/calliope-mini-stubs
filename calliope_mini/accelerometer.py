
# source/microbit/calliopeaccelerometer.cpp

from typing import Tuple

class CalliopeAccelerometer:
    """
    Calliope Mini has a BMX055 sensor which is capable to measure the
    acceleration of the device in a range of 2 g with a
    sensitivity of about 0.001 g, a tolerance in the order of 0.1 g and a
    bandwidth of about 16 Hz.

    Note: For the accelerometer to deliver reasonable values, turn the device
    on when it is lying flat on its back on an even surface.

    This module allows to access the data.
    """
    # Note: the BMX055 has different modi for the accelerometer.
    #       See the init(..) function of BMX055 in
    #       inc/lib/bmx055.h
    #       where the parameters are selected.
    #       Currently, this is a range of 2g and 15.63 Hz bandwidth, 32 ms update time.
    #       See also the datasheet
    #       https://www.mouser.de/datasheet/2/783/BST-BMX055-DS000-1509552.pdf
    #       and an explanation for LSB/degree/sec here
    #       https://arduino.stackexchange.com/a/14476

    def get_x(self: "CalliopeAccelerometer") -> int:
        """
        Return the x-component of the acceleration.

        Note: For the accelerometer to deliver reasonable values, turn the device
        on when it is lying flat on its back on an even surface.

        The x-axis is parallel to the board and points from the USB connector
        (up) to the small connector holes (down).

        The value is positive, if the acceleration is going into the
        direction of the USB connector.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_y(self: "CalliopeAccelerometer") -> int:
        """
        Return the y-component of the acceleration.

        Note: For the accelerometer to deliver reasonable values, turn the device
        on when it is lying flat on its back on an even surface.

        The y-axis is parallel to the board and points from button B (right)
        to button A (left).

        The value is positive, when the acceleration is going into the
        direction of Button A.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_z(self: "CalliopeAccelerometer") -> int:
        """
        Return the z-component of the acceleration.

        Note: For the accelerometer to deliver reasonable values, turn the device
        on when it is lying flat on its back on an even surface.

        The z-axis is perpendicular to the board and points from the side
        with buttons, display etc. (top) to the backside (bottom).

        The value is positive, when the acceleration is going into the
        direction of the bottom of the board.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_values(self: "CalliopeAccelerometer") -> Tuple[int, int, int]:
        """
        Return a tuple with x, y and z components of the acceleration
        -- see the ``get_x``, ``get_y`` and ``get_z`` methods for more info.

        The result is a tuple with three signed integers with 16 bit, i.e. values between -32768 and 32767.
        """
        return (int(), int(), int())
