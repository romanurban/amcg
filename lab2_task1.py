import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


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

window = glfw.create_window(800, 600, "Lab2 Task1", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glfw.set_window_pos(window, 100, 150)

glfw.make_context_current(window)

glfw.set_window_size_callback(window, window_resize)

window_resize(window, 600, 400)

points = [
    # R letter
    (20, 20),
    # outer shape
    (20, 340),
    (100, 340),
    (140, 320),
    (160, 300),
    (160, 220),
    (140, 200),
    (100, 180),
    (160, 20),
    (120, 20),
    (60, 180),
    (60, 20),
    # inner shape
    (60, 300),
    (80, 300),
    (120, 280),
    (120, 240),
    (80, 220),
    (60, 220),
    # U letter
    (240, 20),
    (200, 60),
    (200, 340),
    (240, 340),
    (240, 80),
    (260, 60),
    (320, 60),
    (340, 80),
    (340, 340),
    (380, 340),
    (380, 60),
    (340, 20),
    # O letter outer shape
    (460, 20),
    (420, 60),
    (420, 300),
    (460, 340),
    (560, 340),
    (600, 300),
    (600, 60),
    (560, 20),
    # O letter inner shape
    (480, 60),
    (460, 80),
    (460, 280),
    (480, 300),
    (540, 300),
    (560, 280),
    (560, 80),
    (540, 60),
]

move_codes = [
    # R letter outer shape
    -1,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    1,
    # inner shape
    -1,
    13,
    14,
    15,
    16,
    17,
    18,
    13,
    # U letter
    -1,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    19,
    # O letter outer shape
    -1,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    31,
    # O letter inner shape
    -1,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    39,
]


def draw_shape():
    # Setting the clipping plane
    plane = (GLdouble * 4)(-1, 1.7, 0, 0)  # Ax + By + Cz + D = 0 -> x - y = 0
    glClipPlane(GL_CLIP_PLANE0, plane)
    glEnable(GL_CLIP_PLANE0)

    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14

    # Initialize the current point
    current_point = None

    for code in move_codes:
        if code == -1:
            # Move without drawing
            current_point = None
        else:
            x, y = points[code - 1]  # Adjust for 0-based indexing
            x = int(x)
            y = int(y)

            if current_point is not None:
                glVertex2f(*current_point)
                glVertex2f(x, y)
            current_point = (x, y)

    glEnd()
    # Disabling the clipping plane after drawing
    glDisable(GL_CLIP_PLANE0)


while not glfw.window_should_close(window):
    glfw.poll_events()

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    draw_shape()

    glfw.swap_buffers(window)

glfw.terminate()