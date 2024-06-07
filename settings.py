class Settings():

    def __init__(self):
        self.screen_width = 1900
        self.screen_height = 1000
        self.bg_color = (65, 74, 76)
        self.ship_speed = 1

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (226, 88, 34)
        self.bullets_allowed = 3
        
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.ship_limit = 3