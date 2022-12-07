from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import *


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    #matcher = QueryBuilder().playsIn("NYR").hasAtLeast(10, "goals").build()
    matcher = (
        QueryBuilder()
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .build()
    )
    for player in stats.matches(matcher):
        print(player)
    matcher = (
        QueryBuilder()
        .oneOf(
            QueryBuilder().playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            QueryBuilder().playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)
    matcher = (
        QueryBuilder().build())
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
