EMPTY = 0 
WALL = 1
MAGIC = 2

#WHITE BLACK RED
COLORS = [(255, 255, 255), (0, 0, 0), (255, 0, 0)]

class Editor:
    def __init__(self, rows, cols) -> None:
        self.map = [[] * cols] * rows
        self.rows = rows
        self.cols = cols
        
    def input(self, event):
        pass
    
    def render(self, width, height):
        step_x = width / self.cols
        step_y = height / self.rows
        pass