# this class will contain all the settings' values for our alien game
# so that it makes it easier for us to work with the settings via the Settings object like adding new values or changing values
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 3.5