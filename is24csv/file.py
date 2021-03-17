"""IS24 CSV file DOM."""

from csv import reader
from logging import getLogger
from pathlib import Path

from is24csv.barrierfree import BarrierFreeRecord
from is24csv.record import IS24Record


__all__ = ['CSVFile']


LOGGER = getLogger('IS24CSV')
RECORDS = {
    IS24Record.columns: IS24Record,
    BarrierFreeRecord.columns: BarrierFreeRecord
}


def line_to_record(record):
    """Converts a CSV file line into a record object."""

    try:
        record_class = RECORDS[len(record)]
    except KeyError:
        raise ValueError(f'Not a valid IS24 CSV record: {record}.')

    return record_class(record)


def lines_to_records(records):
    """Yields records."""

    for record in records:
        try:
            yield line_to_record(record)
        except ValueError as value_error:
            LOGGER.error(value_error)


class CSVFile(tuple):
    """An IS24 CSV file."""

    @classmethod
    def read(cls, filename, encoding='latin-1', delimiter='|'):
        """Reads in a file."""
        path = Path(filename)

        with path.open(mode='r', encoding=encoding, newline='') as csv_file:
            return cls(lines_to_records(reader(csv_file, delimiter=delimiter)))
