
import pygame
from pygame.locals import *
import sys
from editor import Editor

TILE__HEIGHT_CAMERA = 5
TILE_PIXEL_DIMENSIONS = 100
FPS = 60

SAVE_PATH = './map.txt'

WIDTH = 500
HEIGHT = 500
editor = Editor(5, 5, WIDTH, HEIGHT)

#setup pygame
pygame.init()
clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💀💀")
pygame.display.flip()

#gameLoop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            editor.save(SAVE_PATH)
            sys.exit()
   
        #HANDLE KEY, MOUSE INPUT  
        editor.input(event)
     
    #FILL COLOR
    displaysurface.fill((0,0,0))
    #UPDATE THE GAME HERE
    editor.render(displaysurface)
    
    pygame.display.update()
    clock.tick(FPS)
    