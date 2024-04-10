import pygame

import sys

from Scripts.Utils import load_image

from Scripts.Entities import PhysicsEntity


class Game:  # Turns the game code into an object.
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1250, 675))  # Creates game
        # window. screen = window
        self.display = pygame.Surface((320, 240))
        self.timer = pygame.time.Clock()  # Restricts framerate to a fixed
        # amount. clock = timer
        pygame.display.set_caption("Pizza Pursuit")
        self.movement = [False, False]  # Updates cloud movement depending on
        # character movement.
        self.assets = {
            'player': load_image('images/Pierre.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():  # Gets user input.
                if event.type == pygame.QUIT:  # Allows user to exit out of
                    # the game.
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Takes user input and checks
                    # if a specific key is held down to move clouds.
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))

            pygame.display.update()  # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # sets framerate to 60 FPS.


Game().run()
