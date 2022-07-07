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
    # when the line is parallel to x-axis
    if x0 == x1:
        if y0 > y1:
            while y1 != y0:
                glBegin(GL_POINTS)
                glVertex2f(x1, y1)
                glEnd()
                y1 = y1 + 1
        elif y1 > y0:
            while y0 != y1:
                glBegin(GL_POINTS)
                glVertex2f(x0, y0)
                glEnd()
                y0 = y0 + 1
    else:
        dx = x1 - x0
        dy = y1 - y0
        d = 2 * dy - dx
        incrNE = 2 * (dy - dx)
        incrE = 2 * dy

        x = x0
        y = y0
        while x <= x1:
            if d <= 0:
                d += incrE
                x += 1
            else:
                d += incrNE
                x += 1
                y += 1
            originalZone(x, y, zone)


def FindZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    zone = 0
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx > 0 and dy < 0:
            zone = 7
    else:
        if dx > 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx > 0 and dy < 0:
            zone = 6
    return zone


def convertToZone0(x0, y0, x1, y1):
    zone = FindZone(x0, y0, x1, y1)
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
    glViewport(150, 150, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def drawEight():
    convertToZone0(200, 100, 200, 200)
    convertToZone0(200, 200, 200, 300)
    convertToZone0(200, 300, 300, 300)
    convertToZone0(300, 300, 300, 200)
    convertToZone0(300, 200, 300, 100)
    convertToZone0(200, 200, 300, 200)
    convertToZone0(200, 100, 300, 100)


def drawTwo():
    convertToZone0(400, 300, 500, 300)
    convertToZone0(500, 300, 500, 200)
    convertToZone0(400, 200, 500, 200)
    convertToZone0(400, 200, 400, 100)
    convertToZone0(400, 100, 500, 100)


def showScreen():
    iterate()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(0, 1, 1)

    drawEight()
    drawTwo()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID: 20101482. Let's draw: 82")
glutDisplayFunc(showScreen)

glutMainLoop()
