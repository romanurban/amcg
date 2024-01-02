from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

PI = 3.141592653
light_sample = 1

def init():
    glClearColor(0.3, 0.3, 0.3, 0.0)
    glEnable(GL_LIGHTING)
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glEnable(GL_NORMALIZE)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.2, 1.2, -1.2, 1.2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    material_diffuse = [1.0, 1.0, 1.0, 1.0]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material_diffuse)
    
    global light_sample
    # Installation of light sources
    if light_sample == 1:  # directional light source
        light0_diffuse = [0.4, 0.7, 0.2]
        light0_direction = [0.0, 0.0, 1.0, 0.0]
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
        glLightfv(GL_LIGHT0, GL_POSITION, light0_direction)

    elif light_sample == 2:  # point light source
        light1_diffuse = [0.4, 0.7, 0.2]
        light1_position = [0.0, 0.0, 1.0, 1.0]
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
        glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
    elif light_sample == 3:  # point light source with attenuation
        light2_diffuse = [0.4, 0.7, 0.2]
        light2_position = [0.0, 0.0, 1.0, 1.0]
        glEnable(GL_LIGHT2)
        glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
        glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
        glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.4)

    elif light_sample == 4:  # spotlight
        light3_diffuse = [0.4, 0.7, 0.2]
        light3_position = [0.0, 0.0, 1.0, 1.0]
        light3_spot_direction = [0.0, 0.0, -1.0]
        glEnable(GL_LIGHT3)
        glLightfv(GL_LIGHT3, GL_DIFFUSE, light3_diffuse)
        glLightfv(GL_LIGHT3, GL_POSITION, light3_position)
        glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 30)
        glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, light3_spot_direction)

    elif light_sample == 5:  # floodlight with spotlight effect
        light4_diffuse = [0.4, 0.7, 0.2]
        light4_position = [0.0, 0.0, 1.0, 1.0]
        light4_spot_direction = [0.0, 0.0, -1.0]
        glEnable(GL_LIGHT4)
        glLightfv(GL_LIGHT4, GL_DIFFUSE, light4_diffuse)
        glLightfv(GL_LIGHT4, GL_POSITION, light4_position)
        glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 30)
        glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, light4_spot_direction)
        glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, 15.0)

    elif light_sample == 6:  # multiple light sources
        light_colors_positions = [
            ([1.0, 0.0, 0.0], [0.5 * math.cos(0.0), 0.5 * math.sin(0.0), 1.0, 1.0]),
            ([0.0, 1.0, 0.0], [0.5 * math.cos(2 * PI / 3), 0.5 * math.sin(2 * PI / 3), 1.0, 1.0]),
            ([0.0, 0.0, 1.0], [0.5 * math.cos(4 * PI / 3), 0.5 * math.sin(4 * PI / 3), 1.0, 1.0])
        ]
        for i, (color, position) in enumerate(light_colors_positions, start=5):
            glEnable(GL_LIGHT0 + i)
            glLightfv(GL_LIGHT0 + i, GL_DIFFUSE, color)
            glLightfv(GL_LIGHT0 + i, GL_POSITION, position)
            glLightf(GL_LIGHT0 + i, GL_CONSTANT_ATTENUATION, 0.0)
            glLightf(GL_LIGHT0 + i, GL_LINEAR_ATTENUATION, 0.4)
            glLightf(GL_LIGHT0 + i, GL_QUADRATIC_ATTENUATION, 0.8)
    elif light_sample == 7:  # Trying to replicate the success of light_sample == 6
        glEnable(GL_LIGHT4)
        light4_diffuse = [1.0, 0.0, 0.0]  # Red color, full intensity
        light4_position = [0.5 * math.cos(0.0), 0.5 * math.sin(0.0), 1.0, 1.0]  # Position similar to a working light
        light4_spot_direction = [0.0, 0.0, -1.0]  # Pointing directly downwards
        light4_cutoff = 180  # Wide angle to ensure visibility
        light4_exponent = 0  # No focus, to ensure visibility

        glLightfv(GL_LIGHT4, GL_DIFFUSE, light4_diffuse)
        glLightfv(GL_LIGHT4, GL_POSITION, light4_position)
        glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, light4_spot_direction)
        glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, light4_cutoff)
        glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, light4_exponent)

    
    # Drawing the quads as in the C code
    x, y = -1.0, -1.0
    glBegin(GL_QUADS)
    glNormal3f(0.0, 0.0, -1.0)
    while x < 1.0:
        while y < 1.0:
            glVertex3f(x, y, 0.0)
            glVertex3f(x, y + 0.005, 0.0)
            glVertex3f(x + 0.005, y + 0.005, 0.0)
            glVertex3f(x + 0.005, y, 0.0)
            y += 0.005
        x += 0.005
        y = -1.0
    glEnd()

    # Turning off light sources
    for i in range(8):
        glDisable(GL_LIGHT0 + i)

    glutSwapBuffers()

def keyboard_function(key, x, y):
    global light_sample
    if key in [b'1', b'2', b'3', b'4', b'5', b'6', b'7']:
        light_sample = int(key)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(50, 100)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"An example of installing light sources in OpenGL")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard_function)
    glutMainLoop()

if __name__ == "__main__":
    main()
