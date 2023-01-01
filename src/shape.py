#in the name of Allah
import math

class Point:
    def __init__(self, x:float, y:float) -> None :
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, p):
        return Point(p.x + self.x, p.y + self.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    
class Shape:
    def __init__(self) -> None:
        self.vertices = []

    def add_vertex(self, p:Point) -> None:
        self.vertices.append(p)
    
    def __str__(self):
        return f"number of vertics: {len(self.vertices)}"
    
    def length(self, p1, p2):
            return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
        
    def perimeter(self) -> float:
        
        if len(self.vertices) == 0:
            raise RuntimeError
        
        perm = 0 
        for i in range(len(self.vertices)):
            if i+2 <= len(self.vertices) :
                perm += self.length(self.vertices[i], self.vertices[i+1])
            
        perm += self.length(self.vertices[0], self.vertices[-1])
        if len(self.vertices) == 2 :
            perm = perm / 2 
        return perm
    

class Line(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        Shape.__init__(self)
        self.vertices.append(p1)
        self.vertices.append(p2)
        
    def __str__(self):
        ret_str = "Line : \n"
        ret_str += f"\t p1:(x: {self.vertices[0].x}, y: {self.vertices[0].y})\n"
        ret_str += f"\t p2:(x: {self.vertices[1].x}, y: {self.vertices[1].y})\n"
        return ret_str
    
    def area(self) -> float:
        return 0

class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point) -> None:
        Shape.__init__(self)
        if (p1.x == p2.x) & (p2.x == p3.x) & (p3.x == p1.x):
            raise RuntimeError
        if (p1.y == p2.y) & (p2.y == p3.y) & (p3.y == p1.y):
            raise RuntimeError
        self.vertices.append(p1)
        self.vertices.append(p2)
        self.vertices.append(p3)

    def __str__(self):
        ret_str = "Triangle : \n"
        ret_str += f"\t p1:(x: {self.vertices[0].x}, y: {self.vertices[0].y})\n"
        ret_str += f"\t p2:(x: {self.vertices[1].x}, y: {self.vertices[1].y})\n"
        ret_str += f"\t p2:(x: {self.vertices[2].x}, y: {self.vertices[2].y})\n"
        return ret_str

    def area(self) -> float:
        s = self.perimeter()/2
        a = self.length(self.vertices[0],self.vertices[1])
        b = self.length(self.vertices[1],self.vertices[2])
        c = self.length(self.vertices[2],self.vertices[0])
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
        

class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        Shape.__init__(self)
        self.vertices.append(p1)
        self.vertices.append(Point(p1.x, p2.y))
        self.vertices.append(Point(p2.x, p1.y))
        self.vertices.append(p2)

    def __str__(self):
        ret_str = "Rectangle : \n"
        ret_str += f"\t p1:(x: {self.vertices[0].x}, y: {self.vertices[0].y})\n"
        ret_str += f"\t p2:(x: {self.vertices[1].x}, y: {self.vertices[1].y})\n"
        ret_str += f"\t p2:(x: {self.vertices[2].x}, y: {self.vertices[2].y})\n"
        ret_str += f"\t p2:(x: {self.vertices[3].x}, y: {self.vertices[3].y})\n"
        return ret_str

    def area(self) -> float:
        a = self.length(self.vertices[0], self.vertices[1])
        return a * a
    
