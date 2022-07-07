from decimal import DivisionByZero
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points():
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(100, 400, 10):
        glVertex2f(i, 400)

    glEnd()


def DDA(x1, y1, x2, y2, method):
    glBegin(GL_POINTS)
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    try:
        x_increment = dx/steps
        y_increment = dy/steps
    except ZeroDivisionError:
        x_increment = 0
        y_increment = 0
    i = 0

    while i < steps:
        if method == "points":
            i += 1
            x1 = x1 + 5
            y1 = y1 + y_increment
        else:
            i += 1
            x1 = x1 + x_increment
            y1 = y1 + y_increment
        glVertex2f(x1, y1)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # call the draw methods here

    # draw_points()
    DDA(100, 400, 400, 400, "points")
    DDA(280, 400, 280, 100, "line")
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
