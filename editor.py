import sys
import pygame
from Scripts.Utils import load_images
from Scripts.tilemap import TileMap

render_scale = 2.0


class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Editor')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.timer = pygame.time.Clock()
        self.assets = {
<<<<<<< HEAD
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'food': load_images('tiles/food'),
            'spawn_banana': load_images('tiles/spawners/banana'),
            'spawn_tomato': load_images('tiles/spawners/tomato'),
        }
        self.movement = [False, False, False, False]
        self.tileMap = TileMap(self, tile_size=16)
=======
             'decor': load_images('tiles/decor'),
             'grass': load_images('tiles/grass'),
             'large_decor': load_images('tiles/large_decor'),
             'stone': load_images('tiles/stone'),
             'food': load_images('tiles/food'),
        }  # Loads assets for many aspects of the game.

        self.movement = [False, False, False, False] # Controls editor movement by setitng values to true when a key si pressed.

        self.tileMap = Tilemap(self, tile_size=16)  # Loads tiles and sets size.

>>>>>>> feaabdf48bfdffd8f52d2bd099ddc5134b7cd10a
        try:
            self.tileMap.load('map.json') # Loads the level, if not found creates a new level.
        except FileNotFoundError:
            pass
        self.scroll = [0, 0]
        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0
<<<<<<< HEAD
        self.clicking = False
=======

        self.clicking = False # Checks keybinds, which selects different objects and decorations to place.
>>>>>>> feaabdf48bfdffd8f52d2bd099ddc5134b7cd10a
        self.right_clicking = False
        self.shift = False
        self.onGrid = True

    def run(self):
        while True:
<<<<<<< HEAD
            self.display.fill((0, 0, 0))
            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[0] += (self.movement[3] - self.movement[2]) * 2
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.tileMap.render(self.display, offset=render_scroll)
=======
            self.display.fill((0, 0, 0)) # Sets background to black.

            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[0] += (self.movement[3] - self.movement[2]) * 2
            render_scroll = (int(self.scroll[0]), int(self.scroll[1])) # Camera movement. *****

            self.tileMap.render(self.display, offset=render_scroll) # Renders tilemap with camera offsets.

>>>>>>> feaabdf48bfdffd8f52d2bd099ddc5134b7cd10a
            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            current_tile_img.set_alpha(100)
<<<<<<< HEAD
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] / render_scale, mpos[1] / render_scale)
            tile_pos = (int((mpos[0] + self.scroll[0]) // self.tileMap.tile_size),
                        int(mpos[1] + self.scroll[1]) // self.tileMap.tile_size)
            if self.onGrid:
                self.display.blit(current_tile_img, (tile_pos[0] * self.tileMap.tile_size - self.scroll[0],
                                                     tile_pos[1] * self.tileMap.tile_size - self.scroll[1]))
            else:
                self.display.blit(current_tile_img, mpos)

            try:
                if self.clicking and self.onGrid:
                    self.tileMap.tileMap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = \
                        {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}
            except KeyError:
                pass

            if self.right_clicking:
=======

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
            if self.right_clicking: # Deletes the tile when right clicking.
>>>>>>> feaabdf48bfdffd8f52d2bd099ddc5134b7cd10a
                tile_loc = str(tile_pos[0]) + ';' + str(tile_pos[1])
                if tile_loc in self.tileMap.tileMap:
                    del self.tileMap.tileMap[tile_loc]
                for tile in self.tileMap.offgrid_tiles.copy():
                    tile_img = self.assets[tile['type']][tile['variant']]
                    tile_r = pygame.Rect(tile['pos'][0] - self.scroll[0], tile['pos'][1] - self.scroll[1],
                                         tile_img.get.width(), tile_img.get_height())
                    if tile_r.collidepoint(mpos):
                        self.tileMap.offgrid_tiles.remove(tile)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
<<<<<<< HEAD
                        if not self.onGrid:
                            self.tileMap.offgrid_tiles.append({'type': self.tile_list[self.tile_group],
                                                               'variant': self.tile_variant, 'pos':
                                                                   (
                                                                   mpos[0] + self.scroll[0], mpos[1] + self.scroll[1])})
=======
                        if not self.ongrid:
                            self.tileMap.offgrid_tiles.append(
                                {'type': self.tile_list[self.tile_group],
                                 'variant': self.tile_variant, 'pos': (
                                mpos[0] + self.scroll[0],
                                mpos[1] + self.scroll[1])})
>>>>>>> feaabdf48bfdffd8f52d2bd099ddc5134b7cd10a
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_g:
<<<<<<< HEAD
                        self.onGrid = not self.onGrid
                    if event.key == pygame.K_o:
=======
                        self.ongrid = not self.ongrid
                    if event.key == pygame.K_t:
                        self.tileMap.autotile()
                    if event.key ==pygame.K_o:
>>>>>>> feaabdf48bfdffd8f52d2bd099ddc5134b7cd10a
                        self.tileMap.save('map.json')
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0))
            pygame.display.update()
            self.timer.tick(60)


Editor().run()
