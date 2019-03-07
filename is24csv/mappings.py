"""Real estate type → field index mappings."""

from functools import partial

from is24csv.enumerations import Objektkategorie2
from is24csv.enumerations import Immobilienart
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
from is24csv.parsers import parse_bool
from is24csv.parsers import parse_date
from is24csv.parsers import parse_enum
from is24csv.parsers import parse_float
from is24csv.parsers import parse_int


__all__ = ['ATTRIBUTES', 'TYPES']


OBJEKTKATEGORIE_2 = {
    Immobilienart.WOHNUNG_MIETE: 60,
    Immobilienart.HAUS_MIETE: 60,
    Immobilienart.WOHNUNG_KAUF: 60,
    Immobilienart.HAUS_KAUF: 60,
    Immobilienart.ANLAGEOBJEKTE: 60,
    Immobilienart.BUERO_PRAXEN: 61,
    Immobilienart.EINZELHANDEL: 61,
    Immobilienart.GASTRONOMIE_HOTELS: 61,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 61,
    Immobilienart.SONSTIGE_OBJEKTE: 61
}
WOHNRAUMART = {Immobilienart.WAZ: 60}
VERMARKTUNGSART = {
    Immobilienart.GRUNDSTUECK: 60,
    Immobilienart.BUERO_PRAXEN: 60,
    Immobilienart.EINZELHANDEL: 60,
    Immobilienart.GASTRONOMIE_HOTELS: 60,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 60,
    Immobilienart.SONSTIGE_OBJEKTE: 60
}
OBJEKTART = {
    Immobilienart.GARAGE_STELLPLATZ_MIETE:60,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 60
}
WOHNFLAECHE = {
    Immobilienart.WOHNUNG_MIETE: 61,
    Immobilienart.HAUS_MIETE: 61,
    Immobilienart.WOHNUNG_KAUF: 61,
    Immobilienart.HAUS_KAUF: 61,
    Immobilienart.WAZ: 61,
    Immobilienart.ANLAGEOBJEKTE: 63
}
NUTZUNGSART = {Immobilienart.GRUNDSTUECK: 61}
LAENGE = {
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 61,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 61
}
NUTZFLAECHE = {
    Immobilienart.WOHNUNG_MIETE: 62,
    Immobilienart.HAUS_MIETE: 62,
    Immobilienart.WOHNUNG_KAUF: 62,
    Immobilienart.HAUS_KAUF: 62,
    Immobilienart.BUERO_PRAXEN: 62
}
VERKAUFSFLAECHE = {Immobilienart.EINZELHANDEL: 62}
GASTRAUMFLAECHE = {Immobilienart.EINZELHANDEL: 62}
LAGERFLAECHE = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 62}
HAUPTFLAECHE = {Immobilienart.SONSTIGE_OBJEKTE: 62}
PRODUKTIONSFLAECHE = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 62}
VERMIETBARE_FLAECHE = {Immobilienart.ANLAGEOBJEKTE: 62}
BREITE = {
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 62,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 62
}
ZIMMER = {
    Immobilienart.WOHNUNG_MIETE: 63,
    Immobilienart.HAUS_MIETE: 63,
    Immobilienart.WOHNUNG_KAUF: 63,
    Immobilienart.HAUS_KAUF: 63,
    Immobilienart.WAZ: 62
}
FREI_BIS = {
    Immobilienart.WAZ: 63,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 66
}
TEILBAR_AB = {
    Immobilienart.GRUNDSTUECK: 63,
    Immobilienart.BUERO_PRAXEN: 65,
    Immobilienart.EINZELHANDEL: 65,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 65,
    Immobilienart.SONSTIGE_OBJEKTE: 65
}
NEBENFLAECHE = {
    Immobilienart.BUERO_PRAXEN: 63,
    Immobilienart.EINZELHANDEL: 63,
    Immobilienart.GASTRONOMIE_HOTELS: 63,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 63,
    Immobilienart.SONSTIGE_OBJEKTE: 63
}
HOEHE = {
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 63,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 63
}
BADEZIMMER = {
    Immobilienart.WOHNUNG_MIETE: 64,
    Immobilienart.HAUS_MIETE: 64,
    Immobilienart.WOHNUNG_KAUF: 64,
    Immobilienart.HAUS_KAUF: 64
}
MINDESTMIETDAUER = {Immobilienart.WAZ: 64}
EMPFOHLENE_NUTZUNG = {Immobilienart.GRUNDSTUECK: 64}
GESAMTFLAECHE = {
    Immobilienart.BUERO_PRAXEN: 64,
    Immobilienart.EINZELHANDEL: 64,
    Immobilienart.GASTRONOMIE_HOTELS: 64,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 64,
    Immobilienart.SONSTIGE_OBJEKTE: 64,
    Immobilienart.ANLAGEOBJEKTE: 61
}
GEWERBEFLAECHEN = {Immobilienart.ANLAGEOBJEKTE: 64}
FLAECHE = {
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 64,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 64
}
ETAGE = {
    Immobilienart.WOHNUNG_MIETE: 65,
    Immobilienart.WOHNUNG_KAUF: 65,
    Immobilienart.WAZ: 66
}
GRUNDSTUECKSFLAECHE = {
    Immobilienart.HAUS_MIETE: 65,
    Immobilienart.HAUS_KAUF: 65,
    Immobilienart.ANLAGEOBJEKTE: 65,
    Immobilienart.GRUNDSTUECK: 62,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 80,
    Immobilienart.SONSTIGE_OBJEKTE: 76
}
MAXIMALMIETDAUER = {Immobilienart.WAZ: 65}
BEBAUBAR_NACH = {Immobilienart.GRUNDSTUECK: 65}
ETAGENZAHL = {
    Immobilienart.WOHNUNG_MIETE: 66,
    Immobilienart.HAUS_MIETE: 66,
    Immobilienart.WOHNUNG_KAUF: 66,
    Immobilienart.HAUS_KAUF: 66,
    Immobilienart.WAZ: 67
}
ERBPACHT_JAHRE = {Immobilienart.GRUNDSTUECK: 66}
PARKFLAECHEN = {
    Immobilienart.BUERO_PRAXEN: 66,
    Immobilienart.EINZELHANDEL: 66,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 66,
    Immobilienart.SONSTIGE_OBJEKTE: 66,
    Immobilienart.GASTRONOMIE_HOTELS: 65,
    Immobilienart.ANLAGEOBJEKTE: 74
}
SONSTIGE_FLAECHEN = {Immobilienart.ANLAGEOBJEKTE: 66}
BAUJAHR = {
    Immobilienart.WOHNUNG_MIETE: 67,
    Immobilienart.HAUS_MIETE: 67,
    Immobilienart.WOHNUNG_KAUF: 67,
    Immobilienart.HAUS_KAUF: 67,
    Immobilienart.GASTRONOMIE_HOTELS: 67,
    Immobilienart.BUERO_PRAXEN: 68,
    Immobilienart.EINZELHANDEL: 68,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 68,
    Immobilienart.SONSTIGE_OBJEKTE: 68,
    Immobilienart.ANLAGEOBJEKTE: 68,
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 68,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 68
}
BAUGENEHMIGUNG_VORHANDEN = {Immobilienart.GRUNDSTUECK: 67}
ETAGEN = {
    Immobilienart.BUERO_PRAXEN: 67,
    Immobilienart.EINZELHANDEL: 67,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 67,
    Immobilienart.SONSTIGE_OBJEKTE: 67,
    Immobilienart.ANLAGEOBJEKTE: 67,
    Immobilienart.GASTRONOMIE_HOTELS: 66
}
OBJEKTZUSTAND = {
    Immobilienart.WOHNUNG_MIETE: 68,
    Immobilienart.HAUS_MIETE: 68,
    Immobilienart.WOHNUNG_KAUF: 68,
    Immobilienart.HAUS_KAUF: 68,
    Immobilienart.WAZ: 68,
    Immobilienart.GASTRONOMIE_HOTELS: 68,
    Immobilienart.BUERO_PRAXEN: 69,
    Immobilienart.EINZELHANDEL: 69,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 69,
    Immobilienart.SONSTIGE_OBJEKTE: 69,
    Immobilienart.ANLAGEOBJEKTE: 69,
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 69,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 69
}
ABRISS_ERFORDERLICH = {Immobilienart.GRUNDSTUECK: 68}
HEIZUNGSART = {
    Immobilienart.WOHNUNG_MIETE: 69,
    Immobilienart.HAUS_MIETE: 69,
    Immobilienart.WOHNUNG_KAUF: 69,
    Immobilienart.HAUS_KAUF: 69,
    Immobilienart.WAZ: 69,
    Immobilienart.BUERO_PRAXEN: 87,
    Immobilienart.EINZELHANDEL: 87,
    Immobilienart.GASTRONOMIE_HOTELS: 87,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 87,
    Immobilienart.SONSTIGE_OBJEKTE: 87,
    Immobilienart.ANLAGEOBJEKTE: 87
}
GRZ = {Immobilienart.GRUNDSTUECK: 69}
AUFZUG = {
    Immobilienart.WOHNUNG_MIETE: 70,
    Immobilienart.WOHNUNG_KAUF: 70,
    Immobilienart.WAZ: 70,
    Immobilienart.SONSTIGE_OBJEKTE: 70,
    Immobilienart.ANLAGEOBJEKTE: 70,
    Immobilienart.BUERO_PRAXEN: 71,
    Immobilienart.EINZELHANDEL: 71,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 71,
    Immobilienart.GASTRONOMIE_HOTELS: 69
}
GFZ = {Immobilienart.GRUNDSTUECK: 70}
BODENBELAG = {
    Immobilienart.BUERO_PRAXEN: 70,
    Immobilienart.EINZELHANDEL: 70,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 70,
    Immobilienart.SONSTIGE_OBJEKTE: 77
}
PLAETZE_GASTRAUM = {Immobilienart.GASTRONOMIE_HOTELS: 70}
HAUSTIERE = {
    Immobilienart.WOHNUNG_MIETE: 71,
    Immobilienart.WAZ: 71,
    Immobilienart.HAUS_MIETE: 70
}
ERSCHLIESSUNG = {Immobilienart.GRUNDSTUECK: 71}
BETTEN = {Immobilienart.GASTRONOMIE_HOTELS: 71}
X_FACHE = {Immobilienart.ANLAGEOBJEKTE: 71}
BALKON_TERRASSE = {
    Immobilienart.WOHNUNG_MIETE: 72,
    Immobilienart.WAZ: 72,
    Immobilienart.WOHNUNG_KAUF: 71
}
KURZFRISTIG_BEBAUBAR = {Immobilienart.GRUNDSTUECK: 72}
CANTINE_CAFETERIA = {Immobilienart.BUERO_PRAXEN: 72}
SCHAUFENSTERFRONT = {Immobilienart.EINZELHANDEL: 72}
GASTTERRASSE = {Immobilienart.GASTRONOMIE_HOTELS: 72}
GARTEN_MITNUTZUNG = {
    Immobilienart.WOHNUNG_MIETE: 73,
    Immobilienart.WAZ: 73,
    Immobilienart.WOHNUNG_KAUF: 72
}
HEBEBUEHNE = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 72}
MIETEINNAHMEN_IST = {Immobilienart.ANLAGEOBJEKTE: 72}
DV_VERKABELUNG = {Immobilienart.BUERO_PRAXEN: 73}
LAGEART = {Immobilienart.EINZELHANDEL: 73}
HALLENHOEHE = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 73}
MIETEINNAHMEN_SOLL = {Immobilienart.ANLAGEOBJEKTE: 73}
EINBAUKUECHE = {
    Immobilienart.WOHNUNG_MIETE: 74,
    Immobilienart.HAUS_MIETE: 71,
    Immobilienart.WOHNUNG_KAUF: 73,
    Immobilienart.BUERO_PRAXEN: 97
}
MOBILIAR = {Immobilienart.WAZ: 74}
FUSSWEG_OEPNV = {
    Immobilienart.BUERO_PRAXEN: 74,
    Immobilienart.EINZELHANDEL: 78,
    Immobilienart.GASTRONOMIE_HOTELS: 73,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 82,
    Immobilienart.SONSTIGE_OBJEKTE: 71,
    Immobilienart.ANLAGEOBJEKTE: 75
}
RAMPE = {
    Immobilienart.EINZELHANDEL: 74,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 74
}
SENIORENGERECHTES_WOHNEN = {
    Immobilienart.WOHNUNG_MIETE: 75,
    Immobilienart.HAUS_MIETE: 72,
    Immobilienart.WOHNUNG_KAUF: 74
}
RAUCHER = {Immobilienart.WAZ: 75}
FAHRZEIT_HBF = {
    Immobilienart.BUERO_PRAXEN: 75,
    Immobilienart.EINZELHANDEL: 79,
    Immobilienart.GASTRONOMIE_HOTELS: 74,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 83,
    Immobilienart.SONSTIGE_OBJEKTE: 72,
    Immobilienart.ANLAGEOBJEKTE: 76
}
ZULIEFERUNG = {Immobilienart.EINZELHANDEL: 75}
BODENBELASTUNG = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 75}
FOERDERUNG = {Immobilienart.WOHNUNG_MIETE: 76}
VERMIETET = {
    Immobilienart.WOHNUNG_KAUF: 76,
    Immobilienart.HAUS_KAUF: 72
}
GESCHLECHT = {Immobilienart.WAZ: 76}
FAHRZEIT_BUS = {
    Immobilienart.BUERO_PRAXEN: 76,
    Immobilienart.EINZELHANDEL: 80,
    Immobilienart.GASTRONOMIE_HOTELS: 75,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 84,
    Immobilienart.SONSTIGE_OBJEKTE: 73,
    Immobilienart.ANLAGEOBJEKTE: 77
}
LASTENAUFZUG = {
    Immobilienart.EINZELHANDEL: 76,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 76
}
GARAGEN_STELLPLAETZE = {
    Immobilienart.WOHNUNG_MIETE: 77,
    Immobilienart.HAUS_MIETE: 73,
    Immobilienart.WOHNUNG_KAUF: 75,
    Immobilienart.HAUS_KAUF: 78,
    Immobilienart.WAZ: 81
}
PERSONENZAHL = {Immobilienart.WAZ: 77}
FAHRZEIT_FLUGHAFEN = {
    Immobilienart.BUERO_PRAXEN: 77,
    Immobilienart.EINZELHANDEL: 81,
    Immobilienart.GASTRONOMIE_HOTELS: 76,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 85,
    Immobilienart.SONSTIGE_OBJEKTE: 74,
    Immobilienart.ANLAGEOBJEKTE: 78
}
LASTENAUFZUG_TRAGKRAFT = {
    Immobilienart.EINZELHANDEL: 77,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 77
}
PARKPLATZ_STELLPLATZ = {
    Immobilienart.WOHNUNG_MIETE: 78,
    Immobilienart.HAUS_MIETE:74,
    Immobilienart.WOHNUNG_KAUF: 77,
    Immobilienart.HAUS_KAUF: 73,
    Immobilienart.WAZ: 79
}
FREI_AB = {
    Immobilienart.WOHNUNG_MIETE: 79,
    Immobilienart.HAUS_MIETE: 75,
    Immobilienart.WOHNUNG_KAUF: 78,
    Immobilienart.HAUS_KAUF: 74,
    Immobilienart.WAZ: 78,
    Immobilienart.GRUNDSTUECK: 73,
    Immobilienart.BUERO_PRAXEN: 78,
    Immobilienart.EINZELHANDEL: 82,
    Immobilienart.GASTRONOMIE_HOTELS: 77,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 86,
    Immobilienart.SONSTIGE_OBJEKTE: 75,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 65
}
KLIMAANLAGE = {Immobilienart.BUERO_PRAXEN: 79}
ROLLSTUHLGERECHT = {
    Immobilienart.WOHNUNG_MIETE: 80,
    Immobilienart.HAUS_MIETE: 76,
    Immobilienart.WOHNUNG_KAUF: 79,
    Immobilienart.HAUS_KAUF: 75,
    Immobilienart.WAZ: 80
}
SCHLAFZIMMER = {
    Immobilienart.WOHNUNG_MIETE: 81,
    Immobilienart.HAUS_MIETE: 77,
    Immobilienart.WOHNUNG_KAUF: 80,
    Immobilienart.HAUS_KAUF: 76
}
EINLIEGERWOHNUNG = {Immobilienart.HAUS_KAUF: 77}
KRANBAHN = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 78}
KRANBAHN_TRAGKRAFT = {Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 79}
FERIENWOHNUNG = {
    Immobilienart.WOHNUNG_KAUF: 81,
    Immobilienart.HAUS_KAUF: 70
}
STARKSTROM = {Immobilienart.BUERO_PRAXEN: 81}
STROMANSCHLUSSWERT = {Immobilienart.BUERO_PRAXEN: 81}
BARRIEREFREI = {
    Immobilienart.WOHNUNG_MIETE: 82,
    Immobilienart.HAUS_MIETE: 86,
    Immobilienart.WOHNUNG_KAUF: 82,
    Immobilienart.HAUS_KAUF: 79,
    Immobilienart.WAZ: 82,
    Immobilienart.BUERO_PRAXEN: 82
}
BAUPHASE = {Immobilienart.HAUS_KAUF: 82}
BEFEUERUNGSART = {
    Immobilienart.WOHNUNG_MIETE: 83,
    Immobilienart.HAUS_MIETE: 78,
    Immobilienart.WOHNUNG_KAUF: 83,
    Immobilienart.HAUS_KAUF: 83,
    Immobilienart.WAZ: 83,
    Immobilienart.BUERO_PRAXEN: 83,
    Immobilienart.EINZELHANDEL: 83,
    Immobilienart.GASTRONOMIE_HOTELS: 83,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 89,
    Immobilienart.SONSTIGE_OBJEKTE: 83,
    Immobilienart.ANLAGEOBJEKTE: 83
}
ENERGIEAUSWEISTYP = {
    Immobilienart.WOHNUNG_MIETE: 84,
    Immobilienart.HAUS_MIETE: 79,
    Immobilienart.WOHNUNG_KAUF: 84,
    Immobilienart.HAUS_KAUF: 84,
    Immobilienart.WAZ: 84,
    Immobilienart.BUERO_PRAXEN: 84,
    Immobilienart.EINZELHANDEL: 84,
    Immobilienart.GASTRONOMIE_HOTELS: 84,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 96,
    Immobilienart.SONSTIGE_OBJEKTE: 84,
    Immobilienart.ANLAGEOBJEKTE: 84
}
KENNWERT = {
    Immobilienart.WOHNUNG_MIETE: 85,
    Immobilienart.HAUS_MIETE: 80,
    Immobilienart.WOHNUNG_KAUF: 85,
    Immobilienart.HAUS_KAUF: 85,
    Immobilienart.WAZ: 85,
    Immobilienart.BUERO_PRAXEN: 85,
    Immobilienart.EINZELHANDEL: 85,
    Immobilienart.GASTRONOMIE_HOTELS: 85,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 97,
    Immobilienart.SONSTIGE_OBJEKTE: 85,
    Immobilienart.ANLAGEOBJEKTE: 85
}
ENERGIEVERBRAUCH_MITWARMWASSER = {
    Immobilienart.WOHNUNG_MIETE: 86,
    Immobilienart.HAUS_MIETE: 81,
    Immobilienart.WOHNUNG_KAUF: 86,
    Immobilienart.HAUS_KAUF: 86,
    Immobilienart.WAZ: 86,
    Immobilienart.BUERO_PRAXEN: 86,
    Immobilienart.EINZELHANDEL: 86,
    Immobilienart.GASTRONOMIE_HOTELS: 86,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 98,
    Immobilienart.SONSTIGE_OBJEKTE: 86,
    Immobilienart.ANLAGEOBJEKTE: 86
}
GAESTE_WC = {
    Immobilienart.WOHNUNG_MIETE: 87,
    Immobilienart.HAUS_MIETE: 82,
    Immobilienart.WOHNUNG_KAUF: 87,
    Immobilienart.HAUS_KAUF: 87,
    Immobilienart.WAZ: 87
}
LETZTE_MODERNISIERUNG = {
    Immobilienart.WOHNUNG_MIETE: 88,
    Immobilienart.HAUS_MIETE: 88,
    Immobilienart.WOHNUNG_KAUF: 97,
    Immobilienart.HAUS_KAUF: 80,
    Immobilienart.BUERO_PRAXEN: 80,
    Immobilienart.EINZELHANDEL: 97,
    Immobilienart.GASTRONOMIE_HOTELS: 80,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 88,
    Immobilienart.SONSTIGE_OBJEKTE: 80,
    Immobilienart.ANLAGEOBJEKTE: 80,
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 67,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 67
}
DENKMALSCHUTZOBJEKT = {
    Immobilienart.WOHNUNG_KAUF: 88,
    Immobilienart.HAUS_KAUF: 88,
    Immobilienart.BUERO_PRAXEN: 88,
    Immobilienart.EINZELHANDEL: 88,
    Immobilienart.GASTRONOMIE_HOTELS: 88,
    Immobilienart.SONSTIGE_OBJEKTE: 88,
    Immobilienart.ANLAGEOBJEKTE: 88
}
KELLER = {
    Immobilienart.WOHNUNG_MIETE: 89,
    Immobilienart.HAUS_MIETE: 85,
    Immobilienart.WOHNUNG_KAUF: 89,
    Immobilienart.HAUS_KAUF: 89,
    Immobilienart.WAZ: 89,
    Immobilienart.BUERO_PRAXEN: 89,
    Immobilienart.EINZELHANDEL: 89,
    Immobilienart.GASTRONOMIE_HOTELS: 89,
    Immobilienart.SONSTIGE_OBJEKTE: 89
}
KALTMIETE = {
    Immobilienart.WOHNUNG_MIETE: 90,
    Immobilienart.HAUS_MIETE: 90,
    Immobilienart.WAZ: 92,
    Immobilienart.BUERO_PRAXEN: 90,
    Immobilienart.EINZELHANDEL: 90,
    Immobilienart.GASTRONOMIE_HOTELS: 90,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 90,
    Immobilienart.SONSTIGE_OBJEKTE: 90,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 90
}
KAUFPREIS = {
    Immobilienart.WOHNUNG_KAUF: 90,
    Immobilienart.HAUS_KAUF: 90,
    Immobilienart.GRUNDSTUECK: 90,
    Immobilienart.BUERO_PRAXEN: 93,
    Immobilienart.EINZELHANDEL: 93,
    Immobilienart.GASTRONOMIE_HOTELS: 90,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 93,
    Immobilienart.SONSTIGE_OBJEKTE: 90,
    Immobilienart.ANLAGEOBJEKTE: 90,
    Immobilienart.GARAGE_STELLPLATZ_MIETE: 90
}
PAUSCHALMIETE = {
    Immobilienart.WAZ: 90,
    Immobilienart.SONSTIGE_OBJEKTE: 90,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 90
}
ERBPACHT = {Immobilienart.GRUNDSTUECK: 90}
PACHT_MIETE = {Immobilienart.GRUNDSTUECK: 90}
NEBENKOSTEN = {
    Immobilienart.WOHNUNG_MIETE: 91,
    Immobilienart.HAUS_MIETE: 91,
    Immobilienart.WAZ: 93,
    Immobilienart.BUERO_PRAXEN: 91,
    Immobilienart.EINZELHANDEL: 91,
    Immobilienart.GASTRONOMIE_HOTELS: 91,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 91,
    Immobilienart.SONSTIGE_OBJEKTE: 91
}
HAUSGELD = {Immobilienart.WOHNUNG_KAUF: 91}
PAUSCHALMIETE_PRO = {Immobilienart.WAZ: 91}
KAUFPREIS_PRO_QM = {Immobilienart.ANLAGEOBJEKTE: 91}
WARMMIETE = {
    Immobilienart.WOHNUNG_MIETE: 92,
    Immobilienart.HAUS_MIETE: 92,
    Immobilienart.GASTRONOMIE_HOTELS: 90,
    Immobilienart.SONSTIGE_OBJEKTE: 90,
    Immobilienart.GARAGE_STELLPLATZ_KAUF: 90
}
KALTMIETE_PRO_EINHEIT = {
    Immobilienart.BUERO_PRAXEN: 92,
    Immobilienart.EINZELHANDEL: 92,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 92
}
BETRIEBSKOSTEN_UMGELEGT = {Immobilienart.ANLAGEOBJEKTE: 92}
PARKPLATZMIETE = {
    Immobilienart.WOHNUNG_MIETE: 93,
    Immobilienart.HAUS_MIETE: 93,
    Immobilienart.WAZ: 95
}
PARKPLATZKAUFPREIS = {
    Immobilienart.WOHNUNG_KAUF: 93,
    Immobilienart.HAUS_KAUF: 92
}
NICHT_UMLEGBARE_KOSTEN = {Immobilienart.ANLAGEOBJEKTE: 93}
KAUTION = {
    Immobilienart.WOHNUNG_MIETE: 94,
    Immobilienart.HAUS_MIETE: 94,
    Immobilienart.WAZ: 94,
    Immobilienart.BUERO_PRAXEN: 95,
    Immobilienart.EINZELHANDEL: 95,
    Immobilienart.GASTRONOMIE_HOTELS: 93,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 95,
    Immobilienart.SONSTIGE_OBJEKTE: 93
}
MIETEINNAHMEN = {
    Immobilienart.WOHNUNG_KAUF: 94,
    Immobilienart.HAUS_KAUF: 93
}
PREIS_PRO_PARKFLAECHE = {
    Immobilienart.BUERO_PRAXEN: 94,
    Immobilienart.EINZELHANDEL: 94,
    Immobilienart.GASTRONOMIE_HOTELS: 92,
    Immobilienart.HALLEN_UND_PRODUKTIONSFLAECHEN: 94,
    Immobilienart.SONSTIGE_OBJEKTE: 92,
    Immobilienart.ANLAGEOBJEKTE: 94
}
HEIZKOSTEN = {
    Immobilienart.WOHNUNG_MIETE: 96,
    Immobilienart.HAUS_MIETE: 96
}
HEIZKOSTEN_IN_NEBENKOSTEN = {
    Immobilienart.WOHNUNG_MIETE: 97,
    Immobilienart.HAUS_MIETE: 97
}
AUSSTATTUNGSQUALITAET = {
    Immobilienart.WOHNUNG_MIETE: 98,
    Immobilienart.HAUS_MIETE: 83,
    Immobilienart.WOHNUNG_KAUF: 96,
    Immobilienart.HAUS_KAUF: 81,
    Immobilienart.BUERO_PRAXEN: 96,
    Immobilienart.EINZELHANDEL: 96,
    Immobilienart.GASTRONOMIE_HOTELS: 81,
    Immobilienart.SONSTIGE_OBJEKTE: 81,
    Immobilienart.ANLAGEOBJEKTE: 81
}
DECKENLAST = {Immobilienart.EINZELHANDEL: 98}

