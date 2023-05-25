import pygame as pg
import math
from utils import load_image

PLAYER_SIZE = 50
PLAYER_SPEED = 0.1
PLAYER_TURNING_SPEED =  2

class Player(pg.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        # Load player sprite
        ship_surface = load_image("Player.png")
        # print(ship_surface.get_at((0,0)))
        ship_surface = pg.transform.scale(ship_surface, (PLAYER_SIZE,PLAYER_SIZE))
        # ship_surface.set_colorkey((0,0,0))

    
        self.orig_image = pg.Surface([PLAYER_SIZE,PLAYER_SIZE])           # Surface -> Surface
        self.orig_image.blit(ship_surface,(0,0,PLAYER_SIZE,PLAYER_SIZE))
        self.image = self.orig_image

        self.angle = 0                                      # Direction -> Vector2

        self.rect = self.image.get_rect()                   # Rectangle -> Rect
        self.rect.center = pos

        self.inertia = pg.math.Vector2(0)                     # Inertia -> Vector2

        self.speed = PLAYER_SPEED

    def rotate(self,angle):
        """Rotate the image of the sprite around its center."""
        self.image = pg.transform.rotozoom(self.orig_image, angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)

    def accelerate(self):
        self.inertia += pg.math.Vector2(0,-1).rotate(-self.angle) * self.speed

    def collides_with(self, other_obj):
        distance = math.sqrt((self.rect.center[0] - other_obj.rect.center[0]) ** 2 + 
                             (self.rect.center[1] - other_obj.rect.center[1]) ** 2)
        return distance < 45
    
    def update(self,screen):
        self.rect.center += self.inertia
        self.rect.clamp_ip(screen.get_rect())
        self.rotate(self.angle)

    
        
