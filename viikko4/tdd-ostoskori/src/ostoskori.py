from typing import List
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset: List[Ostos] = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(
            [ostos.lukumaara() for ostos in self._ostokset]
        )
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum(
            [ostos.hinta() for ostos in self._ostokset]
        )
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for i, ostos in enumerate(self._ostokset):
            if ostos.tuote== lisattava:
                self._ostokset[i].muuta_lukumaaraa(1)
                return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        
        index, found= None, False
        for i, ostos in enumerate(self._ostokset):
            if ostos.tuote == poistettava:
                index, found= i, True
                break
        if not found:
            return
        if self._ostokset[index].lukumaara() > 1:
            self._ostokset[index].muuta_lukumaaraa(-1)
        else:
            self._ostokset.pop(index)

    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
