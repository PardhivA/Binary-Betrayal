import pygame

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    
    def transition(self):
         keys = pygame.key.get_pressed()
         
         if keys[pygame.K_SPACE]:
             self.gameStateManager.set_state('level')
    
    def run(self):
        self.display.fill('red')
        self.transition()
        
