import sys

import pygame

from Scripts.Utils import load_image, load_images
from Scripts.Entities import PhysicsEntity
from Scripts.tilemap import Tilemap
from Scripts.clouds import Clouds


class Game: # Turns the game code into an object.
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(
            'Pizza Pursuit')  # Sets the title of the window.
        self.screen = pygame.display.set_mode((640, 480)) # Creates game window. screen = window
        self.display = pygame.Surface((320, 240))

        self.timer = pygame.time.Clock() # Restricts framerate to a fixe amount. clock = timer

        self.movement = [False, False]

        self.assets = {
             'decor': load_images('tiles/decor'),
             'grass': load_images('tiles/grass'),
             'large_decor': load_images('tiles/large_decor'),
             'stone': load_images('tiles/stone'),
            'player': load_image('Entities/Pierre/Pierre 1.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds')
        }  # Loads assets for many aspects of the game.

        self.clouds = Clouds(self.assets['clouds'], count = 16)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        # Creates the player.
        self.tileMap = Tilemap(self, tile_size=16)  # Creates clouds.

        self.scroll = [0, 0] # Creating Camera to follow player

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0,0)) # Renders background objects.

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset = render_scroll)

            self.tileMap.render(self.display, offset=render_scroll)

            self.player.update(self.tileMap,(self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            for event in pygame.event.get():  # Takes user input.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # Takes user input and checks
                    # if a specific key is held down to move.
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0))
            pygame.display.update() # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # Sets game to 60 FPS.

Game().run()
