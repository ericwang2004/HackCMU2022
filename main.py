
import pygame
from pygame.locals import *
import sys
from camera import Camera
 

#define constants and camera
TILE__HEIGHT_CAMERA = 5
TILE_PIXEL_DIMENSIONS = 100
FPS = 15
camera = Camera(TILE__HEIGHT_CAMERA, TILE_PIXEL_DIMENSIONS)

#setup pygame
pygame.init()
clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode(camera.get_screen_dimensions())
pygame.display.set_caption("💀💀")
pygame.display.flip()

#gameLoop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
          
        #HANDLE KEY, MOUSE INPUT  
     
    #FILL COLOR
    displaysurface.fill((0,0,0))
    #UPDATE THE GAME HERE
    #RENDER HERE
    
    pygame.display.update()
    clock.tick(FPS)
    