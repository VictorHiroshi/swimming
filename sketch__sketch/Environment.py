from Creature import Creature
class Environment(object):
    def __init__(self, background_color, setup):
        self.bg_color = background_color
        self._setup = setup
        creature_pos = PVector(setup['screen_width'] / 2, setup['screen_height'] / 2)
        self.creature = Creature(creature_pos)
    
    def update(self):
        if self._setup["rendering"]:
            self.draw()
    
    def draw(self):
        background(self.bg_color["r"], self.bg_color["g"], self.bg_color["b"])
        self.creature.draw()
        stroke(255, 255, 100)
        strokeWeight(2)
        ellipse(self._setup['screen_width'] / 2, self._setup['screen_height'] / 2, 3, 3)
