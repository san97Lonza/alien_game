import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #store decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #Using the movement flag to update the ships's movement
        #using multipe if statemets to check for when both keys are pressed down together
        #updating the ship's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.rect.x -=1
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)