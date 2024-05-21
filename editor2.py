import sys

import pygame

from Scripts.Utils import load_images, load_images_tran
from Scripts.tilemap import Tilemap


render_scale = 2.0
level = 0

class Editor: # Turns the game code into an object.
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(
            'Editor')  # Sets the title of the window.
        self.screen = pygame.display.set_mode((640, 480))  # Creates game window. screen = window
        self.display = pygame.Surface((320, 240))

        self.timer = pygame.time.Clock()  # Restricts framerate to a fixe amount. clock = timer

        self.assets = {
             'decor': load_images('tiles/decor'),
             'grass': load_images('tiles/grass'),
             'large_decor': load_images('tiles/large_decor'),
             'stone': load_images('tiles/stone'),
             'food': load_images('tiles/food'),
             'spawners': load_images('tiles/spawners')
        }  # Loads assets for many aspects of the game.

        self.movement = [False, False, False, False] # Controls editor movement by setitng values to true when a key si pressed.

        self.tileMap = Tilemap(self, tile_size=16)  # Loads tiles and sets size.

        try:
            self.tileMap.load('data/maps/1.json') # Loads the level, if not found creates a new level.
        except FileNotFoundError:
            pass

        self.scroll = [0, 0]  # # Creating Camera to follow player

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.clicking = False # Checks keybinds, which selects different objects and decorations to place.
        self.right_clicking = False
        self.shift = False
        self.ongrid = True

    def run(self):
        while True:
            self.display.fill((0, 0, 0)) # Sets background to black.

            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2
            render_scroll = (int(self.scroll[0]), int(self.scroll[1])) # Camera movement. *****

            self.tileMap.render(self.display, offset=render_scroll) # Renders tilemap with camera offsets.

            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            # Takes from list of tiles, and index, and takes the tile variant.
            current_tile_img.set_alpha(100)

            mpos = pygame.mouse.get_pos() # Takes mouse position
            mpos = (mpos[0]/render_scale, mpos[1]/render_scale)
            tile_pos = (int((mpos[0] + self.scroll[0]) // self.tileMap.tile_size), int(mpos[1] + self.scroll[1]) // self.tileMap.tile_size)
            # Calculates the tile position

            if self.ongrid:
                self.display.blit(current_tile_img, (tile_pos[0] * self.tileMap.tile_size - self.scroll[0], tile_pos[1] * self.tileMap.tile_size - self.scroll[1]))
              # Converts tile position to pixel coordinates
            else:
                self.display.blit(current_tile_img, mpos)

            if self.clicking and self.ongrid:
                self.tileMap.tileMap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos} # Takes tile position and type when placed.
            if self.right_clicking: # Deletes the tile when right clicking
                tile_loc = str(tile_pos[0]) + ';' + str(tile_pos[1])
                if tile_loc in self.tileMap.tileMap:
                    del self.tileMap.tileMap[tile_loc]
                for tile in self.tileMap.offgrid_tiles.copy():
                    tile_img = self.assets[tile['type']][tile['variant']]
                    tile_r = pygame.Rect(tile['pos'][0] - self.scroll[0],
                                         tile['pos'][1] - self.scroll[1],
                                         tile_img.get_width(),
                                         tile_img.get_height())
                    if tile_r.collidepoint(mpos):
                        self.tileMap.offgrid_tiles.remove(tile)

            self.display.blit(current_tile_img, (5, 5))

            for event in pygame.event.get():  # Takes user input.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        if not self.ongrid:
                            self.tileMap.offgrid_tiles.append(
                                {'type': self.tile_list[self.tile_group],
                                 'variant': self.tile_variant, 'pos': (
                                mpos[0] + self.scroll[0],
                                mpos[1] + self.scroll[1])})
                    if event.button == 3:
                        self.right_clicking = True
                    if self.shift:
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(
                                self.assets[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(
                                self.assets[self.tile_list[self.tile_group]])
                    else:
                        if event.button == 4:
                            self.tile_group = (self.tile_group - 1) % len(
                                self.tile_list)
                            self.tile_variant = 0
                        if event.button == 5:
                            self.tile_group = (self.tile_group + 1) % len(
                                self.tile_list)
                            self.tile_variant = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.right_clicking = False

                if event.type == pygame.KEYDOWN:  # Takes user input and checks
                    # if a specific key is held down to move.
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_g:
                        self.ongrid = not self.ongrid #Places tiles off the 16x16 grid.
                    if event.key == pygame.K_t:
                        self.tileMap.autotile() # T - auto places correct tile type.
                    if event.key ==pygame.K_o:
                        self.tileMap.save('data/maps/1.json') # O - saves edited level.
                        pygame.quit()
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True # If left shift is clicked, scrolls through selected tile type.
                if event.type == pygame.KEYUP: # Checks if key is released
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT: # When left shift realeased, exits selection.
                        self.shift = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0))
            pygame.display.update()  # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # Sets game to 60 FPS.


Editor().run()
