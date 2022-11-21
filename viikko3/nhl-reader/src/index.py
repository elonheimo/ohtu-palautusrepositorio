import requests
from player import Player
class PlayerReader:
    def __init__(self, url :str) -> None:
        response = requests.get(url).json()
        self.players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['nationality'],
                player_dict['assists']
            )

            self.players.append(player)

class PlayerStats:
    def __init__(self, playerReader: PlayerReader) -> None:
        self.players = playerReader.players

    def top_scorers_by_nationality(self, nationality :str):
        
        return list(filter(
            lambda x: (x.nationality == nationality),
            self.players
        ))
        

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality('FIN')

    for player in players:
        print(player)

if __name__ == "__main__":
    main()