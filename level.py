import pygame
from player import Player

from settings import DEFAULT_IMAGE_SIZE, TILESIZE, WORLD_MAP
from tile import Tile
from tools import import_from_csv
class Level:
    def __init__(self,params):
       
        self.display_surface = pygame.display.get_surface()
        #sprite group setup 
        self.obstacles_sprites = pygame.sprite.Group()
        self.params = params
        self.visible_sprites = YSortCameraGroup(self.params['floor'])
        self.create_map()

    def remap(self,params):
        self.display_surface = pygame.display.get_surface()
        #sprite group setup 
        self.obstacles_sprites = pygame.sprite.Group()
        self.params = params
        self.visible_sprites = YSortCameraGroup(self.params['floor'])
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary' : import_from_csv(self.params['csv_obstacles'])
        #     # 'charging_center_black'  :import_from_csv('./map/charging_center/scene10_7._black.csv'),
        #     # 'charging_center_layer'  :import_from_csv('./map/charging_center/scene10_7._layer.csv.csv'),
        #     # 'charging_center_monin'  :import_from_csv('./map/charging_center/scene10_7._monin.csv.csv')
        }
        for style,layout in layouts.items():
            
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * 64 - self.params['obstacle_offest'][0]
                        y = row_index * 64 - self.params['obstacle_offest'][1]
                        # image_surface = pygame.image.load('./graphics/grass/grass_1.png')
                        # image_surface = pygame.transform.scale(image_surface, (16*15,16*15 ) )
                        Tile((x,y), [    self.obstacles_sprites],'boundary')  
                        # Tile((x,y), [  self.obstacles_sprites],'boundary')  
        
        # #         if WORLD_MAP[i][j] == 'x':
        # #             Tile((i*TILESIZE,j*TILESIZE), [self.visible_sprites, self.obstacles_sprites])
        # #         elif WORLD_MAP[i][j] == 'p':
        # #            self.player_ini_x = i*TILESIZE
        # #            self.player_ini_y = j*TILESIZE

        # #         # elif WORLD_MAP[i][j] == ' ':
        # #         #     Grass((i*TILESIZE,j*TILESIZE), [self.visible_sprites])
        # Tile((1700, 250), [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load('./graphics/characters/all_char/research center.png').convert_alpha())
        # # 2750, 1700
        # Tile((2650, 1700), [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load('./graphics/characters/all_char/b1.png').convert_alpha())
        # #
        # Tile((2850, 2600), [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load('./graphics/characters/all_char/Server_building.png').convert_alpha())
        building_pos = []
        for i in range(len(self.params['building'])):
            building_pos.append(self.params['building'][i]['pos'])
            Tile(self.params['building'][i]['pos'], [self.visible_sprites,self.obstacles_sprites], 'building', pygame.image.load(self.params['building'][i]['image_path']).convert_alpha())
        self.player =  Player(self.params['player_coord'], [self.visible_sprites], self.obstacles_sprites, building_pos)


                

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # self.player.update()



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, floor_path):
        super().__init__()
                # get screen here from main
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        # creating the floor
        self.floor_self = pygame.image.load(floor_path)
        # self.floor_self = pygame.transform.scale(self.floor_self, (DEFAULT_IMAGE_SIZE[0]*15,DEFAULT_IMAGE_SIZE[1]*15 ))
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
        

