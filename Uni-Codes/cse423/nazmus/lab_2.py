from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x,y):
    glPointSize(6)
    glBegin(GL_POINTS)
    glColor3f(0, 1, 1)
    glVertex2f(x, y)
    glEnd()

def convertZone0(X1, Y1, zone):
    if zone==0:
        pass
    elif zone==1:
        X1, Y1=Y1, X1
    elif zone == 2:
        X1, Y1 = Y1, -X1
    elif zone == 3:
        X1, Y1 = -X1, Y1
    elif zone == 4:
        X1, Y1 = -X1, -Y1
    elif zone==5:
        X1, Y1 = -Y1, -X1
    elif zone==6:
        X1, Y1 = -Y1, X1
    elif zone == 7:
        X1, Y1 = X1, -Y1

    return X1, Y1

def originalZone(X1, Y1, zone):
    if zone==0:
        pass
    elif zone==1:
        X1, Y1=Y1, X1
    elif zone == 2:
        X1, Y1 = -Y1, X1
    elif zone == 3:
        X1, Y1 = -X1, Y1
    elif zone == 4:
        X1, Y1 = -X1, -Y1
    elif zone==5:
        X1, Y1 = -Y1, -X1
    elif zone==6:
        X1, Y1 = Y1, -X1
    elif zone == 7:
        X1, Y1 = X1, -Y1

    return X1, Y1

def midPoint(X1, Y1, X2, Y2):
    zone=findZone(X1, Y1, X2, Y2)
    draw_points(X1, Y1)
    X1, Y1=convertZone0(X1, Y1, zone)
    X2, Y2=convertZone0(X2, Y2,zone)
    dx = X2 - X1
    dy = Y2 - Y1
    d = dy - (dx / 2)
    x = X1
    y = Y1

    while (x < X2):
        
        x = x + 1
        if (d < 0):
            d = d + dy
        else:
            d = d + (dy - dx)
            y = y + 1
        x_new, y_new = originalZone(x,y, zone)
        draw_points(x_new, y_new)
        

def findZone(X1, Y1, X2, Y2):
    dx = X2 - X1
    dy = Y2 - Y1
    zone=None
    if (abs(dx) >= abs(dy)):
        if (dx >= 0 and dy >= 0):
            zone=0
        if (dx >= 0 and dy < 0):
            zone=7
        if (dx < 0 and dy >= 0):
            zone=3
        if (dx < 0 and dy < 0):
            zone=4
    elif (abs(dx) < abs(dy)):
        if (dx >= 0 and dy >= 0):
            zone=1
        if (dx >= 0 and dy < 0):
            zone=6
        if (dx < 0 and dy >= 0):
            zone = 2
        if (dx < 0 and dy < 0):
            zone = 5
    return zone

def ShowOutput():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
    id = 20101480
    drawEight(100,100,400,300)
    drawZero(100, 100, 600, 300)
    
    glutSwapBuffers()

def drawEight(length, breadth, offsetX, offsetY):
    
     midPoint(offsetX, offsetY, offsetX, offsetY+length)
     midPoint(offsetX, offsetY+length, offsetX+breadth, offsetY+length)
     midPoint(offsetX+breadth, offsetY+length, offsetX+breadth, offsetY)
     midPoint(offsetX+breadth, offsetY, offsetX, offsetY)
     midPoint(offsetX, offsetY, offsetX, offsetY-length)
     midPoint(offsetX, offsetY-length, offsetX+breadth, offsetY-length)
     midPoint(offsetX+breadth, offsetY-length, offsetX+breadth, offsetY)
     
def drawZero(length, breadth, offsetX, offsetY):
    
     midPoint(offsetX, offsetY, offsetX, offsetY+length)
     midPoint(offsetX, offsetY+length, offsetX+breadth, offsetY+length)
     midPoint(offsetX+breadth, offsetY+length, offsetX+breadth, offsetY)
     midPoint(offsetX, offsetY, offsetX, offsetY-length)
     midPoint(offsetX, offsetY-length, offsetX+breadth, offsetY-length)
     midPoint(offsetX+breadth, offsetY-length, offsetX+breadth, offsetY)


     

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1366, 768) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1")
glutDisplayFunc(ShowOutput)

glutMainLoop()