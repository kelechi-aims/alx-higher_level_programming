#!/usr/bin/python3
"""Has a class MyInt that inherits from int"""


class MyInt(int):
    """
    MyInt class that inherits from int.

    MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Override the equality operator (==) to be inverted.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the equality operator (!=) to be inverted.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__eq__(other)
