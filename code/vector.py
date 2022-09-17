
class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def add(self, other):
         self.x += other.x
         self.y += other.y
         
    def add_new(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def sub(self, other):
         self.x -= other.x
         self.y -= other.y
         
    def sub_new(self, other):
          return Vector(self.x - other.x, self.y - other.y)
    
    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar
        
    def mult_new(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def int_clamp(self):
        self.x = int(self.x)
        self.y = int(self.y)