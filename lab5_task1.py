from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Hardcoded coordinates and faces data
v = [Point(1, 1, 0), Point(9, 1, 0), Point(9, 5, 0), Point(1, 5, 0),
     Point(1, 1, 1), Point(9, 1, 1), Point(9, 5, 1), Point(1, 5, 1)]

faces = [[0, 1, 2, 3], [4, 7, 6, 5], [4, 5, 1, 0], 
         [2, 6, 7, 3], [5, 6, 2, 1], [0, 3, 7, 4]]

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 10, 0, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    for face in faces:
        glBegin(GL_LINE_LOOP)
        for index in face:
            glVertex3f(v[index].x, v[index].y, v[index].z)
        glEnd()
    glutSwapBuffers()

def processNormalKeys(key, x, y):
    if key == b'\x1b':  # ESC
        sys.exit()
    if key == b'A' or key == b'a':
        glMatrixMode(GL_MODELVIEW)
        glTranslated(2, 2, 0)
        glutPostRedisplay()

def processSpecialKeys(key, x, y):
    if key == GLUT_KEY_UP:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, 2, 0)
    elif key == GLUT_KEY_DOWN:
        glMatrixMode(GL_MODELVIEW)
        glRotated(5, 1, 1, 1)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab5 Task1")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)
    glutMainLoop()

if __name__ == "__main__":
    main()
