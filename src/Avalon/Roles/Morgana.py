from src.Avalon.Roles.Role import Role


class Morgana(Role):
    team = Role.EVIL
    name = "Morgana"

    def __init__(self, player):
        super().__init__(player)
