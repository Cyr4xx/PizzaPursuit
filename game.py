import os
import sys
import math
import pygame
import random


from Scripts.Utils import load_image, load_images, Animation, load_images_tran
from Scripts.entities import PhysicsEntity, Player, Enemy, Tomato, Banana
from Scripts.tilemap import Tilemap
from Scripts.clouds import Clouds
from Scripts.particle import Particle
from Scripts.sparks import Spark

class Collectible:
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.hitbox = pygame.Rect(pos[0], pos[1], 16, 16)  # Define hitbox for the bread
        self.collected = False  # Initialize collected flag

    def render(self, display, offset=(0, 0)):
        if not self.collected:  # Render only if not collected
            display.blit(self.game.assets['bread'][0], (self.pos[0] - offset[0], self.pos[1] - offset[1]))

    def update(self):
        player_rect = self.game.player.rect()
        if not self.collected and player_rect.colliderect(self.hitbox):
            self.collected = True  # Mark as collected if player collides with it
            self.game.score += 10  # Increase score by 10 when player collides with bread

class Fridge:
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.hitbox = pygame.Rect(pos[0], pos[1], 32, 32)  # Fridge hitbox size

    def update(self):
        # Add logic to update the fridge position or state if needed
        pass

class Game:  # Turns the game code into an object.
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(
            'Pizza Pursuit')  # Sets the title of the window.
        self.screen = pygame.display.set_mode((640, 480))  # Creates game window. screen = window
        self.display = pygame.Surface((320, 240))
        self.timer = pygame.time.Clock()  # Restricts framerate to a fixe amount. clock = timer
        self.movement = [False, False]

        self.assets = {
             'decor': load_images('tiles/decor'),
             'grass': load_images('tiles/grass'),
             'bread': load_images_tran('tiles/Bread'),
             'fridge': load_images_tran('tiles/fridge'),
             'large_decor': load_images('tiles/large_decor'),
             'stone': load_images('tiles/stone'),
             'lava': load_images('tiles/lava'),
             'player': load_image('Entities/player/idle/Pierre 1.png'),
             'background': load_image('background.png'),
             'background2': load_image('background2.png'),
             'background3': load_image('background3.png'),
             'pause': load_image('pausemenu.png'),
             'clouds': load_images('clouds'),
             'player/idle': Animation(load_images('Entities/player/idle'), img_dur=12),
             'player/run': Animation(load_images('Entities/player/run'),
                                     img_dur=4),
             'monkey/idle': Animation(load_images('Entities/monkey/idle'), img_dur=6),
             'monkey/run': Animation(load_images('Entities/monkey/run'),
                                    img_dur=6),
             'monkey/attack': Animation(load_images('Entities/monkey/Attack'), img_dur=6),
             'player/jump': Animation(load_images('Entities/player/jump')),
             'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
             'projectile': load_image('projectile.png'),
             'gun': load_image('gun.png'),
             'tomato/idle': Animation(load_images_tran('Entities/tomato/idle'), img_dur=6),
             'tomato/run': Animation(load_images_tran('Entities/tomato/run'),
                                     img_dur=6),
             'banana/idle': Animation(load_images_tran('Entities/banana/idle'),
                                      img_dur=6),
             'banana/run': Animation(load_images_tran('Entities/banana/run'),
                                     img_dur=6),
        }  # Loads assets for many aspects of the game.

        self.sfx = {
            'jump': pygame.mixer.Sound('data/sfx/jump.mp3'),
            'shoot': pygame.mixer.Sound('data/sfx/shoot.mp3'),
            'hit': pygame.mixer.Sound('data/sfx/hit.mp3')
        }


        self.sfx['jump'].set_volume(0.5)
        self.sfx['shoot'].set_volume(0.3)
        self.sfx['hit'].set_volume(0.7)


        self.clouds = Clouds(self.assets['clouds'], count=16)  # Prints clouds all over the background.

        self.player = Player(self, (50, 50), (8, 15))
        # Creates the player.
        self.tileMap = Tilemap(self, tile_size=16)  # Loads all tiles and the level.
        self.level = 0
        self.load_level(self.level)
        self.pause = False
        if self.level == 0:
            self.fridge = Fridge(self, (730.0, -474.5))

        self.score = 0  # Initialize score variable
        self.transition_timer = 0  # Initialize transition timer

        # Load font for displaying score
        self.font = pygame.font.Font(None, 36)
        self.font_color = (255, 255, 255)  # White color

    def check_collision_with_fridge(self):
        player_rect = self.player.rect()
        if player_rect.colliderect(self.fridge.hitbox):
            self.transition_timer += 1  # Increment transition timer when player collides with fridge
            if self.transition_timer > 30:  # If transition timer exceeds 30 frames
                self.level = min(self.level + 1, len(os.listdir(
                    'data/maps')) - 1)  # Move to the next level
                self.load_level(self.level)  # Load the next level

                if self.level == 1:
                    pygame.mixer.music.load('data/music2.mp3')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                if self.level == 2:
                    pygame.mixer.music.load('data/music3.mp3')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                self.transition_timer = 0  # Reset transition timer

    def load_level(self, map_id):
        self.tileMap.load('data/maps/' + str(map_id) + '.json')
        self.enemies = []
        for spawner in self.tileMap.extract(
                [('spawners', 0), ('spawners', 1), ('spawners', 2), ('spawners', 3)]):
            if spawner['variant'] == 0:
                self.player.pos = spawner['pos']
                self.player.air_time = 0
            elif spawner['variant'] == 1:
                self.enemies.append(Enemy(self, spawner['pos'], (8, 12)))
            elif spawner['variant'
            ] == 2:
                self.enemies.append(Tomato(self, spawner['pos'], (26, 23)))
            else:
                self.enemies.append(Banana(self, spawner['pos'], (10, 14)))
        self.leaf_spawners = []
        for tree in self.tileMap.extract([('large_decor', 2)], keep=True):
            self.leaf_spawners.append(
               pygame.Rect(4 + tree['pos'][0], 4 + tree['pos'][1], 23, 12))
        # Creates leaves to fall from trees and also finds tree location.
        self.projectiles = []
        self.particles = []
        self.sparks = []

        self.collectibles = []  # List to hold collectible bread instances

        for bread_spawn in self.tileMap.extract([('bread', 0)]):
            self.collectibles.append(Collectible(self, bread_spawn['pos']))



        # code to create a fridge instance at position (100, 100)

        self.scroll = [0, 0]  # Creating Camera to follow player
        self.dead = 0
        self.transition = -30

    def check_collision_with_enemies(self):
        player_rect = self.player.rect()
        for enemy in self.enemies:
            if player_rect.colliderect(enemy.rect()):
                self.dead = 1  # Trigger death sequence
                self.sfx['hit'].play()

    def run(self):
        if self.level == 0:
            pygame.mixer.music.load('data/music.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

        while True:
            if self.level == 1:
                self.fridge = Fridge(self, (920.5, -363.0))
                self.display.blit(self.assets['background2'], (0, 0))
            elif self.level == 2:
                self.fridge = Fridge(self, (3461.5, -763.5))
                self.display.blit(self.assets['background3'], (0, 0))

            if not self.pause:
                if self.level == 0:
                    self.display.blit(self.assets['background'], (0, 0))  # Renders background image.

            if not len(self.enemies):
                self.transition += 1
                if self.transition > 30:
                    self.level = min(self.level + 1,
                                     len(os.listdir('data/maps')) - 1) # Caps the amount of maps to min, so the list doesnt reach over the amount of maps.
                    self.load_level(self.level)
            if self.transition < 0:
                self.transition += 1

            self.check_collision_with_fridge()

            if self.dead:
                self.dead += 1
                if self.dead >= 10:
                    self.transition = min(30, self.transition + 1)
                if self.dead > 40:
                    self.load_level(self.level)



            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30 # Allows scrolling of the camera.
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            for rect in self.leaf_spawners:  # Length * width of the tree gives this area. Multiplying by 49999 allows us to control the number of spawn per second.
              if random.random() * 49999 < rect.width * rect.height: #This takes a random number and makes sure it places leaves in accordance with the hitbox of the tree.
                pos = (rect.x + random.random() * rect.width, rect.y + random.random() * rect.height) # Takes the x coordinate of the tree, multiples by random number.
                self.particles.append(
                        Particle(self, 'leaf', pos, velocity=[-0.3, 0.2], frame=random.randint(0, 20))) # Spawns the particles and dictates the Velocity, timing, position and type.
            if not self.pause:
                if self.level == 0:
                    self.clouds.update()
                    self.clouds.render(self.display, offset=render_scroll)
                self.tileMap.render(self.display, offset=render_scroll)
                for enemy in self.enemies.copy():
                    kill = enemy.update(self.tileMap, (0, 0))
                    enemy.render(self.display, offset=render_scroll)
                    if kill:
                        self.enemies.remove(enemy)
                if not self.dead:
                    self.check_collision_with_enemies()
                    self.player.update(self.tileMap,(self.movement[1] - self.movement[0], 0))
                    self.player.render(self.display, offset=render_scroll)
                for projectile in self.projectiles.copy():
                    projectile[0][0] += projectile[1]
                    projectile[2] += 1
                    img = self.assets['projectile']
                    self.display.blit(img, (
                    projectile[0][0] - img.get_width() / 2 - render_scroll[0],
                    projectile[0][1] - img.get_height() / 2 - render_scroll[1]))
                    if self.tileMap.solid_check(projectile[0]):
                        self.projectiles.remove(projectile)
                        for i in range(4):
                            self.sparks.append(Spark(projectile[0], random.random() - 0.5 + (
                                                     math.pi if projectile[
                                                                    1] > 0 else 0),
                                                 2 + random.random()))
                    elif projectile[2] > 360:
                        self.projectiles.remove(projectile)
                    elif abs(self.player.dashing) < 50:
                        if self.player.rect().collidepoint(projectile[0]):
                            self.projectiles.remove(projectile)
                            self.dead += 1
                            self.sfx['hit'].play()
                       #for i in range(30):
                           # angle = random.random() * math.pi * 2
                           # speed = random.random() * 5
                           # self.sparks.append(
                               # Spark(self.player.rect().center, angle,
                              #        2 + random.random()))
                        #    self.particles.append(Particle(self, 'particle',
                                                        #   self.player.rect().center,
                                                       #    velocity=[math.cos(
                                                            #   angle + math.pi) * speed * 0.5,
                                                            #         math.sin(
                                                           #              angle + math.pi) * speed * 0.5],
                                                        #   frame=random.randint(
                                                          #     0, 7)))
            for spark in self.sparks.copy():
                kill = spark.update()
                spark.render(self.display, offset=render_scroll)
                if kill:
                    self.sparks.remove(spark)
                for particle in self.particles.copy(): # Copies the particles so it can be removed each iteration.
                    kill = particle.update() # Updates the particle allowing them to be deleted.
                    particle.render(self.display, offset=render_scroll) # Adds camera offsets to particles and renders them.
                    if particle.type == 'leaf':
                        particle.pos[0] += math.sin(particle.animation.frame * 0.035) * 0.3  # Animates the particle.
                    if kill:
                        self.particles.remove(particle) # Removes the particle.
            for event in pygame.event.get():  # Takes user input.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Takes user input and checks
                    # if a specific key is held down to move.
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        if self.player.jump():
                            self.sfx['jump'].play()
                    if event.key == pygame.K_o:
                        from mainmenu import main_menu
                        self.screen = pygame.display.set_mode((1080, 1022))
                        main_menu()
                    if event.key == pygame.K_ESCAPE:
                        if self.pause:
                            self.pause = False
                        else:
                            self.pause = True
                            self.screen.fill('White')
                            self.display.blit(self.assets['pause'],
                                              (0, 0))
                if event.type == pygame.K_w:
                    if event.key == pygame.K_s:
                        self.movement[0] = False
                    if event.key == pygame.K_a:
                        self.movement[1] = False
                if event.type == pygame.KEYUP:  # Takes user input and checks
                    # if a specific key is released to move.
                    # Sets movement flags in accordance to keys held and unheld.
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        pass
                if event.type == pygame.K_w:
                    if event.key == pygame.K_s:
                        self.movement[0] = False
                    if event.key == pygame.K_a:
                        self.movement[1] = False

                for collectible in self.collectibles.copy():
                    collectible.render(self.display, offset=render_scroll)
                    collectible.update()
                    if self.player.rect().colliderect(collectible.hitbox):
                        self.score += 10
                        self.collectibles.remove(collectible)

            # Render score ribbon
            self.display.blit(self.font.render(f"Score: {self.score}", True,
                                             self.font_color), (10, 10))

            if self.transition:
                transition_surf = pygame.Surface(self.display.get_size())
                pygame.draw.circle(transition_surf, (255, 255, 255), (self.display.get_width() // 2, self.display.get_height() // 2), (30 - abs(self.transition)) * 8)
                transition_surf.set_colorkey((255, 255, 255))
                self.display.blit(transition_surf, (0, 0))

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0))
            pygame.display.update()  # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # Sets game to 60 FPS.
Game().run()