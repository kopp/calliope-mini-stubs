# source/microbit/microbiti2c.cpp

from typing import List, Union

from .pin_instances import c18, c19


class MicroBitI2C:
    """
    The ``i2c`` module lets you communicate with devices connected to your
    board using the I²C bus protocol. There can be multiple slave devices
    connected at the same time, and each one has its own unique address, that
    is either fixed for the device or configured on it. Your board acts as the
    I²C master.

    The left Grove connector (next to button A) is I²C-capable.

    How exactly you should communicate with the devices, that is, what bytes to
    send and how to interpret the responses, depends on the device in question
    and should be described separately in that device's documentation.

    There are internal pull-up resistors on the I²C lines of the board, but
    with particularly long wires or large number of devices you may need to add
    additional pull-up resistors, to ensure noise-free communication.
    """

    def init(self: "MicroBitI2C", freq: int = 100000,
             sda: int = c18, scl: int = c19) -> None:
        """(Re-)initialize peripheral with the specified clock frequency
        ``freq`` on the specified ``sda`` and ``scl`` pins.

        .. warning::

            Changing the I²C pins from defaults will make the accelerometer and
            compass stop working, as they are connected internally to those
            pins.
        """

    def scan(self: "MicroBitI2C") -> List[int]:
        """
        Scan for available i2c slaves and return a list of addresses.

        For all addresses in the range 0x08 to 0x78 an empty write is
        performed.
        A slave should react with an ACK.
        All addresses, for which a slave reacted this way, are returned.
        """
        return []

    def read(self: "MicroBitI2C", addr: int, n: int,
             repeat: bool = False) -> bytes:
        """Read ``n`` bytes from the device with 7-bit address ``addr``. If
        ``repeat`` is ``True``, no stop bit will be sent.

        May raise an OSError.
        """
        return bytes()

    def write(self: "MicroBitI2C", addr: int,
              buf: Union[bytes, bytearray], repeat=False) -> None:
        """Write bytes from ``buf`` to the device with 7-bit address ``addr``.
        If ``repeat`` is ``True``, no stop bit will be sent.

        May raise an OSError.
        """
