import pygame


class Grid:
    """A class to represent the grid on which units can be placed."""

    def __init__(self, game, rows):
        """Initialize the grid with the game instance and number of rows."""
        self.game = game
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

    def snap_to_center(self, mouse_pos):
        """Calculates the center coordinates of the grid cell under the mouse."""
        grid_x = (mouse_pos[0] // self.tile_size) * \
            self.tile_size + self.tile_size // 2
        grid_y = (mouse_pos[1] // self.tile_size) * \
            self.tile_size + self.tile_size // 2
        return grid_x, grid_y

    def can_place_defender(self, position):
        """Check if a defender can be placed at the given position."""
        grid_x, grid_y = self.snap_to_center(position)
        grid_coord = (grid_x // self.tile_size, grid_y // self.tile_size)
        return not self.game.occupied_cells.get(grid_coord, False)

    def mark_cell(self, position, status):
        """Mark or unmark the cell at the given position as occupied."""
        grid_x, grid_y = self.snap_to_center(position)
        grid_coord = (grid_x // self.tile_size, grid_y // self.tile_size)
        self.game.occupied_cells[grid_coord] = status
