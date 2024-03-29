class Defender:
    """A base class for all defender types in the game."""

    def __init__(self, health, cost, position):
        """Initialize the defender and set its starting attributes."""
        self.health = health
        self.cost = cost
        self.position = position
