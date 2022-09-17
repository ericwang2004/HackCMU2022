import pygame
#handles loading assets
#only loads images once for them to be used throughout the entire program during the duration of its life

class AssetManager:
    def __init__(self) -> None:
        self.assets = dict()
        pass
    
    def add_asset(self, asset_path):
        self.assets[asset_path] = pygame.image.load(asset_path)
    def retrieve(self, asset_path):
        return self.assets[asset_path]
    def contains_asset(self, asset_path):
        return self.assets.__contains__(asset_path)