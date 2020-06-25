# document
# source/microbit/microbitdisplay.cpp

from typing import overload, Union, Iterable
from .image import MicroBitImage


class MicroBitDisplay:

    def get_pixel(self: "MicroBitDisplay", x: int, y: int) -> int:
        """
        Return the brightness of the LED at column ``x`` and row ``y`` as an
        integer between 0 (off) and 9 (bright).
        """
        return int()

    def set_pixel(self: "MicroBitDisplay", x: int, y: int, value: int) -> None:
        """Set the brightness of the pixel at column ``x`` and row ``y`` to the
        ``value``, which has to be between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in
        read-only images, like ``Image.HEART``.
        """

    # microbit_display_show_func
    def show(self: "MicroBitDisplay",
             image: Union[Union[str, MicroBitImage], Iterable[Union[str, MicroBitImage]]],
             delay: int = 150,
             *,  # remainder is keyword only
             clear: bool = False,
             wait: bool = True,
             loop: bool = False,
             ) -> None:
        """Show the thing."""
        ...

    def scroll(self: "MicroBitDisplay",
               text: str,
               delay: int = 150,
               *,
               wait: bool = True,
               monospace: bool = False,
               loop: bool = False,
               ) -> None:
        ...

    def clear(self: "MicroBitDisplay") -> None:
        ...

    def on(self: "MicroBitDisplay") -> None:
        ...

    def off(self: "MicroBitDisplay") -> None:
        ...

    def is_on(self: "MicroBitDisplay") -> bool:
        ...
