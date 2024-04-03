class PhysicsEntity:  # Creates entity class group that handles the physics
    def __init__(self, game, e_type, pos, size):  # Defines game initialization
        self.game = game  # Makes anything in the game accessible through the entity
        self.e_type = e_type  # Will use later, come back to this
        self.pos = list(pos)  # Where the entity will spawn
        self.size = size  # Size of the entity

    def update(self, movement=(0,0), velocity=(0,0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement
        self.pos[1] += frame_movement

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
