import arcade
from configparser import ConfigParser
from Assets.Scripts.Levels.test_level import TestLevel
from Assets.Scripts.Levels.Level import Level


class Application:
    def __init__(self, settings_path: str):
        self.settings = ConfigParser()
        self.settings.read(settings_path)
        self.width = float(self.settings["Application"]["ScreenWidth"])
        self.height = float(self.settings["Application"]["ScreenHeight"])
        self.window = arcade.Window(self.width, self.height)
        self.last_started_level = None
        self.start_level(TestLevel(self))
    
    def start_level(self, level: Level):
        self.last_started_level = level
        self.last_started_level.setup()
        self.window.show_view(self.last_started_level)

    def run(self):
        arcade.run()