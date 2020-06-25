from typing import overload, List, Any


class MicroBitImage:
    """
    Use this class to create images that can be displayed easily on the
    device's LED matrix.
    Given an image object it's possible to display it via the ``display``
    API::

        from calliope_mini import *
        display.show(Image.HAPPY)

    The following (read only) images are avaliable to use (e.g. ``Image.HEART``).
    To edit one of them, copy them first, e.g.

        my_image = Image.SMILE.copy()
        my_image.set_pixel(2, 2, 5)
        display.show(my_image)

     - ``HEART``
     - ``HEART_SMALL``
     - ``HAPPY``
     - ``SMILE``
     - ``SAD``
     - ``CONFUSED``
     - ``ANGRY``
     - ``ASLEEP``
     - ``SURPRISED``
     - ``SILLY``
     - ``FABULOUS``
     - ``MEH``
     - ``YES``
     - ``NO``
     - ``CLOCK12``
     - ``CLOCK1``
     - ``CLOCK2``
     - ``CLOCK3``
     - ``CLOCK4``
     - ``CLOCK5``
     - ``CLOCK6``
     - ``CLOCK7``
     - ``CLOCK8``
     - ``CLOCK9``
     - ``CLOCK10``
     - ``CLOCK11``
     - ``ALL_CLOCKS``: A tuple containing all clocks (starting at 12, then 1, ...)
     - ``ARROW_N``
     - ``ARROW_NE``
     - ``ARROW_E``
     - ``ARROW_SE``
     - ``ARROW_S``
     - ``ARROW_SW``
     - ``ARROW_W``
     - ``ARROW_NW``
     - ``ALL_ARROWS``: A tuple containing all arrows (starting from top, then top rigth, ...)
     - ``TRIANGLE``
     - ``TRIANGLE_LEFT``
     - ``CHESSBOARD``
     - ``DIAMOND``
     - ``DIAMOND_SMALL``
     - ``SQUARE``
     - ``SQUARE_SMALL``
     - ``RABBIT``
     - ``COW``
     - ``MUSIC_CROTCHET``
     - ``MUSIC_QUAVER``
     - ``MUSIC_QUAVERS``
     - ``PITCHFORK``
     - ``XMAS``
     - ``PACMAN``
     - ``TARGET``
     - ``TSHIRT``
     - ``ROLLERSKATE``
     - ``DUCK``
     - ``HOUSE``
     - ``TORTOISE``
     - ``BUTTERFLY``
     - ``STICKFIGURE``
     - ``GHOST``
     - ``SWORD``
     - ``GIRAFFE``
     - ``SKULL``
     - ``UMBRELLA``
     - ``SNAKE``
    """

    @overload
    def __init__(self, string: str) -> None:
        """``string`` has to consist of digits 0-9 arranged into lines,
        describing the image, for example::

            image = Image("90009:"
                          "09090:"
                          "00900:"
                          "09090:"
                          "90009")

        will create a 5×5 image of an X. The end of a line is indicated by a
        colon. It's also possible to use a newline (\n) to indicate the end of
        a line like this::

            image = Image("90009\n"
                          "09090\n"
                          "00900\n"
                          "09090\n"
                          "90009")
        """
        ...

    @overload
    def __init__(self, width: int = None, height: int = None,
                 buffer: Any = None) -> None:
        """Create an empty image with ``width`` columns and ``height`` rows.
        Optionally ``buffer`` can be an array of ``width``×``height`` integers
        in range 0-9 to initialize the image.
        """
        ...

    def __init__(self: "MicroBitImage", *args, **kwargs):
        ...

    def width(self: "MicroBitImage") -> int:
        return int()

    def height(self: "MicroBitImage") -> int:
        return int()

    def get_pixel(self: "MicroBitImage", x: int, y: int) -> int:
        return int()

    def set_pixel(self: "MicroBitImage", x: int, y: int, brightness: int) -> None:
        """
        Set the pixel at position ``x, y`` to given ``brightness`` which
        must be ``0, 1, ..., 9``.
        """

    def shift_left(self: "MicroBitImage", n: int) -> "MicroBitImage":
        """
        Shift the image content left by ``n`` pixels.
        Use a negative value to shift right.
        """
        return MicroBitImage()

    def shift_right(self: "MicroBitImage", n: int) -> "MicroBitImage":
        """
        Shift the image content right by ``n`` pixels.
        Use a negative value to shift left.
        """
        return MicroBitImage()

    def shift_up(self: "MicroBitImage", n: int) -> "MicroBitImage":
        """
        Shift the image content up by ``n`` pixels.
        Use a negative value to shift down.
        """
        return MicroBitImage()

    def shift_down(self: "MicroBitImage", n: int) -> "MicroBitImage":
        """
        Shift the image content down by ``n`` pixels.
        Use a negative value to shift upwards.
        """
        return MicroBitImage()

    def copy(self: "MicroBitImage") -> "MicroBitImage":
        """Return a copy of the this image."""
        return MicroBitImage()

    def crop(self: "MicroBitImage", x: int, y: int, w: int, h: int) -> "MicroBitImage":
        """
        Return a new image by cropping the picture to a width of ``w`` and a
        height of ``h``, starting with the pixel at column ``x`` and row
        ``y``.
        """
        return MicroBitImage()

    def invert(self: "MicroBitImage") -> "MicroBitImage":
        return MicroBitImage()

    def fill(self: "MicroBitImage", brightness: int) -> None:
        """
        Fill all pixels in the image with the given ``brightness`` (which
        must be between 0 (dark) and 9 (bright).
        """

    def blit(self: "MicroBitImage",
             src: "MicroBitImage",
             x: int, y: int, w: int, h: int,
             xdest: int = 0, ydest: int = 0,
             ) -> None:
        """
        Copy the rectangle defined by ``x``, ``y``, ``w``, ``h`` from the
        image ``src`` into this image at ``xdest``, ``ydest``. Areas in the
        source rectangle, but outside the source image are treated as having a
        value of 0.

        This is a quite advanced function -- prefer to use one of
        ``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
        and ``crop()`` which are all implemented by using ``blit()``.

        For example, img.crop(x, y, w, h) can be implemented as::

            def crop(self, x, y, w, h):
                res = Image(w, h)
                res.blit(self, x, y, w, h)
                return res
        """

    HEART: "MicroBitImage"
    HEART_SMALL: "MicroBitImage"
    HAPPY: "MicroBitImage"
    SMILE: "MicroBitImage"
    SAD: "MicroBitImage"
    CONFUSED: "MicroBitImage"
    ANGRY: "MicroBitImage"
    ASLEEP: "MicroBitImage"
    SURPRISED: "MicroBitImage"
    SILLY: "MicroBitImage"
    FABULOUS: "MicroBitImage"
    MEH: "MicroBitImage"
    YES: "MicroBitImage"
    NO: "MicroBitImage"
    CLOCK12: "MicroBitImage"
    CLOCK1: "MicroBitImage"
    CLOCK2: "MicroBitImage"
    CLOCK3: "MicroBitImage"
    CLOCK4: "MicroBitImage"
    CLOCK5: "MicroBitImage"
    CLOCK6: "MicroBitImage"
    CLOCK7: "MicroBitImage"
    CLOCK8: "MicroBitImage"
    CLOCK9: "MicroBitImage"
    CLOCK10: "MicroBitImage"
    CLOCK11: "MicroBitImage"
    ARROW_N: "MicroBitImage"
    ARROW_NE: "MicroBitImage"
    ARROW_E: "MicroBitImage"
    ARROW_SE: "MicroBitImage"
    ARROW_S: "MicroBitImage"
    ARROW_SW: "MicroBitImage"
    ARROW_W: "MicroBitImage"
    ARROW_NW: "MicroBitImage"
    TRIANGLE: "MicroBitImage"
    TRIANGLE_LEFT: "MicroBitImage"
    CHESSBOARD: "MicroBitImage"
    DIAMOND: "MicroBitImage"
    DIAMOND_SMALL: "MicroBitImage"
    SQUARE: "MicroBitImage"
    SQUARE_SMALL: "MicroBitImage"
    RABBIT: "MicroBitImage"
    COW: "MicroBitImage"
    MUSIC_CROTCHET: "MicroBitImage"
    MUSIC_QUAVER: "MicroBitImage"
    MUSIC_QUAVERS: "MicroBitImage"
    PITCHFORK: "MicroBitImage"
    XMAS: "MicroBitImage"
    PACMAN: "MicroBitImage"
    TARGET: "MicroBitImage"
    TSHIRT: "MicroBitImage"
    ROLLERSKATE: "MicroBitImage"
    DUCK: "MicroBitImage"
    HOUSE: "MicroBitImage"
    TORTOISE: "MicroBitImage"
    BUTTERFLY: "MicroBitImage"
    STICKFIGURE: "MicroBitImage"
    GHOST: "MicroBitImage"
    SWORD: "MicroBitImage"
    GIRAFFE: "MicroBitImage"
    SKULL: "MicroBitImage"
    UMBRELLA: "MicroBitImage"
    SNAKE: "MicroBitImage"
    ALL_CLOCKS: List["MicroBitImage"]
    ALL_ARROWS: List["MicroBitImage"]
