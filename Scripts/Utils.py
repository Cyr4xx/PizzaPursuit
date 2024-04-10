import pygame

BASE_IMG_PATH = 'data/images/Pierre.png'


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH).convert()
    img.set_colorkey((0, 0, 0))
    return img
