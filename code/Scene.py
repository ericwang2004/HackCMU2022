from curses import KEY_LEFT, KEY_RIGHT, KEY_UP
from player import Player
from maze import Maze
from assetManager import AssetManager
from player import Player
from pygame import Rect
import random
import pygame
#Where the game takes place
#Contains the player, camera, tileMap, AssetManager, etc

ASSETS = ['../asset/finger.jpeg', '../asset/finger.jpeg', '../asset/finger.jpeg']
MAP_SIZE_WIDTH = 10
MAP_SIZE_HEIGHT = 10
        
class Scene:
    def __init__(self, camera) -> None:
        self.camera = camera
        self.assetManager = AssetManager()
        #TODO DO THIS SHIT !!!!!!!!!!!!!!!!!!
        self.maze = Maze([[random.randint(0, 3) for i in range(10)] for j in range(10)])
        self.player = Player(1, 1, 'n', self.maze, self.camera)
        
        for asset in ASSETS:
            self.assetManager.add_asset(asset)
    def render(self, display):
        tiles = self.player.view()
        
        rows = len(tiles)
        cols = len(tiles[0])
        screen_size = self.camera.get_screen_dimensions()
        step_x = screen_size[0] / cols
        step_y = screen_size[1] / rows
        
        for y in range(rows):
            for x in range(cols):
                tile = tiles[y][x]
                asset_path = tile.get_typ()
                display.blit(self.asset_manager.retrieve(asset_path), (step_x * x, step_y * y), 
                             area=Rect(step_x * x, step_y * y, step_x, step_y))
        
    
    def input(self, event):
        #handle input from user, pass this to the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.player.forward()
            elif event.key == pygame.KEY_LEFT:
                self.player.left()
            elif event.key == pygame.KEY_RIGHT:
                self.player.right()
            elif event.key == pygame.KEY_UP:
                pass
            
    def update(self, delta_time):
        #handle background logic
        self.camera.center(self.player)
        pass