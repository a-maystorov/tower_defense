from defender import Defender


class Archer(Defender):
    """A class to manage the archer defender type in the game."""
    default_health = 100
    default_cost = 50
    default_attack_power = 15
    default_attack_range = 5

    def __init__(self, game, position, health=default_health, cost=default_cost,
                 attack_power=default_attack_power,
                 attack_range=default_attack_range):
        """Initialize the archer and set its starting attributes."""
        super().__init__(game, health, cost, position)
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.load_image("images/archer.png")
