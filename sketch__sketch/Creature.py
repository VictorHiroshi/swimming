from Rig import Rig

class Creature(object):
    def __init__(self, initial_position):
        self.position = initial_position
        self.generate_rigs()
    
    def generate_rigs(self):
        self.root = Rig(50, head_vertex=self.position)
        self.tail = Rig(30, direction=PVector(1, 1).normalize())
        self.root.set_bending_angle(-120)
        self.root.set_child(self.tail)
    
    def draw(self):
        self.root.draw()
        self.tail.draw()
        
        
