import pygame



class PhysicsEntity:  # Creates entity class group that handles the physics
    def __init__(self, game, type, pos, size):  # Defines game initialization
        self.game = game  # Makes anything in the game accessible through the entity
        self.type = type  # Will use later, come back to this
        self.pos = list(pos)  # Where the entity will spawn
        self.size = size  # Size of the entity
        self.velocity = [0,
                         0]  # Used to represent the rate of change in the position
        self.collisions = {'up': False, 'down': False, 'right': False,
                           'left': False}
        self.action = ''
        self.anim_offset = (-3, -3) # Renders images with an offset to account for differing backgrounds.
        self.flip = False
        self.set_action('idle')

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0],
                           self.size[1])

    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type +'/' + self.action].copy()

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

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

        self.animation.update()

    def collects(self, tilemap):
        entity_rect = self.rect()
        for rect in tilemap.collectable(self.pos):
            if entity_rect.colliderect(rect):
                tilemap.FOOD = 1

    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))

class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0
        self.jumps = 1

    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        self.air_time += 1 # Checks air time and applies a jump animation
        # when jumping.
        if self.collisions['down']:
            self.air_time = 0
            self.jumps = 2

        if self.air_time > 4:
            self.set_action('jump')
        elif movement[0] != 0: # If the X axis of movement does not equal
            # zero then player is running.
            self.set_action('run')
        else:
            self.set_action('idle') # Sets player to idle if they are not
            # running or jumping.

    def jump(self):
        if self.jumps:
            self.velocity[1] = -3
            self.jumps -= 1
            self.air_time = 5




