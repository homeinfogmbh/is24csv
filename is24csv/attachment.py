"""Attachments DOM."""

from typing import NamedTuple


__all__ = ['Attachment']


class Attachment(NamedTuple):
    """Represents a real estate attachment."""

    title: str
    filename: str
    suffix: str
    filetype: str
    playtime: int
