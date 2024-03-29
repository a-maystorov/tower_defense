import pygame

from defender import Defender


class Archer(Defender):
    """A class to manage the archer defender type in the game."""

    def __init__(self, game, health, cost, position, attack_power, attack_range):
        """Initialize the archer and set its starting attributes."""
        super().__init__(health, cost, position)
        self.attack_power = attack_power
        self.attack_range = attack_range

        self.screen = game.screen

        # Load the archer image.
        self.image = pygame.image.load("images/archer.png").convert()

    def blitme(self):
        """Draw the archer at its current position"""
        self.screen.blit(self.image, self.position)
