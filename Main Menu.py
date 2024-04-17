import pygame
import sys
from button import Button
import time

pygame.init()
window = pygame.display.set_mode((1280, 1022))  # Creates game
# window. screen = window
pygame.display.set_caption("Pizza Pursuit: Chef's Revenge")

bg = pygame.image.load("data/images/bg.png")  # Menu background.
ss = pygame.image.load("data/Pizza.png")  # Splash Screen.

def get_font(size):
    return pygame.font.Font("data/PixelatedPusab.ttf", size)

# Takes the font file I provided, and allows utilization of the fonts for
# the menu screen.
window.fill('white')

window.blit(ss, (0, 0))  # Places background photo.
pygame.display.update()
time.sleep(4)

def play():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()  # Takes mouse position

        window.fill('black')

        play_text = get_font(45).render("Play ", True, "White")
        play_rect = play_text.get_rect(center=(640, 260))
        window.blit(play_text, play_rect)  # Creates the play button.

        play_back = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75),
                           base_color="White", hovering_color="Green")

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
        options_mouse_pos = pygame.mouse.get_pos()  # Takes mouse position

        window.fill(
            'white')  # Creates the illusion of multiple screens by filling screen with black

        options_text = get_font(45).render("Options.", True, "Black")
        options_rect = options_text.get_rect(center=(640, 260))
        window.blit(options_text,
                    options_rect)  # When options is pressed shows the word options.

        options_back = Button(image=None, pos=(640, 460), text_input="Back",
                              # Creates the back button when options is pressed
                              font=get_font(75), base_color="Black",
                              hovering_color="Green")

        options_back.changeColor(
            options_mouse_pos)  # Changes button colour if hovering over back button.
        options_back.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:

        window.fill('black')

        window.blit(bg, (0, 0))  # Places background photo.

        menu_mouse_pos = pygame.mouse.get_pos()  # Tracks mouse position.

        menu_text = get_font(75).render('Pizza Pursuit', True, "#ffffff")
        menu_rect = menu_text.get_rect(
            center=(640, 100))  # SHows the Title of the game.

        play_button = Button(image=pygame.image.load("data/Play Rect.png"),
                             pos=(640, 250),
                             text_input="Play", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        # Creates a play button
        options_button = Button(
            image=pygame.image.load("data/Options Rect.png"), pos=(640, 400),
            text_input="Tutorial", font=get_font(75), base_color="#d7fcd4",
            hovering_color="White")
        # Places an options button.
        quit_button = Button(image=pygame.image.load("data/Quit Rect.png"),
                             pos=(640, 920),
                             text_input="Exit", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        window.blit(menu_text, menu_rect)
        # Places a quit button
        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # When each button is clicked the following things will happen.
                if play_button.checkForInput(menu_mouse_pos):
                    from game import Game
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()