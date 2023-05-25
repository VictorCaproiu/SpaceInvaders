import pygame as pg
import os

SCREEN_WIDTH = 1280   #1280
SCREEN_HEIGHT = 720  #720

main_dir = os.path.split(os.path.abspath(__file__))[0]
pg.mixer.pre_init(44100, 32, 2, 1024)

def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface.convert_alpha()

def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print(f"Warning, unable to load, {file}")
    return None