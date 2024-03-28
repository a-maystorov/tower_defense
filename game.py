import pygame
import sys


class Game:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Tower Defense Game")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            self.screen.fill((0, 155, 0))
            pygame.display.flip()

            # limit FPS to 60
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    td = Game()
    td.run_game()
