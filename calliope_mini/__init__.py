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
    "pin0", "pin1", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8",
    "pin9", "pin10", "pin11", "pin12", "pin13", "pin14", "pin15", "pin16",
    "pin17", "pin18", "pin19", "pin20", "pin21", "pin22", "pin23", "pin24",
    "pin25", "pin26", "pin27", "pin28", "pin29", "pin30",
    "p0", "p1", "p2", "p3",
    "c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11",
    "c12", "c16", "c17", "c18", "c19", "c21",
]


from .display import MicroBitDisplay
from .image import MicroBitImage
from .button import MicroBitButton
from .toplevel_functions import reset, sleep, running_time, panic, temperature
from .magnetometer import CalliopeMagnetometer
from .gyrometer import CalliopeGyrometer
from .accelerometer import CalliopeAccelerometer
from .sensor import CalliopeSensor
from .led import CalliopeLED
from .pin import MicroBitAnalogDigitalPin, MicroBitDigitalPin, MicroBitTouchPin


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


# types in source/microbit/microbitpin.cpp
pin0 = MicroBitTouchPin()
pin1 = MicroBitTouchPin()
pin2 = MicroBitTouchPin()
pin3 = MicroBitAnalogDigitalPin()
pin4 = MicroBitAnalogDigitalPin()
pin5 = MicroBitDigitalPin()
pin6 = MicroBitDigitalPin()
pin7 = MicroBitDigitalPin()
pin8 = MicroBitDigitalPin()
pin9 = MicroBitDigitalPin()
pin10 = MicroBitDigitalPin()
pin11 = MicroBitDigitalPin()
pin12 = MicroBitDigitalPin()
pin13 = MicroBitDigitalPin()
pin14 = MicroBitDigitalPin()
pin15 = MicroBitDigitalPin()
pin16 = MicroBitDigitalPin()
pin17 = MicroBitDigitalPin()
pin18 = MicroBitDigitalPin()
pin19 = MicroBitDigitalPin()
pin20 = MicroBitDigitalPin()
pin21 = MicroBitDigitalPin()
pin22 = MicroBitTouchPin()
pin23 = MicroBitDigitalPin()
pin24 = MicroBitDigitalPin()
pin25 = MicroBitDigitalPin()
pin26 = MicroBitDigitalPin()
pin27 = MicroBitDigitalPin()
pin28 = MicroBitDigitalPin()
pin29 = MicroBitDigitalPin()
pin30 = MicroBitDigitalPin()

# aliases in source/microbit/modmicrobit.cpp
p0 = pin0
p1 = pin1
p2 = pin2
p3 = pin22

c0 = pin0
c1 = pin1
c2 = pin2
c3 = pin22
c4 = pin4
c5 = pin5
c6 = pin6
c7 = pin7
c8 = pin8
c9 = pin9
c10 = pin10
c11 = pin11
c12 = pin12
c16 = pin26
c17 = pin27
c18 = pin20
c19 = pin19
c21 = pin3
