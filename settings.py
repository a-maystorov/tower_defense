class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        self.starting_resources = 200

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 155, 0)

        # Grid settings
        self.grid_rows = 5
        self.grid_columns = 8
        self.grid_tile_size = 120

        # Arrow settings
        self.arrow_speed = 2.0
        self.arrow_width = 50
        self.arrow_height = 3
        self.arrow_color = (60, 60, 60)
        self.arrow_fire_interval = 3000
