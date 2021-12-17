class Door(object):
    def __init__(self):
        self.width=1
        self.height=1
        self.open = False
    

    def is_open(self):
        return self.open

    def door_area(self):
        area = self.height*self.width
        return area

    