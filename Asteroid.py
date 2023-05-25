import pygame as pg
from utils import load_image , SCREEN_WIDTH , SCREEN_HEIGHT
import random as rd

ASTEROID_SIZE = 50

class Asteroid(pg.sprite.Sprite):
    def __init__(self,pos=0,size=ASTEROID_SIZE):

        self.size = size

        super().__init__()

        # Load asteroid sprite
        asteroid_surface = load_image("BigAsteroid.png")
        asteroid_surface = pg.transform.scale(asteroid_surface, (size,size))
    
        self.orig_image = pg.Surface([size,size])
        self.orig_image.blit(asteroid_surface,(0,0,size,size))
        self.image = self.orig_image

        if not pos:
            self.random_start(rd.randrange(0,4)) # asteroids can spawn from all 4 sides of the screen
        else:
            self.angle = 0
            self.rotation_speed = 0
            self.rect = self.image.get_rect()
            self.rect.center = pos
            self.inertia = pg.math.Vector2(0)

    def random_start(self,direction):
        self.angle = rd.randrange(-180,180)
        self.rotation_speed = rd.randrange(-4,4)
        self.rect = self.image.get_rect()

        if direction == 0:
            self.rect.center = (rd.randrange(SCREEN_WIDTH),rd.randrange(SCREEN_HEIGHT-100,SCREEN_HEIGHT)) # incepe sub fereastra
            self.inertia = pg.math.Vector2((rd.randrange(-3,3),rd.randrange(-3,0))) # merge in sus
        
        if direction == 1: 
            self.rect.center = (rd.randrange(SCREEN_WIDTH),rd.randrange(0,100)) # incepe deasupra ferestrei
            self.inertia = pg.math.Vector2((rd.randrange(-3,3),rd.randrange(2,3))) # merge in jos

        if direction == 2: 
            self.rect.center = (rd.randrange(SCREEN_WIDTH-100,SCREEN_WIDTH),rd.randrange(SCREEN_HEIGHT)) # incepe in dreapta ferestrei
            self.inertia = pg.math.Vector2((rd.randrange(-3,0),rd.randrange(-3,3))) # merge in stanga

        if direction == 3: 
            self.rect.center = (rd.randrange(0,100),rd.randrange(SCREEN_HEIGHT)) # incepe in stanga ferestrei
            self.inertia = pg.math.Vector2((rd.randrange(0,3),rd.randrange(-2,2))) # merge in dreapta
    
    def rotate(self):
        """Rotate the image of the sprite around its center."""
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)

    def split(self):
        asteroid1 = Asteroid(self.rect.center,self.size/2)
        asteroid1.angle = self.angle + 90
        asteroid1.inertia = self.inertia.rotate(90)

        asteroid2 = Asteroid(self.rect.center,self.size/2)
        asteroid2.angle = self.angle - 90
        asteroid2.inertia = self.inertia.rotate(-90)

        print(self.groups()[0])
        self.groups()[0].add(asteroid1,asteroid2)

    def update(self):
        self.rect.center += self.inertia
        self.angle += self.rotation_speed
        self.rotate()
        
