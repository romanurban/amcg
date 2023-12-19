import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, pi


# Function to set up the view
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if not glfw.init():
    raise Exception("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "Lab2 Task2", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glfw.set_window_pos(window, 100, 150)

glfw.make_context_current(window)

glfw.set_window_size_callback(window, window_resize)

window_resize(window, 800, 600)


def draw_shape():
    # Control points for the left side of the heart
    ctrlPointsLeft = [
        [350.0, 500.0, 0.0],
        [250.0, 650.0, 0.0],
        [100.0, 400.0, 0.0],
        [350.0, 100.0, 0.0],
    ]

    # Control points for the right side of the heart
    ctrlPointsRight = [
        [350.0, 500.0, 0.0],
        [450.0, 650.0, 0.0],
        [600.0, 400.0, 0.0],
        [350.0, 100.0, 0.0],
    ]

    # The knot vector for a cubic B-spline
    knots = [0.0, 0.0, 0.0, 0.5, 1.0, 1.0, 1.0]

    # Type of data (vertices in 3D)
    type_ = GL_MAP1_VERTEX_3

    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    glLineWidth(5.0)

    # The NURBS object
    theNurb = gluNewNurbsRenderer()

    # Draw the left curve of the heart
    gluBeginCurve(theNurb)
    gluNurbsCurve(theNurb, knots, ctrlPointsLeft, type_)
    gluEndCurve(theNurb)

    # Draw the right curve of the heart
    gluBeginCurve(theNurb)
    gluNurbsCurve(theNurb, knots, ctrlPointsRight, type_)
    gluEndCurve(theNurb)


while not glfw.window_should_close(window):
    glfw.poll_events()

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    draw_shape()

    glfw.swap_buffers(window)

glfw.terminate()