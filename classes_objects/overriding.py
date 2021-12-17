class Fraction(object):
    def __init__(self,top,bottom):
        self.top=top
        self.bottom=bottom
    def __add__(self,other_fraction):
        new_top = self.top*other_fraction.bottom+self.bottom*other_fraction.top
        new_bottom = self.bottom*other_fraction.bottom
        return Fraction(new_top,new_bottom)
    def __mul__(self,other_fraction):
        new_top= self.top*other_fraction.top
        new_bottom= self.bottom*other_fraction.bottom
        return Fraction(new_top,new_bottom)
    def __sub__(self,other_fraction):
        new_top = self.top*other_fraction.bottom-self.bottom*other_fraction.top
        new_bottom = self.bottom*other_fraction.bottom
        return Fraction(new_top,new_bottom)
    def __str__(self):
        return str(self.top)+"/"+str(self.bottom)

half = Fraction(1,2)
print(half)
quarter= Fraction(1,4)
print(half+quarter)