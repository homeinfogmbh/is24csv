"""IS24 CSV record DOM."""

from typing import Any

from is24csv.attachment import Attachment
from is24csv.enumerations import Immobilienart
from is24csv.exceptions import InvalidRecord
from is24csv.mappings import ATTRIBUTES
from is24csv.mappings import TYPES
from is24csv.parsers import parse_enum
from is24csv.parsers import parse_int


__all__ = ['CSVRecord', 'IS24Record']


class CSVRecord(tuple):
    """A single line of an IS24 CSV file."""

    def __init__(self, _):
        """Checks the column count."""
        super().__init__()

        if (length := len(self)) != self.columns:
            raise InvalidRecord(length, self.columns)

    def __init_subclass__(cls, *, grpsep: str = ';', columns: int):
        """Sets column count and group separator."""
        cls.grpsep = grpsep
        cls.columns = columns


class IS24Record(CSVRecord, columns=182):   # pylint: disable=R0904
    """A single line of an IS24 CSV file."""

    def __str__(self):
        """Returns the record's ID."""
        return self.anbieter_id

    def __getattr__(self, attribute: str) -> Any:
        """Returns real estate type-dependent data fields."""
        try:
            mapping = ATTRIBUTES[attribute]
        except KeyError:
            raise AttributeError(attribute) from None

        try:
            type_ = TYPES[attribute]
        except KeyError:
            return self.map(mapping)

        return type_(self.map(mapping))

    @property
    def importmodus(self):
        """Import mode."""
        return self[0]

    @property
    def status(self):
        """The object's status."""
        return self[1] != '0'

    @property
    def immobilienart(self):
        """Real estate type."""
        return parse_enum(Immobilienart, self[2], preprocess=parse_int)

    @property
    def scout_objekt_id(self):
        """IS24's object identifier."""
        return self[3]

    @property
    def terms_region(self):
        """TERMS region."""
        return self[4]

    @property
    def terms_stadt(self):
        """TERMS city."""
        return self[5]

    @property
    def terms_stadtteil(self):
        """TERMS quarter."""
        return self[6]

    @property
    def anbieter_id(self):
        """Realtor's identifier for this object."""
        return self[7]

    @property
    def gruppierungs_id(self):
        """Grouping identifier."""
        return parse_int(self[8])

    @property
    def mehrstufige_objektdarstellung(self):
        """Publish channel identifier."""
        return parse_int(self[9])

    @property
    def gruppen_ids(self):
        """Yields group identifiers."""
        for ident in self[10].split(self.grpsep):
            ident = ident.strip()

            if ident:
                yield ident

    @property
    def api_suchfeld_1(self):
        """First API search field."""
        return self[11]

    @property
    def api_suchfeld_2(self):
        """Second API search field."""
        return self[12]

    @property
    def api_suchfeld_3(self):
        """Third API search field."""
        return self[13]

    @property
    def scout_kunden_id(self):
        """IS24 customer ID of the realtor."""
        return self[15]

    # Customer data.
    @property
    def kontaktperson_anrede(self):
        """Salutation of the contact person."""
        return self[16]

    @property
    def kontaktperson_vorname(self):
        """Given name of the contact person."""
        return self[17]

    @property
    def kontaktperson_nachname(self):
        """Surname of the contact person."""
        return self[18]

    @property
    def kontaktperson_strasse(self):
        """Street of the contact person."""
        return self[19]

    @property
    def kontaktperson_hausnummer(self):
        """House number of the contact person."""
        return self[20]

    @property
    def kontaktperson_plz(self):
        """Zip code of the contact person."""
        return self[21]

    @property
    def kontaktperson_ort(self):
        """City of the contact person."""
        return self[22]

    @property
    def kontaktperson_laenderkennzeichen(self):
        """Country code."""
        return self[23] or 'DEU'

    @property
    def telefon(self):
        """Phone number."""
        return self[24]

    @property
    def mobiltelefon(self):
        """Cell phone number."""
        return self[25]

    @property
    def telefax(self):
        """Fax number."""
        return self[26]

    @property
    def email(self):
        """Email address."""
        return self[27]

    @property
    def homepage(self):
        """The realtor's website."""
        return self[28]

    # Marketing data.
    @property
    def adressdruck(self):
        """Show address flag."""
        return self[35] == 'J'

    @property
    def ueberschrift(self):
        """Exposé title."""
        return self[36]

    @property
    def provision(self):
        """Commission."""
        return self[37]

    @property
    def waehrung(self):
        """Currency."""
        return self[38] or 'EUR'

    @property
    def provisionspflichtig(self):
        """Subject to commission flag."""
        return self[39] == 'J'

    @property
    def provisionshinweis(self):
        """Commission hint."""
        return self[40]

    # Object address.
    @property
    def strasse(self):
        """Street of the real estate."""
        return self[50]

    @property
    def hausnummer(self):
        """House number of the real estate."""
        return self[51]

    @property
    def plz(self):
        """Zip code of the real estate."""
        return self[52]

    @property
    def ort(self):
        """City of the real estate."""
        return self[53]

    @property
    def laenderkennzeichen(self):
        """Country code of the real estate."""
        return self[54]

    @property
    def internationale_region(self):
        """International region for real estates outside of Germany."""
        return self[55]

    # Real estate independent text attachments.
    @property
    def lage(self):
        """Location."""
        return self[99] or None

    @property
    def ausstattung(self):
        """Equipment / furniture."""
        return self[100] or None

    @property
    def objektbeschreibung(self):
        """Object description."""
        return self[101] or None

    @property
    def sonstige_angaben(self):
        """Further annotations."""
        return self[102] or None

    @property
    def anhaenge(self):
        """Yields attachments."""
        for index in range(107, 153, 5):
            filename = self[index].strip()

            if not filename:
                continue

            suffix = self[index+1]
            filetype = self[index+2]
            playtime = parse_int(self[index+3])
            title = self[index+4]
            yield Attachment(title, filename, suffix, filetype, playtime)

    def map(self, type_index_map: dict[Immobilienart, int], *,
            default: Any = None) -> Any:
        """Takes a real estate type → index map and returns the
        respective value for the current real estate type.
        """
        try:
            index = type_index_map[self.immobilienart]
        except KeyError:
            return default

        return self[index]
