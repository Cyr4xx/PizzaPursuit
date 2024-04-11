class TileMap:
    def __init__(self, tile_size=16):
        self.tileSize = tile_size
        self.tileMap = {}
        self.offGrid_tiles = []
