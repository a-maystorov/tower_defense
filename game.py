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

        self.grid = Grid(self)
        self.occupied_cells = {}

        # Initialize the first two archers on the first and second tile
        tile_center_offset = self.grid.tile_size // 2
        first_tile_position = (
            self.grid.start_x + tile_center_offset, self.grid.start_y + tile_center_offset)
        second_tile_position = (self.grid.start_x + self.grid.tile_size +
                                tile_center_offset, self.grid.start_y + tile_center_offset)

        self.defenders = [
            Archer(self, position=first_tile_position),
            Archer(self, position=second_tile_position),
        ]
        for defender in self.defenders:
            self.grid.mark_cell(defender.rect.center, True)

    def _check_mouse_button_down_events(self, event):
        """Respond to mouse button presses."""
        mouse_pos = event.pos
        for defender in self.defenders:
            defender.drag(mouse_pos)

    def _check_mouse_button_up_events(self, event):
        """Respond to mouse button releases."""
        mouse_pos = event.pos
        for defender in self.defenders:
            defender.drop(mouse_pos)

    def _check_mouse_motion_events(self, event):
        """Respond to mouse movements."""
        for defender in self.defenders:
            defender.update_position(event.pos)

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

        for defender in self.defenders:
            defender.blitme()

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
