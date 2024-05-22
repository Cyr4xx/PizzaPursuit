import pygame
import sys
from button import Button
import time


pygame.init()
window = pygame.display.set_mode((1080, 1022))  # Creates game
# window. screen = window
pygame.display.set_caption("Pizza Pursuit: Chef's Revenge")

background_img = pygame.image.load("data/images/bg.png")  # Menu background.
splashscreen = pygame.image.load("data/Pizza.png")  # Splash Screen.
tutorial_screen = pygame.image.load("data/images/tutorial.png")

def get_font(size):
    return pygame.font.Font("data/PixelatedPusab.ttf", size)
# Takes the font file I provided, and allows utilization of the fonts for
# the menu screen.


window.fill('white')
window.blit(splashscreen, (0, 0))  # Places background photo.
pygame.display.update()


def play():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()  # Takes mouse position

        window.fill('black')

        play_text = get_font(75).render("Level Select ", True, "White")
        play_rect = play_text.get_rect(center=(540, 100))
        window.blit(play_text, play_rect)  # Creates the play button.

        play_back = Button(image=None, pos=(540, 780),
                           text_input="BACK", font=get_font(75),
                           base_color="#d7fcd4", hovering_color="White")
        play1 = Button(image=None, pos=(325, 460),
                           text_input="Level 1", font=get_font(45),
                           base_color="Green", hovering_color="White")
        play2 = Button(image=None, pos=(540, 460),
                           text_input="Level 2", font=get_font(45),
                           base_color="Gray", hovering_color="White")
        play3 = Button(image=None, pos=(755, 460),
                           text_input="Level 3", font=get_font(45),
                           base_color="Orange", hovering_color="White")
        for button in [play_back, play1, play2, play3]:
            button.changeColor(play_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu()
                if play1.checkForInput(play_mouse_pos):
                    from game import Game
                    Game().run()
                if play2.checkForInput(play_mouse_pos):
                    from level2 import Game
                    Game().run()
                if play3.checkForInput(play_mouse_pos):
                    from level3 import Game
                    Game().run()

        pygame.display.update()


def tutorial():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()  # Takes mouse position

        window.fill(
            'white')  # Creates the illusion of multiple screens by filling screen with black
        window.blit(tutorial_screen, (0, 0))


        tutorial_back = Button(image=None, pos=(980, 120), text_input="Back",
                              # Creates the back button when options is pressed
                              font=get_font(75), base_color="Green",
                              hovering_color="White")

        tutorial_back.changeColor(
            options_mouse_pos)  # Changes button colour if hovering over back button.
        tutorial_back.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tutorial_back.checkForInput(options_mouse_pos):
                    main_menu()

        pygame.display.update()
def editor():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()  # Takes mouse position

        window.fill('black')

        play_text = get_font(75).render("Edit Select ", True, "White")
        play_rect = play_text.get_rect(center=(540, 100))
        window.blit(play_text, play_rect)  # Creates the play button.

        play_back = Button(image=None, pos=(540, 780),
                           text_input="BACK", font=get_font(75),
                           base_color="#d7fcd4", hovering_color="White")
        play1 = Button(image=None, pos=(325, 460),
                           text_input="Level 1", font=get_font(45),
                           base_color="Green", hovering_color="White")
        play2 = Button(image=None, pos=(540, 460),
                           text_input="Level 2", font=get_font(45),
                           base_color="Gray", hovering_color="White")
        play3 = Button(image=None, pos=(755, 460),
                           text_input="Level 3", font=get_font(45),
                           base_color="Orange", hovering_color="White")
        for button in [play_back, play1, play2, play3]:
            button.changeColor(play_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu()
                if play1.checkForInput(play_mouse_pos):
                    from editor import Editor
                    Editor().run()
                if play2.checkForInput(play_mouse_pos):
                    from editor2 import Editor
                    Editor().run()
                if play3.checkForInput(play_mouse_pos):
                    from editor3 import Editor
                    Editor().run()


        pygame.display.update()

def main_menu():
    while True:

        window.fill('black')

        window.blit(background_img, (0, 0))  # Places background photo.

        menu_mouse_pos = pygame.mouse.get_pos()  # Tracks mouse position.

        menu_text = get_font(75).render('Pizza Pursuit', True, "#ffffff")
        menu_rect = menu_text.get_rect(
            center=(540, 100))  # SHows the Title of the game.

        play_button = Button(image=pygame.image.load("data/play.png"),
                             pos=(540, 250),
                             text_input="Play", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        # Creates a play button
        tutorial_button = Button(image=pygame.image.load("data/Tutorial.png"),
                                 pos=(540, 400),
                                 text_input="Tutorial", font=get_font(75), base_color="#d7fcd4",
                                 hovering_color="White")


        maker_button = Button(image=pygame.image.load("data/Maker.png"),
                                pos=(540, 550),
                                text_input="Level Editor", font=get_font(75),
                                base_color="#d7fcd4",
                                hovering_color="White")
        # Places an options button.

        quit_button = Button(image=pygame.image.load("data/quit.png"),
                             pos=(540, 780),
                             text_input="Exit", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        window.blit(menu_text, menu_rect)
        # Places a quit button
        for button in [play_button, tutorial_button, quit_button, maker_button]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # When each button is clicked the following things will happen.
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if tutorial_button.checkForInput(menu_mouse_pos):
                    tutorial()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
                if maker_button.checkForInput(menu_mouse_pos):
                    editor()

        pygame.display.update()


time.sleep(4)
main_menu()
