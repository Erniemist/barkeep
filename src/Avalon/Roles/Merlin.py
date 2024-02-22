class Merlin:
    team = "Good"
    name = "Merlin"

    def __init__(self, player):
        self.player = player

    def info(self, players):
        evil_players = [player.player for player in players if player.team == "Evil"]
        return f"You are Merlin. {' and '.join(evil_players)} are Evil."
