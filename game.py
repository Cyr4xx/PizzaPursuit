import pygame
import sys
from Scripts.Entities import PhysicsEntity

class Game:  # Turns the game code into an object.
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1250, 675))  # Creates game
        # window. screen = window
        self.timer = pygame.time.Clock()  # Restricts framerate to a fixed
        # amount. clock = timer
        pygame.display.set_caption("Pizza Pursuit: Chef's Revenge")
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0, 0, 0))  # Creates transparency in the image

        self.img_pos = [160, 260]  # Cloud position.
        self.movement = [False, False]  # Updates cloud movement depending on
        # character movement.
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.window.fill((14, 219, 248))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1],
                                self.img.get_width(),
                                self.img.get_height())  # Makes a rectangle which matches the cloud to create collision.
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.window, (0, 100, 255),
                                 self.collision_area)
            else:
                pygame.draw.rect(self.window, (0, 50, 155),
                                 self.collision_area)  # draws the collision rectangle.

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.window.blit(self.img, self.img_pos)  # Creates a cloud collage

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
