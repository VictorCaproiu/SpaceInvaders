import pygame as pg
from pygame.mixer import Sound
import random as rd
from Player import Player , PLAYER_TURNING_SPEED
from Asteroid import Asteroid
from Laser import Laser , LASER_COOLDOWN
from utils import load_image , load_sound , SCREEN_WIDTH , SCREEN_HEIGHT

# Create game window
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('SpaceInvaders')
pg.display.set_icon(pg.transform.scale(load_image("Player.png"), (32, 32)))
pg.mouse.set_visible(False)

# Add music
pg.mixer.init()
pg.mixer.music.load('data\\battle.wav')
pg.mixer.music.play(-1)

# Laser sound
pew_sound = pg.mixer.Sound("data\\pew.wav")

# UI font
pg.font.init() 
my_font = pg.font.SysFont('Comic Sans MS', 40)

# Load and scale background
background1 = load_image("BackGround.png")
background1 = pg.transform.scale(background1, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate the player in the middle of the screen
player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

player_group = pg.sprite.Group()
player_group.add(player)

asteroid_timer = 0
asteroid_group = pg.sprite.Group()
# test_asteroid = Asteroid((300,300))
# asteroid_group.add(test_asteroid)

laser_timer = 0
laser_group = pg.sprite.Group()
# test_laser = Laser(player)
# laser_group.add(test_laser)

clock = pg.time.Clock()
dt = 0
running = True
game_over_timer = 0
pg.init()

# Main loop
while running:
    
    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and laser_timer <= 0  and player.alive(): # SHOOT!! PEW PEW PEW
                laser_group.add(Laser(player))
                laser_timer = LASER_COOLDOWN
                pew_sound.play()
        
    if pg.key.get_pressed()[pg.K_w]: # W - accelerate
        player.accelerate()
    if pg.key.get_pressed()[pg.K_a]: # A - turn counter-clockwise
        player.angle += PLAYER_TURNING_SPEED
    if pg.key.get_pressed()[pg.K_d]: # D - turn clockwise
        player.angle -= PLAYER_TURNING_SPEED

    # Background
    screen.blit(background1,(0,0))
    # screen.fill((255,255,255))
    # print(f"inert: {player.inert}") # print current inertia magnitude

    if asteroid_timer <= 0:
        asteroid_timer = rd.randrange(1000,4000)
        asteroid_group.add(Asteroid())
    else:
        asteroid_timer -= dt

    if laser_timer > 0:
        laser_timer -= dt

    # check collisions
    for asteroid in asteroid_group:
        # player dies
        if player.collides_with(asteroid):
            player.kill()
            game_over_timer = 2000
        # asteroid is hit
        for laser in laser_group:
            if laser.collides_with(asteroid):
                asteroid.split()
                laser.kill()
                asteroid.kill()

    
    laser_group.draw(screen)
    laser_group.update()

    asteroid_group.draw(screen)
    asteroid_group.update()
    
    player_group.draw(screen)
    player_group.update(screen)

    if game_over_timer:
        text_surface = my_font.render('Game Over', False, (255,255,255))
        screen.blit(text_surface, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        game_over_timer -= dt
        if game_over_timer <= 20:
            running = False

    pg.display.flip()
    dt = clock.tick(120)  # framerate

pg.quit()