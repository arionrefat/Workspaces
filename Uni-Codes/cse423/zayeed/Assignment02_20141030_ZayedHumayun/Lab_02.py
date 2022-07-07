from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def originalZone(x, y, zone):

    if zone == 1:
        a, b = y, x
    elif zone == 2:
        a, b = -y, x
    elif zone == 3:
        a, b = -x, y
    elif zone == 4:
        a, b = -x, -y
    elif zone == 5:
        a, b = -y, -x
    elif zone == 6:
        a, b = y, -x
    elif zone == 7:
        a, b = x, -y
    else:
        a, b = x, y

    glBegin(GL_POINTS)
    glVertex2f(a, b)
    glEnd()


def Midpoint(x0, y0, x1, y1, zone):

    if(x0 == x1):  # vertical line
        if(y0 > y1):
            while y1 != y0:
                glBegin(GL_POINTS)
                glVertex2f(x1, y1)
                glEnd()
                y1 = y1 + 1
        elif(y1 > y0):
            while y0 != y1:
                glBegin(GL_POINTS)
                glVertex2f(x0, y0)
                glEnd()
                y0 = y0 + 1
    else:
        dx = x1 - x0
        dy = y1 - y0
        d = 2*dy-dx
        incrNE = 2 * (dy - dx)
        incrE = 2 * dy

        x = x0
        y = y0
        while x <= x1:
            if (d <= 0):
                d += incrE
                x += 1
            else:
                d += incrNE
                x += 1
                y += 1
            originalZone(x, y, zone)


def zoneFinder(x0,  y0,  x1,  y1):
    dx = x1 - x0
    dy = y1 - y0
    zone = 0
    if (abs(dx) > abs(dy)):
        if (dx > 0 and dy > 0):
            zone = 0
        elif (dx < 0 and dy > 0):
            zone = 3
        elif (dx < 0 and dy < 0):
            zone = 4
        elif dx > 0 and dy < 0:
            zone = 7
    else:
        if (dx > 0 and dy > 0):
            zone = 1
        elif (dx < 0 and dy > 0):
            zone = 2
        elif (dx < 0 and dy < 0):
            zone = 5
        elif dx > 0 and dy < 0:
            zone = 6
    return zone


def convertToZone0(x0, y0, x1, y1):
    flag = True
    zone = zoneFinder(x0, y0, x1, y1)
    if zone == 0:
        a, b, c, d = x0, y0, x1, y1
    if zone == 1:
        a, b, c, d = y0, x0, y1, x1
    elif zone == 2:
        a, b, c, d = y0, -x0, y1, -x1
    elif zone == 3:
        a, b, c, d = -x0, y0, -x1, y1
    elif zone == 4:
        a, b, c, d = -x0, -y0, -x1, -y1
    elif zone == 5:
        a, b, c, d = -y0, -x0, -y1, -x1
    elif zone == 6:
        a, b, c, d = -y0, x0, -y1, x1
    elif zone == 7:
        a, b, c, d = x0, -y0, x1, -y1

    Midpoint(a, b, c, d, zone)


def iterate():
    glViewport(0, 0, 550, 550)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    iterate()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glColor3f(0, 1, 1)

    convertToZone0(150, 550, 300, 550)
    convertToZone0(150, 400, 300, 400)
    convertToZone0(150, 250, 300, 250)
    convertToZone0(301, 250, 301, 550)

    convertToZone0(350, 550, 500, 550)
    convertToZone0(350, 550, 350, 250)
    convertToZone0(501, 550, 501, 250)
    convertToZone0(350, 249, 500, 249)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ID: 20141030")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
