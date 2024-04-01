import pygame
import sys

from settings import Settings
from archer import Archer
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
        self.shop = Shop(self)  # Initialize the shop
        self.resources = self.settings.starting_resources  # Initialize player resources
        # This will hold the defender the player has selected to place
        self.selected_defender = None

        # Initialize defenders list.
        self.defenders = []

    def _check_mouse_button_down_events(self, event):
        """Respond to mouse button presses."""
        mouse_pos = event.pos
        if self.selected_defender is None:
            defender_type = self.shop.handle_click(event.pos)
            if defender_type:
                # Create the defender but do not deduct cost yet
                self.selected_defender = defender_type(
                    self, position=event.pos)
                self.selected_defender.held = True  # Indicate that this defender is being held

    def _check_mouse_button_up_events(self, event):
        """Respond to mouse button releases."""
        mouse_pos = event.pos
        if self.selected_defender and self.selected_defender.held:
            # Attempt to place the defender on the grid
            can_place = self.grid.can_place_defender(mouse_pos)
            if can_place and self.resources >= self.selected_defender.cost:
                # Successful drop: defender is placed and resources deducted
                self.selected_defender.drop(mouse_pos)
                self.resources -= self.selected_defender.cost
                self.defenders.append(self.selected_defender)
                # Log the resource change
                print(f"Resources after placement: {self.resources}")
            elif not can_place:
                # Failed drop: defender is not placed
                if hasattr(self.selected_defender, 'original_position'):
                    # Reset the defender's position to the original position if it exists
                    self.selected_defender.rect.center = self.selected_defender.original_position
            # After placement attempt, whether successful or not, the defender is no longer held
            self.selected_defender.held = False
            self.selected_defender = None

    def _check_mouse_motion_events(self, event):
        """Respond to mouse movements."""
        if self.selected_defender and self.selected_defender.held:
            # Update the position of the defender that's currently being dragged
            self.selected_defender.update_position(event.pos)
        else:
            # If no defender is currently selected, check if we start dragging an already placed defender
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
