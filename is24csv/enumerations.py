"""Enumerations."""

from enum import Enum


__all__ = [
    'Immobilienart',
    'Objektkategorie2',
    'Wohnraumart',
    'Vermarktungsart',
    'Objektart',
    'Nutzungsart',
    'EmpfohleneNutzung',
    'Heizungsart',
    'Bodenbelag',
    'Haustiere',
    'Erschliessung',
    'Lageart',
    'Zulieferung',
    'Geschlecht',
    'ParkplatzStellplatz',
    'Bauphase',
    'Energieausweistyp',
    'Ausstattungsqualitaet']


class Immobilienart(Enum):
    """Real estate type."""

    WOHNUNG_MIETE = 0
    HAUS_MIETE = 1
    WOHNUNG_KAUF = 2
    HAUS_KAUF = 3
    WAZ = 4
    GRUNDSTUECK = 5
    BUERO_PRAXEN = 7
    EINZELHANDEL = 8
    GASTRONOMIE_HOTELS = 9
    HALLEN_UND_PRODUKTIONSFLAECHEN = 10
    SONSTIGE_OBJEKTE = 11
    ANLAGEOBJEKTE = 12
    GARAGE_STELLPLATZ_MIETE = 17
    GARAGE_STELLPLATZ_KAUF = 18


class Objektkategorie2(Enum):
    """Object category."""

    KEINE_ANGABE = 0
    DACHGESCHOSS = 3
    LOFT = 6
    MAISONNETTE = 7
    PENTHOUSE = 8
    BAUERNHAUS = 14
    BUNGALOW = 15
    DOPPELHAUSHAELFTE = 17
    EINFAMILIENHAUS = 18
    MEHRFAMILIENHAUS = 21
    VILLA = 24
    REIHENHAUS = 25
    ATELIER = 37
    EIGENTUMSWOHNUNG = 38
    TERRASSENWOHNUNG = 40
    ZWEIFAMILIENHAUS = 43
    ANWESEN = 44
    BAUERNHOF = 54
    REITERHOF = 49
    WEINGUT = 52
    BUERO = 60
    BUEROETAGE = 61
    BUEROHAUS = 62
    BUEROZENTRUM = 63
    BUERO_UND_LAGERGEBAEUDE = 64
    PRAXIS = 65
    PRAXISETAGE = 66
    PRAXISHAUS = 67
    GEWERBEZENTRUM = 68
    AUSSTELLUNGSFLAECHE = 69
    EINKAUFSZENTRUM = 70
    FACTORY_OUTLET = 71
    KAUFHAUS = 72
    KIOSK = 73
    LADEN = 74
    SB_MARKT = 75
    VERKAUFSFLAECHE = 76
    VERKAUFSHALLE = 77
    BARBETRIEB_LOUNGE = 78
    CAFE = 79
    CLUB_DISCOTHEK = 80
    GAESTEHAUS = 81
    GASTSTAETTE = 82
    HOTEL = 83
    HOTELANWESEN = 84
    HOTEL_GARNI = 85
    PENSION = 86
    RESTAURANT = 87
    HALLE = 88
    HOCHREGALLAGER = 89
    INDUSTRIEHALLE = 90
    INDUSTRIEHALLE_MIT_FREIFLAECHE = 91
    KUEHLHAUS = 92
    KUEHLREGALLAGER = 93
    LAGER_MIT_FREIFLAECHE = 94
    LAGERFLAECHE = 95
    LAGERHALLE = 96
    SERVICEFLAECHE = 97
    SPEDITIONSLAGER = 98
    WERKSTATT = 99
    FREIZEITANLAGE = 100
    GEWERBEEINHEIT = 101
    GEWERBEFLAECHE = 102
    SPEZIALOBJEKT = 103
    FERIENBUNGALOW = 104
    GEWERBEPARK = 105
    BUEROGEBAEUDE = 106
    GESCHAEFTSHAUS = 107
    GEWERBEANWESEN = 108
    HALLE_LAGER = 109
    INDUSTRIEANWESEN = 110
    LADEN_VERKAUFSFLAECHE = 111
    SERVICECENTER = 112
    SONSTIGE = 113
    SUPERMARKT = 114
    WOHN_UND_GESCHAEFTSHAUS = 115
    WOHNANLAGE = 116
    ERDGESCHOSSWOHNUNG = 117
    ETAGENWOHNUNG = 118
    BESONDERE_IMMOBILIE = 119
    REIHENMITTELHAUS = 123
    REIHENECKHAUS = 124
    BURG_SCHLOSS = 125
    WOHNIMMOBILIE = 126
    HOCHPARTERRE = 127
    SOUTERRAIN = 128
    WOHN_UND_GESCHAEFTSGEBAEUDE = 138
    BUERO_UND_GESCHAEFTSGEBAEUDE = 139


