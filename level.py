import pygame
from player import Player

from settings import TILESIZE, WORLD_MAP
from tile import Tile
from tools import import_from_csv
class Level:
    def __init__(self):
       
        self.display_surface = pygame.display.get_surface()
        #sprite group setup 
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()


    def create_map(self):
        layouts = {
            'boundary' : import_from_csv('./map/map_FloorBlocks.csv')
            # 'charging_center_black'  :import_from_csv('./map/charging_center/scene10_7._black.csv'),
            # 'charging_center_layer'  :import_from_csv('./map/charging_center/scene10_7._layer.csv.csv'),
            # 'charging_center_monin'  :import_from_csv('./map/charging_center/scene10_7._monin.csv.csv')
        }
        for style,layout in layouts.items():
            
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        Tile((x,y), [ self.obstacles_sprites],'boundary')  
        
        #         if WORLD_MAP[i][j] == 'x':
        #             Tile((i*TILESIZE,j*TILESIZE), [self.visible_sprites, self.obstacles_sprites])
        #         elif WORLD_MAP[i][j] == 'p':
        #            self.player_ini_x = i*TILESIZE
        #            self.player_ini_y = j*TILESIZE

        #         # elif WORLD_MAP[i][j] == ' ':
        #         #     Grass((i*TILESIZE,j*TILESIZE), [self.visible_sprites])
        Tile((1700, 250), [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load('./graphics/characters/all_char/research center.png').convert_alpha())
        # 2750, 1700
        Tile((2650, 1700), [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load('./graphics/characters/all_char/b1.png').convert_alpha())
        #
        Tile((2850, 2600), [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load('./graphics/characters/all_char/Server_building.png').convert_alpha())

        self.player =  Player((2000,1430), [self.visible_sprites], self.obstacles_sprites)
                

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # self.player.update()



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
                # get screen here from main
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        # creating the floor
        self.floor_self = pygame.image.load('./graphics/tilemap/ground.png')
        self.floor_rect=  self.floor_self.get_rect(topleft = (0,0))

    # def custom_draw(self,player,player_ini_x,player_ini_y):
    def custom_draw(self,player):
        # self.offset.x = player.rect.centerx - 
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width 
        self.offset.y = player.rect.centery - self.half_height
        
        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_self, floor_offset_pos)

        for sprite in sorted(self.sprites(), key= lambda sprite : sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset 

            self.display_surface.blit(sprite.image, offset_pos)
        

