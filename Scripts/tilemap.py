class TileMap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tile_map = {}
        self.offGrid_tiles = []

        for i in range(10):
            self.tile_map[str(3+i) + ';10'] = {'type': 'grass', 'variant': 1,'pos': (3+i, 10)}
            self.tile_map[';10' + str(i+5)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}



# When def render is written add offset=(0,0) into the brackets