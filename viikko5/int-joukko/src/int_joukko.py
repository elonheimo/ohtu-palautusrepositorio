from copy import deepcopy
KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, luku):

        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, luku):
        if luku not in self.ljono:
            return False
        kohta = self.ljono.index(luku)
        self.ljono[kohta] = 0
       
        for j in range(kohta, self.alkioiden_lkm - 1):
            self.ljono[j]=self.ljono[j+1]
        
        self.alkioiden_lkm -= 1
        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return deepcopy(self.ljono)[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        [x.lisaa(luku) for luku in (a.to_int_list()+ b.to_int_list())]
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for luku in a_taulu:
            if luku in b_taulu:
                y.lisaa(luku)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku not in b_taulu:
                z.lisaa(luku)

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm):
            tuotos += f"{self.ljono[i]}, "
        return tuotos[:-2] + "}"
