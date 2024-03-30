import pygame


class Grid:
    """A class to represent the grid on which units can be placed."""

    def __init__(self, game, rows):
        """Initialize the grid with the game instance and number of rows."""
        self.screen = game.screen
        self.screen_width = game.settings.screen_width
        self.screen_height = game.settings.screen_height
        self.rows = rows
        self.tile_size = self.screen_height // rows
        self.columns = self.screen_width // self.tile_size

    def draw(self):
        """Draw the grid lines on the screen."""
        # Draw the horizontal grid lines
        for row in range(self.rows + 1):
            y = row * self.tile_size
            pygame.draw.line(self.screen, (255, 255, 255),
                             (0, y), (self.screen_width, y))

        # Draw the vertical grid lines
        for col in range(self.columns + 1):
            x = col * self.tile_size
            pygame.draw.line(self.screen, (255, 255, 255),
                             (x, 0), (x, self.screen_height))
