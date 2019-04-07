class Rig(object):
    def __init__(self, lenght, bending_speed=1, elastic_speed=1, head_vertex=None, direction=PVector(0,1)):
        ''' Class to represent and simulate a rig.
        :param lenght: constant size of the rig, even when bended.
        :param bending_speed: How fast the rig can bend.
        :param elastic_speed: How fast the rig returns to straight position once no bending force applied.
        :param head_vertex: initial position of the head.
        :param direction: Vector representing initial orientation in 2d plane
        '''
        self.head_vertex = head_vertex
        self.lenght = lenght
        self.bending_speed = constrain(bending_speed, 0, 1)
        self.elastic_speed = constrain(elastic_speed, 0, 1)
        self._direction = direction
        self._bending_angle = radians(0) # radians
        self._parent = None
        self._child = None
    
    def get_tail_coord(self):
        dev_angle = (PI - self._bending_angle) / 2 - HALF_PI
        aux_vect = self._direction.copy().rotate(dev_angle)
        mid_point = self.head_vertex - (aux_vect * self.lenght / 2)
        aux_vect = self._direction.copy().rotate(-1 * dev_angle)
        tail_point = mid_point - (aux_vect * self.lenght / 2)
        return tail_point, mid_point
        
    def set_parent(self, rig):
        self._parent = rig
        self.head_vertex, mid_point = rig.get_tail_coord()
    
    def set_child(self, rig):
        ''' Assign rig as own child and self as parent'''
        self._child = rig
        rig.set_parent(self)
    
    def draw(self):
        tail_point, mid_point = self.get_tail_coord()

        strokeWeight(4)
        stroke(150, 10, 150)
        line(self.head_vertex.x, self.head_vertex.y, mid_point.x, mid_point.y)
        line(mid_point.x, mid_point.y, tail_point.x, tail_point.y)
        stroke(255, 10, 10)
        strokeWeight(1)
        ellipse(mid_point.x, mid_point.y, 5, 5)

    def bend(self, force, delta_time):
        ''' bend from 0 to 100% of bending_speed in the direction defined by the sign(+/-)'''
        # force = constrain(force, -1, 1)
        pass
    
    def set_bending_angle(self, deg_angle):
        self._bending_angle = radians(deg_angle)
    
    def apply_force(self, vector, delta_time):
        ''' The function called by a rig in it's children to make them follow it's movement'''
        pass
    
    def propel(self, vector, delta_time):
        ''' After applying all forces, accumulate the resulting force for each parent until reaching the root, which will move and update the children heads'''
        pass
    
    def update_head(self, new_point):
        pass
