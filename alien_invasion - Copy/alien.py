import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    """
    alienexplosion = [pygame.image.load(f'explosionlist/explosion{n}.png') for n in range(12)]
    alien1 = [pygame.image.load(f'images/bee{n+1}.png') for n in range(4)]
    alien2 = [pygame.image.load(f'images/cat{n}.png') for n in range(4)]
    alien3 = [pygame.image.load(f'images/mushroom{n}.png') for n in range(4)]
    ufo = [pygame.image.load(f'images/poop{n+1}.png') for n in range(2)]
    """

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/bee1.png')
        #self.alienexplosion = [pygame.image.load(f'explosionlist/explosion{n}.png') for n in range(12)]
        #self.alien1 = [pygame.image.load(f'images/bee{n+1}.png') for n in range(4)]
        #self.alien2 = [pygame.image.load(f'images/cat{n}.png') for n in range(4)]
        #self.alien3 = [pygame.image.load(f'images/mushroom{n}.png') for n in range(4)]
        #self.ufo = [pygame.image.load(f'images/poop{n+1}.png') for n in range(2)]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x