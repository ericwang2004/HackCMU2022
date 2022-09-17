TILE_WIDTH = 3

class Camera:
    def __init__(self, tile_height, tile_pixel_dimensions) -> None:
        self.tile_height = tile_height
        self.tile_pixel_dimensions = tile_pixel_dimensions
        
    def get_screen_dimensions(self):
        return (TILE_WIDTH * self.tile_pixel_dimensions, self.tile_height * self.tile_pixel_dimensions)