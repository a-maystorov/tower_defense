import pygame

from defender import Defender
from arrow import Arrow


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
        self.last_fired = pygame.time.get_ticks()
        self.load_image("images/archer.png")

    def fire_arrow(self):
        """Check if it's time to fire an arrow, and if so, create and launch it."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fired > self.game.settings.arrow_fire_interval:
            self.last_fired = current_time
            new_arrow = Arrow(self.game, self.rect.midright)
            self.game.arrows.add(new_arrow)
