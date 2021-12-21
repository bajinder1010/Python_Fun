import random
class Player(object):
    def __init__(self, canvas, color):
        self.color = color
        self.canvas =canvas
        size = random.randint(1,100)
        x1 = random.randint(100,700)
        y1 = random.randint(100,700)
        x2 = x1+size
        y2 = y1+size
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_rectangle(self.coords)
        canvas.itemconfig(self.piece, fill=color)
    def move(self, direction):
        if direction == 'u':
             self.coords[1] -= 10
             self.coords[3] -= 10
             self.canvas.coords(self.piece, self.coords)
        if direction == 'd':
            self.coords[1] += 10
            self.coords[3] += 10 
            self.canvas.coords(self.piece, self.coords)
        if direction == 'l':
            self.coords[0] -= 10
            self.coords[2] -= 10 
            self.canvas.coords(self.piece, self.coords)
        if direction == 'r':
            self.coords[0] += 10
            self.coords[2] += 10 
            self.canvas.coords(self.piece, self.coords)