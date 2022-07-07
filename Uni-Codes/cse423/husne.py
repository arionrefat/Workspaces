from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def findzone(a, b, c, d):
    dx = c - a
    dy = d - b

    if abs(dx) >= abs(dy):

        if dx >= 0 and dy >= 0:
            zone=0
            return zone

        elif dx <= 0 and dy >= 0:
            zone=3
            return zone

        elif dx <= 0 and dy <= 0:
            zone=4
            return zone

        else:
            zone=7
            return zone
    else:

        if dx >= 0 and dy >= 0:
            zone=1
            return zone

        elif dx <= 0 and dy >= 0:
            zone=2
            return zone

        elif dx <= 0 and dy <= 0:
            zone=5
            return zone

        else:
            zone=6
            return zone
def zonezeroconverter(a,b,c,d,zone):
    if zone==0:
        return a,b,c,d
    elif zone==1:
        return b,a,d,c
    elif zone==2:
        return -b,a,-d,c
    elif zone==3:
        return -a, b, -c, d
    elif zone==4:
        return a, -b, -c, -d
    elif zone==5:
        return -b, -a, -d, -c
    elif zone==6:
        return b, -a, d, -c
    else:
        return a, -b, c, -d
def draw_zone(x, y, zone):
    if zone == 0:
        draw_points(x, y)
    elif zone == 1:
        draw_points(y, x)
    elif zone == 2:
        draw_points(-y, x)
    elif zone == 3:
        draw_points(-x, y)
    elif zone == 4:
        draw_points(-x, -y)
    elif zone == 5:
        draw_points(-y, -x)
    elif zone == 6:
        draw_points(y, -x)
    else:
        draw_points(x, -y)
def Drawline(x1, y1, x2, y2):
    zone = findzone(x1, y1, x2, y2)
    x1, y1, x2, y2=zonezeroconverter(x1, y1, x2, y2,zone)
    dx = x2 - x1
    dy = y2 - y1

    d = 2*(dy - dx)
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x = x1
    y = y1

    while (x <=x2):
        draw_zone(x, y, zone)
        x+=1
        if (d < 0):
            d = d + incE;
        else:
            d = d + incNE;
            y = y + 1;


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0/255, 8.0/255, 255.0/255)
    # Six
    Drawline(300, 350, 350, 350)
    Drawline(300, 400, 350, 400)
    Drawline(300, 450, 350, 450)
    Drawline(300, 350, 300, 450)
    Drawline(350, 350, 350, 400)
    # Three
    Drawline(200, 400, 250, 400)
    Drawline(200, 450, 250, 450)
    Drawline(200, 350, 250, 350)
    Drawline(250, 350, 250, 450)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 800) #window size
glutInitWindowPosition(20, 80)
wind = glutCreateWindow(b"Student ID: 20101336. Let's draw: 36") #window name
glutDisplayFunc(showScreen)

glutMainLoop()