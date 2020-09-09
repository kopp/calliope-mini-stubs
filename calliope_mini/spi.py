# source/microbit/microbitspi.cpp


from typing import Union

from . import MicroBitDigitalPin, pin13, pin14, pin15


class MicroBitSPI:
    """The ``spi`` module lets you talk to a device connected to your board
    using a serial peripheral interface (SPI) bus. SPI uses a so-called
    master-slave architecture with a single master. You will need to specify
    the connections for three signals:

    * SCLK : Serial Clock (output from master).
    * MOSI : Master Output, Slave Input (output from master).
    * MISO : Master Input, Slave Output (output from slave).
    """

    def init(self: "MicroBitSPI",
             baudrate: int = 1000000, bits: int = 8, mode: int = 0,
             sclk: MicroBitDigitalPin = pin13,
             mosi: MicroBitDigitalPin = pin15,
             miso: MicroBitDigitalPin = pin14) -> None:
        """Initialize SPI communication with the specified parameters on the
        specified pins (``sclk``, ``mosi`` and ``miso``).
        Note that for correct communication, the parameters have to be the same
        on both communicating devices.

        The ``baudrate`` defines the speed of communication.

        The ``bits`` defines the size of bytes being transmitted. Currently
        only ``bits=8`` is supported. However, this may change in the future.

        The ``mode`` determines the combination of clock polarity and phase
        according to the following convention, with polarity as the high order
        bit and phase as the low order bit:

        +----------+-----------------+--------------+
        | SPI Mode | Polarity (CPOL) | Phase (CPHA) |
        +==========+=================+==============+
        | 0        | 0               | 0            |
        +----------+-----------------+--------------+
        | 1        | 0               | 1            |
        +----------+-----------------+--------------+
        | 2        | 1               | 0            |
        +----------+-----------------+--------------+
        | 3        | 1               | 1            |
        +----------+-----------------+--------------+

        Polarity (aka CPOL) 0 means that the clock is at logic value 0 when
        idle and goes high (logic value 1) when active; polarity 1 means the
        clock is at logic value 1 when idle and goes low (logic value 0) when
        active. Phase (aka CPHA) 0 means that data is sampled on the leading
        edge of the clock, and 1 means on the trailing edge (viz.
        https://en.wikipedia.org/wiki/Signal_edge).

        """

    def read(self: "MicroBitSPI", nbytes: int, byte_to_send: int = 0) -> str:
        """Try to read ``nbytes`` bytes. Returns what was read.
        If ``byte_to_send`` is given, that value is written to the SPI while
        reading (again for each byte read). By default, a 0 is written all
        the time.

        Call ``init()`` before using the SPI.
        """
        return str()

    def write(self: "MicroBitSPI",
              buffer: Union[str, bytes, bytearray]) -> None:
        """Write the ``buffer`` of bytes to the bus.
        Ignore received data on the bus.

        Call ``init()`` before using the SPI.
        """

    def write_readinto(self: "MicroBitSPI",
                       write_buffer: Union[str, bytes, bytearray],
                       read_buffer: Union[str, bytes, bytearray],
                       ) -> None:
        """
        Write the content of ``write_buffer`` to the bus and read any
        response into the ``read_buffer``.
        For each byte written, one byte is also read.
        Thus, the ``read_buffer`` should be at least as big as the
        ``write_buffer``.
        The buffers can be the same object.

        Call ``init()`` before using the SPI.
        """
