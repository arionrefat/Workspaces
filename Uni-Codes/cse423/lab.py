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


def originalZoneCircle(x, y, zone, x1, y1):
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
    glVertex2f(a + x1, b + y1)


def midpointCircle(r):
    d_init = 1 - r
    d = d_init
    x = 0
    y = r
    points = []

    while x < y:
        points.append((x, y))
        if d >= 0:
            d += (2 * x) - (2 * y) + 5
            x = x + 1
            y = y - 1
        else:
            d += (2 * x) + 3
            x = x + 1
    return points


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


def convertToZone0Circle(x1, y1, x, y):
    glBegin(GL_POINTS)
    a, b = y1, x1
    glVertex2f(x + a, y + b)
    originalZoneCircle(a, b, 1, x, y)
    originalZoneCircle(a, b, 2, x, y)
    originalZoneCircle(a, b, 3, x, y)
    originalZoneCircle(a, b, 4, x, y)
    originalZoneCircle(a, b, 5, x, y)
    originalZoneCircle(a, b, 6, x, y)
    originalZoneCircle(a, b, 7, x, y)
    glEnd()


def iterate():
    glViewport(150, 150, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def drawCircle(r, x, y):
    z1 = midpointCircle(r)
    for a, b in z1:
        convertToZone0Circle(a, b, x, y)


def drawTwo():
    convertToZone0(400, 300, 500, 300)
    convertToZone0(500, 300, 500, 200)
    convertToZone0(400, 200, 500, 200)
    convertToZone0(400, 200, 400, 100)
    convertToZone0(400, 100, 500, 100)



def drawCircles():
    drawCircle(180, 275, 275)
    drawCircle(90, 345, 220)


def showScreen():
    iterate()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(0, 1, 1)
    glPointSize(2)

    Bx = 200
    By = 0
    Cx = 300
    Cy = 0
    Dx = 200
    Dy = 100
    Ex = 300
    Ey = 100
    Gx = 250
    Gy = 100
    centerx = 250
    centery = 50


    for _ in range(0, 1):
        convertToZone0(Bx, By, Cx, Cy)
        convertToZone0(Cx, Cy, Ex, Ey)
        convertToZone0(Bx, By, Dx, Dy)
        convertToZone0(Dx, Dy, Ex, Ey)
        convertToZone0(Bx, By, Gx, Gy)
        convertToZone0(Cx, Cy, Gx, Gy)

        Bx = Bx + 50
        Cx = Cy + 50
        Dx = Dx - 50
        Dy = Dy + 50
        Ex = Ex + 50
        Ey = Ey - 50
        Gy = Gy + 50

    drawCircle(50, centerx, centery)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID: 20101482")
glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
glutMainLoop()
