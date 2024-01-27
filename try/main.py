import pygame, sys
from main import Main 

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen,self.gameStateManager)
        self.level = Main(self.screen,self.gameStateManager)
        
        self.states = {'start': self.start, 'level':self.level}
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.gameStateManager.get_state()].run()
            
            pygame.display.update()
            
class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    
    def run(self):
        self.display.fill('blue')

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
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        
    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState = state
    
            
if __name__ == '__main__':
    game = Game()
    game.run()