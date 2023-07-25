"""IS24 CSV file DOM."""

from __future__ import annotations
from csv import reader
from logging import getLogger
from pathlib import Path
from typing import Iterator

from is24csv.barrierfree import BarrierFreeRecord
from is24csv.record import CSVRecord, IS24Record


__all__ = ["CSVFile"]


LOGGER = getLogger("IS24CSV")
RECORDS = {IS24Record.columns: IS24Record, BarrierFreeRecord.columns: BarrierFreeRecord}


def line_to_record(record: tuple[str]) -> CSVRecord:
    """Converts a CSV file line into a record object."""

    try:
        record_class = RECORDS[len(record)]
    except KeyError:
        raise ValueError(f"Not a valid IS24 CSV record: {record}.") from None

    return record_class(record)


def lines_to_records(records: Iterator[tuple[str]]) -> Iterator[CSVRecord]:
    """Yields records."""

    for record in records:
        try:
            yield line_to_record(record)
        except ValueError as value_error:
            LOGGER.error(value_error)


class CSVFile(tuple):
    """An IS24 CSV file."""

    @classmethod
    def read(
        cls, filename: Path, *, encoding: str = "latin-1", delimiter: str = "|"
    ) -> CSVFile:
        """Reads in a file."""
        with filename.open(mode="r", encoding=encoding, newline="") as file:
            return cls(lines_to_records(reader(file, delimiter=delimiter)))
