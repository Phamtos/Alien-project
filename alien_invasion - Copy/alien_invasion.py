import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import *
from ship import Ship
import game_functions as gf

def run_game():
    # Initiailize pygame, game, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the Play button.
    playbutton = Button(ai_settings, screen, "Play")
    highsorebutton = Button1(ai_settings, screen, "High Score")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    if stats.game_active:
        gf.create_fleet(ai_settings, screen, ship, aliens)
        
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, playbutton, highsorebutton, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, playbutton, highsorebutton)

run_game()