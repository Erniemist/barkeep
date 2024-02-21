from src.Avalon.Roles.Role import Role


class LoyalServant(Role):
    team = "Good"
    name = "Loyal Servant"

    def __init__(self, player):
        super().__init__(player)
