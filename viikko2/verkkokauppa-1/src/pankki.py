from kirjanpito import Kirjanpito


class Pankki:

    def __init__(self):
        self._kirjanpito = Kirjanpito()

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True
pankki = Pankki()