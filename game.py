import pygame
import sys
from button import Button
from Scripts.Entities import PhysicsEntity

window = pygame.display.set_mode((1250, 675))  # Creates game
        # window. screen = window
pygame.display.set_caption("Pizza Pursuit: Chef's Revenge")

bg = pygame.image.load("data/images/bg.png") #Menu background.

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        window.fill('black')

        play_text = get_font(45).render("Play ", True, "White")
        play_rect = play_text.get_rect(center=(640, 260))
        window.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        play_back.changeColor(play_mouse_pos)
        play_back.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        window.fill('white')

def main_menu():
    while True:
        window.blit(bg, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos() # Tracks mouse position.

        menu_text = get_font(100).render.("Pizza Pursuit", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100)) # SHows the Title of the game.

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            # Creates a play button
        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        window.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get()
            if event.type == pygame.QUIT
             pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                  play()
             if options_button.checkForInput(menu_mouse_pos):
                 options()
             if quit_button.checkForInput(menu_mouse_pos):
                  pygame.quit()
                  sys.exit()

     pygame.display.update()

main_menu()

class Game:  # Turns the game code into an object.
    def __init__(self):
        pygame.init()
        self.timer = pygame.time.Clock()  # Restricts framerate to a fixed
        # amount. clock = timer

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
