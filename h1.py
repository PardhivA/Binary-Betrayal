import pygame, sys
from random import randint, uniform

# each visible object is a sprite class

class Ship(pygame.sprite.Sprite):   # we have to inherit sprite
    def __init__(self, groups):
        super().__init__(groups)
        # we need a surface, here it's called as image
        self.image = pygame.image.load('./images/ship.png').convert_alpha()
        
        self.laser_sound =  pygame.mixer.Sound("./sounds/laser.ogg")
        # we need a rect
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.mask = pygame.mask.from_surface(self.image)
        # timer
        self.can_shoot = True
        self.shoot_time = None
    
    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
    
    def laser_timer(self, duration = 500):
        if not self.can_shoot:
            cur_time = pygame.time.get_ticks();
            if(cur_time-self.shoot_time >duration):
                self.can_shoot = True
        
    def laser_shoot(self):
        if (pygame.mouse.get_pressed()[0] and self.can_shoot):
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            self.laser_sound.play()
            Laser(laser_group, self.rect.midtop)
            
    def meteor_collisions(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            pygame.quit()
            sys.exit()
            
    
    def update(self):
        self.laser_timer()
        self.laser_shoot()
        self.input_position()   
        self.meteor_collisions()
        
class Laser(pygame.sprite.Sprite): 
    def __init__(self, groups,pos):
        super().__init__(groups)
        
        self.image = pygame.image.load('./images/laser.png').convert_alpha()
        self.explosion_sound = pygame.mixer.Sound("./sounds/explosion.wav")
        self.rect = self.image.get_rect(midbottom = pos)
        self.mask = pygame.mask.from_surface(self.image)
        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 600    
        
    def meteor_collisions(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            self.kill()
            self.explosion_sound.play()
        
    def update(self):
        self.pos += self.direction*self.speed*dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.meteor_collisions()
        
        if self.rect.bottom < 0:
            self.kill()
  
class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        
        meteor_surf = pygame.image.load("./images/meteor.png").convert_alpha()
        meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * uniform(0.5, 1)
        self.scaled_surface = pygame.transform.scale(meteor_surf,meteor_size)
        self.image = self.scaled_surface
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.midtop)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(300, 600)
        
        # rotation logic
        self.rotation = 0
        self.rotation_speed = randint(20, 50)
        
    def rotate(self):
        self.rotation += self.rotation_speed* dt
        rotated_surf = pygame.transform.rotozoom(self.scaled_surface, self.rotation, 1)
        self.image = rotated_surf
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.pos += self.direction*self.speed*dt
        self.rect.midtop = (round(self.pos.x), round(self.pos.y))
        self.rotate()
        
        if self.rect.bottom > WINDOW_HEIGHT:
            self.kill()
        
class Score():
    def __init__(self):
        self.font = pygame.font.Font('./font/subatomic.ttf', 50)
        
    def display(self):
        score_text = f'Score: {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(score_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
        display_surf.blit(text_surf, text_rect)
        pygame.draw.rect(display_surf, (255, 255, 255), text_rect.inflate(30,30), width=8, border_radius=5)
        
pygame.init() 

WINDOW_WIDTH, WINDOW_HEIGHT =   1280, 720
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
clock = pygame.time.Clock()

# background
bg_surface = pygame.image.load("./images/background.png").convert()

# sprite groups
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)    
ship.update()

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500) 

score = Score()


# import sound
music = pygame.mixer.Sound("./sounds/music.wav")
music.play(loops=-1)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == meteor_timer:
            meteor_ypos = randint(-150, -50)
            meteor_xpos = randint(-100, WINDOW_WIDTH+100)
            Meteor(meteor_group, (meteor_xpos, meteor_ypos))
            
     #delta time
    dt = clock.tick() / 1000
    
    # background
    display_surf.blit(bg_surface, (0,0))
    
    # update
    spaceship_group.update()
    laser_group.update()
    meteor_group.update()
    
    # score
    score.display()
    
    # graphics
    spaceship_group.draw(display_surf)
    laser_group.draw(display_surf)
    meteor_group.draw(display_surf)
    
    # draw the frame
    pygame.display.update()