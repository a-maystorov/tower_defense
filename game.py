import pygame
import sys

from settings import Settings
from archer import Archer
from grid import Grid


class Game:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tower Defense Game")

        # Entities
        self.grid = Grid(self, rows=5)
        self.archer = Archer(self, health=100, cost=50, position=(
            100, 100), attack_power=15, attack_range=5)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.grid.draw()
        self.archer.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
