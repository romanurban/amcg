from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(250, 450)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(250, 150)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(550, 150)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(550, 450)
    glEnd()
    
	# Reset transformations before drawing axes
    glLoadIdentity()

    # Draw the axes
    # X-axis
    glColor3f(0.0, 0.0, 0.0)  # Black color for axes
    glBegin(GL_LINES)
    glVertex2i(0, 300)  # Assuming 300 is the middle of the window for Y
    glVertex2i(800, 300)  # Assuming 800 is the width of the window
    glEnd()

    # Y-axis
    glBegin(GL_LINES)
    glVertex2i(400, 0)  # Assuming 400 is the middle of the window for X
    glVertex2i(400, 600)  # Assuming 600 is the height of the window
    glEnd()

    glutSwapBuffers()
    glDisable(GL_CLIP_PLANE0)

def processNormalKeys(key, x, y):
    if ord(key) == 27:  # ASCII for escape key
        exit(0)
    if ord(key) == 65:  # ASCII for 'A'
        glMatrixMode(GL_MODELVIEW)
        glTranslated(20, 20, 0)
        display()

def processSpecialKeys(key, x, y):
    if key == GLUT_KEY_UP:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, 20, 0)
        display()
    elif key == GLUT_KEY_DOWN:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, -20, 0)
        display()
    elif key == GLUT_KEY_LEFT:  # Move left
        glMatrixMode(GL_MODELVIEW)
        glTranslated(-20, 0, 0)
        display()
    elif key == GLUT_KEY_RIGHT:  # Move right
        glMatrixMode(GL_MODELVIEW)
        glTranslated(20, 0, 0)
        display()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab3 Task1")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)
    glutMainLoop()

if __name__ == "__main__":
    main()
