import sys

import pygame

from Scripts.Utils import load_images
from Scripts.tilemap import Tilemap

render_scale= 2.0


class Editor: # Turns the game code into an object.
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(
            'Editor')  # Sets the title of the window.
        self.screen = pygame.display.set_mode((640, 480)) # Creates game window. screen = window
        self.display = pygame.Surface((320, 240))

        self.timer = pygame.time.Clock() # Restricts framerate to a fixe amount. clock = timer

        self.assets = {
             'decor': load_images('tiles/decor'),
             'grass': load_images('tiles/grass'),
             'large_decor': load_images('tiles/large_decor'),
             'stone': load_images('tiles/stone'),
        }  # Loads assets for many aspects of the game.

        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, tile_size=16)  # Creates clouds.

        self.scroll = [0, 0] # # Creating Camera to follow player

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.clicking = False
        self.right_clicking = False
        self.shift = False
    def run(self):
        while True:
            self.display.fill((0, 0, 0))

            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.render(self.display, offset=render_scroll)

            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy() # Takes from list of tiles, and index, and takes the tile variant.
            current_tile_img.set_alpha(100)

            self.display.blit(current_tile_img, (5, 5))

            for event in pygame.event.get():  # Takes user input.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                    if event.button == 3:
                        self.right_clicking = True
                    if self.shift:
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(self.tile_list)
                    else:
                        if event.button == 4:
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                            self.tile_variant = 0
                        if event.button == 5:
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                            self.tile_variant = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self. clicking = False
                    if event.button == 3:
                        self.right_clicking = False
                if event.type == pygame.KEYDOWN: # Takes user input and checks
                    # if a specific key is held down to move.
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0))
            pygame.display.update() # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # Sets game to 60 FPS.

Editor().run()
