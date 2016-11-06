import os, sys
import pygame
from pygame.locals import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data',name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.covert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0.0))