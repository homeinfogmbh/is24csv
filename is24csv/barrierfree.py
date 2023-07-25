"""Barrier free extension."""

from typing import Iterator, Optional

from is24csv.record import IS24Record


__all__ = ["BarrierFreeRecord"]


class BarrierFreeRecord(IS24Record, columns=210):
    """Extended record with barrier freeness details.
    Properties are partially documented in German.
    """

    @property
    def keine_stufen_wohnung(self) -> bool:
        """keine Treppenstufen bis zum Wohnungseingang."""
        return self[184] == "45A"

    @property
    def eine_stufe_wohnung(self) -> bool:
        """Maximal 1 Treppe bis zum Wohnungseingang (inkl. Podest)"""
        return self[184] == "45B"

    @property
    def max_8_stufen_wohnung(self) -> bool:
        """2 bis 8 (inkl. Podest) Treppe bis
        zum Wohnungseingang (inkl. Podest).
        """
        return self[184] == "45C"

    @property
    def rampe_barrierefrei(self) -> Optional[bool]:
        """Determines whether the ramp is barrier free."""
        # Rampe mit bis zu 6 % Gefälle (nach DIN-Norm)
        if self[185] == "45D":
            return True

        # Rampe mit über 6 % Gefälle
        if self[185] == "45E":
            return False

        return None

    @property
    def breite_aufzugtuere(self) -> bool:
        """Mindestbreite der Aufzugstür 80 cm."""
        return self[187] == "25B"

    @property
    def grosse_aufzugkabine(self) -> Optional[bool]:
        """Determines whether the lift cabin is large."""
        # Kabinengröße ab 90 x 140 cm Innenmaß (nach DIN-Norm)
        if self[187] == "25C":
            return True

        if self[187] == "25D":
            return False

        return None

    @property
    def badewanne(self) -> bool:
        """Badewanne vorhanden."""
        return self[188] == "31W"

    @property
    def durchgangsbreite_bad_120(self) -> bool:
        """Durchgangsbreite Vorderseite
        Sanitärobjekt zur Wand mind. 120 cm.
        """
        return self[189] == "31E"

    @property
    def badezimmer_3qm(self) -> bool:
        """Größe des Badezimmers ab 3 m²"""
        return self[189] == "31F"

    @property
    def gegensprechanlage(self) -> bool:
        """Gegensprechanlage vorhanden."""
        return bool(self[190])

    @property
    def _balkon_details(self) -> Iterator[str]:
        """Generator für Balkon-Details."""
        for code in self[192].split():
            if code := code.strip():
                yield code

    @property
    def breite_balkontuere(self) -> bool:
        """Mindestbreite Balkontür 80cm."""
        return "23C" in self._balkon_details

    @property
    def balkon_mit_schwelle(self) -> bool:
        """Balkon mit Schwelle  (Höhe 2 cm und mehr)."""
        return "23D" in self._balkon_details

    @property
    def balkon_schwellenlos(self) -> bool:
        """Balkon schwellenlos erreichbar (Absatz bis 2 cm)."""
        return "23E" in self._balkon_details

    @property
    def balkon_gross(self) -> bool:
        """Balkongröße Über 2,5 m²."""
        return "23F" in self._balkon_details

    @property
    def rollstuhl_parkplatz(self) -> Optional[str]:
        """Abstellmöglichkeit für Hilfsmittel
        (Rollator/Rollstuhl) 1,90 x 3 m.
        """
        # innerhalb der Wohnung
        if self[193] == "22B":
            return "indoors"

        # außerhalb der Wohnung
        if self[193] == "22C":
            return "outdoors"

        return None

    @property
    def klingel_behindertengerecht(self) -> bool:
        """Klingeltableau Behindertengerecht
        (große Tasten, große Ziffern, Höhe +/- 85 cm).
        """
        return bool(self[194])

    @property
    def hohe_duschwanne(self) -> bool:
        """Bad mit hoher Duschwanne ab 7 cm."""
        return self[195] == "31D"

    @property
    def flache_duschwanne(self) -> bool:
        """Bad mit flacher Duschwanne bis 7 cm (nach DIN-Norm)."""
        return self[195] == "31C"

    @property
    def bodengleiche_duschwanne(self) -> bool:
        """Bad mit bodengleicher Dusche (nach DIN-Norm)."""
        return self[195] == "31B"

    @property
    def breite_wohnungstuer(self) -> bool:
        """Mindestbreite der Wohnungseingangstür 90 cm."""
        return bool(self[196])

    @property
    def keine_tuerschwellen(self) -> bool:
        """keine Türschwellen > 2cm (außer Balkon)."""
        return bool(self[197])

    @property
    def breite_tueren(self) -> bool:
        """Mindestbreite aller Wohnungstüren 80 cm
        (außer Abstellraum und Balkon).
        """
        return bool(self[198])

    @property
    def tueroeffner(self) -> bool:
        """Automatischer Türöffner an Haustür vorhanden."""
        return bool(self[199])
