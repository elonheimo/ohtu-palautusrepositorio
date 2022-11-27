import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_2_eri_tuotteen_lisaamisen_jlkn_ostoskorissa_2_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Kerma", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_2_eri_tuotteen_lisaamisen_jlkn_hinta_niiden_summa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Kerma", 2))
        self.assertEqual(self.kori.hinta(), 5)

    def test_2_sama_jlkn_2_tavaraa_korissa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_2_sama_korin_hinta_tuplat_tuotteen_hinnasta(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertEqual(self.kori.hinta(), 3*2)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertTrue(
            len(self.kori.ostokset()) == 1
        )

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(
            len(self.kori.ostokset()),
            1
        )
        self.assertEqual(
            ostos.tuotteen_nimi(),
            "Maito"
        )
    
    def test_lisaa_eri_2_tuotetta_korissa_2_eri_ostosta(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Kalja", 3))
        self.assertNotEqual(
            self.kori.ostokset()[0],
            self.kori.ostokset()[1]
        )
    def test_kahden_sama_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
            self.kori.lisaa_tuote(Tuote("Maito", 3))
            self.kori.lisaa_tuote(Tuote("Maito", 3))
            self.assertEqual(
                len(self.kori.ostokset()),
                1
            )
            self.assertEqual(
                self.kori.ostokset()[0].lukumaara(),
                2
            )

