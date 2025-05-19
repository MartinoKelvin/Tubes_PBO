import pygame, sys
from setting import *
from level import Level

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

pygame.mixer.music.load("asset/music.mp3")
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  
    level.run()  
            
    pygame.display.update() 
    clock.tick(60) 