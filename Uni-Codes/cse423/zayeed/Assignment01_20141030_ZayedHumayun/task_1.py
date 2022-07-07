from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
points_list_x = random.sample(range(0, 200), 50)
points_list_y = random.sample(range(201, 400), 50)


def draw_points(points_list_x, points_list_y):
    glPointSize(5)
    glBegin(GL_POINTS)
    for x, y in zip(points_list_x, points_list_y):
        glVertex2f(x, y)
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
    glColor3f(1.0, 1.0, 0.0)
    draw_points(points_list_x, points_list_y)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)  # window size
glutInitWindowPosition(100, 100)
wind = glutCreateWindow(b"Task 1")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
