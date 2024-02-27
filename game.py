import sys

import pygame


class Game:  # Turns the game code into an object.
    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Pizza Pursuit: Chef's Revenge")
        self.window = pygame.display.set_mode((1250, 675))  # Creates game
        # window. screen = window

        self.timer = pygame.time.Clock()  # Restricts framerate to a fixed
        # amount. clock = timer
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")

        self.img_pos = [160, 260]  # Cloud position.
        self.movement = [False, False] # Updates cloud movement depending on
        # character movement.

    def run(self):
        while True:
            self.img_pos[1] += (self.movement[1] - self.movement[0])*5
            self.window.blit(self.img,
                             self.img_pos)  # Creates a cloud collage.

            for event in pygame.event.get():  # Gets user input.
                if event.type == pygame.QUIT:  # Allows user to exit out of
                    # the game.
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Takes user input and checks
                    # if a specific key is held down to move clouds.
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()  # Updates the screen to allow things to
            # display.
            self.timer.tick(60)  # sets framerate to 60 FPS.


Game().run()
