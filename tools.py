from csv import reader
from os import walk

import pygame


def import_from_csv(path):
    map_list = []
    with open(path) as level_map:
        layout  = reader(level_map, delimiter = ',') # it is an array
        for row in layout:
            map_list.append(row)
    print(map_list)
    return map_list



# import_from_csv('./map/charging_center/scene10_7._black.csv')


def import_folder(path):
    surface_list = []
    # for data in walk(path):
    #     print(data)
    print(path)
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
        

# import_folder('./graphics/characters/all_char/Arjun/down')