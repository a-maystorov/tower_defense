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
        self.last_position = position

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

    def drop(self, mouse_pos):
        """Drop the defender into a new position on the grid."""
        if self.held:
            self.held = False
            new_position = self.game.grid.snap_to_center(mouse_pos)

            if self.game.grid.can_place_defender(new_position):
                self.rect.center = new_position
                self.game.grid.mark_cell(new_position, True)
            else:
                self.rect.center = self.last_position

    def update_position(self, mouse_pos):
        """Update the defender's position to the mouse position."""
        if self.held:
            self.rect.center = mouse_pos
