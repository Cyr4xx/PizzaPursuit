import json

import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0),
                    (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}

COLLECTABLES = {'food'}

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tileMap = {}
        self.offgrid_tiles = []

    def extract(self, id_pairs, keep=False): # Checks if tile is in a list to extract it and says where it is.
        matches = []
        for tile in self.offgrid_tiles.copy():
            if (tile['type'], tile['variant']) in id_pairs:
                matches.append(tile.copy())
                if not keep:
                    self.offgrid_tiles.remove(tile)

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            if (tile['type'], tile['variant']) in id_pairs:
                matches.append(tile.copy())
                matches[-1]['pos'] = matches[-1]['pos'.copy()] # Changes tile position into pixels instead of coordinates.
                matches[-1]['pos'][0] *= self.tile_size
                matches[-1]['pos'][1] *= self.tile_size
                if not keep:
                    del self.tilemap[loc]

            return matches

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (
            int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(
                tile_loc[1] + offset[1])
            if check_loc in self.tileMap:
                tiles.append(self.tileMap[check_loc])
        return tiles

    def save(self, path):
        f = open(path, 'w')
        json.dump({'tileMap': self.tileMap, 'tile_size': self.tile_size, 'offgrid': self.offgrid_tiles}, f)
        f.close()

    def load(self, path):
        f = open(path, 'r')
        map_data = json.load(f)
        f.close()

        self.tileMap = map_data['tileMap']
        self.tile_size = map_data['tile_size']
        self.offgrid_tiles = map_data['offgrid']

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size,
                                         tile['pos'][1] * self.tile_size,
                                         self.tile_size, self.tile_size))
        return rects

    def collectable(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in COLLECTABLES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size,
                                         tile['pos'][1] * self.tile_size,
                                         self.tile_size, self.tile_size))
        return rects


    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))

