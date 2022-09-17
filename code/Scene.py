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

ASSETS = ['./asset/finger.jpeg', './asset/finger6.png', './asset/v bts.jpeg', './asset/bts.jpeg']
MAP_SIZE_WIDTH = 10
MAP_SIZE_HEIGHT = 10
        
class Scene:
    def __init__(self, camera) -> None:
        self.camera = camera
        self.assetManager = AssetManager()
        #TODO DO THIS SHIT !!!!!!!!!!!!!!!!!!
        self.maze = Maze([[random.randint(0, 3) for i in range(10)] for j in range(10)])
        self.player = Player(2, 2, 'n', self.maze, self.camera.tile_camera_height)
        
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
                asset_path = ASSETS[tile]
                img = pygame.transform.scale(self.assetManager.retrieve(asset_path), (step_x, step_y))
                display.blit(img, (step_x * x, step_y * y))
        
    
    def input(self, event):
        print(self.player.x, self.player.y)
        #handle input from user, pass this to the player
        if event.type == pygame.KEYDOWN:
            print("EHJEJHHEHEHEHEHEHE")
            if event.key == pygame.K_UP:
                self.player.forward()
            elif event.key == pygame.K_LEFT:
                self.player.left()
            elif event.key == pygame.K_RIGHT:
                self.player.right()
            elif event.key == pygame.K_DOWN:
                pass
            
    def update(self, delta_time):
        #handle background logic
        self.camera.center(self.player, 10, 10)
        