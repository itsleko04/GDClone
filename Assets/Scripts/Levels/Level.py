import arcade
from Assets.Scripts.CustomSystem.events import Event
from Assets.Scripts.Levels.game_over_panel import GameOverView


class Level(arcade.View):
    def __init__(self, application):
        super().__init__(application.window)
        self.application = application

        self.on_game_over = Event()
        self.is_game_over = False
        self.on_game_over.connect(lambda: self.__on_game_over_flag())

    def setup(self):
        self.is_game_over = False

    def __on_game_over_flag(self):
        self.is_game_over = True
        self.window.show_view(GameOverView(self.application))