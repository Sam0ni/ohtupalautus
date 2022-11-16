class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        playerlist = filter(lambda x: x.nationality == nationality, self.reader.get_players())
        players = list(playerlist)
        players.sort(key=lambda x: x.points, reverse=True)
        return players