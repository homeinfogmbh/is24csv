"""IS24 CSV parser."""

from typing import Union

from is24csv.attachment import Attachment
from is24csv.barrierfree import BarrierFreeRecord
from is24csv.enumerations import Immobilienart
from is24csv.enumerations import Objektkategorie2
from is24csv.enumerations import Wohnraumart
from is24csv.enumerations import Vermarktungsart
from is24csv.enumerations import Objektart
from is24csv.enumerations import Nutzungsart
from is24csv.enumerations import EmpfohleneNutzung
from is24csv.enumerations import BebaubarNach
from is24csv.enumerations import Objektzustand
from is24csv.enumerations import Heizungsart
from is24csv.enumerations import Bodenbelag
from is24csv.enumerations import Haustiere
from is24csv.enumerations import Erschliessung
from is24csv.enumerations import Lageart
from is24csv.enumerations import Zulieferung
from is24csv.enumerations import Geschlecht
from is24csv.enumerations import ParkplatzStellplatz
from is24csv.enumerations import Bauphase
from is24csv.enumerations import Befeuerungsart
from is24csv.enumerations import Energieausweistyp
from is24csv.enumerations import Ausstattungsqualitaet
from is24csv.exceptions import InvalidRecord
from is24csv.file import CSVFile
from is24csv.record import IS24Record


__all__ = [
    "InvalidRecord",
    "CSVFile",
    "IS24Record",
    "BarrierFreeRecord",
    "Record",
    "Attachment",
    "Immobilienart",
    "Objektkategorie2",
    "Wohnraumart",
    "Vermarktungsart",
    "Objektart",
    "Nutzungsart",
    "EmpfohleneNutzung",
    "BebaubarNach",
    "Objektzustand",
    "Heizungsart",
    "Bodenbelag",
    "Haustiere",
    "Erschliessung",
    "Lageart",
    "Zulieferung",
    "Geschlecht",
    "ParkplatzStellplatz",
    "Bauphase",
    "Befeuerungsart",
    "Energieausweistyp",
    "Ausstattungsqualitaet",
]


Record = Union[IS24Record, BarrierFreeRecord]
