import pygame, sys
from gameintro.level import Level
from gameintro.settings import *
import gameintro.globals as globals
from gameintro.debug import debug
from gameintro.all_coordinates import params, indices
class MainGame():
    def __init__(self, number,screen, gameStateManager):
        pygame.init()
        self.number = number
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Binary Betrayal')
        globals.__init__()
        self.level = Level(params[indices[globals.SCENE]])
        self.prevScene = globals.SCENE


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            self.screen.fill('black')
            if(self.prevScene != globals.SCENE):
                self.prevScene = globals.SCENE
                self.level.remap(params[indices[globals.SCENE]])
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


# if __name__ == '__main__':
#     game = MainGame(0,0,0)
#     game.run()