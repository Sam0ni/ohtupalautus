class TennisGame:
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.love = 0
        self.fifteen = 1
        self.thirty = 2
        self.forty = 3

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.players_are_tied(self.player1_score)
        elif self.player1_score > self.forty or self.player2_score > self.forty:
            return self.player_is_in_advantage(self.player1_score - self.player2_score)
        else:
            score = self.single_player_score(self.player1_score)
            return score + "-" + self.single_player_score(self.player2_score)

    def players_are_tied(self, score):
        if score == self.love:
            return "Love-All"
        elif score == self.fifteen:
            return  "Fifteen-All"
        elif score == self.thirty:
            return  "Thirty-All"
        elif score == self.forty:
            return  "Forty-All"
        else:
            return  "Deuce"
    
    def player_is_in_advantage(self, score_difference):
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def single_player_score(self, player_score):
        if player_score == self.love:
            return "Love"
        elif player_score == self.fifteen:
            return "Fifteen"
        elif player_score == self.thirty:
            return "Thirty"
        elif player_score == self.forty:
            return "Forty"
