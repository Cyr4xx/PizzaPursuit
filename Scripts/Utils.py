import pygame

import os

BASE_IMG_PATH = 'data/images/'


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

def load_image_tran(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    return img


def load_images_tran(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image_tran(path + '/' + img_name))
    return images



class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images # Images to animate.
        self.loop = loop # Loops Animations
        self.img_duration = img_dur # Duration of the animation.
        self.done = False # If the animation is done it sets this to True.
        self.frame = 0 # Renders images based on the frame

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self): # Choosing the correct image for the frame.
        if self.loop:
            self.frame = (self.frame + 1) % (
                        self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1,
                             self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)] # Increments the frames allowing for the right image to show.