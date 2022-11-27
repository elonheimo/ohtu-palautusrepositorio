import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from pankki import Pankki

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "kerma", 4)
            if tuote_id == 3:
                return Tuote(2, "olut", 10000)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, viitegeneraattori_mock
        )

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, "12345", "33333-44455", 5
    )
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_2_eri_tuotteen_ostoksen_paaytyttya_pankin_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, "12345", "33333-44455", 9
    )
    def test_2_sama_tuotteen_ostoksen_paaytyttya_pankin_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, "12345", "33333-44455", 10
    )

    def test_1_tuote_loppu_toinen_ei_ostoksen_paaytyttya_pankin_tilisiirto(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, "12345", "33333-44455", 5
    )

    def test_aloita_asiointi_nollaa_ostokset(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 42, "12345", "33333-44455", 5
        )
    def test_viite_generaattori_aina_uusi_viite(self):
        viite_generaattori = Viitegeneraattori()
        self.assertNotEqual(
            viite_generaattori.uusi(),
            viite_generaattori.uusi()
        )
    def test_uusi_viite_maksutapahtumilla(self):
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            Mock(wraps=Viitegeneraattori())
        )
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 2, "12345", "33333-44455", 5
        )

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', 3, "12345", "33333-44455", 5
        )
    def test_kauppa_poistaa_korista(self):
        self.kauppa = Kauppa(
            Mock(wraps=Varasto()),
            self.pankki_mock,
            Mock(wraps=Viitegeneraattori())
        )
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            'pekka', ANY, "12345", "33333-44455", 0
        )

    def test_varasto_hae_olematon_tuote(self):
        self.assertEqual(
            None,
            Varasto().hae_tuote(1233321)
        )