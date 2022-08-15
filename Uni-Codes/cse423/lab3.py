from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def main():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


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


def drawCircle(r, x, y):
    z1 = midpointCircle(r)
    for a, b in z1:
        convertToZone0Circle(a, b, x, y)


def window():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    main()
    glColor3f(0, 1, 0.5)
    glPointSize(2)
    glColor3f(255, 255, 255)

    drawCircle(180, 275, 275)
    drawCircle(90, 185, 275)
    drawCircle(90, 365, 275)
    drawCircle(90, 275, 185)
    drawCircle(90, 275, 365)
    drawCircle(90, 205, 330)
    drawCircle(90, 345, 330)
    drawCircle(90, 205, 220)
    drawCircle(90, 345, 220)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"20101482-LAB03")
glutDisplayFunc(window)
glutIdleFunc(window)
glutMainLoop()
