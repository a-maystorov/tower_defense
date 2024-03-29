from defender import Defender


class Archer(Defender):
    """A class to manage the archer defender type in the game."""

    def __init__(self, health, cost, position, attack_power, attack_range):
        """Initialize the archer and set its starting attributes."""
        super().__init__(health, cost, position)
        self.attack_power = attack_power
        self.attack_range = attack_range
