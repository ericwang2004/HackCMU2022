from curses import KEY_LEFT, KEY_RIGHT, KEY_UP
from player import Player
from maze import Maze
from assetManager import AssetManager
from player import Player
from pygame import Rect
import random
import pygame
from txtToMap import txtToInput
from state import State
#Where the game takes place
#Contains the player, camera, tileMap, AssetManager, etc

ASSETS = ['./asset/grass.jpeg', './asset/wood.jpeg', './asset/water.jpeg', './asset/BLACK.jpeg', './asset/BTS MAN.png']
MAP_SIZE_WIDTH = 10
MAP_SIZE_HEIGHT = 10
        
TIME_UNTIL_DEATH = 1024

class Scene(State):
    def __init__(self, camera) -> None:
        self.assetManager = AssetManager()
        #TODO DO THIS SHIT !!!!!!!!!!!!!!!!!!
        tiles, adj_list, endx, endy = txtToInput()
        print(endx, endy)
        self.maze = Maze(tiles, adj_list)
        self.player = Player(2, 2, 'n', self.maze, camera.tile_camera_height, self.assetManager, endx, endy)
        
        for asset in ASSETS:
            self.assetManager.add_asset(asset)
        self.assetManager.add_asset("./map.png")
            
        self.display_map = False
        self.cumulative_time = 0.0
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
    def render(self, display, camera):
        tiles = self.player.view()
        
        rows = len(tiles)
        cols = len(tiles[0])
        screen_size = camera.get_screen_dimensions()
        step_x = screen_size[0] / cols
        step_y = screen_size[1] / rows
        
        for y in range(rows):
            for x in range(cols):
                if (x + self.player.cy, y + self.player.cx) == (self.player.endx, self.player.endy):
                    img = pygame.transform.scale(self.assetManager.retrieve('./asset/BTS MAN.png'), (step_x, step_y))
                    display.blit(img, (step_x * x, step_y * y))
                    continue
                    
                tile = tiles[y][x]
                asset_path = ASSETS[tile]
                img = pygame.transform.scale(self.assetManager.retrieve(asset_path), (step_x, step_y))
                display.blit(img, (step_x * x, step_y * y))
                
        self.player.draw(display, (step_x, step_y))

        if self.display_map:
            img = pygame.transform.scale(self.assetManager.retrieve('./map.png'), screen_size)
            display.blit(img, (0, 0))
            
        text = self.font.render(f"{round(TIME_UNTIL_DEATH - self.cumulative_time, 2)}", False, (255, 255, 255), (0, 0, 0))
        display.blit(text, (0, 0))
            
    def input(self, event, camera):
       
        #handle input from user, pass this to the player
        if event.type == pygame.KEYDOWN:
            stuff = 0
            if event.key == pygame.K_UP:
                stuff = self.player.forward()
            elif event.key == pygame.K_LEFT:
                stuff = self.player.left()
            elif event.key == pygame.K_RIGHT:
                stuff = self.player.right()
            elif event.key == pygame.K_DOWN:
                stuff = self.player.back()
            elif event.key == pygame.K_m:
                self.display_map = not self.display_map
            
            print(stuff, self.player)  
            if stuff == -1:
                return True
        return False
            
    def update(self, delta_time, camera):
        #handle background logic
        camera.center(self.player, 10, 10)
        self.player.update(delta_time)
        
        self.cumulative_time += delta_time
        if self.cumulative_time >= TIME_UNTIL_DEATH:
            return True
        