import pygame, sys
from level import Level
from settings import *
import globals
from debug import debug
from all_coordinates import params, indices
class Game():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
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


if __name__ == '__main__':
    game = Game()
    game.run()