class Wohnraumart(Enum):
    """Living space type."""

    ZIMMER = 0
    APPARTMENT = 1
    WOHNUNG = 2
    HAUS = 3


class Vermarktungsart(Enum):
    """Marketing types."""

    KAUF = 'K'
    ERBPACHT = 'E'
    MIETE = 'M'
    PACHT = 'P'


class Objektart(Enum):
    """Object type."""

    KEINE_ANGABE = 0
    GARAGE = 129
    TIEFGARAGE = 130
    PARKHAUS = 131
    CARPORT = 132
    AUSSENSTELLPLATZ = 133
    DUPLEX = 134


class Nutzungsart(Enum):
    """Usage type."""

    WOHNEN = 56
    GEWERBE = 57
    LAND_UND_FORSTWIRTSCHAFT = 58
    FREIZEIT = 59


class EmpfohleneNutzung(Enum):
    """Recommended usage."""

    ACKERLAND = 1
    BAUERWARTUNGSLAND = 2
    BOOTSSTAENDE = 3
    BUERO = 4
    CAMPING = 5
    DOPPELHAUSHAELFTE = 6
    EINFAMILIENHAUS = 7
    EINZELHANDEL_GROSS = 8
    EINZELHANDEL_KLEIN = 9
    GARAGEN = 10
    GARTEN = 11
    GASTRONOMIE = 12
    GEWERBE = 13
    HOTEL = 14
    INDUSTRIE = 15
    KEINE_BEBAUUNG = 16
    KLEINGEWERBE = 17
    LAGER = 18
    MEHRFAMILIENHAUS = 19
    OBSTPFLANZUNG = 20
    PARKHAUS = 21
    PRODUKTION = 22
    REIHENHAUS = 23
    STELLPLAETZE = 24
    VILLA = 25
    WALD = 26


class Heizungsart(Enum):
    """Heating type.

    Does not apply to WAZ.
    """

    KEINE_ANGABE = 0
    ETAGENHEIZUNG = 1
    OFENHEIZUNG = 4
    ZENTRALHEIZUNG = 5


class Bodenbelag(Enum):
    """Flooring material."""

    KEINE_ANGABE = 0
    BETON = 1
    EPOXIDHARZBODEN = 2
    FLIESEN = 3
    LAMINAT = 4
    PARKETT = 5
    PVC = 6
    TEPPICHBODEN = 7
    ANTISTATISCHER_TEPPICHBODEN = 8
    STUHLROLLENFESTE_TEPPICHFLIESEN = 9
    STEIN = 10
    NACH_MIETERWUNSCH = 11
    OHNE_BODENBELAG = 12


class Haustiere(Enum):
    """Pets allowed type."""

    JA = 'J'
    NEIN = 'N'
    NACH_VEREINBARUNG = 'V'


class Erschliessung(Enum):
    """Development."""

    ERSCHLOSSEN = 'E'
    TEILERSCHLOSSEN = 'T'
    UNERSCHLOSSEN = 'E'


class Lageart(Enum):
    """Location type."""

    KEINE_ANGABE = 0
    A_LAGE = 1
    B_LAGE = 2
    EINKAUFSZENTRUM = 3


class Zulieferung(Enum):
    """Delivery type."""

    KEINE_ANGABE = 0
    DIREKTER_ZUGANG = 1
    KEINE_DIREKTE_ANFAHRT = 2
    PKW_ZUFAHRT = 3
    VON_VORN = 4
    VON_HINTEN = 5
    GANZTAEGIG = 6
    VORMITTAGS = 7


class Geschlecht(Enum):
    """Gender."""

    NUR_MAENNER = 0
    NUR_FRAUEN = 1


class ParkplatzStellplatz(Enum):
    """Parking."""

    KEINE_ANGABE = 1
    GARAGE = 2
    AUSSEN_STELLPLATZ = 3
    CARPORT = 4
    DUPLEX = 5
    PARKHAUS = 6
    TIEFGARAGE = 7


class Bauphase(Enum):
    """Construction stage."""

    KEINE_ANGABE = 1
    HAUS_IN_PLANUNG = 2
    HAUS_IM_BAU = 3
    HAUS_FERTIG_GESTELLT = 4


class Energieausweistyp(Enum):
    """Energy certificate type."""

    KEINE_ANGABE = 1
    ENDENERGIEBEDARF = 2
    ENERGIEVERBRAUCHSKENNWERT = 3


class Ausstattungsqualitaet(Enum):
    """Quality of amenities."""

    KEINE_ANGABE = 1
    LUXUS = 2
    GEHOBEN = 3
    NORMAL = 4
    EINFACH = 5
