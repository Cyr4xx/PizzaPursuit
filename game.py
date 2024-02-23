import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))  # Creates game window.

clock = pygame.time.Clock()  # Restricts framerate to a fixed amount.

while True:
    for event in pygame.event.get():  # Gets user input.
        if event.type == pygame.QUIT:  # Allows user to exit out of the game.
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Updates the screen to allow things to display.
    clock.tick(60)  # sets framerate to 60 FPS.
