import pygame
import sys
from main import Main
from endgame.test import EndGame
from statemanager import GameStateManager
from startfile import Start
from gameintro.main import MainGame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('scene1')
        self.states = {}

        self.create_states()

    def create_states(self):
        self.states = {
            'showdown': Main(self.screen, self.gameStateManager),
            **{f'dscene{i}': MainGame(i, self.screen, self.gameStateManager) for i in range(1, 17)},
            **{f'scene{i}': EndGame(str(i), self.screen, self.gameStateManager) for i in range(1, 17)},
        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            

if __name__ == '__main__':
    game = Game()
    game.run()
