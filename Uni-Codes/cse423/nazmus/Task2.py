from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def drawPoint(size, x, y):
    glPointSize(size)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, y)
    glEnd()

def drawLine(x0,y0,x1,y1):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()


    

def ShowOutput():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
   
    
    x=200
    y=100
    length=200
    drawLine(x,y, x, y+length)
    drawLine(x, y+length, x+length, y+length)
    drawLine(x+length, y+length, x+length, y)
    drawLine(x+length, y, x, y)
    
    x=230
    y=200
    length=50
    drawLine(x,y, x, y+length)
    drawLine(x, y+length, x+length, y+length)
    drawLine(x+length, y+length, x+length, y)
    drawLine(x+length, y, x, y)
    
    x=320
    y=200
    length=50
    drawLine(x,y, x, y+length)
    drawLine(x, y+length, x+length, y+length)
    drawLine(x+length, y+length, x+length, y)
    drawLine(x+length, y, x, y)

    
    x=280
    y=100
    length=75
    breadth=40
    drawLine(x,y, x, y+length)
    drawLine(x, y+length, x+breadth, y+length)
    drawLine(x+breadth, y+length, x+breadth, y)
    drawLine(x+breadth, y, x, y)
    
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)
    xoffset=175
    yoffset=100
    glVertex3f(125+xoffset, 230+yoffset, 0)
    glVertex3f(25+xoffset, 200+yoffset, 0)
    glVertex3f(225+xoffset, 200+yoffset, 0)
    glEnd()

    drawPoint(6, 310, 130)
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1080, 1080) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2") 
glutDisplayFunc(ShowOutput)

glutMainLoop()