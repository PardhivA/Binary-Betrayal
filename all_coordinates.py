indices = ['world_map', 'sanjayroom', 'arjun_room', 'arjun_office', 'sanjay_room2', 'sanjay_lab', 'charging_center', 'main_server', 'moni_room', 'research_interval', 'old_server_room','research_entry']

params  = {'world_map' : {
    'floor' : './graphics/tilemap/ground.png',
    'csv_obstacles' : './map/map_FloorBlocks.csv',
    'obstacle_offest' : (0,0),
    'player_coord'  : (2000,1430),
    'building' : [{'image_path' : './graphics/characters/all_char/research center.png', 'pos' : (1800, 400)}, {'image_path' : './graphics/characters/all_char/b1.png', 'pos' : (2800, 1900)}, {'image_path' : './graphics/characters/all_char/Server_building.png', 'pos' : (2950, 2800)}, {'image_path' : './graphics/characters/all_char/viraj_house_4.png', 'pos' : (900, 500)},{'image_path' : './graphics/characters/all_char/moni_house.png', 'pos' : (590, 1725)},{'image_path' : './graphics/characters/all_char/sanjay_house.png', 'pos' : (1300, 2500)} , {'image_path' : './graphics/characters/all_char/old_server.png', 'pos' : (2400, 2800)}, {'image_path' : './graphics/characters/all_char/moni_server.png', 'pos' : (2600, 1100)}, {'image_path' : './graphics/characters/all_char/random_house_1.png', 'pos' : (1600, 1800)}]
},
 'sanjayroom' : {
     'floor' : './map/places/new_places/sanjayhome1280.png',
     'csv_obstacles' :  './map/places/new_places/sanjayhome1280_obstacle.csv',
    'obstacle_offest' : (30,50),
    'player_coord' : (1000,400),
    'building' : []
 },
 'arjun_room' : {
     'floor' : './map/places/new_places/arjunhouse.png',
     'csv_obstacles' :  './map/places/new_places/arjunroom_ob.csv',
    'obstacle_offest' : (250,0),
    'player_coord' : (300,300),
    'building' : []
 },
 'arjun_office' : {
     'floor' : './map/places/new_places/arjunoffice.png',
     'csv_obstacles' :  './map/places/new_places/arjunoffice_OB.csv',
    'obstacle_offest' : (350,0),
    'player_coord' : (300,300),
    'building' : []
 },
 'sanjay_room2' : {
     'floor' : './map/places/new_places/sanjayhome2.png',
     'csv_obstacles' :  './map/places/new_places/sanjayroom2_ob.csv',
    'obstacle_offest' : (50,50),
    'player_coord' : (300,300),
    'building' : []
 },
 'sanjay_lab' : {
     'floor' : './map/places/new_places/sanjaylab.png',
     'csv_obstacles' :  './map/places/new_places/sanjaylab_ob.csv',
    'obstacle_offest' : (100,50),
    'player_coord' : (300,300),
    'building' : []
 },
 'charging_center' : {
     'floor' : './map/places/new_places/chargingcenter.png',
     'csv_obstacles' :  './map/places/new_places/charginccenter_ob.csv',
    'obstacle_offest' : (125,50),
    'player_coord' : (300,300),
    'building' : []
 },
 'main_server' : {
     'floor' : './map/places/new_places/mainserver.png',
     'csv_obstacles' :  './map/places/new_places/Mainserver_ob.csv',
    'obstacle_offest' : (200,0),
    'player_coord' : (300,500),
    'building' : []
 },
 'moni_room' : {
     'floor' : './map/places/new_places/moniroom.png',
     'csv_obstacles' :  './map/places/new_places/moniroom_ob.csv',
    'obstacle_offest' : (100,50),
    'player_coord' : (300,500),
    'building' : []
 },
 'research_interval' : {
     'floor' : './map/places/new_places/researchinterval.png',
     'csv_obstacles' :  './map/places/new_places/researchinterval_ob.csv',
    'obstacle_offest' : (225,50),
    'player_coord' : (300,500),
    'building' : []
 },
 'oldserver_room' : {
     'floor' : './map/places/new_places/oldserverroom.png',
     'csv_obstacles' :  './map/places/new_places/oldserverroom_obstacle.csv',
    'obstacle_offest' : (200,0),
    'player_coord' : (300,500),
    'building' : []
 },
 'research_entry' : {
     'floor' : './map/places/new_places/researchentry.png',
     'csv_obstacles' :  './map/places/new_places/Reasearchentry_OB.csv',
    'obstacle_offest' : (225,75),
    'player_coord' : (300,500),
    'building' : []
 }
}