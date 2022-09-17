
import pygame
from pygame.locals import *
import sys
from camera import Camera
from Scene import Scene
import time
 

#define constants and camera
TILE__HEIGHT_CAMERA = 10
TILE_PIXEL_DIMENSIONS = 75
FPS = 15

#create the camera
camera = Camera(TILE__HEIGHT_CAMERA, TILE__HEIGHT_CAMERA, TILE_PIXEL_DIMENSIONS, 0, 0)
#create the scene
scene = Scene(camera)

#setup pygame
pygame.init()
clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode(camera.get_screen_dimensions())
pygame.display.set_caption("💀💀")
pygame.display.flip()

now = 0
after = time.time()
#gameLoop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
          
        #HANDLE KEY, MOUSE INPUT  
        scene.input(event)
    

    #FILL COLOR
    displaysurface.fill((0,0,0))
    
    #UPDATE THE GAME HERE
    now = time.time()
    delta = now - after
    after = time.time()
    scene.update(delta)
    
    #RENDER HERE
    scene.render(displaysurface)
    
    pygame.display.update()
    clock.tick(FPS)
    