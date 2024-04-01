class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        self.starting_resources = 500

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 155, 0)

        # Grid settings
        self.grid_rows = 5
        self.grid_columns = 8
        self.grid_tile_size = 120
