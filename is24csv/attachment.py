"""Attachments DOM."""

from collections import namedtuple


__all__ = ['Attachment']


FIELDS = ('title', 'filename', 'suffix', 'filetype', 'playtime')
Attachment = namedtuple('Attachment', FIELDS)
