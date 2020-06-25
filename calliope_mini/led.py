# source/microbit/calliopeled.cpp

from typing import Tuple


class CalliopeLED:
    """
    Calliope Mini has a color-LED which is similar to a NeoPixel strip with only one LED.

    The driver in use is based on this one: https://github.com/lavallc/nrf51-neopixel
    """

    def set_red(self: "CalliopeLED", brightness_red: int) -> None:
        """
        Set the brightness for the red component of the LED.

        Use values between 0 (dark/off) and 255 (maximal brightness) to
        control the brightness.
        Values out of that range will be mapped into that range using ``value % 256``.
        """

    def set_green(self: "CalliopeLED", brightness_green: int) -> None:
        """
        Set the brightness for the green component of the LED.

        Use values between 0 (dark/off) and 255 (maximal brightness) to
        control the brightness.
        Values out of that range will be mapped into that range using ``value % 256``.
        """

    def set_blue(self: "CalliopeLED", brightness_blue: int) -> None:
        """
        Set the brightness for the blue component of the LED.

        Use values between 0 (dark/off) and 255 (maximal brightness) to
        control the brightness.
        Values out of that range will be mapped into that range using ``value % 256``.
        """

    def get_red(self: "CalliopeLED") -> int:
        """
        Returns the brightness for the red component of the LED.

        The output is between 0 (dark/off) and 255 (maximal brightness).
        """
        return int()

    def get_green(self: "CalliopeLED") -> int:
        """
        Returns the brightness for the green component of the LED.

        The output is between 0 (dark/off) and 255 (maximal brightness).
        """
        return int()

    def get_blue(self: "CalliopeLED") -> int:
        """
        Returns the brightness for the blue component of the LED.

        The output is between 0 (dark/off) and 255 (maximal brightness).
        """
        return int()

    def set_colors(self: "CalliopeLED", brightness_red: int, brightness_green: int, brightness_blue: int) -> None:
        """
        Set the brightness for all components of the LED (red, green, blue).

        Use values between 0 (dark/off) and 255 (maximal brightness) to
        control the brightnesses.
        Values out of that range will be mapped into that range using ``value % 256``.

        .. note::
            This corresponds to the HTML notation of colors.
            See e.g. https://htmlcolorcodes.com/
        """

    def get_colors(self: "CalliopeLED") -> Tuple[int, int, int]:
        """
        Returns a tuple containing the brightnesses for all components of the
        LED (red, green, blue).

        The values are between 0 (dark/off) and 255 (maximal brightness).

        .. note::
            This corresponds to the HTML notation of colors.
            See e.g. https://htmlcolorcodes.com/
        """
        return (int(), int(), int())

    def clear(self: "CalliopeLED") -> None:
        """
        Turn the LED off (brightness for all colors is set to 0).
        """
