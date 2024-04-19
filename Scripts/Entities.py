import pygame



class PhysicsEntity:  # Creates entity class group that handles the physics
    def __init__(self, game, e_type, pos, size):  # Defines game initialization
        self.game = game  # Makes anything in the game accessible through the entity
        self.e_type = e_type  # Will use later, come back to this
        self.pos = list(pos)  # Where the entity will spawn
        self.size = size  # Size of the entity
        self.velocity = [0,
                         0]  # Used to represent the rate of change in the position
        self.collisions = {'up': False, 'down': False, 'right': False,
                           'left': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0],
                           self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False,
                           'left': False}

        frame_movement = (
            movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    def render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets['player'],
                  (self.pos[0] - offset[0], self.pos[1] - offset[1]))

