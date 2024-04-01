# Create a new file called shop.py

import pygame
from archer import Archer


class Shop:
    """A class to manage the in-game shop for purchasing defenders."""

    def __init__(self, game):
        """Initialize the shop with the game instance."""
        self.game = game
        self.shop_width = self.game.settings.grid_tile_size  # Single column width
        self.shop_height = self.game.grid.grid_height  # Same height as the grid
        self.shop_x = 0  # Starting x position of the shop
        # Align the shop with the grid's y position
        self.shop_y = self.game.grid.start_y
        self.background_color = (50, 50, 50)  # Shop background color

        # Initialize the shop with a list of defenders.
        self.defenders_for_sale = [Archer(game, position=(
            self.shop_width // 2, self.shop_y + self.game.settings.grid_tile_size // 2))]
        self.defender_costs = {Archer: Archer.default_cost}

    def draw(self):
        """Draw the shop on the screen."""
        shop_rect = pygame.Rect(self.shop_x, self.shop_y,
                                self.shop_width, self.shop_height)
        pygame.draw.rect(self.game.screen, self.background_color, shop_rect)

        # Draw each defender in the shop
        for defender in self.defenders_for_sale:
            defender.blitme()

    def handle_click(self, mouse_pos):
        """Handle clicks within the shop to select defenders."""
        if (self.shop_x <= mouse_pos[0] <= self.shop_x + self.shop_width and
                self.shop_y <= mouse_pos[1] <= self.shop_y + self.shop_height):
            # Determine which defender was clicked
            for defender in self.defenders_for_sale:
                if defender.rect.collidepoint(mouse_pos):
                    return type(defender)
        return None
