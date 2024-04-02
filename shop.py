import pygame

from archer import Archer


class Shop:
    """A class to manage the in-game shop for purchasing defenders."""

    def __init__(self, game):
        """Initialize the shop with the game instance."""
        self.game = game
        self.shop_width = self.game.settings.grid_tile_size
        self.shop_height = self.game.grid.grid_height
        self.shop_x = (self.game.grid.start_x - self.shop_width) // 2
        self.shop_y = self.game.grid.start_y
        self.background_color = (50, 50, 50)

        # TODO: Replace with other classes when implemented.
        self.defender_classes = [Archer, Archer, Archer]
        self.defenders_for_sale = self.initialize_defenders()

    def initialize_defenders(self):
        """Creates and vertically positions a list of defender instances."""
        defenders = []
        for i, DefenderClass in enumerate(self.defender_classes):
            position = (self.shop_x + (self.shop_width // 2),
                        self.shop_y + (self.game.settings.grid_tile_size // 2) +
                        self.game.settings.grid_tile_size * i)
            defenders.append(DefenderClass(self.game, position=position))
        return defenders

    def draw(self):
        """Draw the shop on the screen."""
        shop_rect = pygame.Rect(self.shop_x, self.shop_y,
                                self.shop_width, self.shop_height)
        pygame.draw.rect(self.game.screen, self.background_color, shop_rect)

        # Draw each defender in the shop
        for defender in self.defenders_for_sale:
            defender.blitme()

    def get_selected_defender(self, mouse_pos):
        """Return the currently selected defender in the shop."""
        for defender in self.defenders_for_sale:
            if defender.rect.collidepoint(mouse_pos):
                return type(defender)
        return None
