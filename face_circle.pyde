import subprocess

import sys
from os import environ, listdir, getcwd
from os.path import isfile, join
  
from circle import FaceCircle
from dot_path import DotPath


dotpaths = []


img = None


face_circle = None

def setup():
    global face_circle, img, dotpaths
    size(800, 600, P2D)
    fill(73, 54, 87)
    origin = PVector(width/2, height/8 * 6)
    faces = []
    colleagues = listdir('images')
    meeting_number_choice = environ.get('MEETING_NUMBER_CHOICE', '0')
    process = subprocess.Popen(['bash', 'scripts/get_meeting_attendees.sh', meeting_number_choice],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    next_meeting_colls = stdout.decode('utf-8').strip().strip('][').split(', ')
    next_meeting_colls = [c.strip("'") for c in next_meeting_colls]
    print(next_meeting_colls)
    valid_colls = list(filter(lambda c: c+'.png' in colleagues, next_meeting_colls))
    for face in valid_colls:
        faces.append(loadImage('images/'+face+'.png'))
    
    face_circle = FaceCircle(origin, diameter=650, images=faces)
    dotpaths.append(DotPath(width, height))
    
    
def draw():
    global dotpaths

    background(190, 229, 255)
    
    
    for d in dotpaths:
        d.draw()

    if d.finished:
        dotpaths.append(DotPath(width, height))

    face_circle.draw()
    if 360 <= face_circle.angle <= 360*3:
        saveFrame('frames/face-circle-#####.png')
    
    if face_circle.angle > 360*3:
        exit()
