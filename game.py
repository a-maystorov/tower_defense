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

    def _check_mouse_button_down_events(self, event):
        """Respond to mouse button presses."""
        mouse_pos = event.pos
        # Check if the mouse is over the archer and "pick it up"
        if self.archer.rect.collidepoint(mouse_pos):
            self.archer.held = True

    def _check_mouse_button_up_events(self, event):
        """Respond to mouse button releases."""
        # Place the archer if it is being held
        if self.archer.held:
            self.archer.held = False
            # Snap to the nearest grid cell center
            grid_x = (event.pos[0] // self.grid.tile_size) * \
                self.grid.tile_size + self.grid.tile_size // 2

            grid_y = (event.pos[1] // self.grid.tile_size) * \
                self.grid.tile_size + self.grid.tile_size // 2
            self.archer.rect.center = (grid_x, grid_y)

    def _check_mouse_motion_events(self, event):
        """Respond to mouse movements."""
        if self.archer.held:
            # Move the archer with the mouse
            self.archer.rect.center = event.pos

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_button_down_events(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._check_mouse_button_up_events(event)
            elif event.type == pygame.MOUSEMOTION:
                self._check_mouse_motion_events(event)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.grid.draw()
        self.archer.blitme()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
