class TileMap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tile_map = {}
        self.offGrid_tiles = []

        for i in range(10):
            self.tile_map[str(3+i) + ';10'] =

