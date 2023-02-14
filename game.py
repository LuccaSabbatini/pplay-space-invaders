# Imports
import sys
import pygame
import src.screens.MainMenu
from screeninfo import get_monitors
from pygame.locals import *
from src.pplay.window import Window


# Initializes pygame's modules
pygame.init()
clock = pygame.time.Clock()

# Get Primary Monitor


def get_primary_monitor():
    for monitor in get_monitors():
        if monitor.is_primary:
            return monitor

    return None


# Game Window Initialization
primary_monitor = get_primary_monitor()
game_window = Window(primary_monitor.width, primary_monitor.height)
game_window.set_title("Space Invaders")
game_window.game_difficulty = 3
game_window.game_over = False
game_window.ranking = []

# Controls Initialization
keyboard = game_window.get_keyboard()
mouse = game_window.get_mouse()
RIGHT_CLICKING = False

# Initialize Screen
current_screen = src.screens.MainMenu.MainMenu(game_window, mouse, keyboard)

# Game Loop
while game_window:
    # Clean Background
    game_window.set_background_color((0, 0, 0))

    # Current Screen Game Loop
    current_screen.loop(RIGHT_CLICKING)

    # Get Next Screen
    current_screen = current_screen.screen

    # Resets variable that sees if mouse is right clicking
    RIGHT_CLICKING = False

    # Events Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                RIGHT_CLICKING = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                RIGHT_CLICKING = False

    # Update Window
    game_window.update()
    clock.tick(60)
