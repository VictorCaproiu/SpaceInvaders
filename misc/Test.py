import pygame as pg
import random as rd

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

dir = pg.math.Vector2(0,1)

dir.rotate_ip(90)


clock = pg.time.Clock()
pg.init()

while True:

    pg.display.flip()
    print(rd.randrange(0,5))
    dt = clock.tick(60) / 1000