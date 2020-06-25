# source/microbit/calliopesensor.cpp

# Note: this is copy/paste from the more precise classes; see class docstring.

from typing import Tuple


class CalliopeSensor:
    """
    Calliope Mini has a BMX055 sensor which is capable to measure
    acceleration, rotation and magnetic field.

    Please see the classes

    ``CalliopeAccelerometer``
    ``CalliopeGyrometer``
    ``CalliopeMagnetometer``

    for more info.

    This module is a shortcut to to access the data.
    """

    def get_temp(self: "CalliopeSensor") -> int:
        """
        Return the temperature of the Calliope Mini in degrees Celcius.
        """
        return int()

    def get_acc_x(self: "CalliopeSensor") -> int:
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

    def get_acc_y(self: "CalliopeSensor") -> int:
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

    def get_acc_z(self: "CalliopeSensor") -> int:
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

    def get_acc_values(self: "CalliopeSensor") -> Tuple[int, int, int]:
        """
        Return a tuple with x, y and z components of the acceleration
        -- see the ``get_x``, ``get_y`` and ``get_z`` methods for more info.

        The result is a tuple with three signed integers with 16 bit, i.e. values between -32768 and 32767.
        """
        return (int(), int(), int())

# gyrometer

    def get_gyro_x(self: "CalliopeSensor") -> int:
        """
        Return the x-component of the rotation.

        The x-axis is parallel to the board and points from the USB connector
        (up) to the small connector holes (down).

        The value is positive, if the board is rotated around the x-axis
        such that Button A is moved downwards.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_gyro_y(self: "CalliopeSensor") -> int:
        """
        Return the y-component of the rotation.

        The y-axis is parallel to the board and points from button B (right)
        to button A (left).

        The value is positive, if the board is rotated around the y-axis
        such that the USB connector is moved upwards.

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_gyro_z(self: "CalliopeSensor") -> int:
        """
        Return the z-component of the magnetic field measured.

        The z-axis is perpendicular to the board and points from the side
        with buttons, display etc. (top) to the backside (bottom).

        The value is positive, if the board is rotated around the z-axis
        such that the USB connector is moved to the left (in direction of
        Button A).

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_gyro_values(self: "CalliopeSensor") -> Tuple[int, int, int]:
        """
        Return a tuple with x, y and z components of the rotation
        -- see the ``get_x``, ``get_y`` and ``get_z`` methods for more info.

        The result is a tuple with three signed integers with 16 bit, i.e. values between -32768 and 32767.
        """
        return (int(), int(), int())

# magnetometer

    def get_mag_x(self: "CalliopeSensor") -> int:
        """
        Return the x-component of the magnetic field measured.

        The x-axis is parallel to the board and points from the USB connector
        (up) to the small connector holes (down).

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_mag_y(self: "CalliopeSensor") -> int:
        """
        Return the y-component of the magnetic field measured.

        The y-axis is parallel to the board and points from button B (right)
        to button A (left).

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_mag_z(self: "CalliopeSensor") -> int:
        """
        Return the z-component of the magnetic field measured.

        The z-axis is perpendicular to the board and points from the side
        with buttons, display etc. (top) to the backside (bottom).

        The result is a signed integer with 16 bit, i.e. values between -32768 and 32767.
        """
        return int()

    def get_mag_values(self: "CalliopeSensor") -> Tuple[int, int, int]:
        """
        Return a tuple with x, y and z components of the magnetic field
        -- see the ``get_x``, ``get_y`` and ``get_z`` methods for more info.

        The result is a tuple with three signed integers with 16 bit, i.e. values between -32768 and 32767.
        """
        return (int(), int(), int())

