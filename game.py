import sys
import math
import pygame

from Scripts.Utils import load_image, load_images, Animation, load_images_tran
from Scripts.Entities import PhysicsEntity, Player
from Scripts.tilemap import Tilemap
from Scripts.clouds import Clouds


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
             'large_decor': load_images('tiles/large_decor'),
             'stone': load_images('tiles/stone'),
             'food': load_images_tran('tiles/food'),
             'player': load_image('Entities/player/idle/Pierre 1.png'),
             'background': load_image('background.png'),
             'clouds': load_images('clouds'),
             'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
             'player/run': Animation(load_images('entities/player/run'),
                                     img_dur=4),
             'player/jump': Animation(load_images('entities/player/jump')),
             'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
        }  # Loads assets for many aspects of the game.

        self.clouds = Clouds(self.assets['clouds'], count=16)

        self.player = Player(self, (50, 50), (8, 15))

        # Creates the player.
        self.tileMap = Tilemap(self, tile_size=16)  # Loads all tiles and the level.
        self.tileMap.load('map.json')

        self.leaf_spawners = []
        for tree in self.tileMap.extract([('large_decor', 2)], keep=True):
            self.leaf_spawners.append(
                pygame.Rect(4 + tree['pos'][0], 4 + tree['pos'][1], 23, 13))
            # Creates leaves to fall from trees and also finds tree location.

        self.particles = []

        self.scroll = [0, 0]  # Creating Camera to follow player

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))  # Renders background objects.
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            self.tileMap.render(self.display, offset=render_scroll)

            self.player.update(self.tileMap, (self.movement[1] - self.movement[0], 0))
            self.player.collects(self.tileMap)

            self.player.render(self.display, offset=render_scroll)

            for particle in self.particles.copy():
                kill = particle.update()
                particle.render(self.display, offset=render_scroll)
                if particle.type == 'leaf':
                    particle.pos[0] += math.sin(
                        particle.animation.frame * 0.035) * 0.3
                if kill:
                    self.particles.remove(particle)

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
                        self.player.jump()
                if event.type == pygame.K_w:
                    if event.key == pygame.K_s:
                        self.movement[0] = False
                    if event.key == pygame.K_a:
                        self.movement[1] = False

                if event.type == pygame.KEYUP:  # Takes user input and checks
                    # if a specific key is held down to move.
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
            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0))
            pygame.display.update()  # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # Sets game to 60 FPS.


Game().run()
