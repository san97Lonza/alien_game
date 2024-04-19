import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):

        #the below method will initialize the background settings that pygame need to work properly
        pygame.init()

        self.settings = Settings()

        #to a diaplay window and assign it to a attribute so that the display will be available to all the methods
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invadion")
        self.ship = Ship(self)
    
    def run_game(self):
        while True:

            #for loop will check for a list of events that have happen and perform tasks depending on the kinds of events that occur
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #this pygame.display.flip() will update the latest changes to the screen
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()