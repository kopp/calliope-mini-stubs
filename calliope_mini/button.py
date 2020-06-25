
class MicroBitButton:

    """
    One of the two Buttons A and B.
    Use the instances ``button_a`` or ``button_b``.
    """

    def is_pressed(self) -> bool:
        """
        Returns whether the button is pressed at the time of the method call.

        See also the ``was_pressed`` method.
        """
        return True

    def was_pressed(self) -> bool:
        """
        Returns whether the button was pressed since the device started or
        the last time this method was called.

        Prefer this method over the ``is_pressed` method:
        If you ask for ``is_pressed``, the user has to have the button
        pressed in precisely the moment that you ask.
        If you use ``was_pressed``, it is ok for the user to press/release
        before you ask -- e.g. when Calliope Mini is currently
        computing/displaying something else.
        """
        return True

    def get_presses(self) -> int:
        """
        Returns the running total of button presses, and resets this total
        to zero before returning.
        """
        return 0
