class PhysicsEntity:  # Creates entity class group that handles the physics
    def __init__(self, game, e_type, pos, size):  # Defines game initialization
        self.game = game  #
        self.e_type = e_type  #
        self.pos = list(pos)  #
        self.size = size  #

    def update(self, movement=(0,0), velocity=(0,0)):
        frame_movement = (movement[0] +self.velocity[0],movement[1] +self.velocity[1])

        self.pos[0] += frame_movement
        self.pos[1] += frame_movement

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
