class Settings:
    """A class to store all settings for this game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (179, 180, 182)

        # Ship Settings
        self.ship_speed = 4.5