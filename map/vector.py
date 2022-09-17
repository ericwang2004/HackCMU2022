
from cmath import sqrt


class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def add(self, other):
         self.x += other.x
         self.y += other.y
         self.z += other.z
         
    def add_new(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def sub(self, other):
         self.x -= other.x
         self.y -= other.y
         self.z -= other.z
         
    def sub_new(self, other):
          return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        
    def mult_new(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def int_clamp(self):
        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)
        
    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        
    def normalize(self):
        mag = self.mag()
        if mag == 0: return 0
        
        self.x /= mag
        self.y /= mag
        self.z /= mag
        
    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.x * other.z - self.z * other.x, self.x * other.y - self.y * other.x)
        