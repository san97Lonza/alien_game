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
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invadion")
        self.ship = Ship(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    #these helper method are created to help simplify the tasks
    #for example: _check_events() will help manage events
    #while _update_screen() will handle the updating of screen with the latest updates

    def _check_events(self):
        #for loop will check for a list of events that have happen and perform tasks depending on the kinds of events that occur
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                #these confitional statements check for right or left key when a key is pressed and update the ship movement falg accordingly
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                
                #these confitional statements check for right or left key when a key is realsed and update the ship movement falg accordingly
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    #Refractoring the event checker for right and left keys when they are pressed or realeased
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #quits the game when q is pressed
        elif event.key == pygame.K_q:
            sys.exit()

    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #this pygame.display.flip() will update the latest changes to the screen
        pygame.display.flip()
         
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()