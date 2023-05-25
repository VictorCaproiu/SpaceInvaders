import pygame as pg
import math
from utils import load_image

LASER_SIZE = 10
LASER_SPEED = 5
LASER_COOLDOWN = 500

class Laser(pg.sprite.Sprite):
    def __init__(self,Player):
        super().__init__()

        # Load laser sprite
        laser_surface = load_image("Laser.png")
        laser_surface = pg.transform.scale(laser_surface, (LASER_SIZE,LASER_SIZE))
    
        self.orig_image = pg.Surface([LASER_SIZE,LASER_SIZE])
        self.orig_image.blit(laser_surface,(0,0,LASER_SIZE,LASER_SIZE))
        self.image = self.orig_image

        self.angle = Player.angle
        self.rect = self.image.get_rect()
        self.rect.center = Player.rect.center + pg.math.Vector2(0,-1).rotate(-self.angle) * 30
        self.inertia = pg.math.Vector2(0,-1).rotate(-self.angle) * LASER_SPEED

        self.rotate(self.angle)

    def rotate(self,angle):
        """Rotate the image of the sprite around its center."""
        self.image = pg.transform.rotozoom(self.orig_image, angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def collides_with(self, other_obj):
        distance = math.sqrt((self.rect.center[0] - other_obj.rect.center[0]) ** 2 + 
                             (self.rect.center[1] - other_obj.rect.center[1]) ** 2)
        return distance < other_obj.size/2
    
    def update(self):
        self.rect.center += self.inertia
        # self.angle += self.rotation_speed
        # self.rotate()