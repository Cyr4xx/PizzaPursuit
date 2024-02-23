import sys

import pygame


class Game:  # Turns the game code into an object.
    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Pizza Pursuit: Chef's Revenge")
        self.screen = pygame.display.set_mode((1250, 675))  # Creates game
        # window.

        self.clock = pygame.time.Clock()  # Restricts framerate to a fixed
        # amount.

    def run(self):
        while True:
            for event in pygame.event.get():  # Gets user input.
                if event.type == pygame.QUIT:  # Allows user to exit out of
                    # the game.
                    pygame.quit()
                    sys.exit()

            pygame.display.update()  # Updates the screen to allow things to
            # display.
            self.clock.tick(60)  # sets framerate to 60 FPS.

Game().run()