import arcade


PLAYER_SPEED = 6
PLAYER_JUMP_FORCE = 8


class Player(arcade.Sprite):
    def __init__(self, path_or_texture, scale=1, x=0, y=0, movement_speed=PLAYER_SPEED, jump_force=PLAYER_JUMP_FORCE):
        super().__init__(path_or_texture, scale, center_x=x, center_y=y)
        self.is_freeze = False
        self.movement_speed = movement_speed
        self.jump_force = jump_force
        self.change_x = movement_speed
    
    def update(self, delta_time = 1 / 60, gravity=10):
        if self.is_freeze:
            self.change_x = 0
            self.change_y = 0
        if self.angle % 180 == 0:
            self.change_angle = 0

    def freeze(self):
        self.is_freeze = True
    
    def unfreeze(self):
        self.is_freeze = False
    
    def jump(self):
        angle_speed = 4
        self.change_y += self.jump_force
        self.change_angle = angle_speed
        self.angle = angle_speed

    def die(self):
        self.remove_from_sprite_lists()