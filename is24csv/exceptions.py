"""CSV exceptions."""


__all__ = ['InvalidRecord']


class InvalidRecord(Exception):
    """indicates that the provided lines are not a valid record."""


    def __init__(self, length_is, length_shall):
        """Sets actual and target length."""
        super().__init__()
        self.length_is = length_is
        self.length_shall = length_shall

    def __str__(self):
        """Returns a human readable string."""
        return f'Expected {self.length_shall} columns' \
            f', but got {self.length_is}.'
