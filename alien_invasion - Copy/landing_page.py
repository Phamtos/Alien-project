from multiprocessing.context import SpawnContext
import sys
import pygame

from bullet import Bullet
from alien import Alien
from vector import Vector
from button import Button

WHITE = (0, 0, 0)
GREEN = (0, 255, 0)

class LandingPage:

    alien_one_imgs = [pygame.image.load(f'images/bee{n+1}.png') for n in range(2)]
    alien_two_imgs = [pygame.image.load(f'images/cat{n+1}.png') for n in range(2)]
    alien_three_imgs = [pygame.image.load(f'images/mushroom{n+1}.png') for n in range(2)]
    ufo_imgs = [pygame.image.load(f'images/poop{n+1}.png') for n in range(2)]

    """A class to create the landing page of the game."""
    def __init__(self, ai_settings, screen):
        """Initialize some attributes of the landing page."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.font = pygame.font.SysFont(None, 190)

    def Lpage(self, screen):
        # Keep the screen black for landing page
        screen.fill(self.ai_settings.lp_color)

    def title(self):
        """Turn the Title into a rendered image."""
        self.titleLine1 = self.font.render("ALIEN", True, WHITE, self.ai_settings.lp_color)
        self.titleLine2 = self.font.render("INVASION", True, GREEN, self.ai_settings.lp_color)

        # Diplay the Title in the center top of the screen.
        self.title1_rect = self.titleLine1.get_rect()
        self.title1_rect.centerx = self.screen_rect.centerx
        self.title1_rect.top = self.screen_rect.top - 100
        
        # Position the second half of the title below the first half
        self.title2_rect = self.titleLine2.get_rect()
        self.title2_rect.centerx = self.screen_rect.centerx
        self.title2_rect.top = self.title1_rect.bottom

    def aliensscoring():
        pass