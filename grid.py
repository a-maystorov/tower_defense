import pygame


class Grid:
    """A class to represent the grid on which units can be placed."""

    def __init__(self, game):
        """Initialize the grid with the game instance and number of rows."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = game.settings.screen_width
        self.screen_height = game.settings.screen_height

        self.rows = self.game.settings.grid_rows
        self.columns = self.game.settings.grid_columns
        self.tile_size = self.game.settings.grid_tile_size
        self.grid_width = self.columns * self.tile_size
        self.grid_height = self.rows * self.tile_size
        self.start_x = (self.screen_rect.width - self.grid_width) // 2
        self.start_y = (self.screen_rect.height - self.grid_height) // 2

    def draw(self):
        """Draw the grid lines on the screen."""
        # Draw the horizontal grid lines
        for row in range(self.rows + 1):
            y = self.start_y + row * self.tile_size
            pygame.draw.line(self.screen, (255, 255, 255),
                             (self.start_x, y),
                             (self.start_x + self.grid_width, y))

        # Draw the vertical grid lines
        for col in range(self.columns + 1):
            x = self.start_x + col * self.tile_size
            pygame.draw.line(self.screen, (255, 255, 255),
                             (x, self.start_y),
                             (x, self.start_y + self.grid_height))

    def snap_to_center(self, mouse_pos):
        """Calculates the center coordinates of the grid cell under the mouse."""
        col = (mouse_pos[0] - self.start_x) // self.tile_size
        row = (mouse_pos[1] - self.start_y) // self.tile_size
        grid_x = self.start_x + col * self.tile_size + self.tile_size // 2
        grid_y = self.start_y + row * self.tile_size + self.tile_size // 2
        return grid_x, grid_y

    def can_place_defender(self, position):
        """Check if a defender can be placed at the given position in the grid."""
        if not (self.start_x <= position[0] <= self.start_x + self.grid_width and
                self.start_y <= position[1] <= self.start_y + self.grid_height):
            return False  # The position is outside the grid

        grid_x, grid_y = self.snap_to_center(position)
        grid_coord = (grid_x // self.tile_size, grid_y // self.tile_size)
        return not self.game.occupied_cells.get(grid_coord, False)

    def mark_cell(self, position, status):
        """Mark the cell at the given position as occupied."""
        grid_x, grid_y = self.snap_to_center(position)
        grid_coord = (grid_x // self.tile_size, grid_y // self.tile_size)
        self.game.occupied_cells[grid_coord] = status
