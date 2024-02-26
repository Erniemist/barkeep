from src.avalon.Roles.role import Role


class LoyalServant(Role):
    team = Role.GOOD
    name = "Loyal Servant"

    def __init__(self, player):
        super().__init__(player)

    def info(self, players: list[Role]) -> str:
        return "You are a Loyal Servant of King Arthur of Britain. You don't know anything."
