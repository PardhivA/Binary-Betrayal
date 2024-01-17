import pygame, sys
from settings import *
from pytmx.util_pygame import load_pygame
from tile import Tile, CollisionTile, MovingPlatform
from player import Player
from pygame.math import Vector2 as vector
from bullet import Bullet
from enemy import Enemy
from overlay import Overlay

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
        
        # sky
        self.fg_sky = pygame.image.load('./graphics/sky/fg_sky.png').convert_alpha();
        self.bg_sky = pygame.image.load('./graphics/sky/bg_sky.png').convert_alpha();
        tmx_map = load_pygame('./data/map.tmx')
        
        self.sky_width = self.fg_sky.get_width()
        self.padding = WINDOW_WIDTH/2
        map_width = tmx_map.tilewidth * tmx_map.width + (2*self.padding)
        self.sky_num = map_width // self.sky_width
        
        
        
    def custom_draw(self, player):
        # CAMERA
        # change the offset vector (so that player is always at the center of the window)
        self.offset.x = player.rect.centerx - WINDOW_WIDTH/2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT/2
        
        for x in range (int(self.sky_num)):
           x_pos = -self.padding + (x * self.sky_width) 
           self.display_surface.blit(self.bg_sky,( x_pos - self.offset.x/2.5,  850 - self.offset.y/2.5 ))
           self.display_surface.blit(self.fg_sky,( x_pos - self.offset.x/2,  850 - self.offset.y/2))
        
        # blit all sprites (give appropriate z and sort , then blit them)
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.z):
            offset_rect = sprite.image.get_rect(center = sprite.rect.center)
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
            
        

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Binary Betrayal")
        self.clock = pygame.time.Clock()
        
        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.platforms_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.vulnerable_sprites = pygame.sprite.Group()
        
        self.setup()
        self.overlay = Overlay(self.player)
        
        # bullet images
        self.bullet_surf = pygame.image.load('./graphics/bullet.png').convert_alpha()
        
        # music
        self.music = pygame.mixer.Sound('./sounds/whoisthevillain.wav')
        self.music.set_volume(0.2 )
        self.music.play(loops = -1)        
    
    def setup(self):
        tmx_map = load_pygame('./data/map.tmx') 
        #  but we have x,y,suf, and not the sprite, so we need to create now
        
        # tiles
        for x, y, surf in tmx_map.get_layer_by_name('Level').tiles():
            CollisionTile((x*64,y*64), surf, [self.all_sprites, self.collision_sprites])
            
        # 4 more layers we need to import, bg, bg detail, f detail btm, fg detail top
        for layer in ['BG', 'BG Detail', 'FG Detail Bottom', 'FG Detail Top']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Tile((x*64,y*64), surf, self.all_sprites, LAYERS[layer])
        
        
        # objects
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name ==  'Player':
                self.player = Player(
                    pos = (obj.x, obj.y), 
                    groups =[self.all_sprites, self.vulnerable_sprites], 
                    path = './graphics/player', 
                    collision_sprites = self.collision_sprites, 
                    shoot = self.shoot)
            if obj.name == 'Enemy':
                Enemy(
                    pos = (obj.x, obj.y), 
                    path = './graphics/enemy', 
                    groups = [self.all_sprites, self.vulnerable_sprites],
                    shoot = self.shoot, 
                    player = self.player, 
                    collision_sprites = self.collision_sprites)
        
        self.platform_border_rects = []
        for obj in tmx_map.get_layer_by_name('Platforms'):
            if obj.name == 'Platform':
                MovingPlatform((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.platforms_sprites])
            else:
                border_rect = pygame.Rect(obj.x,obj.y,obj.width, obj.height)
                self.platform_border_rects.append(border_rect)
                
    def shoot(self, pos, direction, entity):
        Bullet(pos, self.bullet_surf, direction, [self.all_sprites, self.bullet_sprites])
        
    def bullet_collision(self):
        # obstacles 
        for obj in self.collision_sprites.sprites():
            pygame.sprite.spritecollide(obj, self.bullet_sprites, True) 
            # this destroys all bulltes in the bullte spries if it collides with any of the objtacles
        
        # entity collision
        for sprite in self.vulnerable_sprites.sprites():
            if pygame.sprite.spritecollide(sprite, self.bullet_sprites, True, pygame.sprite.collide_mask):
                sprite.damage()                    
                
    def platform_collision(self):
        for platform in self.platforms_sprites.sprites():
            for border in self.platform_border_rects:
                # bounce the platforms
                #  if platform is moving up, place the top in btm and change the dir
                if platform.rect.colliderect(border):
                    if platform.direction.y < 0 : # up
                        platform.rect.top = border.bottom
                        platform.pos.y = platform.rect.y
                        platform.direction.y = 1
                    else:
                        platform.rect.bottom = border.top
                        platform.pos.y = platform.rect.y
                        platform.direction.y = -1
                if platform.rect.colliderect(self.player.rect) and self.player.rect.centery > platform.rect.centery :
                    platform.rect.bottom = self.player.rect.top
                    platform.pos.y = platform.rect.y
                    platform.direction.y = -1
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.display_surface.fill((249, 131, 103))
            
            self.platform_collision()
            self.all_sprites.update(dt)
            self.bullet_collision()
            # self.all_sprites.draw(self.display_surface)
            #
            self.all_sprites.custom_draw(self.player)
            self.overlay.display()
            pygame.display.update()
        
if __name__ ==  '__main__':
    main = Main()
    main.run()