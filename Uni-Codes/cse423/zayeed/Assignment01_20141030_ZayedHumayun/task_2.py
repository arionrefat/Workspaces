from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_lines():
    glBegin(GL_LINES)

    glVertex2f(50, 300)

    glVertex2f(50, 20)
    glVertex2f(50, 20)
    glVertex2f(350, 20)
    glVertex2f(350, 20)

    glVertex2f(350, 300)

    glVertex2f(350, 300)


    glEnd()


def draw_window_1():
    glBegin(GL_LINES)
    glVertex2f(75, 160)
    glVertex2f(160, 160)
    glVertex2f(160, 160)
    glVertex2f(160, 245)
    glVertex2f(160, 245)
    glVertex2f(75, 245)
    glVertex2f(75, 245)
    glVertex2f(75, 160)

    glEnd()
def triangle():
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex2f(200,400)
    glVertex2f(350, 300)
    glVertex2f(50, 300)    
    glEnd()

def draw_window_2():
    glBegin(GL_LINES)
    glVertex2f(325, 160)
    glVertex2f(240, 160)
    glVertex2f(240, 160)
    glVertex2f(240, 245)
    glVertex2f(240, 245)
    glVertex2f(325, 245)
    glVertex2f(325, 245)
    glVertex2f(325, 160)
    glEnd()


def draw_door():
    glBegin(GL_LINES)

    glVertex2f(175, 20)
    glVertex2f(175, 100)
    glVertex2f(175, 100)
    glVertex2f(225, 100)
    glVertex2f(225, 100)
    glVertex2f(225, 20)

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
    glColor3f(255, 255, 255)  # konokichur color set (RGB)
    # call the draw methods here
    draw_lines()
    triangle()
    draw_window_1()
    draw_window_2()
    draw_door()
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(215, 60)
    glEnd()

    # draw_points(200, 250)
    # drawTriangle()
    # drawQuads()
    # DDA(100,100,200,150)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
