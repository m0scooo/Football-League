from elo import update_elo

class League:
    def __init__(self, teams):
        self.ratings = {team: 1500 for team in teams}

    def play_match(self, team_a, team_b, goals_a, goals_b):

        if goals_a > goals_b:
            score_a = 1
        elif goals_a < goals_b:
            score_a = 0
        else:
            score_a = 0.5

        new_a, new_b = update_elo(
            self.ratings[team_a],
            self.ratings[team_b],
            score_a
        )

        self.ratings[team_a] = new_a
        self.ratings[team_b] = new_b
