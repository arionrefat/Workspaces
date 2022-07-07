from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def ShowOutput():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
   
    for i in range(50):
        x = random.randint(0, 768)
        y = random.randint(0, 768)
        
        glPointSize(6)
        glBegin(GL_POINTS)
        glColor3f(1.0, 1.0, 0)
        glVertex2f(x, y)
        glEnd()

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1080, 1080) #size of window
glutInitWindowPosition((768//2)-80, 0)
wind = glutCreateWindow(b"Task 1") #Name 
glutDisplayFunc(ShowOutput)

glutMainLoop()