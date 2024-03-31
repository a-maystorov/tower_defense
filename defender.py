import pygame


class Defender:
    """A base class for all defender types in the game."""

    def __init__(self, game, health, cost, position):
        """Initialize the defender and set its starting attributes."""
        self.game = game
        self.health = health
        self.cost = cost
        self.position = position

        self.held = False
        self.screen = game.screen
        self.image = None
        self.rect = None

    def load_image(self, image_path):
        """Load defender image."""
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect(center=self.position)

    def blitme(self):
        """Draw the defender at its current position."""
        if self.held:
            # TODO: Maybe add some visual feedback that the defender is being held
            pass
        self.screen.blit(self.image, self.rect)

    def handle_drag_and_drop(self, mouse_pos):
        """Set the defender as held when it is clicked."""
        if self.rect.collidepoint(mouse_pos):
            self.held = True

    def update_position(self, mouse_pos):
        """Update the defender's position to the mouse position."""
        if self.held:
            self.rect.center = mouse_pos
