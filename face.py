class Face:
    """ A rotating face
    """
    def __init__(self, img, x, y, w=100, h=100, circle_angle=0):
        self.img = img
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.rotation_degree = 0
        self.rotation_speed = 4
        self.circle_angle = circle_angle
        
    def draw(self):
        x_off = self.w / 2
        y_off = self.h / 2
        
        pushMatrix()
        translate(self.x + x_off, self.y + y_off);
        rotate(radians(self.rotation_degree))
        image(self.img, -x_off, -y_off, self.w, self.h)
        popMatrix()
        
        self.rotation_degree += self.rotation_speed
