class CircleRectangle:
    pi = 3.14
    
    def __init__(self, radius, length, breadth):
        self.radius = radius
        self.length = length
        self.breadth = breadth
        
    def circle(self):
        area = self.pi * self.radius**2
        return area
    
    def rect(self):
        rect_area = self.length*self.breadth
        perimeter = 2 * (self.length + self.breadth)
        
        return rect_area, perimeter
    
x = CircleRectangle(radius=1, length=10, breadth=10)

print(x.circle())
print(x.rect())