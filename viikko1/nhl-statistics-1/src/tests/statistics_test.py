import unittest
from statistics_nhl import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def __init__(self) -> None:
        pass

    def get_players(self):
        players = [
            Player(
                "name", "team", 3, 0
            ),
            Player(
                "jussi", "team", 0, 3
            ),
            Player(
                "another name", "another team", 2, 2
            )
        ]

        return players

class TestStatistics(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_haku_toimii_oikea(self):
        self.assertAlmostEqual(
            self.statistics.search("name").name,
            "name"
        )
    def test_haku_toimii_vaara(self):
        self.assertAlmostEqual(
            self.statistics.search("vaara"),
            None
        )
    def test_tiimi(self):
        self.assertAlmostEqual(
            [x.name for x in self.statistics.team("team")],
            ["name", "jussi"]
        )
    def test_top(self):
        self.assertAlmostEqual(
            self.statistics.top(1)[0].name,
            "another name"
        )

    def test_top_assists(self):
        self.assertAlmostEqual(
            self.statistics.top(1, SortBy.ASSISTS)[0].name,
            "jussi"
        )

    def test_top_goals(self):
        self.assertAlmostEqual(
            self.statistics.top(1, SortBy.GOALS)[0].name,
            "name"
        )

    


    

    