import pygame
from pygame.math import Vector2 as vector
from settings import *
from os import walk
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, path, groups, shoot):
        super().__init__(groups)
        self.import_assets(path)
        self.frame_index = 0
        self.status = 'right'
        
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.z = LAYERS['Level']
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = 400
        self.duck = False
        self.old_rect = self.rect.copy()
        
        # interaction
        self.shoot = shoot
        self.can_shoot = True
        self.shoot_time = None
        self.cooldown = 100
        
        self.health = 3 
        self.is_vulnerable= True
        self.hit_time = None
        self.invul_duration = 400
        
        # audio
        self.hit_sound = pygame.mixer.Sound('./sounds/hit.wav')
        self.hit_sound.set_volume(0.2)
        self.shoot_sound =  pygame.mixer.Sound('./sounds/bullet.wav')
        self.shoot_sound.set_volume(0.2)
        
    def blink(self):
        if not self.is_vulnerable:
            if self.wave_value:
                mask = pygame.mask.from_surface(self.image)
                white_surf = mask.to_surface()
                white_surf.set_colorkey((0,0,0))
                self.image = white_surf
    
    def wave_value(self):
        val = sin(pygame.time.get_ticks())
        if val >=0 :
            return True
        return False
        
    def damage(self):
        if self.is_vulnerable:
            self.is_vulnerable = False
            self.health -= 1;
            self.hit_time = pygame.time.get_ticks()
            self.hit_sound.play()
        
    def invul_timer(self):
        if not self.is_vulnerable:
            cur = pygame.time.get_ticks()
            if cur - self.hit_time > self.invul_duration:
                self.is_vulnerable = True
    
    def check_death(self):
        if self.health <= 0:
            self.kill()
        
    def shoot_timer(self):
        if not self.can_shoot:
            cur = pygame.time.get_ticks()
            if cur-self.shoot_time > self.cooldown:
                self.can_shoot = True   
        
    def import_assets(self, path):
        self.animations = {}
        for index, folder in enumerate(walk(path)):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in sorted(folder[2], key=lambda string: int(string.split('.')[0])):
                    path = folder[0].replace('\\', '/') + '/' + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split('\\')[1]
                    self.animations[key].append(surf)
                    
    
    def animate(self, dt):
        self.frame_index += 7*dt
        if int(self.frame_index) >= len(self.animations[self.status]):
            self.frame_index = 0
            
        self.image = self.animations[self.status][int(self.frame_index)]
        self.mask = pygame.mask.from_surface(self.image)