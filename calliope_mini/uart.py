
# source/microbit/microbituart.cpp
# read/write are in source/py/stream.c

from typing import List, Optional, Union, overload

from . import MicroBitDigitalPin


class MicroBitUART:
    """
    The ``uart`` module lets you talk to a device connected to your board using
    a serial interface.

    The right Groove connector (close to button B) has the UART pins.
    """

    ODD: int = 1
    EVEN: int = 2

    def init(self: "MicroBitUART",
             baudrate: int = 9600, bits: int = 8, parity: int = None,
             stop: int = 1,
             *,
             pins: List[int] = None,
             tx: MicroBitDigitalPin = None,
             rx: MicroBitDigitalPin = None) -> None:
        """Initialize serial communication with the specified parameters on the
        specified ``tx`` and ``rx`` pins. Note that for correct communication,
        the parameters have to be the same on both communicating devices.

        .. warning::

            Initializing the UART on external pins will cause the Python
            console on USB to become unaccessible, as it uses the same
            hardware. To bring the console back you must reinitialize the UART
            without passing anything for ``tx'' or ``rx'' (or passing ``None''
            to these arguments).  This means that calling ``uart.init(115200)''
            is enough to restore the Python console.

        The ``baudrate`` defines the speed of communication. Common baud
        rates include:

            * 9600
            * 14400
            * 19200
            * 28800
            * 38400
            * 57600
            * 115200

        The ``bits`` defines the size of bytes being transmitted, and the board
        only supports 8. The ``parity`` parameter defines how parity is
        checked, and it can be ``None``, ``uart.ODD`` or ``uart.EVEN``.  The
        ``stop`` parameter tells the number of stop bits (Note: It may not work
        if this parameter is other than 1.)

        If ``tx`` and ``rx`` are not specified then the internal USB-UART TX/RX
        pins are used which connect to the USB serial convertor on the
        micro:bit, thus connecting the UART to your PC.  You can specify any
        other pins you want by passing the desired pin objects to the ``tx``
        and ``rx`` parameters.

        The ``pins`` argument allows to define the rx and tx pins as well.
        This is deprecated but still supported.  If you use it, use ``[tx,
        rx]``.

        Note, that this will override rx/tx pins specified using the ``rx`` or
        ``tx`` argument.

        .. note::

            When connecting the device, make sure you "cross" the wires -- the
            TX pin on your board needs to be connected with the RX pin on the
            device, and the RX pin -- with the TX pin on the device. Also make
            sure the ground pins of both devices are connected.  """

    def any(self: "MicroBitUART") -> bool:
        """Return ``True`` if any characters waiting, else ``False``."""
        return bool()

    def read(self: "MicroBitUART", nbytes: int = None) -> Optional[bytes]:
        """Read characters.  If ``nbytes`` is specified then read at most that
        many bytes.
        If no bytes are available, returns ``None``.
        """
        return bytes()

    def readinto(self: "MicroBitUART", buf: bytearray,
                 nbytes: int = None) -> Optional[int]:
        """Read bytes into the ``buf``.  If ``nbytes`` is specified then read
        at most that many bytes.  Otherwise, read at most ``len(buf)`` bytes.

        Return value: number of bytes read and stored into ``buf`` or ``None``
        on timeout.
        """
        return int()

    def readline(self: "MicroBitUART",
                 max_size: int = None) -> Optional[bytes]:
        """Read a line, ending in a newline character.

        If ``max_size`` is given, read at most so many characters.

        Return value: the line read or ``None`` on timeout. The newline
        character is included in the returned bytes.
        """
        return bytes()

    @overload
    def write(self: "MicroBitUART", buf: Union[str, bytes, bytearray],
              offset: int = None, length: int = None) -> Optional[int]:
        ...

    @overload
    def write(self: "MicroBitUART",
              buf: Union[str, bytes, bytearray],
              length: int = None) -> Optional[int]:
        ...

    def write(self, *args):
        """
        Write the buffer of bytes to the bus. If ``length`` is given,
        write that number of bytes only, otherwise write the whole buffer.
        If ``offset`` is given, start at the byte at this index.

        Return value: number of bytes written or ``None`` on timeout.

        Note: In the two overloads, ``length`` is at different positions!
        """
        return int()
