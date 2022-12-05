class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo


class Komento():
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, syote) -> None:
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.edellinen = 0

    def suorita(self):
        return 0

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen)


class Erotus(Komento):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, syote) -> None:
        super().__init__(sovelluslogiikka, syote)

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.miinus(self.syote())


class Summa(Komento):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, syote) -> None:
        super().__init__(sovelluslogiikka, syote)

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.plus(self.syote())


class Nollaus(Komento):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, syote) -> None:
        super().__init__(sovelluslogiikka, syote)

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa()
