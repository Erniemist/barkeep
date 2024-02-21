from src.Avalon.Roles.Role import Role


class Percival(Role):
    team = Role.GOOD
    name = "Percival"

    def __init__(self, player):
        super().__init__(player)

    def info(self, players: list[Role]) -> str:
        wizards = [player.player for player in players if player.name in ["Morgana", "Merlin"]]
        return f"You are Percival. {' and '.join(wizards)} are Merlin and Morgana, but you know not who is who..."