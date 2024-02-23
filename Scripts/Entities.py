import sys  # Impo

import pygame  # Imports pygame into this code

pygame.init()  # Starts up Pygame

pygame.display.set_caption("Pizza Pursuit")  # Creates name for the window that will be opened
window = pygame.display.set_mode((1250, 675))  # Creates window and the numbers determine the size of the window

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
