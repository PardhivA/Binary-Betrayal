import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('code/gameintro/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft =pos)