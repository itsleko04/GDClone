import arcade
from pyglet.graphics import Batch


class GameOverView(arcade.View):
    def __init__(self, application):
        super().__init__(application.window)

        self.gui_camera = arcade.camera.Camera2D()
        
        self.window.set_caption("GameOver")
        self.application = application
        self.batch = Batch()
        self.restart_info = arcade.Text(
            text="Нажмите R, чтобы перезапустить уровень.",
            color=arcade.color.WHITE,
            x=self.center_x,
            y=self.center_y,
            font_size=24,
            anchor_x="center",
            batch=self.batch
        )

    def on_draw(self):
        self.clear()
        self.gui_camera.use()
        self.batch.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.restart()
    
    def restart(self):
        self.application.start_level(self.application.last_started_level)