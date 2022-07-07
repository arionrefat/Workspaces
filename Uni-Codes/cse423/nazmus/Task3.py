from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def dda(x0, y0, x1, y1):
    if abs(x1-x0) > abs(y1-y0):
        steps = abs(x1-x0)
    else:
        steps = abs(y1-y0)
     
    x_increment = (x1-x0) / steps
    y_increment = (y1-y0) / steps
    x = x0
    y = y0
    for i in range(0, steps):
        
        glPointSize(6)
        glBegin(GL_POINTS)
        glColor3f(0, 1, 1)
        glVertex2f(x, y)
        glEnd()
        x += x_increment
        y += y_increment

def ddda(x0, y0, x1, y1):
    if abs(x1-x0) > abs(y1-y0):
        steps = abs(x1-x0)
    else:
        steps = abs(y1-y0)
    x_increment = (x1-x0) / steps
    y_increment = (y1-y0) / steps
    x = x0
    y = y0
    count = 0
    for i in range(0, steps):
        if count % 2 == 0:
            
            glPointSize(6)
            glBegin(GL_POINTS)
            glColor3f(0, 1, 1)
            glVertex2f(x, y)
            glEnd()
        else:
            
            glPointSize(6)
            glBegin(GL_POINTS)
            glColor3f(0, 0, 0)
            glVertex2f(x, y)
            glEnd()
        x += x_increment
        y += y_increment
        count += 1

def ShowOutput():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
    id = 20101480
    if id % 2 == 0:
        # Even/Tails
        ddda(80, 220, 220, 220)
        dda(150, 220, 150, 80)
    else:
        # Odd/Heads
        dda(75, 225, 75, 75)
        ddda(225, 225, 225, 75)
        ddda(75, 150, 225, 150)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1080, 1080) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3")
glutDisplayFunc(ShowOutput)

glutMainLoop()