"""
This module contains objects and functions to control the and interact with the
hardware of the Calliope Mini.

For example, use the object ``button_a`` to read the state of the button A.
See the documentation of those objects for details.
"""


__all__ = [
    "display",
    "Image",
    "button_a", "button_b",
    "reset", "sleep", "running_time", "panic", "temperature",
    "magnetometer", "gyrometer", "accelerometer", "sensor",
    "led",
    "i2c",
    "spi",
    "pin0", "pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8",
    "pin9", "pin10", "pin11", "pin12", "pin13", "pin14", "pin15", "pin16",
    "pin17", "pin18", "pin19", "pin20", "pin21", "pin22", "pin23", "pin24",
    "pin25", "pin26", "pin27", "pin28", "pin29", "pin30",
    "p0", "p1", "p2", "p3",
    "c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11",
    "c12", "c16", "c17", "c18", "c19", "c21",
]


from .accelerometer import CalliopeAccelerometer
from .button import MicroBitButton
from .display import MicroBitDisplay
from .gyrometer import CalliopeGyrometer
from .i2c import MicroBitI2C
from .image import MicroBitImage
from .led import CalliopeLED
from .magnetometer import CalliopeMagnetometer
from .pin_instances import (  # noqa: I101
    pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8,
    pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16,
    pin17, pin18, pin19, pin20, pin21, pin22, pin23, pin24,
    pin25, pin26, pin27, pin28, pin29, pin30,
    p0, p1, p2, p3,
    c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11,
    c12, c16, c17, c18, c19, c21,
)
from .sensor import CalliopeSensor
from .spi import MicroBitSPI
from .toplevel_functions import panic, reset, running_time, sleep, temperature
from .uart import MicroBitUART


display = MicroBitDisplay()


Image = MicroBitImage
Image.SKULL = MicroBitImage()


button_a = MicroBitButton()
button_b = MicroBitButton()


magnetometer = CalliopeMagnetometer()
gyrometer = CalliopeGyrometer()
accelerometer = CalliopeAccelerometer()
sensor = CalliopeSensor()


led = CalliopeLED()

i2c = MicroBitI2C()

uart = MicroBitUART()

spi = MicroBitSPI()
