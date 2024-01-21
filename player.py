import pygame
from debug import debug
from settings import TILESIZE

from tools import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        # from PIL import Image
        super().__init__(groups)
        # imageinit = Image.open('')
        self.image = pygame.image.load('./graphics/characters/ALL_characters/Arjun/bbb.png').convert_alpha()
        
        self.frame_index = 0
        self.animation_speed = 0.15
        self.DEFAULT_IMAGE_SIZE = (80, 80)
 
# Scale the image to your needed size
        

        self.rect = self.image.get_rect(topleft =pos)
        # self.rect = self.rect.
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.collisions_sprites = collision_sprites
        # self.total_x = 0
        # self.total_y =0  
        self.animations = {}
        self.status = 'down'
        self.import_player_assets()

    def import_player_assets(self):
        character_path = './graphics/characters/all_char/Arjun/'
        self.animations = {
            'up' : [], 'down' : [], 'left' : [], 'right' : [],
            'right_idle' : [], 'left_idle' : [], 'up_idle': [], 'down_idle': []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)



    def movement(self):

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            self.direction.y -= 1
            self.status = 'up'
            # self.total_y -= 1
            return
        if keys_pressed[pygame.K_DOWN]:
            self.direction.y += 1
            self.status = 'down'

            # self.total_y += 1
            return
        if keys_pressed[pygame.K_LEFT]:
            self.direction.x -= 1
            self.status = 'left'
            # self.total_x -= 1
            return
        if keys_pressed[pygame.K_RIGHT]:
            # self.total_x += 1
            self.status = 'right'
            self.direction.x += 1
            return
        self.direction.x = 0
        self.direction.y = 0

    
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # print('direction ', self.direction)
        self.hitbox.x += self.direction.x * speed
        self.collision('Horizontal')
        self.hitbox.y += self.direction.y * speed
        if self.direction.y:
            print(self.hitbox.y)
            print(self.direction.y)
            print(speed)
            print('\n')
        self.collision('Vertical')
        self.rect.center = self.hitbox.center
        # print(self.rect.x, self.rect.y)

    def collision(self, type):
        if type == 'Horizontal':
            for sprite in self.collisions_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        # self.total_x += -1 * self.direction.x
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                        # self.total_x -= self.direction.x
        if type == 'Vertical':
            for sprite in self.collisions_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                        # self.total_y += -1 * self.direction.y
                    if self.direction.y > 0:
                        print('Im colliding bottom  ', self.hitbox.bottom,'  ', sprite.hitbox.top)
                        self.hitbox.bottom = sprite.hitbox.top
                        # self.total_y -= self.direction.y


    def get_status(self):

        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        #set the image 
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        
        self.rect = self.image.get_rect(center = self.hitbox.center)
        # self.rect = self.rect.inflate(-10,-10)

    def update(self):
        self.movement()
        self.get_status()
        self.animate()
        self.move(self.speed)
        debug(self.rect.center)
