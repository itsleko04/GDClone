import arcade
from Assets.Scripts.Player import Player
from Assets.Scripts.Levels.Level import Level


CAMERA_LERP = 0.8
GRAVITY = 0.35


class TestLevel(Level):
    def __init__(self, application):
        super().__init__(application)
        self.application = application

        self.bg = arcade.load_texture(application.settings["Sprites"]["LevelsBG"])
        self.cell_size = 51.2

    def setup(self):
        """Настраиваем игру здесь. Вызывается при старте и при рестарте"""
        super().setup()
        self.window.set_caption("Test Level")
        self.player_list = arcade.SpriteList()
        self.world_camera = arcade.camera.Camera2D()
        self.tile_map = arcade.load_tilemap(self.application.settings["Tilemap"]["TestLevel"], scaling=0.1)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.shapes_list = self.scene["shapes"]
        self.collision_list = self.scene["collision"]
        self.player = Player(self.application.settings["Sprites"]["PlayerIdle"], 0.075)
        self.player.left = self.cell_size * 11
        self.player.bottom = self.cell_size * 11
        self.player_list.append(self.player)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player, 
            walls=self.collision_list,
            gravity_constant=GRAVITY
        )

    def on_draw(self):
        self.clear()
        self.world_camera.use()
        for i in range(1, 20):
            rect = arcade.XYWH(self.window.rect.x * i, self.window.rect.y * 3, 
                               self.window.rect.width, self.window.rect.height)
            arcade.draw_texture_rect(self.bg, rect)
        self.scene.draw()
        self.player_list.draw()
    
    def on_update(self, delta_time):
        if self.is_game_over:
            return
        self.player_list.update(delta_time, GRAVITY)
        self.physics_engine.update()

        self.world_camera.position = arcade.math.lerp_2d(  # Изменяем позицию камеры
            self.world_camera.position,
            self.player.position,
            CAMERA_LERP,  # Плавность следования камеры
        )

        if len(self.physics_engine.player_sprite.collides_with_list(self.shapes_list)) != 0:
            self.player.die()
            self.player = None
            self.on_game_over.invoke()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if not self.physics_engine.can_jump(5):
                return
            self.player.jump()