ATTRIBUTES = {
    'objektkategorie_2': OBJEKTKATEGORIE_2,
    'wohnraumart': WOHNRAUMART,
    'vermarktungsart': VERMARKTUNGSART,
    'objektart': OBJEKTART,
    'wohnflaeche': WOHNFLAECHE,
    'nutzungsart': NUTZUNGSART,
    'laenge': LAENGE,
    'nutzflaeche': NUTZFLAECHE,
    'verkaufsflaeche': VERKAUFSFLAECHE,
    'gastraumflaeche': GASTRAUMFLAECHE,
    'lagerflaeche': LAGERFLAECHE,
    'hauptflaeche': HAUPTFLAECHE,
    'produktionsflaeche': PRODUKTIONSFLAECHE,
    'vermietbare_flaeche': VERMIETBARE_FLAECHE,
    'breite': BREITE,
    'zimmer': ZIMMER,
    'frei_bis': FREI_BIS,
    'teilbar_ab': TEILBAR_AB,
    'nebenflaeche': NEBENFLAECHE,
    'hoehe': HOEHE,
    'badezimmer': BADEZIMMER,
    'mindestmietdauer': MINDESTMIETDAUER,
    'empfohlene_nutzung': EMPFOHLENE_NUTZUNG,
    'gesamtflaeche': GESAMTFLAECHE,
    'gewerbeflaechen': GEWERBEFLAECHEN,
    'flaeche': FLAECHE,
    'etage': ETAGE,
    'grundstuecksflaeche': GRUNDSTUECKSFLAECHE,
    'maximalmietdauer': MAXIMALMIETDAUER,
    'bebaubar_nach': BEBAUBAR_NACH,
    'etagenzahl': ETAGENZAHL,
    'erbpacht_jahre': ERBPACHT_JAHRE,
    'parkflaechen': PARKFLAECHEN,
    'sonstige_flaechen': SONSTIGE_FLAECHEN,
    'baujahr': BAUJAHR,
    'baugenehmigung_vorhanden': BAUGENEHMIGUNG_VORHANDEN,
    'etagen': ETAGEN,
    'objektzustand': OBJEKTZUSTAND,
    'abriss_erforderlich': ABRISS_ERFORDERLICH,
    'heizungsart': HEIZUNGSART,
    'grz': GRZ,
    'aufzug': AUFZUG,
    'gfz': GFZ,
    'bodenbelag': BODENBELAG,
    'plaetze_gastraum': PLAETZE_GASTRAUM,
    'haustiere': HAUSTIERE,
    'erschliessung': ERSCHLIESSUNG,
    'betten': BETTEN,
    'x_fache': X_FACHE,
    'balkon_terrasse': BALKON_TERRASSE,
    'kurzfristig_bebaubar': KURZFRISTIG_BEBAUBAR,
    'cantine_cafeteria': CANTINE_CAFETERIA,
    'schaufensterfront': SCHAUFENSTERFRONT,
    'gastterrasse': GASTTERRASSE,
    'garten_mitbenutzung': GARTEN_MITNUTZUNG,
    'hebebuehne': HEBEBUEHNE,
    'mieteinnahmen_ist': MIETEINNAHMEN_IST,
    'dv_verkabelung': DV_VERKABELUNG,
    'lageart': LAGEART,
    'hallenhoehe': HALLENHOEHE,
    'mieteinnahmen_soll': MIETEINNAHMEN_SOLL,
    'einbaukueche': EINBAUKUECHE,
    'mobiliar': MOBILIAR,
    'fussweg_oepnv': FUSSWEG_OEPNV,
    'rampe': RAMPE,
    'senioregerechtes_wohnen': SENIORENGERECHTES_WOHNEN,
    'raucher': RAUCHER,
    'fahrzeit_hbf': FAHRZEIT_HBF,
    'zulieferung': ZULIEFERUNG,
    'bodenbelastung': BODENBELASTUNG,
    'foerderung': FOERDERUNG,
    'vermietet': VERMIETET,
    'geschlecht': GESCHLECHT,
    'fahrzeit_bus': FAHRZEIT_BUS,
    'lastenaufzug': LASTENAUFZUG,
    'garagen_stellplaetze': GARAGEN_STELLPLAETZE,
    'personenzahl': PERSONENZAHL,
    'fahrzeit_flughafen': FAHRZEIT_FLUGHAFEN,
    'lastenaufzug_tragkraft': LASTENAUFZUG_TRAGKRAFT,
    'parkplatz_stellplatz': PARKPLATZ_STELLPLATZ,
    'frei_ab': FREI_AB,
    'klimaanlage': KLIMAANLAGE,
    'rollstuhlgerecht': ROLLSTUHLGERECHT,
    'schlafzimmer': SCHLAFZIMMER,
    'einliegerwohnung': EINLIEGERWOHNUNG,
    'kranbahn': KRANBAHN,
    'kranbahn_tragkraft': KRANBAHN_TRAGKRAFT,
    'ferienwohnung': FERIENWOHNUNG,
    'starkstrom': STARKSTROM,
    'stromanschlusswert': STROMANSCHLUSSWERT,
    'barrierefrei': BARRIEREFREI,
    'bauphase': BAUPHASE,
    'befeuerungsart': BEFEUERUNGSART,
    'energieausweistyp': ENERGIEAUSWEISTYP,
    'kennwert': KENNWERT,
    'energieverbrauch_mitwarmwasser': ENERGIEVERBRAUCH_MITWARMWASSER,
    'gaeste_wc': GAESTE_WC,
    'letzte_modernisierung': LETZTE_MODERNISIERUNG,
    'denkmalschutzobjekt': DENKMALSCHUTZOBJEKT,
    'keller': KELLER,
    'kaltmiete': KALTMIETE,
    'kaufpreis': KAUFPREIS,
    'pauschalmiete': PAUSCHALMIETE,
    'erbpacht': ERBPACHT,
    'pacht_miete': PACHT_MIETE,
    'nebenkosten': NEBENKOSTEN,
    'hausgeld': HAUSGELD,
    'pauschalmiete_pro': PAUSCHALMIETE_PRO,
    'kaufpreis_pro_qm': KAUFPREIS_PRO_QM,
    'warmmiete': WARMMIETE,
    'kaltmiete_pro_einheit': KALTMIETE_PRO_EINHEIT,
    'betriebskosten_umgelegt': BETRIEBSKOSTEN_UMGELEGT,
    'parkplatzmiete': PARKPLATZMIETE,
    'parkplatzkaufpreis': PARKPLATZKAUFPREIS,
    'nicht_umlegbare_kosten': NICHT_UMLEGBARE_KOSTEN,
    'kaution': KAUTION,
    'mieteinnahmen': MIETEINNAHMEN,
    'preis_pro_parkflaeche': PREIS_PRO_PARKFLAECHE,
    'heizkosten': HEIZKOSTEN,
    'heizkosten_in_nebenkosten': HEIZKOSTEN_IN_NEBENKOSTEN,
    'ausstattungsqualitaet': AUSSTATTUNGSQUALITAET,
    'deckenlast': DECKENLAST
}
TYPES = {
    'objektkategorie_2': partial(
        parse_enum, Objektkategorie2, preprocess=parse_int),
    'wohnraumart': partial(parse_enum, Wohnraumart, preprocess=parse_int),
    'vermarktungsart': partial(parse_enum, Vermarktungsart),
    'objektart': partial(parse_enum, Objektart, preprocess=parse_int),
    'wohnflaeche': parse_float,
    'nutzungsart': partial(
        parse_enum, Nutzungsart, preprocess=parse_int,
        default=Nutzungsart.WOHNEN),
    'laenge': parse_float,
    'nutzflaeche': parse_float,
    'verkaufsflaeche': parse_float,
    'gastraumflaeche': parse_float,
    'lagerflaeche': parse_float,
    'hauptflaeche': parse_float,
    'produktionsflaeche': parse_float,
    'vermietbare_flaeche': parse_float,
    'breite': parse_float,
    'zimmer': parse_float,
    'frei_bis': parse_date,
    'teilbar_ab': parse_float,
    'nebenflaeche': parse_float,
    'hoehe': parse_float,
    'badezimmer': parse_int,
    'mindestmietdauer': parse_float,
    'empfohlene_nutzung': partial(
        parse_enum, EmpfohleneNutzung, preprocess=parse_int),
    'gesamtflaeche': parse_float,
    'gewerbeflaechen': parse_float,
    'flaeche': parse_float,
    'etage': parse_int,
    'grundstuecksflaeche': parse_float,
    'bebaubar_nach': partial(
        parse_enum, BebaubarNach, default=BebaubarNach.UNBEKANNT)
    'etagenzahl': parse_int,
    'erbpacht_jahre': parse_int,
    'parkflaechen': parse_int,
    'sonstige_flaechen': parse_float,
    'baujahr': parse_int,
    'baugenehmigung_vorhanden': parse_bool,
    'objektzustand': partial(
        parse_enum, Objektzustand, preprocess=parse_int,
        default=Objektzustand.KEINE_ANGABE),
    'abriss_erforderlich': parse_bool,
    'heizungsart': partial(
        parse_enum, Heizungsart, preprocess=parse_int,
        default=Heizungsart.KEINE_ANGABE),
    'grz': parse_float,
    'aufzug': parse_bool,
    'gfz': parse_float,
    'bodenbelag': partial(
        parse_enum, Bodenbelag, preprocess=parse_int,
        default=Bodenbelag.KEINE_ANGABE),
    'plaetze_gastraum': parse_int,
    'haustiere': partial(parse_enum, Haustiere),
    'erschliessung': partial(parse_enum, Erschliessung),
    'betten': parse_int,
    'x_fache': parse_float,
    'balkon_terrasse': parse_bool,
    'kurzfristig_bebaubar': parse_bool,
    'cantine_cafeteria': parse_bool,
    'schaufensterfront': parse_float,
    'gastterrasse': parse_bool,
    'garten_mitbenutzung': parse_bool,
    'hebebuehne': parse_bool,
    'mieteinnahmen_ist': parse_float,
    'dv_verkabelung': parse_bool,
    'lageart': partial(
        parse_enum, Lageart, preprocess=parse_int,
        default=Lageart.KEINE_ANGABE),
    'hallenhoehe': parse_float,
    'mieteinnahmen_soll': parse_float,
    'einbaukueche': parse_bool,
    'mobiliar': parse_bool,
    'fussweg_oepnv': parse_int,
    'rampe': parse_bool,
    'senioregerechtes_wohnen': parse_bool,
    'raucher': partial(parse_bool, true='1', false='0'),
    'fahrzeit_hbf': parse_int,
    'zulieferung': partial(
        parse_enum, Zulieferung, preprocess=parse_int,
        default=Zulieferung.KEINE_ANGABE),
    'bodenbelastung': parse_float,
    'foerderung': parse_bool,
    'vermietet': parse_bool,
    'geschlecht': partial(parse_enum, Geschlecht, preprocess=parse_int),
    'fahrzeit_bus':  parse_int,
    'lastenaufzug': parse_bool,
    'garagen_stellplaetze': parse_int,
    'personenzahl': parse_int,
    'fahrzeit_flughafen': parse_int,
    'lastenaufzug_tragkraft': parse_float,
    'parkplatz_stellplatz': partial(
        parse_enum, ParkplatzStellplatz, preprocess=parse_int,
        default=ParkplatzStellplatz.KEINE_ANGABE),
    'frei_ab': lambda string: parse_date(string, default=string),
    'klimaanlage': parse_bool,
    'rollstuhlgerecht': parse_bool,
    'schlafzimmer': parse_int,
    'einliegerwohnung': parse_bool,
    'kranbahn': parse_bool,
    'kranbahn_tragkraft': parse_float,
    'ferienwohnung': parse_bool,
    'starkstrom': parse_bool,
    'stromanschlusswert': parse_int,
    'barrierefrei': parse_bool,
    'bauphase': partial(
        parse_enum, Bauphase, preprocess=parse_int,
        default=Bauphase.KEINE_ANGABE),
    'befeuerungsart': partial(
        parse_enum, Befeuerungsart, preprocess=parse_int,
        default=Befeuerungsart.KEINE_ANGABE),
    'energieausweistyp': partial(
        parse_enum, Energieausweistyp, preprocess=parse_int,
        default=Energieausweistyp.KEINE_ANGABE),
    'kennwert': parse_float,
    'energieverbrauch_mitwarmwasser': parse_bool,
    'gaeste_wc': parse_bool,
    'letzte_modernisierung': parse_int,
    'denkmalschutzobjekt': parse_bool,
    'keller': parse_bool,
    'kaltmiete': parse_float,
    'kaufpreis': parse_float,
    'pauschalmiete': parse_float,
    'erbpacht': parse_float,
    'pacht_miete': parse_float,
    'nebenkosten': parse_float,
    'hausgeld': parse_float,
    'kaufpreis_pro_qm': parse_float,
    'warmmiete': parse_float,
    'kaltmiete_pro_einheit': parse_float,
    'betriebskosten_umgelegt': parse_float,
    'parkplatzmiete': parse_float,
    'parkplatzkaufpreis': parse_float,
    'nicht_umlegbare_kosten': parse_float,
    'kaution': parse_float,
    'mieteinnahmen': parse_float,
    'preis_pro_parkflaeche': parse_float,
    'heizkosten': parse_float,
    'heizkosten_in_nebenkosten': parse_bool,
    'ausstattungsqualitaet': partial(
        parse_enum, Ausstattungsqualitaet, preprocess=parse_int,
        default=Ausstattungsqualitaet.KEINE_ANGABE),
    'deckenlast': parse_float
}
