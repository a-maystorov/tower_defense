import pygame
import sys

from settings import Settings
from grid import Grid
from shop import Shop


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

        self.shop = Shop(self)
        self.resources = self.settings.starting_resources

        self.defenders = []
        self.selected_defender = None

    def _instantiate_selected_defender(self, defender_class, position):
        """Instantiates the selected defender at the given position."""
        self.selected_defender = defender_class(self, position=position)
        self.selected_defender.held = True

    def _try_select_defender(self, mouse_pos):
        """Attempts to select a defender based on the mouse position."""
        defender_class = self.shop.get_selected_defender(mouse_pos)
        if defender_class:
            self._instantiate_selected_defender(defender_class, mouse_pos)

    def _check_mouse_button_down_events(self, event):
        """Respond to mouse button presses."""
        if self.selected_defender is None:
            self._try_select_defender(event.pos)

    def _is_defender_selected_and_held(self):
        """Check if a defender is currently selected and held."""
        return self.selected_defender and self.selected_defender.held

    def _can_place_defender(self, position):
        """Check if the selected defender can be placed at the specified position."""
        return self.grid.can_place_defender(position) and self.resources >= self.selected_defender.cost

    def _reset_selected_defender(self):
        """Reset the state of the selected defender."""
        self.selected_defender.held = False
        self.selected_defender = None

    def _place_defender(self, position):
        """Place the selected defender on the grid and deduct its cost."""
        self.selected_defender.drop(position)
        self.resources -= self.selected_defender.cost
        self.defenders.append(self.selected_defender)
        print(f"Resources after placement: {self.resources}")
        self._reset_selected_defender()

    def _check_mouse_button_up_events(self, event):
        """Respond to mouse button releases."""
        if not self._is_defender_selected_and_held():
            return

        if self._can_place_defender(event.pos):
            self._place_defender(event.pos)
        else:
            self._reset_selected_defender()

    def _check_mouse_motion_events(self, event):
        """Respond to mouse movements."""
        if self.selected_defender:
            self.selected_defender.update_position(event.pos)

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
        self.shop.draw()

        for defender in self.defenders:
            defender.blitme()

        if self.selected_defender is not None:
            # If a defender is selected, draw it on top of everything
            self.selected_defender.blitme()

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
