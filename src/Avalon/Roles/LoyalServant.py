from src.Avalon.Roles.Role import Role


class LoyalServant(Role):
    team = Role.GOOD
    name = "Loyal Servant"

    def __init__(self, player):
        super().__init__(player)
