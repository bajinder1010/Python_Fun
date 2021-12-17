class  Circle(object):
    def __init__(self):
        self.radius=0
    
    def change_radius(self,radius):
        self.radius=radius
    
    def get_radius(self):
        return self.radius


circle1 = Circle()
circle2 =Circle()
circle1.change_radius(5)
print(circle1.get_radius())
print(circle2.get_radius())


