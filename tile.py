import pygame

from settings import TILESIZE

class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        # self.image = pygame.image.load('./graphics/test/rock.png').convert_alpha()
        self.image = surface  
        self.DEFAULT_IMAGE_SIZE = (250, 250)
        self.sprite_type = sprite_type
        if self.sprite_type == 'building':
            self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect(topleft =pos)
        self.hitbox = self.rect.inflate(0,-10)
