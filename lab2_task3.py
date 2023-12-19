import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if not glfw.init():
    raise Exception("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "Lab2 Task3", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glfw.set_window_pos(window, 100, 150)

glfw.make_context_current(window)

glfw.set_window_size_callback(window, window_resize)

window_resize(window, 800, 600)


def draw_shape():
    # Control points for the left side of the upper heart
    ctrlPointsLeft = [
        [350.0, 500.0, 0.0],  # Start at the middle top
        [250.0, 650.0, 0.0],  # Control point for the curve
        [100.0, 400.0, 0.0],  # Control point for the descent
        [350.0, 100.0, 0.0],  # End at the center bottom
    ]

    # Control points for the right side of the upper heart
    ctrlPointsRight = [
        [350.0, 500.0, 0.0],  # Start at the middle top
        [450.0, 650.0, 0.0],  # Control point for the curve
        [600.0, 400.0, 0.0],  # Control point for the descent
        [350.0, 100.0, 0.0],  # End at the center bottom
    ]

    # The knot vector for a cubic curve
    knots = [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0]

    # Type of data (vertices in 3D)
    type_ = GL_MAP1_VERTEX_3

    # The NURBS object
    theNurb = gluNewNurbsRenderer()

    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    glLineWidth(5.0)

    # Draw the left upper curve of the heart
    gluBeginCurve(theNurb)
    gluNurbsCurve(theNurb, knots, ctrlPointsLeft, type_)
    gluEndCurve(theNurb)

    # Draw the right upper curve of the heart
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