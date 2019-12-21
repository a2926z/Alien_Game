import pygame

class Adonis:
    """A class to manage the image."""
    def __init__(self, bs_game):
        """Initialize the image and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the image and get its rect.
        self.image = pygame.image.load('images/adonis.bmp')
        self.rect = self.image.get_rect()
        # Start each image at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)