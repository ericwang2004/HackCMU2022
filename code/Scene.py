from player import Player
from maze import Maze
from assetManager import AssetManager
#Where the game takes place
#Contains the player, camera, tileMap, AssetManager, etc

class Scene:
    def __init__(self, camera) -> None:
        self.player = Player()
        self.camera = camera
        self.assetManager = AssetManager()
        #TODO DO THIS SHIT !!!!!!!!!!!!!!!!!!
        self.maze = Maze()
        
    def render(self, display):
        pass
    
    def input(self):
        #handle input from user, pass this to the player
        pass
    def update(self):
        #handle background logic
        self.camera.center(self.player)
        pass