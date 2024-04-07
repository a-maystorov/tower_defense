import pygame
from pygame.sprite import Sprite


class Arrow(Sprite):
    """A class to manage arrows fired by archers."""

    def __init__(self, game, start_pos):
        """Create an arrow object at the archer's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.arrow_color

        # Create an arrow rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.arrow_width, self.settings.arrow_height)
        # Use start_pos for setting the initial position
        self.rect.midtop = start_pos

        self.x = float(self.rect.x)

    def update(self):
        """Move the arrow up the screen and remove old ones."""
        # Update the decimal position of the arrow.
        self.x += self.settings.arrow_speed
        # Update the rect position.
        self.rect.x = self.x
        # Check if the arrow has left the screen and delete it if so
        if self.rect.left > self.screen.get_width():
            self.kill()

    def draw_arrow(self):
        """Draw the arrow to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
