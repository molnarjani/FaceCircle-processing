from face import Face

class FaceCircle:
    """ A circle of rotating faces
    
        Parameters:
            origin: PVector
            - Origin of circle
            
            diameter: <Int, Float>
            - Diameter of circle
    """
    def __init__(self, origin, diameter=600, images=None):
        self.origin = origin
        self.diameter = diameter
        self.faces = []
        self.images = images
        self.image_count = len(images)
        if images:
            self.faces.append(Face(images[0], 0, 0, circle_angle=0))
        
        self.angle = 0
        self.rotation_speed = 0.5
        self.images_added = 1
        
    def draw(self):
        if not self.faces:
            return

        if self.angle < 360 and self.angle > (degrees(2*PI)/self.image_count * self.images_added):
            self.faces.append(Face(self.images[self.images_added], 0, 0, circle_angle=0))
            self.images_added += 1
        
        for face in self.faces:
            x_off = face.w / 2
            y_off = face.h / 2
            face.x = self.origin.x + (self.diameter / 2) * cos(radians(face.circle_angle)) - x_off
            face.y = self.origin.y + (self.diameter / 2) * sin(radians(face.circle_angle)) - y_off
            face.draw()
            face.circle_angle += self.rotation_speed

        self.angle += self.rotation_speed
