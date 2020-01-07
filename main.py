import sys

import pygame

from settings import Settings

def run_game():
    # Initialize Game Screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space Invader")

    # Set the background color:
    bg_color = (250, 0, 0)

    # Start Game Loop

    while True:

        # What for mouse keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()


