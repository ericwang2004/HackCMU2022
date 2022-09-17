import pygame 
#handles loading assets
#only loads images once for them to be used throughout the entire program during the duration of its life

class AssetManager:
    def __init__(self) -> None:
        self.assets = dict()
        pass
    
    def add_image(self, path, asset_name):
        self.assets[asset_name] = pygame.image.load(path)
    
    def retrieve(self, asset_name):
        return self.assets[asset_name]
    
    def contains_asset(self, asset_name):
        return self.assets.__contains__(asset_name)