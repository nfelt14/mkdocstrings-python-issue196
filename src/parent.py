"""Module with a parent class."""


class Parent:
    """Parent class."""

    def __init__(self, param1: int, param2: str):
        """Create a Parent class instance.

        Args:
            param1: An integer.
            param2: A string.
        """
        print("Parent.__init__")

    def method(self) -> float:
        """Parent method.

        Returns:
            A float.
        """
        print("Parent.method")

        return 1.0


class ChildSameFile(Parent):
    """A child class in the same file as the parent class."""
