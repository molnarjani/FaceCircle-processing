from timer import Timer


class DotPath(object):
    def __init__(self, width=None, height=None, dot_spacing=None, dot_size=None, dot_color=None, y_off=None, y=None, point_tick=None, line_tick=None, line_color=None, stroke_weight=None):
        self.width = width
        self.height = height
        self.finished = False
        
        self.dot_spacing = dot_spacing if dot_spacing is not None else random(20, 50)
        self.dot_size = dot_size if dot_size is not None else random(1, 15)
        self.dot_color = dot_color if dot_color is not None else (random(255), random(255), random(255)) 
        self.y_off = y_off if y_off is not None else random(30, 80)
        self.point_tick = point_tick if point_tick is not None else random(10, 100)
        self.line_tick = line_tick if line_tick is not None else random(20, 200)
        self.line_color = line_color if line_color is not None else random(0, 100)
        self.line_stroke_weight = stroke_weight if stroke_weight else random(1, 5)
        
        self.y = y if y is not None else random(0 + self.dot_size + self.y_off, self.height - (self.dot_size + self.y_off))
        
        self.points = [(random(self.dot_size, self.dot_size*2), random(self.y, self.y + self.y_off))]
        self.lines = []
        
        self.point_timer = Timer(tick_miliseconds=self.point_tick, callback_function=lambda: self.add_point())
        self.point_timer.start()
        
        self.line_timer = Timer(tick_miliseconds=self.line_tick, callback_function=lambda: self.add_line())

    def add_line(self):
        if len(self.lines) < len(self.points) - 2:
            self.lines.append((self.points[len(self.lines)], self.points[len(self.lines)+1]))
        else:
            self.point_timer.stop()
            self.line_timer.stop()
            self.finished = True

    def add_point(self):
        last_x = self.points[-1][0]
        if last_x > self.width:
            self.point_timer.stop()
            self.line_timer.start()
            return
    
        x = last_x + random(self.dot_size, self.dot_spacing)
        y = random(self.y, self.y + self.y_off)
        self.points.append((x, y))

    def draw(self):
        self.point_timer.step()
        self.line_timer.step()
    
        for p in self.points:
            x, y = p
            fill(*self.dot_color)
            strokeWeight(self.line_stroke_weight)
            ellipse(x, y, self.dot_size, self.dot_size)    

        for p0, p1 in self.lines:
            stroke(self.line_color)
            strokeWeight(self.line_stroke_weight)
            line(p0[0], p0[1], p1[0], p1[1])
        
