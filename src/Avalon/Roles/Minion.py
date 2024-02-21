from src.Avalon.Roles.Role import Role


class Minion(Role):
    team = "Evil"
    name = "Loathsome Minion of Mordred"

    def __init__(self, player):
        super().__init__(player)
