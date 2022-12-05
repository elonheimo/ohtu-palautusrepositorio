class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def even_score_text(self, even_score):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }.get(even_score, "Deuce")

    def under_40_text(self):
        case_dict = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        player_1 = case_dict.get(self.m_score1)
        player_2 = case_dict.get(self.m_score2)
        return f"{player_1}-{player_2}"

    def over_40_text(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result == 1:
            return "Advantage player1"
        if minus_result == -1:
            return "Advantage player2"
        if minus_result >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return self.even_score_text(
                self.m_score1
            )

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.over_40_text()

        return self.under_40_text()
